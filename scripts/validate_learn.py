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
    r"<\s*/?\s*[a-z][^>]*>|\bon[a-z]+\s*=|(?:javascript|vbscript|data)\s*:",
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


def _specification_unit_issue(specification: dict[str, Any]) -> Optional[str]:
    name = str(specification.get("name") or "").strip().lower()
    unit = str(specification.get("unit") or "").strip().lower()
    if any(
        token in name
        for token in ("coefficient", "ratio", "efficiency", "마찰계수", "비율", "효율")
    ) and unit not in {"1", "%", "dimensionless", "무차원"}:
        return "coefficient, ratio, and efficiency must be dimensionless or percent"
    return None


def _measurement_in_evidence(specification: dict[str, Any]) -> bool:
    excerpt = str(specification.get("evidence_excerpt") or "").lower()
    if not excerpt.strip():
        return False
    value = str(specification.get("value") or "").replace(",", "").strip().lower()
    unit = str(specification.get("unit") or "").strip().lower()
    compact = re.sub(r"\s+", "", excerpt.replace(",", ""))
    compact = compact.replace("·", "").replace("×", "x")
    compact_unit = re.sub(r"\s+", "", unit).replace("·", "").replace("×", "x")
    compact_value = re.sub(r"\s+", "", value)
    if unit in {
        "1", "dimensionless", "무차원", "pin", "pins", "gpio", "gpios",
        "channel", "channels", "piece", "pieces", "pcs", "ea", "개",
    }:
        return compact_value in compact
    if re.search(rf"\bunit\s*:\s*{re.escape(unit)}\b", excerpt, re.I):
        return compact_value in compact
    return (
        f"{compact_value}{compact_unit}" in compact
        or f"{compact_unit}{compact_value}" in compact
    )


def _module_bom_consistency_errors(
    modules: list[Any], bom: list[Any], label: str
) -> list[str]:
    errors: list[str] = []
    actuators = [
        item for item in bom
        if isinstance(item, dict) and item.get("category") == "actuator"
    ]
    if not actuators:
        return errors
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
        text = "\n".join(_string_values(module))
        lowered = text.lower()
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
        for match in re.finditer(
            r"(?:(?:로봇손|전체|총)\s*(?:의\s*)?(?:모터|액추에이터)\s*"
            r"|(?:모터|액추에이터)(?:는|가|의)?\s*(?:전체|총)\s*)"
            r"(\d+)\s*(?:개|대)",
            text,
        ):
            claimed = int(match.group(1))
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
        if actuator_peak and "메인 전원" in text:
            for item in undersized_paths:
                identifiers = (str(item.get("name") or ""), str(item.get("model") or ""))
                if any(identifier and identifier.lower() in lowered for identifier in identifiers):
                    errors.append(
                        f"{label}: module {module_id} uses {item.get('model')} below BOM peak {actuator_peak:g} A as main power path"
                    )
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
            if not re.search(pattern, text, re.I):
                continue
            if any(token in bom_component_text for token in bom_tokens):
                continue
            errors.append(
                f"{label}: module {module_id} requires {component_label} absent from BOM"
            )
    return errors


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
    if not isinstance(manifest.get("capstone"), dict):
        errors.append(f"{label}: capstone must be a mapping")

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
    power_branch_count = sum(
        int(item.get("quantity") or 0)
        for item in power_parts
        if int(item.get("quantity") or 0) > 1
    )
    if power_branch_count:
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
        fuse_count = sum(
            int(item.get("quantity") or 0)
            for item in bom
            if isinstance(item, dict)
            and re.search(
                r"퓨즈|fuse",
                " ".join(str(item.get(field) or "") for field in ("name", "model", "function")),
                re.I,
            )
        )
        if fuse_count < power_branch_count:
            errors.append(
                f"{label}: {power_branch_count} independent power branches lack matching fuse BOM units"
            )
    safety_capacity = max(
        (
            (_current_amps(item) or 0.0) * int(item.get("quantity") or 0)
            for item in bom
            if isinstance(item, dict) and item.get("category") == "safety"
        ),
        default=0.0,
    )
    if actuator_peak and safety_capacity < actuator_peak:
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

    errors.extend(_module_bom_consistency_errors(modules, bom, label))

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
