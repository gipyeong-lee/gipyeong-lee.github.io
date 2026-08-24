#!/usr/bin/env python3
"""Validate Studio-generated Learn files and built no-ad pages."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any, Optional


AD_MARKERS = ("adsbygoogle", "pagead2.googlesyndication.com", "ad-slot")
SOURCE_TYPES = {
    "university",
    "paper",
    "patent",
    "standard",
    "datasheet",
    "textbook",
    "technical_documentation",
}


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


def _validate_manifest(repo: Path, slug: str, manifest: Any) -> list[str]:
    errors: list[str] = []
    label = f"_data/learn/{slug}.yml"
    if not isinstance(manifest, dict):
        return [f"{label}: manifest must be a mapping"]
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
    bom = _require_list(manifest, "bom", label, errors)
    if not isinstance(manifest.get("capstone"), dict):
        errors.append(f"{label}: capstone must be a mapping")

    source_ids: set[str] = set()
    source_types: dict[str, str] = {}
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
        source_type = source.get("type")
        source_types[source_id] = str(source_type or "")
        if source_type not in SOURCE_TYPES:
            errors.append(f"{label}: source {source_id} has invalid type")
        if not str(source.get("url") or "").startswith(("https://", "http://")):
            errors.append(f"{label}: source {source_id} URL missing")

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
        elif source_types.get(str(datasheet_id)) != "datasheet":
            errors.append(f"{label}: BOM {item_id} source is not a datasheet")
        specifications = item.get("specifications")
        if not isinstance(specifications, list) or not specifications:
            errors.append(f"{label}: BOM {item_id} specifications missing")
        else:
            for specification in specifications:
                if not isinstance(specification, dict) or not all(
                    str(specification.get(key) or "").strip() for key in ("name", "value", "unit")
                ):
                    errors.append(f"{label}: BOM {item_id} has incomplete specification")

    _check_generated_front_matter(
        repo / "_learn" / slug / "index.md",
        run_id,
        ("layout: learn-course", f"course_slug: {slug}"),
        errors,
    )
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
