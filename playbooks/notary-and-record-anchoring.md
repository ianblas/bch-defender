# Notary and Record Anchoring

## Goal

Help a user or builder understand when and how BCH can support timestamping, record anchoring, or lightweight notary-style use cases.

## Core Rule

Do not confuse record anchoring with storing everything directly on-chain.

## Standard Flow

### 1. Clarify the record goal

Determine whether the user wants:

- proof a file existed at a certain time
- evidence of document integrity
- a simple historical anchor
- a lightweight notary-style workflow

### 2. Explain the role of hashes and timestamps

A good answer should emphasize:

- hashing for integrity
- on-chain anchoring for timestamped evidence
- the difference between the file itself and its anchor

### 3. Separate anchoring from storage

If storage is also needed, explain that:

- BCH can anchor records
- storage may be handled separately
- the user should not assume every full document belongs directly in every on-chain action

### 4. Keep the workflow practical

The answer should remain useful for ordinary builders, not only experts.

## Mistakes to Avoid

- saying BCH should directly store every raw file by default
- confusing anchoring with centralized verification services
- overselling the legal or social effect of anchoring without context

## Escalate When

Escalate if:

- the user needs legal-process advice rather than technical guidance
- the record workflow involves sensitive institutional or evidentiary assumptions
- the user is mixing storage, privacy, and record-integrity needs without clarity

## Short Answer

BCH can support lightweight notary-style workflows by anchoring hashes and timestamps, while keeping storage and verification concerns clearly separated.