# Eval Run Spec

## Goal

Define what a standard BCH Defender evaluation run should include.

## Required Inputs

A run should specify:

- prompt layer or prompt stack under test
- dataset or dataset slice
- evaluation rubric or rubric set
- baseline version
- candidate version
- run metadata

## Prompt Inputs

A run may use:

- one prompt layer, such as `prompts/support.md`
- a stack, such as `system + support + escalation`

The exact prompt configuration should be recorded explicitly.

## Dataset Inputs

A run should reference one or more of:

- `datasets/support-gold.jsonl`
- `datasets/support-gold-extended.jsonl`
- `datasets/objections-gold.jsonl`
- `datasets/knowledge-gold.jsonl`
- `datasets/adversarial-cases.jsonl`
- `datasets/multi-turn-cases.jsonl`
- `datasets/merchant-specific-cases.jsonl`
- `datasets/confusion-cases.jsonl`

## Evaluation Inputs

A run should specify which rubrics apply.

Examples:

- `evaluations/support-rubric.md`
- `evaluations/multi-turn-rubric.md`
- `evaluations/confusion-handling-rubric.md`
- `evaluations/merchant-policy-rubric.md`
- `evaluations/objections-rubric.md`
- `evaluations/knowledge-rubric.md`

## Standard Run Flow

### 1. Select the run target

Choose what you are trying to improve.

Examples:

- support verification quality
- merchant policy quality
- objection tone quality
- confusion handling

### 2. Run baseline prompt(s)

Capture the current behavior on the chosen dataset slice.

### 3. Run candidate prompt(s)

Run the changed prompt(s) on the same cases.

### 4. Score with the selected rubric(s)

Each case should receive structured scoring.

### 5. Flag automatic failures

If the candidate triggers explicit failure conditions, that should be recorded even if average scores improved elsewhere.

### 6. Summarize run outcome

The run summary should state:

- where the candidate improved
- where it regressed
- whether the candidate is acceptable

## Run Granularity

A run may be:

- full-dataset
- slice-based
- category-specific
- adversarial-only
- multi-turn-only

## Acceptance Rule

A candidate prompt should not be accepted only because it improves average scores.

It should also avoid unacceptable regressions in:

- safety
- BCH alignment
- operational usefulness
- confusion handling

## Output Rule

A run should produce both:

- per-case results
- a summary result
