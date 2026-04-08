#!/usr/bin/env python3
"""Prefill baseline and candidate responses inside an existing BCH Defender run artifact.

This helper complements the minimal runner by taking an existing run artifact and
injecting response text from one or two JSON files keyed by case_id.

Example response bundle shape:
{
  "support_payment_not_received_001": "Response text here",
  "support_fake_payment_proof_001": "Another response"
}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


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
    args = parser.parse_args()

    artifact = load_json(args.artifact)
    baseline_bundle = load_json(args.baseline) if args.baseline else {}
    candidate_bundle = load_json(args.candidate) if args.candidate else {}

    for case_result in artifact.get("case_results", []):
        case_id = case_result.get("case_id")
        if case_id in baseline_bundle:
            case_result["baseline_response"] = baseline_bundle[case_id]
        if case_id in candidate_bundle:
            case_result["candidate_response"] = candidate_bundle[case_id]

    output_path = args.output or args.artifact
    save_json(output_path, artifact)
    print(f"Wrote updated artifact: {output_path}")


if __name__ == "__main__":
    main()
