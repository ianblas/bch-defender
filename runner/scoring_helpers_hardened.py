#!/usr/bin/env python3
"""Hardened scoring helper for BCH Defender run artifacts."""

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


def ensure_within_root(path: Path, root: Path) -> Path:
    resolved = path.resolve()
    root_resolved = root.resolve()
    if root_resolved not in (resolved, *resolved.parents):
        raise ValueError(f"Path escapes repository root: {path}")
    return resolved


def safe_repo_path(path: Path, root: Path) -> Path:
    if path.is_absolute():
        return ensure_within_root(path, root)
    if ".." in path.parts:
        raise ValueError(f"Parent directory traversal is not allowed: {path}")
    return ensure_within_root(root / path, root)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def validate_numeric_scores(scores: dict[str, Any]) -> None:
    for metric, value in scores.items():
        if metric not in NUMERIC_FIELDS:
            raise ValueError(f"Unknown score metric: {metric}")
        if not isinstance(value, (int, float)):
            raise ValueError(f"Score for {metric} must be numeric")


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
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow overwriting the output file when --output is used",
    )
    args = parser.parse_args()

    repo_root = Path.cwd().resolve()
    artifact_path = safe_repo_path(args.artifact, repo_root)
    artifact = load_json(artifact_path)
    score_patch = load_json(safe_repo_path(args.scores, repo_root)) if args.scores else {}

    if score_patch:
        by_case = {case_result.get("case_id"): case_result for case_result in artifact.get("case_results", [])}
        for case_id, patch in score_patch.items():
            if case_id not in by_case:
                continue
            case_result = by_case[case_id]
            if "scores" in patch:
                for side in ("baseline", "candidate"):
                    if side in patch["scores"]:
                        validate_numeric_scores(patch["scores"][side])
                        case_result.setdefault("scores", {}).setdefault(side, {}).update(patch["scores"][side])
            if "automatic_failures" in patch:
                for side in ("baseline", "candidate"):
                    if side in patch["automatic_failures"]:
                        failures = patch["automatic_failures"][side]
                        if not isinstance(failures, list):
                            raise ValueError(f"automatic_failures.{side} must be a list")
                        case_result.setdefault("automatic_failures", {}).setdefault(side, [])
                        case_result["automatic_failures"][side] = failures
            if "notes" in patch:
                case_result["notes"] = patch["notes"]

    recompute_summary(artifact)
    output_path = safe_repo_path(args.output, repo_root) if args.output else artifact_path
    if output_path.exists() and output_path != artifact_path and not args.force:
        raise FileExistsError(
            f"Refusing to overwrite existing output without --force: {output_path}"
        )

    save_json(output_path, artifact)
    print(f"Wrote scored artifact: {output_path}")


if __name__ == "__main__":
    main()
