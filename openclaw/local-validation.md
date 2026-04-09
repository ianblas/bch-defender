# Local Validation

## Purpose

This document explains how to validate the first live BCH Defender OpenClaw workspace setup locally.

## Validation Goals

Confirm that:

- the workspace is recognized
- the `skills/` directory is present
- each core `SKILL.md` is available to the runtime
- the intended prompt stack for each profile is known
- the runtime mapping and read-only-first policy can be checked with simple sessions

## Validation Sequence

### 1. Confirm workspace structure

Check that the workspace contains:

- `skills/`
- `prompts/`
- `routing/`
- `datasets/`
- `evaluations/`
- `runner/`
- `iteration/`
- `openclaw/`

### 2. Confirm skill folders

Check that the following skill paths exist:

- `skills/bch_merchant_ops/SKILL.md`
- `skills/bch_comparative_objections/SKILL.md`
- `skills/bch_privacy_network/SKILL.md`
- `skills/bch_record_anchoring/SKILL.md`

### 3. Confirm example config consistency

Check that `openclaw/openclaw.example.json` references:

- valid prompt paths
- valid skill names
- the intended default profile

### 4. Start a clean session for each profile

Use one fresh session per focused profile.

Suggested prompts:

- merchant: "How do I start accepting BCH in my business?"
- comparative: "Why not BTC?"
- privacy: "What is CashFusion for?"
- record anchoring: "What is OP_RETURN useful for?"

### 5. Validate expected behavior

The session should reflect:

- the correct dominant profile
- the expected skill theme
- the expected prompt stack direction
- read-only-first behavior unless a stronger tool is clearly required

### 6. Map back to evaluation

After local validation, map the session to:

- the matching runner manifest
- the relevant LEP2P slice
- any neighboring regression check if needed

## Rule

A local validation pass is successful when runtime behavior is focused, traceable, and consistent with the expected profile and skill rather than merely producing a plausible answer.
