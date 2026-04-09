#!/usr/bin/env python3
"""Hardened response prefill helper for BCH Defender run artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


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


def main() -> None:
    parser = argparse.ArgumentParser(description="Prefill responses in a BCH Defender run artifact")
    parser.add_argument("artifact", type=Path, help="Path to run artifact JSON")
    parser.add_argument("--baseline", type=Path, help="JSON mapping case_id to baseline response")
    parser.add_argument("--candidate", type=Path, help="JSON mapping case_id to candidate response")
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
    baseline_bundle = load_json(safe_repo_path(args.baseline, repo_root)) if args.baseline else {}
    candidate_bundle = load_json(safe_repo_path(args.candidate, repo_root)) if args.candidate else {}

    for case_result in artifact.get("case_results", []):
        case_id = case_result.get("case_id")
        if case_id in baseline_bundle:
            case_result["baseline_response"] = baseline_bundle[case_id]
        if case_id in candidate_bundle:
            case_result["candidate_response"] = candidate_bundle[case_id]

    output_path = safe_repo_path(args.output, repo_root) if args.output else artifact_path
    if output_path.exists() and output_path != artifact_path and not args.force:
        raise FileExistsError(
            f"Refusing to overwrite existing output without --force: {output_path}"
        )

    save_json(output_path, artifact)
    print(f"Wrote updated artifact: {output_path}")


if __name__ == "__main__":
    main()
