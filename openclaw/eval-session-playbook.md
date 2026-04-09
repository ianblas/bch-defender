# Eval Session Playbook

## Purpose

This document explains how a BCH Defender OpenClaw session should connect back to the runner, manifests, and evaluation slices.

## Core Rule

A runtime session should never be treated as untestable freeform behavior.

Each focused session should map back to:

- a dominant route or subroute
- a focused profile
- a prompt stack
- a runner manifest or evaluation slice

## Standard Flow

### 1. Start a clean session

Use a fresh session after skill or prompt changes so the runtime uses the intended workspace snapshot.

### 2. Identify the dominant session type

Examples:

- merchant operations
- comparative objections
- privacy and network
- record anchoring

### 3. Map the session to the matching runner artifact

Examples:

- merchant session → `runner/run-manifest.lep2p-merchant.example.json`
- comparative session → `runner/run-manifest.lep2p-comparative.example.json`
- privacy session → `runner/run-manifest.lep2p-privacy.example.json`

### 4. Select the matching evaluation slice

Examples:

- merchant operations → `iteration/lep2p-slices.md` merchant slice
- privacy/infrastructure → privacy slice
- comparative objections → comparative slice

### 5. Record what changed

A session-based test should note:

- which profile was used
- which skills were active
- which prompt layers were expected
- which manifest and rubrics were used afterward

### 6. Check for regressions

A good runtime change should not improve one focused session while silently damaging BCH framing, safety, or clarity in neighboring slices.

## Practical Rule

Session testing should be traceable.

If a session cannot be mapped back to a known manifest or slice, it is harder to compare and easier to rationalize.