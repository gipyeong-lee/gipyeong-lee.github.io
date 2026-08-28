#!/usr/bin/env python3
"""Validate Studio-generated Learn files and built no-ad pages."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse


AD_MARKERS = ("adsbygoogle", "pagead2.googlesyndication.com", "ad-slot")
UNSAFE_GENERATED_MARKUP = re.compile(
    r"(?:\{\{|\{%|\{#)|<\s*/?\s*[a-z][^>]*>|\bon[a-z]+\s*=|(?:javascript|vbscript|data)\s*:",
    re.IGNORECASE,
)
SOURCE_TYPES = {
    "university",
    "paper",
    "patent",
    "standard",
    "datasheet",
    "textbook",
    "technical_documentation",
}
BOM_CATEGORIES = {
    "actuator",
    "bearing",
    "controller",
    "fastener",
    "power",
    "safety",
    "sensor",
    "structure",
    "transmission",
    "wiring",
}
OFFICIAL_STANDARD_HOSTS = (
    "astm.org",
    "bsigroup.com",
    "din.de",
    "iec.ch",
    "ieee.org",
    "iso.org",
    "kats.go.kr",
    "nist.gov",
    "osha.gov",
    "ul.com",
)
PAPER_HOSTS = (
    "acm.org",
    "alliedacademies.org",
    "arxiv.org",
    "doi.org",
    "frontiersin.org",
    "ieee.org",
    "intechopen.com",
    "mdpi.com",
    "nature.com",
    "ncbi.nlm.nih.gov",
    "sciencedirect.com",
    "springer.com",
    "wiley.com",
    "wseas.org",
)
PATENT_HOSTS = (
    "epo.org",
    "espacenet.com",
    "google.com",
    "patentscope.wipo.int",
    "uspto.gov",
    "wipo.int",
)
TEXTBOOK_HOSTS = (
    "books.google.com",
    "doabooks.org",
    "intechopen.com",
    "libretexts.org",
    "openstax.org",
    "springer.com",
)
BLOCKED_REFERENCE_HOSTS = (
    "aliexpress.com",
    "amazon.com",
    "arxiv.org",
    "bing.com",
    "digikey.com",
    "ebay.com",
    "element14.com",
    "farnell.com",
    "github.com",
    "github.io",
    "gitlab.com",
    "google.com",
    "mcmaster.com",
    "mouser.com",
    "researchgate.net",
    "robotshop.com",
    "rs-online.com",
    "thingiverse.com",
    "tribotix.com",
    "wikipedia.org",
)
GENERIC_MANUFACTURER_TOKENS = {
    "co",
    "company",
    "com",
    "corp",
    "corporation",
    "custom",
    "generic",
    "inc",
    "industries",
    "industry",
    "ltd",
    "manufacturer",
    "net",
    "org",
    "standard",
}


def _hostname(url: str) -> str:
    return (urlparse(url).hostname or "").lower().rstrip(".")


def _host_matches(host: str, suffixes: tuple[str, ...]) -> bool:
    return any(host == suffix or host.endswith(f".{suffix}") for suffix in suffixes)


def _source_type_authoritative(url: str, source_type: str) -> bool:
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower().rstrip(".")
    if not host or parsed.path in {"", "/"} and source_type in {"paper", "patent"}:
        return False
    if source_type == "paper":
        return _host_matches(host, PAPER_HOSTS)
    if source_type == "patent":
        path = parsed.path.lower()
        if host == "patents.google.com":
            return path.startswith("/patent/")
        if _host_matches(host, ("patentscope.wipo.int",)):
            return "detail.jsf" in path and "docid=" in parsed.query.lower()
        if _host_matches(host, ("espacenet.com",)):
            return "publication" in path or "family" in path
        if _host_matches(host, ("epo.org", "uspto.gov")):
            return "downloadpdf" in path or path.endswith(".pdf")
        return False
    if source_type == "standard":
        return _host_matches(host, OFFICIAL_STANDARD_HOSTS)
    if source_type == "university":
        labels = set(host.split("."))
        return "edu" in labels or "ac" in labels
    if source_type == "textbook":
        return _host_matches(host, TEXTBOOK_HOSTS)
    return source_type in {"datasheet", "technical_documentation"}


def _bom_source_authority_error(item: dict[str, Any], source: dict[str, Any]) -> Optional[str]:
    source_type = str(source.get("type") or "")
    parsed = urlparse(str(source.get("url") or ""))
    host = (parsed.hostname or "").lower().rstrip(".")
    if not host or _host_matches(host, BLOCKED_REFERENCE_HOSTS):
        return "source host is not authoritative"
    if host.split(".", 1)[0] in {"community", "e2e", "forum", "forums"}:
        return "community attachments are not official product documents"
    if parsed.path in {"", "/"}:
        return "source must link to a specific document or product page"
    if source_type == "standard":
        if not _host_matches(host, OFFICIAL_STANDARD_HOSTS):
            return "standard source is not an official standards-body URL"
        return None
    if source_type not in {"datasheet", "technical_documentation"}:
        return "source is not specification material"

    manufacturer = str(item.get("manufacturer") or "").lower()
    tokens = {
        token
        for token in re.findall(r"[a-z0-9]+", manufacturer)
        if len(token) >= 2 and token not in GENERIC_MANUFACTURER_TOKENS
    }
    host_key = re.sub(r"[^a-z0-9]", "", host)
    if not tokens:
        return "item needs a specific manufacturer or official standard"
    if not any(token in host_key for token in tokens):
        return "source host does not match item manufacturer"
    return None


def _load_yaml(path: Path) -> Any:
    """Load YAML without making PyYAML a requirement of the Jekyll repository."""
    try:
        import yaml  # type: ignore

        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except ModuleNotFoundError:
        result = subprocess.run(
            [
                "ruby",
                "-ryaml",
                "-rjson",
                "-e",
                "puts JSON.generate(YAML.load_file(ARGV.fetch(0)))",
                str(path),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            raise ValueError(result.stderr.strip() or "Ruby YAML parser failed")
        return json.loads(result.stdout)


def _require_list(manifest: dict[str, Any], key: str, label: str, errors: list[str]) -> list[Any]:
    value = manifest.get(key)
    if not isinstance(value, list) or not value:
        errors.append(f"{label}: {key} must be a non-empty list")
        return []
    return value


def _check_generated_front_matter(path: Path, run_id: str, values: tuple[str, ...], errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"{path}: generated page missing")
        return
    text = path.read_text(encoding="utf-8")
    if UNSAFE_GENERATED_MARKUP.search(text):
        errors.append(f"{path}: unsafe generated markup")
    required = (
        "generated_by: mindtickle-studio",
        f"generation_run_id: {run_id}",
        "no_ads: true",
        *values,
    )
    for marker in required:
        if marker not in text:
            errors.append(f"{path}: missing front matter {marker}")
    for marker in AD_MARKERS:
        if marker in text:
            errors.append(f"{path}: advertising marker {marker}")


def _front_matter(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            return {}
        closing = text.find("\n---\n", 4)
        if closing < 0:
            return {}
        loaded = _load_yaml_text(text[4:closing])
        return loaded if isinstance(loaded, dict) else {}
    except (OSError, ValueError):
        return {}


def _load_yaml_text(text: str) -> Any:
    result = subprocess.run(
        ["ruby", "-ryaml", "-rjson", "-e", "puts JSON.generate(YAML.safe_load(STDIN.read, aliases: true))"],
        input=text,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        return {}
    return json.loads(result.stdout)


def _current_amps(item: dict[str, Any]) -> Optional[float]:
    values: list[float] = []
    for specification in item.get("specifications") or []:
        if not isinstance(specification, dict):
            continue
        name = str(specification.get("name") or "").lower()
        unit = str(specification.get("unit") or "").strip().lower()
        if ("current" not in name and "전류" not in name) or unit not in {
            "a", "amp", "amps", "ampere", "amperes", "ma",
        }:
            continue
        match = re.search(r"-?\d+(?:\.\d+)?", str(specification.get("value") or "").replace(",", ""))
        if match:
            value = float(match.group()) / (1000 if unit == "ma" else 1)
            if value > 0:
                values.append(value)
    return max(values) if values else None


def _named_current_amps(
    item: dict[str, Any], required_tokens: tuple[str, ...]
) -> Optional[float]:
    values: list[float] = []
    for specification in item.get("specifications") or []:
        if not isinstance(specification, dict):
            continue
        name = str(specification.get("name") or "").lower()
        if not all(token.lower() in name for token in required_tokens):
            continue
        unit = str(specification.get("unit") or "").strip().lower()
        if unit not in {"a", "amp", "amps", "ampere", "amperes", "ma"}:
            continue
        match = re.search(r"-?\d+(?:\.\d+)?", str(specification.get("value") or "").replace(",", ""))
        if not match:
            continue
        value = float(match.group()) / 1000 if unit == "ma" else float(match.group())
        if value > 0:
            values.append(value)
    return max(values) if values else None


def _voltage_volts(item: dict[str, Any]) -> Optional[float]:
    values: list[float] = []
    for specification in item.get("specifications") or []:
        if not isinstance(specification, dict):
            continue
        name = str(specification.get("name") or "").lower()
        unit = str(specification.get("unit") or "").strip().lower()
        if ("voltage" not in name and "전압" not in name) or unit not in {
            "v", "vdc", "volt", "volts",
        }:
            continue
        match = re.search(r"-?\d+(?:\.\d+)?", str(specification.get("value") or ""))
        if match and float(match.group()) > 0:
            values.append(float(match.group()))
    return max(values) if values else None


def _string_values(value: Any) -> list[str]:
    if isinstance(value, dict):
        return [text for child in value.values() for text in _string_values(child)]
    if isinstance(value, list):
        return [text for child in value for text in _string_values(child)]
    return [value] if isinstance(value, str) else []


def _citation_like_token(raw_token: str) -> bool:
    return any(
        re.fullmatch(
            r"(?:[SB](?:\d[A-Za-z0-9_-]*|-[A-Za-z0-9_-]+)?|BOM|bom_system_truth)",
            token.strip(),
        )
        for token in re.split(r"\s*,\s*", raw_token)
    )


def _unsafe_generated_values(value: Any, path: str = "manifest") -> list[str]:
    errors: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            errors.extend(_unsafe_generated_values(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            errors.extend(_unsafe_generated_values(child, f"{path}.{index}"))
    elif isinstance(value, str) and UNSAFE_GENERATED_MARKUP.search(value):
        errors.append(f"{path}: unsafe generated markup")
    return errors


def _unsupported_module_estop_reference(value: str) -> bool:
    return bool(
        re.search(r"비상\s*(?:정지|차단)|E[- ]?stop|emergency\s+(?:stop|cutoff)", value, re.I)
        and not re.search(
            r"금지|하지\s*않|아니|범위\s*밖|별도|자격.{0,12}전문|대신하지|오인하지|"
            r"never|do\s+not|must\s+not|out\s+of\s+scope|qualified|not\s+an?",
            value,
            re.I,
        )
    )


def _unsafe_safety_system_requirement(value: str) -> bool:
    return bool(
        re.search(
            r"안전\s*(?:회로|시스템|기능)|시스템\s*안전\s*기능|safety\s+(?:circuit|system|function)",
            value,
            re.I,
        )
        and re.search(
            r"배선|설계|제작|구현|조립|작동|동작|시험|검증|완결|"
            r"wire|design|build|implement|assembl|operate|test|verify|complete",
            value,
            re.I,
        )
        and not re.search(
            r"금지|하지\s*않|아니|범위\s*밖|별도|자격.{0,12}전문|"
            r"never|do\s+not|out\s+of\s+scope|qualified",
            value,
            re.I,
        )
    )


def _unsafe_emergency_isolation_instruction(value: str) -> bool:
    if re.search(
        r"금지|하지\s*않|사용하지|대신하지|오인하지|"
        r"never|do\s+not|must\s+not|not\s+an?",
        value,
        re.I,
    ):
        return False
    manual_isolation = bool(
        re.search(
            r"(?:물리적\s*)?(?:전원|에너지).{0,16}(?:분리|격리)|"
            r"(?:physical\s+)?(?:power|energy).{0,16}(?:isolat|disconnect)",
            value,
            re.I,
        )
        or (
            re.search(
                r"(?:\d+\s*개\s*)?(?:절연\s*)?(?:전원\s*)?(?:어댑터|플러그)|"
                r"(?:multiple|several|all)\s+(?:power\s+)?(?:adapters?|plugs?)",
                value,
                re.I,
            )
            and re.search(r"즉시|분리|뽑|immediate|unplug|disconnect", value, re.I)
        )
    )
    if not manual_isolation:
        return False
    if re.search(
        r"계획\s*정지\s*후.{0,40}(?:정비|접근)|"
        r"planned\s+shutdown.{0,40}(?:before|prior\s+to).{0,20}(?:maintenance|access)",
        value,
        re.I,
    ):
        return False
    return bool(
        re.search(
            r"비상|긴급|정지|멈춤|emergency|(?:normal|all)\s+stops?|"
            r"when\s+(?:a\s+)?stop\s+is\s+needed|shutdown|stop(?:ping|ped)?",
            value,
            re.I,
        )
    )


def _unsafe_live_fault_injection(value: str) -> bool:
    return bool(
        re.search(r"퓨즈|fuse", value, re.I)
        and re.search(r"단락|합선|short[- ]?circuit", value, re.I)
        and re.search(
            r"시험|실험|기록|검증|확인|유도|재현|주입|test|record|verify|inject|induce",
            value,
            re.I,
        )
        and not re.search(
            r"금지|하지\s*않|데이터시트|시간[- ]전류\s*곡선|시뮬레이션|전류\s*제한.{0,12}(?:지그|치구)|"
            r"never|do\s+not|datasheet|time[- ]current\s+curve|simulation|current[- ]limited.{0,12}fixture",
            value,
            re.I,
        )
    )


def _reversed_fsr_pulldown_formula(value: str) -> bool:
    compact = re.sub(r"[\s{}()_*\\]", "", value).lower()
    return bool(
        "rfsrfixed" in compact
        or "fsr" in compact
        and "10k" in compact
        and (
            "fracrfsrrfsr+10k" in compact
            or "rfsr/rfsr+10k" in compact
            or "fracrfsrrfsr+rfix" in compact
            or "rfsr/rfsr+rfix" in compact
        )
        or re.search(
            r"(?:fracrfsr|rfsr/)(?:rfsr\+(?:10k|rfix(?:ed)?)|(?:10k|rfix(?:ed)?)\+rfsr)",
            compact,
        )
    )


def _fsr_voltage_example_values(value: str) -> Optional[tuple[float, float]]:
    if not re.search(r"FSR", value, re.I):
        return None
    fsr_match = re.search(
        r"(?:FSR.{0,80}?저항(?:이|은)?|R_?\{?FSR\}?\s*=?)\s*"
        r"(\d+(?:\.\d+)?)\s*kΩ",
        value,
        re.I | re.S,
    )
    fixed_match = re.search(
        r"(?:R_?\{?fixed\}?\s*=\s*|분압\s*회로\s*\()"
        r"(\d+(?:\.\d+)?)\s*kΩ",
        value,
        re.I,
    )
    reference_match = re.search(
        r"(?:V_?\{?ref\}?\s*=\s*|센서\s*전원(?:은|이)?\s*)"
        r"(\d+(?:\.\d+)?)\s*V",
        value,
        re.I,
    )
    has_opencr_reference = bool(re.search(r"(?<![\d.])3\.3\s*V", value, re.I))
    result_match = re.search(
        r"(?:결과|result)\s*:\s*(\d+(?:\.\d+)?)\s*V",
        value,
        re.I,
    )
    if not all((fsr_match, fixed_match, result_match)) or not (
        reference_match or has_opencr_reference
    ):
        return None
    fsr_kohm = float(fsr_match.group(1))
    fixed_kohm = float(fixed_match.group(1))
    reference_volts = 3.3 if has_opencr_reference else float(reference_match.group(1))
    stated_volts = float(result_match.group(1))
    if fsr_kohm <= 0 or fixed_kohm <= 0 or reference_volts <= 0:
        return None
    expected_volts = reference_volts * fixed_kohm / (fsr_kohm + fixed_kohm)
    return expected_volts, stated_volts


def _undersized_power_path_claim(value: str) -> bool:
    if re.search(
        r"메인\s*전원\s*경로가\s*아닌|손가락별\s*퓨즈\s*분기|"
        r"not\s+(?:on|for)\s+(?:the\s+)?main\s+power|finger.{0,20}fused\s+branch",
        value,
        re.I,
    ):
        return False
    return bool(
        re.search(
            r"사용|쓰|쓴|썼|적합|연결|배치|제작|구성|use|used|suit|connect|place|build|fabricat",
            value,
            re.I,
        )
        and re.search(
            r"메인\s*전원|전원\s*제어기|"
            r"(?:독립\s*)?분기\s*전원|"
            r"(?:독립\s*)?(?:\d+(?:\.\d+)?\s*V\s*)?분기.{0,40}(?:양\s*\(\+\)\s*)?출력|"
            r"main\s+power|power\s+controller|branch.{0,40}(?:power|output)",
            value,
            re.I,
        )
    )


def _specification_unit_issue(specification: dict[str, Any]) -> Optional[str]:
    name = str(specification.get("name") or "").strip().lower()
    unit = str(specification.get("unit") or "").strip().lower()
    if any(
        token in name
        for token in ("coefficient", "ratio", "efficiency", "마찰계수", "비율", "효율")
    ) and unit not in {"1", "%", "dimensionless", "무차원"}:
        return "coefficient, ratio, and efficiency must be dimensionless or percent"
    return None


_EVIDENCE_LABEL_ALIASES = {
    "호칭 나사 지름": ("nominal diameter", "diameter of thread"),
    "나사 피치": ("pitch of screw thread", "pitch"),
    "기본 머리 지름": ("basic size", "dk max"),
}


def _measurement_in_evidence(specification: dict[str, Any]) -> bool:
    excerpt = str(specification.get("evidence_excerpt") or "").lower()
    if not excerpt.strip():
        return False
    value = str(specification.get("value") or "").replace(",", "").strip().lower()
    unit = str(specification.get("unit") or "").strip().lower()
    name = str(specification.get("name") or "").strip().lower()
    compact = re.sub(r"\s+", "", excerpt.replace(",", ""))
    compact = compact.replace("·", "").replace("×", "x")
    compact_unit = re.sub(r"\s+", "", unit).replace("·", "").replace("×", "x")
    compact_value = re.sub(r"\s+", "", value)
    if unit in {
        "1", "dimensionless", "무차원", "pin", "pins", "gpio", "gpios",
        "channel", "channels", "piece", "pieces", "pcs", "ea", "개",
    }:
        return compact_value in compact
    if (
        f"{compact_value}{compact_unit}" in compact
        or f"{compact_unit}{compact_value}" in compact
    ):
        return True
    unit_header = re.search(
        rf"\bunit\s*:\s*{re.escape(unit)}\b", excerpt, re.I
    )
    if not unit_header:
        return False
    nearby = excerpt[unit_header.end() : unit_header.end() + 120]
    value_pattern = re.compile(
        rf"(?<![\d.]){re.escape(value)}(?![\d.])", re.I
    )
    conflicting_unit = re.compile(
        r"^\s*(?:mm|cm|km|m|ma|a|vdc|vac|v|w|kw|n(?:[·.]?m)?|kg|g|hz|rpm|ohms?|Ω|°c|deg(?:rees?)?|denier)\b",
        re.I,
    )
    labels = {
        name,
        *_EVIDENCE_LABEL_ALIASES.get(name, ()),
    }
    return any(
        not conflicting_unit.search(nearby[match.end() : match.end() + 16])
        and any(
            label and label in nearby[max(0, match.start() - 100) : match.start()]
            for label in labels
        )
        for match in value_pattern.finditer(nearby)
    )


def _module_bom_consistency_errors(
    modules: list[Any],
    bom: list[Any],
    label: str,
    allowed_source_ids: Optional[set[str]] = None,
) -> list[str]:
    errors: list[str] = []
    architecture_text = " ".join(
        text
        for item in bom
        if isinstance(item, dict)
        for text in _string_values(item)
    )
    if any(
        re.search(token, architecture_text, re.I)
        for token in (r"\bA22E\b", r"\bG7SA\b", r"\bG2R-1\b", r"\bEV200\b")
    ):
        errors.append(
            f"{label}: learner-built E-stop hardware is outside scope; human-accessible use needs qualified dual-channel, manual-reset, EDM validation"
        )
    ev200_parts = [
        item for item in bom
        if isinstance(item, dict) and "ev200" in str(item.get("model") or "").lower()
    ]
    if ev200_parts:
        for item in ev200_parts:
            for specification in item.get("specifications") or []:
                if not isinstance(specification, dict):
                    continue
                if (
                    re.search(r"차단\s*전압|breaking\s+voltage|interrupt(?:ing)?\s+voltage", str(specification.get("name") or ""), re.I)
                    and re.search(r"900", str(specification.get("value") or ""))
                ):
                    errors.append(
                        f"{label}: EV200 900 VDC is switching operating voltage, not standalone breaking voltage"
                    )
        safety_relays = [
            item for item in bom
            if isinstance(item, dict) and "g7sa" in str(item.get("model") or "").lower()
        ]
        interposing_relays = [
            item for item in bom
            if isinstance(item, dict) and "g2r-1" in str(item.get("model") or "").lower()
        ]
        ev200_count = sum(int(item.get("quantity") or 0) for item in ev200_parts)
        if any(str(item.get("model") or "").strip().lower() == "ev200" for item in ev200_parts):
            errors.append(f"{label}: EV200 family name is ambiguous; exact EV200AAANA model required")
        if not safety_relays:
            errors.append(f"{label}: EV200 E-stop architecture missing low-current safety relay")
        if sum(int(item.get("quantity") or 0) for item in interposing_relays) < ev200_count:
            errors.append(f"{label}: EV200 E-stop architecture needs one interposing relay per coil")
        ev200_inrush = max(
            (_named_current_amps(item, ("코일", "돌입")) or 0.0)
            for item in ev200_parts
        )
        interposing_capacity = max(
            (_named_current_amps(item, ("접점", "전류")) or 0.0)
            for item in interposing_relays
        ) if interposing_relays else 0.0
        if ev200_inrush and interposing_capacity < ev200_inrush:
            errors.append(
                f"{label}: interposing relay contact {interposing_capacity:g} A below EV200 coil inrush {ev200_inrush:g} A"
            )
        interposing_coil = max(
            (_named_current_amps(item, ("코일", "전류")) or 0.0)
            for item in interposing_relays
        ) if interposing_relays else 0.0
        safety_capacity = max(
            (_named_current_amps(item, ("접점", "전류")) or 0.0)
            for item in safety_relays
        ) if safety_relays else 0.0
        if interposing_coil and safety_capacity < interposing_coil:
            errors.append(
                f"{label}: safety relay contact {safety_capacity:g} A below interposing coil {interposing_coil:g} A"
            )
        if (
            re.search(r"A22E[^.\n]{0,100}EV200", architecture_text, re.I)
            and re.search(r"직접|direct", architecture_text, re.I)
            and not re.search(r"직접\s*(?:구동|연결)[^.\n]{0,30}(?:금지|하지\s*않)|must\s+not\s+direct", architecture_text, re.I)
        ):
            errors.append(f"{label}: A22E must not directly drive EV200 coils")
    actuators = [
        item for item in bom
        if isinstance(item, dict) and item.get("category") == "actuator"
    ]
    actuator_count = sum(int(item.get("quantity") or 0) for item in actuators)
    actuator_peak = sum(
        (_current_amps(item) or 0.0) * int(item.get("quantity") or 0)
        for item in actuators
    )
    actuator_voltages = [
        value for item in actuators if (value := _voltage_volts(item))
    ]
    max_voltage = max(actuator_voltages) if actuator_voltages else 0.0
    actuator_tokens = {
        token.lower()
        for item in actuators
        for token in (str(item.get("name") or ""), str(item.get("model") or ""))
        if len(token.strip()) >= 3
    }
    bom_component_text = "\n".join(
        " ".join(
            str(item.get(field) or "") for field in ("name", "model", "function")
        ).lower()
        for item in bom
        if isinstance(item, dict)
    )
    bom_citation_ids = {
        str(item.get("id") or "").strip().upper()
        for item in bom
        if isinstance(item, dict) and str(item.get("id") or "").strip()
    }
    undersized_paths = [
        item
        for item in bom
        if isinstance(item, dict)
        and item.get("category") == "wiring"
        and (_current_amps(item) or 0.0) < actuator_peak
    ]

    for index, module in enumerate(modules):
        if not isinstance(module, dict):
            continue
        module_id = str(module.get("id") or index)
        module_data = dict(module)
        module_source_ids = {
            str(source_id) for source_id in (module_data.get("source_ids") or [])
        }
        valid_source_ids = (
            module_source_ids & allowed_source_ids
            if allowed_source_ids is not None and module_source_ids
            else set(allowed_source_ids or module_source_ids)
        )
        quiz = module_data.pop("quiz", [])
        engineering_values = _string_values(module_data)
        for item in quiz:
            if not isinstance(item, dict):
                continue
            engineering_values.append(str(item.get("question") or ""))
            engineering_values.append(str(item.get("explanation") or ""))
            choices = item.get("choices")
            answer_index = item.get("answer_index")
            if (
                isinstance(choices, list)
                and isinstance(answer_index, int)
                and 0 <= answer_index < len(choices)
            ):
                engineering_values.append(str(choices[answer_index]))
        text = "\n".join(engineering_values)
        lowered = text.lower()
        invalid_citations = []
        for raw_token in re.findall(r"\[([^\]\n]{1,80})\]", text):
            if not _citation_like_token(raw_token):
                continue
            citation_ids = [
                token.strip() for token in re.split(r"\s*,\s*", raw_token)
            ]
            if citation_ids and all(
                token in valid_source_ids
                or token.upper() in bom_citation_ids
                for token in citation_ids
            ):
                continue
            invalid_citations.append(raw_token)
        if invalid_citations:
            errors.append(
                f"{label}: module {module_id} has invalid citation token [{invalid_citations[0]}]"
            )
        for sentence in re.split(r"[.!?\n]", text):
            resistance_check = re.search(
                r"저항|무한대|도통|resistan|ohm|continuity", sentence, re.I
            )
            verifies_state = re.search(
                r"확인|검증|측정|점검|verify|confirm|measure|check", sentence, re.I
            )
            claims_deenergized = re.search(
                r"무전원|무전압|전원\s*(?:차단|분리)\s*상태|"
                r"de[- ]?energized|zero\s+voltage",
                sentence,
                re.I,
            )
            connects_power_source = re.search(
                r"(?:전원\s*(?:어댑터|공급기|공급장치)|power\s*(?:adapter|supply))"
                r"[^.!?\n]{0,60}(?:연결|접속|connect|plug)",
                sentence,
                re.I,
            )
            rejects_resistance_check = re.search(
                r"(?:저항|무한대|도통|resistan|ohm|continuity)"
                r"[^.!?\n]{0,100}(?:사용하지\s*않|사용\s*금지|쓰지\s*않|"
                r"증명할\s*수\s*없|금지|do\s+not\s+use|never\s+use|"
                r"cannot\s+(?:verify|confirm|prove)|not\s+(?:proof|evidence))",
                sentence,
                re.I,
            )
            if (
                resistance_check
                and verifies_state
                and (claims_deenergized or connects_power_source)
                and not rejects_resistance_check
            ):
                errors.append(
                    f"{label}: module {module_id} must verify de-energized state in DC voltage mode, not by resistance"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if (
                re.search(
                    r"(?:IEC|ISO|EN|기계\s*안전|안전\s*(?:표준|규격))",
                    sentence,
                    re.I,
                )
                and re.search(r"준수|충족|인증|compli(?:ant|es)|certif", sentence, re.I)
                and not re.search(
                    r"아니|않|미인증|불충족|보장하지|not|non[- ]?certified|does\s+not",
                    sentence,
                    re.I,
                )
            ):
                errors.append(
                    f"{label}: module {module_id} makes unsubstantiated machinery-safety compliance claim"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if (
                re.search(r"비상\s*정지|E[- ]?stop|emergency\s+stop", sentence, re.I)
                and re.search(r"배선|연결|조립|구성|시운전|wire|connect|assembl|commission", sentence, re.I)
                and not re.search(
                    r"금지|하지\s*않|범위\s*밖|별도|자격.{0,12}전문|never|do\s+not|out\s+of\s+scope|qualified",
                    sentence,
                    re.I,
                )
            ):
                errors.append(
                    f"{label}: module {module_id} includes learner E-stop assembly instruction"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if _unsupported_module_estop_reference(sentence):
                errors.append(
                    f"{label}: module {module_id} has unsupported module E-stop reference; use planned shutdown and physical isolation"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if _unsafe_safety_system_requirement(sentence):
                errors.append(
                    f"{label}: module {module_id} requires learner safety-system work"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if _unsafe_emergency_isolation_instruction(sentence):
                errors.append(
                    f"{label}: module {module_id} describes manual isolation as emergency stop; use only planned shutdown and maintenance isolation"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if _unsafe_live_fault_injection(sentence):
                errors.append(
                    f"{label}: module {module_id} requires unsafe live fault injection; use datasheet curve analysis, simulation, or certified current-limited fixture"
                )
                break
        if _reversed_fsr_pulldown_formula(text):
            errors.append(
                f"{label}: module {module_id} has reversed FSR pulldown formula; use Vref x 10 kΩ / (R_FSR + 10 kΩ)"
            )
        fsr_example = _fsr_voltage_example_values(text)
        if fsr_example is not None:
            expected_volts, stated_volts = fsr_example
            if abs(expected_volts - stated_volts) > max(0.05, expected_volts * 0.05):
                errors.append(
                    f"{label}: module {module_id} FSR example states {stated_volts:g} V but calculates to {expected_volts:.1f} V"
                )
        for sentence in re.split(r"[.!?\n]", text):
            if (
                re.search(r"EV200", sentence, re.I)
                and re.search(r"900\s*VDC", sentence, re.I)
                and re.search(r"차단\s*전압|breaking\s+voltage|interrupt(?:ing)?\s+voltage", sentence, re.I)
            ):
                errors.append(
                    f"{label}: module {module_id} treats 900 VDC as breaking voltage instead of switching operating voltage"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if (
                re.search(r"ATOF|퓨즈|fuse", sentence, re.I)
                and re.search(r"즉시|즉각|immediate(?:ly)?|instant(?:ly)?", sentence, re.I)
                and re.search(
                    r"차단|보호|보장|open|interrupt|protect|guarantee", sentence, re.I
                )
                and not re.search(
                    r"(?:즉시|즉각|immediate(?:ly)?|instant(?:ly)?)"
                    r"[^.!?\n]{0,40}(?:아닌|아니|않|not)|"
                    r"\bnot\b[^.!?\n]{0,20}(?:immediate(?:ly)?|instant(?:ly)?)",
                    sentence,
                    re.I,
                )
            ):
                errors.append(
                    f"{label}: module {module_id} claims immediate fuse opening instead of using time-current curve"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if (
                re.search(
                    r"EV200[^.\n]{0,60}(?:코일의\s*NC\s*접점|coil(?:'s|\s+has)\s+(?:an?\s+)?(?:NC|normally[- ]closed)\s+contact)",
                    sentence,
                    re.I,
                )
                and not re.search(r"없|아니|not|no\s+NC", sentence, re.I)
            ):
                errors.append(
                    f"{label}: module {module_id} misattributes an NC contact to EV200 coil; coil has no NC contact"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if (
                re.search(r"A22E", sentence, re.I)
                and re.search(r"EV200", sentence, re.I)
                and re.search(r"직접|direct", sentence, re.I)
                and not re.search(r"금지|하지\s*않|must\s+not|never", sentence, re.I)
            ):
                errors.append(f"{label}: module {module_id} directly drives EV200 coils from A22E")
                break
        for sentence in re.split(r"[.!?\n]", text):
            if (
                re.search(r"비상\s*정지|E[- ]?stop|emergency\s+stop", sentence, re.I)
                and re.search(r"단락|short[- ]?circuit", sentence, re.I)
                and not re.search(
                    r"금지|하지\s*않|아니|없어야|never|do\s+not|must\s+not",
                    sentence,
                    re.I,
                )
            ):
                errors.append(
                    f"{label}: module {module_id} instructs E-stop short-circuit verification instead of open/de-energized verification"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if (
                "ev200" in lowered
                and re.search(r"500\s*A", sentence, re.I)
                and re.search(
                    r"차단\s*정격|차단\s*(?:용량|성능)|breaking\s+(?:rating|capacity)|interrupt(?:ing|ion)?\s+rating",
                    sentence,
                    re.I,
                )
            ):
                errors.append(
                    f"{label}: module {module_id} misstates EV200 500 A continuous-carry rating as breaking rating"
                )
                break
        for sentence in re.split(r"[.!?\n]", text):
            if not re.search(r"FSR|분압|voltage\s+divider", sentence, re.I):
                continue
            if re.search(
                r"초과하지|연결하지|사용하지|분리|금지|never|do\s+not|must\s+not",
                sentence,
                re.I,
            ):
                continue
            context_voltages = [
                float(value)
                for value in re.findall(
                    r"(?<![\d.])(\d+(?:\.\d+)?)\s*V(?![A-Za-z])",
                    sentence,
                    re.I,
                )
            ]
            if any(value > 3.3 for value in context_voltages):
                errors.append(
                    f"{label}: module {module_id} drives an OpenCR FSR divider above 3.3 V: "
                    f"{re.sub(r'\s+', ' ', sentence).strip()[:160]}"
                )
                break
        count_patterns = (
            r"(?:(?:로봇손|전체|총)\s*(?:의\s*)?(?:모터|액추에이터)\s*"
            r"|(?:모터|액추에이터)(?:는|가|의)?\s*(?:전체|총)\s*)"
            r"(\d+)\s*(?:개|대)",
            r"(?:본\s*(?:프로젝트|과정)|로봇손|전체|총)[^\n.]{0,24}?"
            r"(\d+)\s*(?:개|대)(?:의)?[^\n.]{0,36}?(?:모터|액추에이터)",
            r"(?:[A-Za-z][A-Za-z0-9-]{2,})\s+(?:모터|액추에이터)\s*"
            r"(\d+)\s*(?:개|대)",
        )
        claimed_counts = {
            int(match.group(1))
            for pattern in count_patterns[:2]
            for match in re.finditer(pattern, text)
        }
        claimed_counts.update(
            claimed
            for match in re.finditer(count_patterns[2], text)
            if (claimed := int(match.group(1))) != 1
        )
        for claimed in claimed_counts:
            if actuator_count and claimed != actuator_count:
                errors.append(
                    f"{label}: module {module_id} claims {claimed} actuators but BOM contains {actuator_count}"
                )
                break
        if actuator_peak:
            totals = [
                float(value)
                for value in re.findall(
                    r"(?:총|전체|합산)(?:\s*(?:소비)?\s*전류)?[^\d]{0,20}"
                    r"(\d+(?:\.\d+)?)\s*(?:A|amps?|amperes?)(?![A-Za-z])",
                    text,
                    flags=re.IGNORECASE,
                )
            ]
            if totals and max(totals) < actuator_peak:
                errors.append(
                    f"{label}: module {module_id} aggregate current {max(totals):g} A below BOM peak {actuator_peak:g} A"
                )
        if max_voltage and (
            any(token in lowered for token in actuator_tokens)
            or "모터" in text
            or "액추에이터" in text
        ):
            ranges = re.findall(
                r"(\d+(?:\.\d+)?)\s*V\s*[~\-–]\s*(\d+(?:\.\d+)?)\s*V",
                text,
                flags=re.IGNORECASE,
            )
            if any(max(float(left), float(right)) > max_voltage for left, right in ranges):
                errors.append(
                    f"{label}: module {module_id} permits voltage above BOM actuator rating {max_voltage:g} V"
                )
            voltage_issue = False
            for sentence in re.split(r"[.!?\n]", text):
                sentence_lower = sentence.lower()
                has_actuator_context = any(
                    token in sentence_lower for token in actuator_tokens
                ) or any(token in sentence for token in ("모터", "액추에이터"))
                has_supply_context = bool(
                    re.search(r"전원|전압|공급|인가|구동|input\s+voltage|supply", sentence, re.I)
                )
                is_prohibition = bool(
                    re.search(r"금지|사용하지|연결하지|인가하지|초과하지|넘지|아니", sentence)
                )
                if not (has_actuator_context and has_supply_context) or is_prohibition:
                    continue
                claimed_voltages = [
                    float(value)
                    for value in re.findall(
                        r"(?<![\d.])(\d+(?:\.\d+)?)\s*V(?:DC)?(?![A-Za-z])",
                        sentence,
                        flags=re.IGNORECASE,
                    )
                ]
                if any(value > max_voltage for value in claimed_voltages):
                    voltage_issue = True
                    break
            voltage_error = (
                f"{label}: module {module_id} permits voltage above BOM actuator rating {max_voltage:g} V"
            )
            if voltage_issue and voltage_error not in errors:
                errors.append(voltage_error)
        if actuator_peak:
            undersized_issue = False
            for sentence in re.split(r"(?<!\d)[.!?](?!\d)|\n", text):
                if not _undersized_power_path_claim(sentence):
                    continue
                for item in undersized_paths:
                    identifiers = (
                        str(item.get("name") or ""),
                        str(item.get("model") or ""),
                    )
                    if any(
                        identifier and identifier.lower() in sentence.lower()
                        for identifier in identifiers
                    ):
                        errors.append(
                            f"{label}: module {module_id} uses {item.get('model')} below BOM peak {actuator_peak:g} A as main or branch power path"
                        )
                        undersized_issue = True
                        break
                if undersized_issue:
                    break
        for sentence in re.split(r"[.!?\n]", text):
            if not re.search(r"어댑터|전원|출력|power\s*supply|adapter", sentence, re.I):
                continue
            if not re.search(r"병렬|parallel", sentence, re.I):
                continue
            if re.search(
                r"금지|하지\s*않|연결하지|묶지|(?:허용|사용)하지\s*않|"
                r"안\s*(?:됨|된다)|불가|말아야|아니|잘못|오해|피하|방지|"
                r"never|do\s+not|must\s+not|shall\s+not|forbidden|prohibited|avoid",
                sentence,
                re.I,
            ):
                continue
            if re.search(r"(?:하면|할\s*(?:경우|때)|했을\s*때|시)", sentence) and re.search(
                r"위험|순환\s*전류|역류|화재|손상|고장|과열", sentence
            ):
                continue
            if re.search(
                r"병렬(?:로)?\s*(?:묶|연결|합산|구성)"
                r"(?:한다|하여|하고|해\s*(?:사용|공급|운용|합산)|하도록|한다는)"
                r"|parallel(?:ed|ly)?\s+(?:connect|combine|wire)",
                sentence,
                re.I,
            ):
                errors.append(
                    f"{label}: module {module_id} parallels independent power-supply outputs: "
                    f"{re.sub(r'\s+', ' ', sentence).strip()[:160]}"
                )
                break

        required_components = (
            (r"(?:RS[- ]?485|TTL)[^\n.]{0,20}(?:브리지|bridge)|통신\s*브리지", ("브리지", "bridge"), "communication bridge"),
            (r"(?:10\s*k(?:Ω|ohm)?[^\n.]{0,16})?(?:저항|resistor)", ("저항", "resistor"), "resistor"),
            (r"(?:퓨즈|fuse)", ("퓨즈", "fuse"), "fuse"),
            (r"(?:나사산\s*)?인서트|threaded\s+insert|heat[- ]set\s+insert", ("인서트", "insert"), "threaded insert"),
            (r"(?:\d+(?:\.\d+)?\s*mm\s*)?(?:샤프트|shaft)", ("샤프트", "shaft"), "shaft"),
        )
        for pattern, bom_tokens, component_label in required_components:
            if not bom:
                continue
            if not re.search(pattern, text, re.I):
                continue
            if any(token in bom_component_text for token in bom_tokens):
                continue
            errors.append(
                f"{label}: module {module_id} requires {component_label} absent from BOM"
            )
    return errors


def _unsafe_estop_requirement(value: str) -> bool:
    return bool(
        re.search(
            r"비상\s*(?:정지|차단기?)|E[- ]?stop|emergency\s+(?:stop|cutoff)",
            value,
            re.I,
        )
        and re.search(
            r"적용|설치|사용|구성|배선|연결|조립|시운전|작동|동작|시험|검증|확인|"
            r"apply|install|use|wire|connect|assembl|commission|operate|test|verify|check",
            value,
            re.I,
        )
        and not re.search(
            r"금지|하지\s*않|아니|범위\s*밖|별도|자격.{0,12}전문|"
            r"never|do\s+not|out\s+of\s+scope|qualified",
            value,
            re.I,
        )
    )


def _validate_manifest(repo: Path, slug: str, manifest: Any) -> list[str]:
    errors: list[str] = []
    label = f"_data/learn/{slug}.yml"
    if not isinstance(manifest, dict):
        return [f"{label}: manifest must be a mapping"]
    errors.extend(
        f"{label}: {error}" for error in _unsafe_generated_values(manifest)
    )
    if manifest.get("schema_version") != 1:
        errors.append(f"{label}: schema_version must be 1")
    if not manifest.get("curriculum_version"):
        errors.append(f"{label}: curriculum_version missing")
    course = manifest.get("course")
    if not isinstance(course, dict) or course.get("slug") != slug:
        errors.append(f"{label}: course slug mismatch")
        course = {}
    safety_text = " ".join(str(item) for item in course.get("safety_summary") or [])
    required_tools_text = " ".join(str(item) for item in course.get("required_tools") or [])
    if re.search(r"보안경|eye\s+protection|safety\s+(?:glasses|goggles)", safety_text, re.I) and not re.search(
        r"보안경|eye\s+protection|safety\s+(?:glasses|goggles)",
        required_tools_text,
        re.I,
    ):
        errors.append(f"{label}: safety summary eye protection is missing from required tools")
    for index, summary in enumerate(course.get("safety_summary") or []):
        summary = str(summary)
        if _unsafe_estop_requirement(summary):
            errors.append(
                f"{label}: safety summary requires learner E-stop hardware at item {index}"
            )
        if _unsafe_emergency_isolation_instruction(summary):
            errors.append(
                f"{label}: safety summary describes manual isolation as stop at item {index}"
            )
    generation = manifest.get("generation")
    if not isinstance(generation, dict) or not generation.get("run_id"):
        errors.append(f"{label}: generation provenance missing")
        generation = {}
    run_id = str(generation.get("run_id") or "")

    phases = _require_list(manifest, "phases", label, errors)
    modules = _require_list(manifest, "modules", label, errors)
    sources = _require_list(manifest, "sources", label, errors)
    raw_bom = manifest.get("bom")
    if not isinstance(raw_bom, list):
        errors.append(f"{label}: bom must be a list")
        bom: list[Any] = []
    else:
        bom = raw_bom
    capstone = manifest.get("capstone")
    if not isinstance(capstone, dict):
        errors.append(f"{label}: capstone must be a mapping")
    else:
        for field in ("deliverables", "rubric", "safety"):
            for index, criterion in enumerate(capstone.get(field) or []):
                criterion = str(criterion)
                if _unsafe_estop_requirement(criterion):
                    errors.append(
                        f"{label}: capstone requires learner E-stop hardware at {field} item {index}"
                    )
                if _unsafe_safety_system_requirement(criterion):
                    errors.append(
                        f"{label}: capstone requires learner safety-system work at {field} item {index}"
                    )
                if _unsafe_emergency_isolation_instruction(criterion):
                    errors.append(
                        f"{label}: capstone describes manual isolation as stop at {field} item {index}"
                    )

    source_ids: set[str] = set()
    source_types: dict[str, str] = {}
    source_rows: dict[str, dict[str, Any]] = {}
    present_source_types: set[str] = set()
    for source in sources:
        if not isinstance(source, dict):
            errors.append(f"{label}: source must be a mapping")
            continue
        source_id = source.get("id")
        if not isinstance(source_id, str) or not source_id:
            errors.append(f"{label}: source id missing")
            continue
        if source_id in source_ids:
            errors.append(f"{label}: duplicate source {source_id}")
        source_ids.add(source_id)
        source_rows[source_id] = source
        source_type = source.get("type")
        source_types[source_id] = str(source_type or "")
        present_source_types.add(str(source_type or ""))
        if source_type not in SOURCE_TYPES:
            errors.append(f"{label}: source {source_id} has invalid type")
        source_url = str(source.get("url") or "")
        if not source_url.startswith(("https://", "http://")):
            errors.append(f"{label}: source {source_id} URL missing")
        elif not _source_type_authoritative(source_url, str(source_type or "")):
            errors.append(
                f"{label}: source {source_id} URL does not match {source_type} family"
            )

    module_ids: set[str] = set()
    module_slugs: set[str] = set()
    for module in modules:
        if not isinstance(module, dict):
            errors.append(f"{label}: module must be a mapping")
            continue
        module_id = str(module.get("id") or "")
        module_slug = str(module.get("slug") or "")
        if not module_id or module_id in module_ids:
            errors.append(f"{label}: missing or duplicate module id {module_id}")
        if not module_slug or module_slug in module_slugs:
            errors.append(f"{label}: missing or duplicate module slug {module_slug}")
        module_ids.add(module_id)
        module_slugs.add(module_slug)
        used_sources = module.get("source_ids")
        if not isinstance(used_sources, list) or not used_sources:
            errors.append(f"{label}: module {module_id} source_ids missing")
        else:
            for source_id in used_sources:
                if source_id not in source_ids:
                    errors.append(f"{label}: module {module_id} references unknown source {source_id}")
        _check_generated_front_matter(
            repo / "_learn" / slug / f"{module_slug}.md",
            run_id,
            ("layout: learn-module", f"module_id: {module_id}"),
            errors,
        )

    phased_ids: list[str] = []
    for phase in phases:
        if not isinstance(phase, dict) or not isinstance(phase.get("module_ids"), list):
            errors.append(f"{label}: phase module_ids missing")
            continue
        phased_ids.extend(str(module_id) for module_id in phase["module_ids"])
    if set(phased_ids) != module_ids or len(phased_ids) != len(module_ids):
        errors.append(f"{label}: phases must cover every module exactly once")

    for item in bom:
        if not isinstance(item, dict):
            errors.append(f"{label}: BOM item must be a mapping")
            continue
        item_id = str(item.get("id") or "unknown")
        datasheet_id = item.get("datasheet_source_id")
        if datasheet_id not in source_ids:
            errors.append(f"{label}: BOM {item_id} references unknown datasheet")
        elif source_types.get(str(datasheet_id)) not in {
            "datasheet",
            "standard",
            "technical_documentation",
        }:
            errors.append(f"{label}: BOM {item_id} lacks authoritative specification source")
        else:
            if (
                item.get("category") == "safety"
                and source_types.get(str(datasheet_id)) == "standard"
            ):
                errors.append(
                    f"{label}: BOM {item_id} safety cutoff requires a product document"
                )
            authority_error = _bom_source_authority_error(
                item, source_rows[str(datasheet_id)]
            )
            if authority_error:
                errors.append(
                    f"{label}: BOM {item_id} has invalid specification source: "
                    f"{authority_error}"
                )
        specifications = item.get("specifications")
        if not isinstance(specifications, list) or len(specifications) < 2:
            errors.append(f"{label}: BOM {item_id} requires at least two specifications")
        else:
            quantitative = 0
            for specification in specifications:
                if not isinstance(specification, dict) or not all(
                    str(specification.get(key) or "").strip() for key in ("name", "value", "unit")
                ):
                    errors.append(f"{label}: BOM {item_id} has incomplete specification")
                    continue
                value = str(specification.get("value") or "")
                unit = str(specification.get("unit") or "").strip().lower()
                unit_issue = _specification_unit_issue(specification)
                if unit_issue:
                    errors.append(
                        f"{label}: BOM {item_id} has incompatible unit: {unit_issue}"
                    )
                if not _measurement_in_evidence(specification):
                    errors.append(
                        f"{label}: BOM {item_id} specification needs evidence excerpt with exact value and unit"
                    )
                if re.search(r"\d", value) and unit not in {
                    "n/a",
                    "na",
                    "none",
                    "-",
                    "unitless",
                    "1",
                    "dimensionless",
                    "무차원",
                }:
                    quantitative += 1
            if quantitative < 2:
                errors.append(
                    f"{label}: BOM {item_id} requires two numeric specifications with real units"
                )

    actuator_peak = 0.0
    actuator_unit_peak = 0.0
    actuator_count = 0
    missing_actuator_current = False
    power_capacity = 0.0
    missing_power_current = False
    for item in bom:
        if not isinstance(item, dict):
            continue
        category = item.get("category")
        if category not in {"actuator", "power"}:
            continue
        current = _current_amps(item)
        if current is None:
            if category == "actuator":
                missing_actuator_current = True
            else:
                missing_power_current = True
            continue
        aggregate = current * int(item.get("quantity") or 0)
        if category == "actuator":
            actuator_peak += aggregate
            actuator_count += int(item.get("quantity") or 0)
            actuator_unit_peak = max(actuator_unit_peak, current)
        else:
            power_capacity += aggregate
    if missing_actuator_current:
        errors.append(f"{label}: actuator peak/stall current specification missing")
    if missing_power_current:
        errors.append(f"{label}: power rated output current specification missing")
    if actuator_peak and power_capacity and power_capacity < actuator_peak:
        errors.append(
            f"{label}: aggregate power {power_capacity:g} A below actuator peak {actuator_peak:g} A"
        )
    power_parts = [
        item
        for item in bom
        if isinstance(item, dict) and item.get("category") == "power"
    ]
    for item in bom:
        if not isinstance(item, dict) or "ev200" not in str(item.get("model") or "").lower():
            continue
        compatibility = " ".join(str(value) for value in item.get("compatibility") or [])
        if re.search(r"500\s*A", compatibility, re.I) and re.search(
            r"차단\s*정격|차단\s*(?:용량|성능)|breaking\s+(?:rating|capacity)|interrupt(?:ing|ion)?\s+rating",
            compatibility,
            re.I,
        ):
            errors.append(
                f"{label}: EV200 500 A is continuous-carry current, not breaking rating"
            )
    power_branch_count = sum(
        int(item.get("quantity") or 0)
        for item in power_parts
        if int(item.get("quantity") or 0) > 1
    )
    if power_branch_count:
        branch_peak_limits: list[float] = []
        branch_supply_limits: list[float] = []
        for item in power_parts:
            if int(item.get("quantity") or 0) <= 1:
                continue
            compatibility = " ".join(
                str(value) for value in item.get("compatibility") or []
            ).lower()
            if "독립" not in compatibility or not re.search(
                r"병렬.{0,12}(?:금지|않)|never.{0,12}parallel", compatibility, re.I
            ):
                errors.append(
                    f"{label}: multiple power supplies must use isolated branches and prohibit output paralleling"
                )
            allocations = re.search(
                r"(?:\d+\s*대\s*/\s*)+\d+\s*대", compatibility
            )
            if not allocations:
                errors.append(
                    f"{label}: power branch actuator allocation missing for multiple supplies"
                )
            else:
                branch_loads = [
                    int(value) for value in re.findall(r"\d+", allocations.group())
                ]
                supply_count = int(item.get("quantity") or 0)
                if len(branch_loads) != supply_count:
                    errors.append(
                        f"{label}: power BOM has {supply_count} supplies but allocation declares {len(branch_loads)} branches"
                    )
                if actuator_count and sum(branch_loads) != actuator_count:
                    errors.append(
                        f"{label}: branch allocation covers {sum(branch_loads)} actuators but BOM contains {actuator_count}"
                    )
                per_supply_current = _current_amps(item) or 0.0
                if branch_loads and actuator_unit_peak:
                    branch_peak_limits.append(max(branch_loads) * actuator_unit_peak)
                if per_supply_current:
                    branch_supply_limits.append(per_supply_current)
                overloaded = [
                    load
                    for load in branch_loads
                    if actuator_unit_peak
                    and per_supply_current
                    and load * actuator_unit_peak > per_supply_current
                ]
                if overloaded:
                    errors.append(
                        f"{label}: branch load {max(overloaded)} x {actuator_unit_peak:g} A exceeds per-supply capacity {per_supply_current:g} A"
                    )
        fuse_parts = [
            item
            for item in bom
            if isinstance(item, dict)
            and (
                re.search(
                    r"퓨즈|fuse",
                    " ".join(
                        str(item.get(field) or "")
                        for field in ("name", "model", "function")
                    ),
                    re.I,
                )
                and not re.search(
                    r"퓨즈\s*홀더|fuse\s*holder",
                    " ".join(
                        str(item.get(field) or "")
                        for field in ("name", "model", "function")
                    ),
                    re.I,
                )
            )
        ]
        fuse_count = sum(int(item.get("quantity") or 0) for item in fuse_parts)
        if fuse_count < power_branch_count:
            errors.append(
                f"{label}: {power_branch_count} independent power branches lack matching fuse BOM units"
            )
        fuse_holder_parts = [
            item
            for item in bom
            if isinstance(item, dict)
            and re.search(
                r"퓨즈\s*홀더|fuse\s*holder",
                " ".join(
                    str(item.get(field) or "")
                    for field in ("name", "model", "function")
                ),
                re.I,
            )
        ]
        fuse_holder_count = sum(
            int(item.get("quantity") or 0) for item in fuse_holder_parts
        )
        if fuse_holder_count < power_branch_count:
            errors.append(
                f"{label}: {power_branch_count} independent power branches lack matching fuse-holder BOM units"
            )
        fuse_ratings = [
            rating for item in fuse_parts if (rating := _current_amps(item))
        ]
        if fuse_parts and len(fuse_ratings) != len(fuse_parts):
            errors.append(f"{label}: every branch fuse needs an explicit current rating")
        if fuse_ratings and branch_peak_limits:
            branch_peak = max(branch_peak_limits)
            if any(rating <= branch_peak for rating in fuse_ratings):
                errors.append(
                    f"{label}: fuse rating must exceed branch peak {branch_peak:g} A"
                )
        if fuse_ratings and branch_supply_limits:
            supply_limit = min(branch_supply_limits)
            if any(rating >= supply_limit for rating in fuse_ratings):
                errors.append(
                    f"{label}: fuse rating must stay below per-supply capacity {supply_limit:g} A"
                )
    cutoff_parts = [
        item
        for item in bom
        if isinstance(item, dict)
        and item.get("category") == "safety"
        and re.search(
            r"비상\s*정지|emergency\s+stop|E[- ]?stop|비상\s*차단|emergency\s+cutoff",
            " ".join(str(item.get(field) or "") for field in ("name", "function", "model")),
            re.I,
        )
    ]
    safety_capacity = max(
        (
            (_current_amps(item) or 0.0) * int(item.get("quantity") or 0)
            for item in cutoff_parts
        ),
        default=0.0,
    )
    if actuator_peak and cutoff_parts and safety_capacity < actuator_peak:
        errors.append(
            f"{label}: emergency cutoff {safety_capacity:g} A below actuator peak {actuator_peak:g} A"
        )

    tools = " ".join(str(tool) for tool in course.get("required_tools") or []).lower()
    for item in bom:
        if not isinstance(item, dict) or item.get("category") != "structure":
            continue
        material = " ".join(
            [
                str(item.get("name") or ""),
                str(item.get("model") or ""),
                " ".join(str(row) for row in item.get("compatibility") or []),
            ]
        ).lower()
        if ("resin" in material or "레진" in material) and not any(
            token in tools for token in ("sla", "msla", "광경화", "resin")
        ):
            errors.append(f"{label}: resin structure material lacks SLA/MSLA required tool")

    course_type = str(course.get("course_type") or "build_project")
    requires_bom = course_type == "build_project"
    if course_type not in {"academic", "build_project"}:
        errors.append(f"{label}: invalid course_type {course_type}")
    if requires_bom and len(bom) < 10:
        errors.append(f"{label}: buildable BOM requires at least 10 item types")
    present_categories = {
        str(item.get("category") or "") for item in bom if isinstance(item, dict)
    }
    for category in sorted(BOM_CATEGORIES - present_categories) if requires_bom else ():
        errors.append(f"{label}: buildable BOM missing category {category}")

    required_source_types = ("university", "paper", "patent") if requires_bom else ("university", "paper")
    for source_type in required_source_types:
        if source_type not in present_source_types:
            errors.append(f"{label}: sources missing required family {source_type}")

    errors.extend(
        _module_bom_consistency_errors(
            modules, bom, label, allowed_source_ids=source_ids
        )
    )

    _check_generated_front_matter(
        repo / "_learn" / slug / "index.md",
        run_id,
        ("layout: learn-course", f"course_slug: {slug}"),
        errors,
    )
    expected_pages = {"index.md", *(f"{slug}.md" for slug in module_slugs)}
    course_dir = repo / "_learn" / slug
    if course_dir.is_dir():
        for page_path in course_dir.glob("*.md"):
            if page_path.name in expected_pages:
                continue
            if _front_matter(page_path).get("generated_by") == "mindtickle-studio":
                errors.append(f"{page_path}: orphan Studio-generated module")
    return errors


def validate_repo(repo: Path, site_dir: Optional[Path] = None) -> list[str]:
    repo = repo.resolve()
    errors: list[str] = []
    index_path = repo / "_data" / "learn" / "courses.yml"
    if not index_path.is_file():
        errors.append(f"{index_path}: course index missing")
        entries: list[Any] = []
    else:
        try:
            loaded = _load_yaml(index_path)
            entries = loaded if isinstance(loaded, list) else []
            if not isinstance(loaded, list):
                errors.append(f"{index_path}: course index must be a list")
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(f"{index_path}: cannot parse YAML: {error}")
            entries = []

    seen: set[str] = set()
    for entry in entries:
        slug = entry.get("slug") if isinstance(entry, dict) else None
        if not isinstance(slug, str) or not slug:
            errors.append(f"{index_path}: index entry slug missing")
            continue
        if slug in seen:
            errors.append(f"{index_path}: duplicate course {slug}")
            continue
        seen.add(slug)
        manifest_path = repo / "_data" / "learn" / f"{slug}.yml"
        if not manifest_path.is_file():
            errors.append(f"{manifest_path}: manifest missing")
            continue
        try:
            errors.extend(_validate_manifest(repo, slug, _load_yaml(manifest_path)))
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(f"{manifest_path}: cannot parse YAML: {error}")

    if site_dir is not None:
        learn_site = site_dir.resolve() / "learn"
        if not learn_site.is_dir():
            errors.append(f"{learn_site}: built Learn directory missing")
        else:
            for html in learn_site.rglob("*.html"):
                text = html.read_text(encoding="utf-8")
                for marker in AD_MARKERS:
                    if marker in text:
                        errors.append(f"{html}: advertising marker {marker}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--site", type=Path)
    args = parser.parse_args()
    errors = validate_repo(args.repo, args.site)
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print("Learn validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
