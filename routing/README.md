# Routing

## Purpose

This directory defines how BCH Defender should route user requests into the right response mode.

The goal is to connect the repo's prompts, datasets, FAQs, playbooks, edge cases, and evaluation standards into a practical decision layer.

## Core Principle

Route by the user's real need, not just by keywords.

A good routing decision should identify whether the user mainly needs:

- support help
- merchant guidance
- objection handling
- knowledge explanation
- escalation or cautious handling

## Initial Routing Artifacts

- `intent-map.md`
- `decision-tree.md`
- `label-schema.md`

## Design Notes

Routing should be:

- BCH-first
- practical
- conservative when ambiguity creates risk
- aligned with the repo's support and evaluation standards

When a case is ambiguous, prefer the safer route and use escalation logic rather than false certainty.
