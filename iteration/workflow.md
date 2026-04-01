# Workflow

## Goal

Improve BCH Defender prompts by testing them against the repo's datasets and evaluation rubrics.

## Standard Iteration Loop

### 1. Choose a target behavior to improve

Examples:

- support verification quality
- merchant operational clarity
- objection tone quality
- knowledge simplicity
- escalation caution

Do not change many goals at once unless the prompt architecture requires it.

### 2. Select the relevant prompt layer

Examples:

- `prompts/support.md`
- `prompts/merchant.md`
- `prompts/objections.md`
- `prompts/knowledge.md`
- `prompts/escalation.md`

### 3. Select the relevant dataset slice

Examples:

- `datasets/support-gold.jsonl`
- `datasets/objections-gold.jsonl`
- `datasets/knowledge-gold.jsonl`
- `datasets/adversarial-cases.jsonl`

### 4. Run a baseline

Capture how the current prompt performs before changing it.

### 5. Make one clear prompt change

The change should be small enough that its effect can be interpreted.

Examples:

- add stronger verification language
- reduce tribal objection language
- clarify beginner explanation structure
- strengthen wrong-network caution

### 6. Re-run the same cases

Compare the updated prompt against the same slice of cases.

### 7. Judge with the relevant rubric

Examples:

- `evaluations/support-rubric.md`
- `evaluations/objections-rubric.md`
- `evaluations/knowledge-rubric.md`

### 8. Record both improvements and regressions

Do not keep a prompt change just because it improved one case if it damaged safety, BCH alignment, or clarity elsewhere.

## Decision Rule

A prompt change is good when it:

- improves the target behavior
- does not create obvious regressions in safety
- does not weaken BCH-first framing
- does not make answers less usable in common cases

## Failure Modes to Watch

### Support prompt regressions

- blaming BCH too early
- failing to ask for verification
- accepting weak proof
- overpromising recovery

### Objection prompt regressions

- becoming tribal
- becoming too vague
- denying real tradeoffs
- losing BCH use-case framing

### Knowledge prompt regressions

- becoming too abstract
- using too much jargon
- drifting into generic crypto language
- giving unsafe wallet guidance

## Practical Rule

Prefer many small prompt iterations over one large prompt rewrite.
