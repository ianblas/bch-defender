# Runner Hardening Notes

## Purpose

This document explains the first hardening pass applied to BCH Defender's local runner helpers.

## What Was Hardened

### 1. Repository-Bounded Path Handling

The hardened runner helpers reject paths that try to escape the repository root.

This blocks unsafe patterns such as:

- absolute-path reads outside the repo
- `..` traversal
- accidental writes to unrelated locations

### 2. Safer `run_id` Handling

The hardened minimal runner sanitizes `run_id` before using it as an output filename.

This reduces the risk of unsafe path-like output names.

### 3. Overwrite Protection

The hardened runner helpers avoid overwriting alternate output files unless `--force` is provided.

This reduces accidental file clobbering during local use.

### 4. Basic Score Validation

The hardened scoring helper rejects unknown score metrics and non-numeric score values.

This makes malformed patches easier to catch early.

## Scope

These changes are hardening improvements for local tooling.

They do not turn the runner into a hostile-input sandbox, but they do reduce the most obvious path and overwrite risks.
