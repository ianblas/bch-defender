# Experiment Template

## Experiment Name

Use a short descriptive name.

Example:

`support-verification-language-v2`

## Objective

What behavior are you trying to improve?

Examples:

- improve support verification quality
- reduce tribal tone in objections
- make knowledge answers simpler for beginners

## Prompt Layer

Which prompt is being changed?

Examples:

- `prompts/support.md`
- `prompts/objections.md`

## Baseline Prompt Version

Record the prompt version or commit reference.

## Candidate Change

Describe the exact change.

Keep it specific enough that another person could understand what changed and why.

## Dataset Slice

Record which cases were used.

Examples:

- `datasets/support-gold.jsonl` full
- support cases tagged `wrong_network`
- `datasets/adversarial-cases.jsonl` exchange-related subset

## Evaluation Rubric

Record which rubric was used.

Examples:

- `evaluations/support-rubric.md`
- `evaluations/objections-rubric.md`

## Expected Improvement

State what you expect to improve.

Examples:

- better issue identification
- fewer unsafe shortcut suggestions
- clearer BCH framing

## Observed Result

Record what actually improved, what stayed flat, and what got worse.

## Regression Check

Explicitly note whether the change caused regressions in:

- safety
- BCH alignment
- clarity
- operational usefulness

## Decision

Choose one:

- accept
- reject
- revise and retest

## Notes

Add any insights worth reusing in future iterations.
