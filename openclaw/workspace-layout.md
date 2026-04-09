# OpenClaw Workspace Layout

## Purpose

This document defines a practical starting workspace layout for running BCH Defender inside OpenClaw.

## Recommended Structure

```text
workspace/
  skills/
    bch_merchant_ops/
      SKILL.md
    bch_comparative_objections/
      SKILL.md
    bch_privacy_network/
      SKILL.md
    bch_record_anchoring/
      SKILL.md
  prompts/
  routing/
  datasets/
  evaluations/
  runner/
  iteration/
  openclaw/
```

## Design Rule

BCH Defender logic should stay in the repo's existing layers.

The OpenClaw workspace should expose and apply that logic through skills and runtime configuration, not replace it.

## What Lives Where

### `skills/`

Runtime-facing guidance for agent behavior inside OpenClaw.

### `prompts/`

The reusable prompt layers BCH Defender already defines.

### `routing/`

The route and subroute logic used to decide which prompt or skill path should apply.

### `datasets/` and `evaluations/`

Evaluation assets used to check whether runtime behavior stays aligned.

### `runner/` and `iteration/`

Artifacts for run selection, iteration slicing, and regression checking.

## Starting Rule

Do not begin with too many skills.

Start with a few core skills that correspond to the strongest and most grounded BCH Defender capability clusters.
