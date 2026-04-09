---
name: bch_record_anchoring
description: Use for BCH OP_RETURN, hashes, timestamps, record anchoring, and lightweight notary-style explanations.
---

# BCH Record Anchoring

Use this skill when the user asks about BCH for timestamping, hashes, integrity proofs, or notary-style workflows.

## Focus

Prioritize:

- clarifying whether the user wants anchoring, storage, or evidentiary explanation
- explaining hashes and timestamps simply
- separating anchoring from raw content storage
- keeping the answer practical and not overclaiming

## Key Behavior Rules

- Do not say every raw file should be stored on-chain by default.
- Do not confuse hashing with full storage.
- Do not overstate legal certainty.
- Keep the answer usable for ordinary builders and users.

## Common Questions

- Can BCH timestamp a document?
- What is OP_RETURN useful for?
- Why anchor a hash instead of storing the whole file?
- Can BCH help with notary-style workflows?

## Suggested Internal References

- `prompts/record-anchoring.md`
- `playbooks/notary-and-record-anchoring.md`
- `datasets/lep2p-privacy-and-infrastructure.jsonl`
- `evaluations/record-anchoring-rubric.md`
