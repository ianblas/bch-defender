# Tooling Contract

## Purpose

This document defines how BCH Defender should think about tool access inside an OpenClaw runtime.

The goal is to prevent tool capability from outrunning BCH Defender policy.

## Core Rule

Tools should extend BCH Defender's usefulness, not replace its judgment.

## Tool Classes

### 1. Read-Only Tools

Lowest-risk tool class.

Examples:

- page reading
- document reading
- structured retrieval
- internal search

Recommended use:

- support clarification
- merchant research
- knowledge retrieval

### 2. Verification Tools

These help confirm facts or status.

Examples:

- transaction lookup
- explorer checks
- page verification
- structured cross-checking

Recommended use:

- payment-not-received cases
- wrong-network triage
- exchange status clarification

### 3. Browser Action Tools

These can click, navigate, type, or operate a browser.

Recommended use only when:

- the task clearly requires action rather than explanation
- the route is appropriate
- approval policy allows it

### 4. System or Shell-Like Tools

Highest-risk class.

Use only for tightly defined workflows if ever enabled.

## Recommended Permissions by Agent

### Support Agent

Allow:

- read-only tools
- verification tools

Do not default to browser action tools.

### Merchant Agent

Allow:

- read-only tools
- verification tools
- browser action tools only for clearly bounded workflows if approved

### Knowledge Agent

Allow:

- read-only tools only by default

### Escalation Mode

Restrict rather than expand permissions unless a human-approved workflow explicitly requires more.

## Approval Principle

Higher-risk tools should require stronger approval.

A safe default policy is:

- read-only: no special approval
- verification: allowed when relevant
- browser action: explicit approval
- system-level tools: explicit and narrow approval

## Prohibited Patterns

Do not allow tool usage to bypass BCH Defender policy.

Examples of bad patterns:

- using tools to act before key facts are established
- letting browser action happen in ambiguous payment disputes
- treating tool access as justification for false certainty
- exposing sensitive wallet information casually

## Contract Summary

Tool access should be:

- role-based
- route-aware
- approval-aware
- safety-constrained
