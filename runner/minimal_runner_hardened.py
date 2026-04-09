#!/usr/bin/env python3
"""Hardened minimal runner implementation for BCH Defender.

This variant keeps the original lightweight, provider-agnostic behavior while
adding safer path handling, run-id sanitization, and overwrite protection.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any


SAFE_RUN_ID_RE = re.compile(r"[^A-Za-z0-9._-]+")


def ensure_within_root(path: Path, root: Path) -> Path:
    resolved = path.resolve()
    root_resolved = root.resolve()
    if root_resolved not in (resolved, *resolved.parents):
        raise ValueError(f"Path escapes repository root: {path}")
    return resolved


def safe_repo_path(raw_path: str, root: Path) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        raise ValueError(f"Absolute paths are not allowed: {raw_path}")
    if ".." in path.parts:
        raise ValueError(f"Parent directory traversal is not allowed: {raw_path}")
    return ensure_within_root(root / path, root)


def sanitize_run_id(run_id: str) -> str:
    cleaned = SAFE_RUN_ID_RE.sub("-", run_id.strip()).strip(".-")
    if not cleaned:
        raise ValueError("run_id is empty or unsafe after sanitization")
    return cleaned


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_case_result(case: dict[str, Any]) -> dict[str, Any]:
    return {
        "case_id": case.get("id"),
        "category": case.get("category"),
        "baseline_response": None,
        "candidate_response": None,
        "scores": {
            "baseline": {},
            "candidate": {},
        },
        "automatic_failures": {
            "baseline": [],
            "candidate": [],
        },
        "notes": "",
        "source_case": case,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Hardened BCH Defender eval runner")
    parser.add_argument("manifest", type=Path, help="Path to run manifest JSON")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("runner_runs"),
        help="Directory for generated run artifacts",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing output artifact if present",
    )
    args = parser.parse_args()

    repo_root = Path.cwd().resolve()
    manifest_path = ensure_within_root(args.manifest.resolve(), repo_root)
    manifest = load_json(manifest_path)

    prompt_paths = [safe_repo_path(p, repo_root) for p in manifest.get("prompt_target", [])]
    dataset_paths = [safe_repo_path(p, repo_root) for p in manifest.get("dataset_slice", [])]
    rubric_paths = [safe_repo_path(p, repo_root) for p in manifest.get("rubrics_used", [])]

    prompt_bundle = {str(p.relative_to(repo_root)): read_text(p) for p in prompt_paths}
    rubric_bundle = {str(p.relative_to(repo_root)): read_text(p) for p in rubric_paths}

    cases: list[dict[str, Any]] = []
    for dataset_path in dataset_paths:
        cases.extend(load_jsonl(dataset_path))

    case_results = [build_case_result(case) for case in cases]

    raw_run_id = manifest.get("run_id") or f"run-{dt.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}"
    run_id = sanitize_run_id(raw_run_id)
    artifact = {
        "run_id": run_id,
        "date": dt.datetime.utcnow().strftime("%Y-%m-%d"),
        "prompt_target": manifest.get("prompt_target", []),
        "dataset_slice": manifest.get("dataset_slice", []),
        "rubrics_used": manifest.get("rubrics_used", []),
        "baseline_version": manifest.get("baseline_version"),
        "candidate_version": manifest.get("candidate_version"),
        "summary": {
            "average_score_delta": {},
            "automatic_failure_counts": {
                "baseline": 0,
                "candidate": 0,
            },
            "improvement_areas": [],
            "regression_areas": [],
            "decision": "revise_and_retest",
        },
        "prompt_bundle": prompt_bundle,
        "rubric_bundle": rubric_bundle,
        "case_results": case_results,
    }

    output_dir = ensure_within_root((repo_root / args.output_dir).resolve(), repo_root)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{run_id}.json"
    if output_path.exists() and not args.force:
        raise FileExistsError(
            f"Refusing to overwrite existing artifact without --force: {output_path}"
        )

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(artifact, f, ensure_ascii=False, indent=2)

    print(f"Created run artifact: {output_path}")
    print(f"Loaded {len(case_results)} cases")


if __name__ == "__main__":
    main()
