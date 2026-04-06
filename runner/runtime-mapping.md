# Runtime Mapping

## Purpose

This document defines a more concrete mapping between BCH Defender's routing, prompt layers, datasets, and the minimal runner.

## Core Mapping

### Support Route

Prompt stack:

- `prompts/system.md`
- `prompts/support.md`
- add `prompts/escalation.md` when routing includes escalation

Typical datasets:

- `datasets/support-gold.jsonl`
- `datasets/support-gold-extended.jsonl`
- `datasets/adversarial-cases.jsonl`
- `datasets/confusion-cases.jsonl`
- `datasets/multi-turn-cases.jsonl`

Typical rubrics:

- `evaluations/support-rubric.md`
- `evaluations/multi-turn-rubric.md`
- `evaluations/confusion-handling-rubric.md`

### Merchant Route

Prompt stack:

- `prompts/system.md`
- `prompts/merchant.md`
- optionally `prompts/objections.md`
- add `prompts/escalation.md` if policy risk or ambiguity is high

Typical datasets:

- `datasets/merchant-specific-cases.jsonl`
- `datasets/support-gold-extended.jsonl`
- `datasets/multi-turn-cases.jsonl`

Typical rubrics:

- `evaluations/merchant-policy-rubric.md`
- `evaluations/support-rubric.md`
- `evaluations/multi-turn-rubric.md`

### Objections Route

Prompt stack:

- `prompts/system.md`
- `prompts/objections.md`

Typical datasets:

- `datasets/objections-gold.jsonl`
- relevant objection-style multi-turn cases

Typical rubrics:

- `evaluations/objections-rubric.md`
- `evaluations/multi-turn-rubric.md`

### Knowledge Route

Prompt stack:

- `prompts/system.md`
- `prompts/knowledge.md`

Typical datasets:

- `datasets/knowledge-gold.jsonl`
- relevant multi-turn beginner cases

Typical rubrics:

- `evaluations/knowledge-rubric.md`
- `evaluations/multi-turn-rubric.md`

## Minimal Runner Role

The minimal runner does not execute model inference itself.

Its role is to:

- assemble the run
- bundle prompt text and rubric text
- load the chosen dataset slice
- create a structured artifact for later response insertion and scoring

## Suggested Near-Term Workflow

### 1. Route the test target

Decide whether the run is support, merchant, objections, or knowledge focused.

### 2. Assemble the prompt stack

Choose the right prompt combination based on routing.

### 3. Choose dataset slice and rubrics

Select only the cases that match the behavior you are trying to improve.

### 4. Generate run artifact

Use `runner/minimal_runner.py` and a manifest file.

### 5. Fill responses and scores

This can initially be manual or semi-manual.

### 6. Compare baseline and candidate

Use the run artifact plus the repo's iteration workflow to decide whether the prompt change is acceptable.

## Rule

Routing decides the prompt stack.

The prompt stack plus dataset slice determines the run.

The run result should always keep safety and BCH alignment visible.
