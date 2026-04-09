# Session Model

## Purpose

This document defines how BCH Defender sessions should begin and remain structured inside OpenClaw.

## Session Start

At session start, the runtime should determine:

- the most relevant agent profile
- the primary route
- any important secondary labels
- whether escalation should also apply

## Session Snapshot Rule

Each session should be treated as using a snapshot of the currently selected skills and prompt layers.

If skill or prompt logic changes later, a fresh session is the safest way to test the new behavior.

## Prompt Stack Rule

A session should always begin from BCH Defender's shared system layer and then add the most relevant focused prompt layers.

Examples:

- system + merchant + merchant-operations
- system + objections + comparative-objections
- system + knowledge + privacy-and-network
- system + knowledge + record-anchoring

## Session Discipline

Do not overload a single session with too many competing skill goals.

Prefer a clear dominant use case.

## Escalation Rule

If a session becomes risky or ambiguous, the runtime should move toward a stricter response style instead of widening confidence or permissions.

## Evaluation Rule

When testing a session change, it should be easy to map the session back to:

- a route or subroute
- a prompt stack
- a runner manifest or iteration slice
