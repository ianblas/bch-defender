#!/usr/bin/env python3
"""Minimal runner implementation for BCH Defender.

This runner is intentionally lightweight and provider-agnostic.
It does not call a model by itself. Instead, it:

- loads a run manifest
- loads dataset cases from JSONL
- records prompt and rubric references
- creates a structured run artifact with per-case scaffolding

This gives BCH Defender a concrete starting point for evaluation runs
without locking the repo into a specific model SDK or runtime.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any


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
    parser = argparse.ArgumentParser(description="Minimal BCH Defender eval runner")
    parser.add_argument("manifest", type=Path, help="Path to run manifest JSON")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("runner_runs"),
        help="Directory for generated run artifacts",
    )
    args = parser.parse_args()

    manifest = load_json(args.manifest)

    prompt_paths = [Path(p) for p in manifest.get("prompt_target", [])]
    dataset_paths = [Path(p) for p in manifest.get("dataset_slice", [])]
    rubric_paths = [Path(p) for p in manifest.get("rubrics_used", [])]

    prompt_bundle = {str(p): read_text(p) for p in prompt_paths}
    rubric_bundle = {str(p): read_text(p) for p in rubric_paths}

    cases: list[dict[str, Any]] = []
    for dataset_path in dataset_paths:
        cases.extend(load_jsonl(dataset_path))

    case_results = [build_case_result(case) for case in cases]

    run_id = manifest.get("run_id") or f"run-{dt.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}"
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

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / f"{run_id}.json"
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(artifact, f, ensure_ascii=False, indent=2)

    print(f"Created run artifact: {output_path}")
    print(f"Loaded {len(case_results)} cases")


if __name__ == "__main__":
    main()
