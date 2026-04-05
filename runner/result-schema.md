# Result Schema

## Purpose

This document defines the shape of evaluation results for BCH Defender runner v1.

The schema is intentionally simple and framework-agnostic.

## Run-Level Result

A run-level result should include:

- `run_id`
- `date`
- `prompt_target`
- `dataset_slice`
- `rubrics_used`
- `baseline_version`
- `candidate_version`
- `summary`
- `case_results`

## Suggested Run-Level Shape

```json
{
  "run_id": "support-verification-v2-001",
  "date": "2026-04-01",
  "prompt_target": ["prompts/system.md", "prompts/support.md"],
  "dataset_slice": ["datasets/support-gold.jsonl"],
  "rubrics_used": ["evaluations/support-rubric.md"],
  "baseline_version": "baseline-a",
  "candidate_version": "candidate-b",
  "summary": {},
  "case_results": []
}
```

## Case-Level Result

Each case result should include:

- `case_id`
- `category`
- `baseline_response`
- `candidate_response`
- `scores`
- `automatic_failures`
- `notes`

## Suggested Case-Level Shape

```json
{
  "case_id": "support_payment_not_received_001",
  "category": "support",
  "baseline_response": "...",
  "candidate_response": "...",
  "scores": {
    "baseline": {
      "issue_identification": 4,
      "verification_quality": 3,
      "operational_usefulness": 4,
      "bch_alignment": 4,
      "safety": 5
    },
    "candidate": {
      "issue_identification": 5,
      "verification_quality": 5,
      "operational_usefulness": 5,
      "bch_alignment": 5,
      "safety": 5
    }
  },
  "automatic_failures": {
    "baseline": [],
    "candidate": []
  },
  "notes": "Candidate improved verification language without reducing clarity."
}
```

## Summary Block

The summary should capture:

- average score deltas
n- failure counts
- improvement areas
- regression areas
- final decision

## Suggested Summary Shape

```json
{
  "average_score_delta": {
    "issue_identification": 1.0,
    "verification_quality": 1.5,
    "operational_usefulness": 0.5,
    "bch_alignment": 0.5,
    "safety": 0.0
  },
  "automatic_failure_counts": {
    "baseline": 1,
    "candidate": 0
  },
  "improvement_areas": ["verification_quality", "issue_identification"],
  "regression_areas": [],
  "decision": "accept"
}
```

## Decision Values

Recommended values:

- `accept`
- `reject`
- `revise_and_retest`

## Rule

A higher average score is not enough by itself.

Automatic failures and major regressions should remain visible in the result schema.
