#!/usr/bin/env python3
"""Scoring helpers for BCH Defender run artifacts.

This helper adds a lightweight way to:
- insert numeric rubric scores for baseline/candidate per case
- record automatic failures
- compute simple run-level summary counts and averages

It is intentionally minimal and does not attempt to fully automate judgment.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


NUMERIC_FIELDS = [
    "issue_identification",
    "verification_quality",
    "operational_usefulness",
    "bch_alignment",
    "safety",
    "objection_identification",
    "honesty_about_tradeoffs",
    "tone_quality",
    "bch_framing_quality",
    "practical_persuasiveness",
    "concept_accuracy",
    "clarity",
    "simplicity",
    "bch_specificity",
    "cross_turn_consistency",
    "context_retention",
    "escalation_stability",
    "distinction_quality",
    "verification_discipline",
    "panic_reduction",
    "policy_clarity",
    "operational_realism",
    "separation_of_roles",
    "safety_and_process_discipline",
]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def recompute_summary(artifact: dict[str, Any]) -> None:
    baseline_failures = 0
    candidate_failures = 0
    baseline_scores: dict[str, list[float]] = {}
    candidate_scores: dict[str, list[float]] = {}

    for case_result in artifact.get("case_results", []):
        baseline_failures += len(case_result.get("automatic_failures", {}).get("baseline", []))
        candidate_failures += len(case_result.get("automatic_failures", {}).get("candidate", []))

        for metric, value in case_result.get("scores", {}).get("baseline", {}).items():
            if isinstance(value, (int, float)):
                baseline_scores.setdefault(metric, []).append(float(value))
        for metric, value in case_result.get("scores", {}).get("candidate", {}).items():
            if isinstance(value, (int, float)):
                candidate_scores.setdefault(metric, []).append(float(value))

    deltas: dict[str, float] = {}
    for metric in set(baseline_scores) | set(candidate_scores):
        deltas[metric] = round(average(candidate_scores.get(metric, [])) - average(baseline_scores.get(metric, [])), 3)

    artifact.setdefault("summary", {})["average_score_delta"] = deltas
    artifact["summary"]["automatic_failure_counts"] = {
        "baseline": baseline_failures,
        "candidate": candidate_failures,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Score and summarize BCH Defender run artifacts")
    parser.add_argument("artifact", type=Path, help="Path to run artifact JSON")
    parser.add_argument("--scores", type=Path, help="Optional JSON patch with case_id keyed score updates")
    parser.add_argument("--output", type=Path, help="Optional output path; overwrites artifact if omitted")
    args = parser.parse_args()

    artifact = load_json(args.artifact)
    score_patch = load_json(args.scores) if args.scores else {}

    if score_patch:
        by_case = {case_result.get("case_id"): case_result for case_result in artifact.get("case_results", [])}
        for case_id, patch in score_patch.items():
            if case_id not in by_case:
                continue
            case_result = by_case[case_id]
            if "scores" in patch:
                for side in ("baseline", "candidate"):
                    if side in patch["scores"]:
                        case_result.setdefault("scores", {}).setdefault(side, {}).update(patch["scores"][side])
            if "automatic_failures" in patch:
                for side in ("baseline", "candidate"):
                    if side in patch["automatic_failures"]:
                        case_result.setdefault("automatic_failures", {}).setdefault(side, [])
                        case_result["automatic_failures"][side] = patch["automatic_failures"][side]
            if "notes" in patch:
                case_result["notes"] = patch["notes"]

    recompute_summary(artifact)
    output_path = args.output or args.artifact
    save_json(output_path, artifact)
    print(f"Wrote scored artifact: {output_path}")


if __name__ == "__main__":
    main()
