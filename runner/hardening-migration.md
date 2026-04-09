# Hardening Migration Guide

## Purpose

This document explains how to adopt the hardened runner helpers.

## Hardened Variants

- `runner/minimal_runner_hardened.py`
- `runner/prefill_responses_hardened.py`
- `runner/scoring_helpers_hardened.py`

## Why Separate Files

These hardened variants were added as explicit replacements so they can be reviewed and tested safely without forcing immediate behavior changes in existing local workflows.

## Suggested Adoption Path

### 1. Use the hardened scripts for new local runs

Prefer the hardened variants for:

- new artifact generation
- response prefilling
- score patch application

### 2. Keep the old scripts only as compatibility fallback

Do not treat the older versions as the safer default after review.

### 3. Switch CLI examples later if desired

A future cleanup PR can update:

- `runner/cli-usage.md`
- other example docs

so the hardened variants become the documented default.

## Practical Rule

If the runner will be used with anything less than fully trusted local inputs, prefer the hardened variants.
