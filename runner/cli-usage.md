# CLI Usage

## Purpose

This document shows a simple end-to-end CLI workflow for the BCH Defender runner.

The current flow is:

1. create a run artifact
2. prefill baseline and candidate responses
3. apply scoring patches
4. recompute the run summary

## Step 1: Create a run artifact

Example:

```bash
python3 runner/minimal_runner.py runner/run-manifest.example.json --output-dir runner_runs
```

This creates a JSON run artifact containing:

- run metadata
- bundled prompt text
- bundled rubric text
- case scaffolding for the selected dataset slice

## Step 2: Prefill responses

Example:

```bash
python3 runner/prefill_responses.py runner_runs/support-verification-v1-example.json \
  --baseline runner/prefill.example.baseline.json \
  --candidate runner/prefill.example.candidate.json
```

This injects response text into matching case ids.

## Step 3: Apply scoring helper

Example:

```bash
python3 runner/scoring_helpers.py runner_runs/support-verification-v1-example.json \
  --scores runner/scoring.example.json
```

This applies:

- numeric score patches
- automatic failure patches
- notes
- recomputed summary fields

## Step 4: Review the artifact

The resulting artifact can now be inspected manually or used by future tooling.

## Example Workflow Summary

A minimal test cycle looks like this:

```bash
python3 runner/minimal_runner.py runner/run-manifest.example.json --output-dir runner_runs
python3 runner/prefill_responses.py runner_runs/support-verification-v1-example.json --baseline runner/prefill.example.baseline.json --candidate runner/prefill.example.candidate.json
python3 runner/scoring_helpers.py runner_runs/support-verification-v1-example.json --scores runner/scoring.example.json
```

## Notes

This workflow is intentionally lightweight.

It does not yet perform direct model inference. Instead, it provides a structured path for:

- artifact generation
- response injection
- scoring
- summary recomputation

That makes it easier to add stronger automation later without redesigning the runner structure.
