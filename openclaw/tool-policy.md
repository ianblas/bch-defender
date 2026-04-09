# Tool Policy

## Purpose

This document defines the first practical tool-usage policy for BCH Defender inside OpenClaw.

## Core Rule

Tool capability must not outrun BCH Defender policy.

A runtime that can browse, click, or execute still needs to respect BCH-first logic, verification discipline, and safety boundaries.

## Tool Classes

### 1. Read-Only Tools

Examples:

- page reading
- document reading
- internal retrieval
- lightweight search

Default use:

- allowed first
- preferred when explanation is enough
- preferred for low-risk merchant, knowledge, and comparative sessions

### 2. Verification Tools

Examples:

- explorer checks
- structured page verification
- status confirmation

Default use:

- allowed when the question requires confirmation rather than general explanation
- useful in support or merchant clarification flows

### 3. Browser Action Tools

Examples:

- clicking
- typing
- navigation that changes runtime state

Default use:

- not the default
- only after route and profile are clear
- only when read-only behavior is insufficient

### 4. System or Exec-Like Tools

Examples:

- shell execution
- local file mutation
- process control

Default use:

- highest caution tier
- not part of normal user-answer flows
- only for tightly bounded workflows

## Policy Rules

### Rule 1: Read-Only First

If read-only behavior can answer the question well, do not escalate to action tools.

### Rule 2: Verification Before Action

Do not use action tools to compensate for unresolved ambiguity.

### Rule 3: Escalation Tightens, Not Widens

If a case is risky or ambiguous, become more conservative.

Do not widen permissions automatically.

### Rule 4: Preserve BCH Framing

Tool use must not collapse BCH Defender into generic crypto support or vague browsing behavior.

### Rule 5: No Wallet-Secrets Handling

The runtime should never normalize unsafe handling of:

- seed phrases
- private keys
- recovery material
- sensitive wallet secrets

## Practical Rule

For most early BCH Defender runtime use, the safe default is:

- read-only first
- verification when justified
- browser action only with stronger approval
- exec-like tools only in tightly bounded implementation workflows
