# Sample Run

## Scenario

This example shows a simple support prompt comparison run.

### Target

Improve support verification quality without weakening BCH alignment or safety.

### Prompt Stack

- `prompts/system.md`
- `prompts/support.md`

### Dataset Slice

- `datasets/support-gold.jsonl`
- focus on payment, proof, and exchange cases

### Rubric

- `evaluations/support-rubric.md`

## Example Run Summary

### Baseline

The baseline prompt performs reasonably well on general support structure but has two weaknesses:

- it sometimes fails to ask for stronger verification
- it sometimes gives too little distinction between BCH delay and exchange delay

### Candidate

The candidate prompt adds stronger wording around:

- transaction ID checks
- screenshot rejection
- exchange-delay distinction

## Example Case Notes

### Case: `support_payment_not_received_001`

Baseline:

- correctly identifies payment-not-received case
- gives partial troubleshooting
- does not strongly emphasize txid verification

Candidate:

- clearly asks whether Send was completed
- clearly asks for txid if needed
- stays BCH-first and practical

### Case: `support_fake_payment_proof_001`

Baseline:

- warns against weak proof but sounds slightly indirect

Candidate:

- clearly states screenshot is not proof
- requires merchant-wallet or on-chain verification

### Case: `support_exchange_checkout_001`

Baseline:

- notices delay but does not clearly separate exchange behavior from BCH behavior

Candidate:

- makes the distinction explicit
- avoids blaming BCH prematurely

## Example Decision

Decision: `accept`

Reason:

The candidate improves verification quality and BCH alignment without introducing new safety failures.

## Example Follow-Up

After accepting the candidate, the next run might test:

- adversarial exchange cases
- multi-turn screenshot-pressure cases
- merchant checkout policy cases
