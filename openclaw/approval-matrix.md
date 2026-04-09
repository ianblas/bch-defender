# Approval Matrix

## Purpose

This document defines how strongly different tool classes should be gated for BCH Defender's first OpenClaw runtime phase.

## Approval Levels

### Level A

No special approval beyond normal route/profile selection.

### Level B

Route must be clear and the tool must materially improve the answer.

### Level C

Stronger explicit approval required before use.

## Matrix by Tool Class

### Read-Only Tools

Default approval:

- Level A

Typical use:

- merchant clarification
- comparative explanation support
- privacy/infrastructure reading
- record-anchoring explanation support

### Verification Tools

Default approval:

- Level B

Typical use:

- confirming a status
- checking a public record or explorer page
- validating a factual condition relevant to the answer

### Browser Action Tools

Default approval:

- Level C

Typical use:

- bounded workflow execution
- task completion that cannot be handled read-only

### System / Exec-Like Tools

Default approval:

- Level C+

Meaning:

- strongest caution tier
- outside normal end-user answer flows
- only for bounded implementation or maintenance workflows

## Matrix by Profile

### Merchant Operations Agent

- read-only: Level A
- verification: Level B
- browser action: Level C
- exec-like: Level C+

### Comparative Objections Agent

- read-only: Level A
- verification: Level B only if truly needed
- browser action: Level C and usually unnecessary
- exec-like: Level C+

### Privacy and Network Agent

- read-only: Level A
- verification: Level B
- browser action: Level C
- exec-like: Level C+

### Record Anchoring Agent

- read-only: Level A
- verification: Level B
- browser action: Level C
- exec-like: Level C+

## Rule

If there is doubt between two approval levels, use the stricter one.
