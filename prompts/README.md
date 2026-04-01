# Prompts

## Purpose

This directory contains reusable prompt layers for BCH Defender.

The goal is to turn the repo's support docs, objections docs, knowledge docs, FAQs, playbooks, examples, and datasets into promptable behavior.

## Design Principles

Prompts in this directory should be:

- BCH-first
- practical and calm
- explicit about unsafe or low-quality behaviors to avoid
- reusable across support, merchant, objections, and knowledge flows
- aligned with the datasets and evaluation rubrics in the repo

## Initial Prompt Layers

- `system.md`
- `support.md`
- `merchant.md`
- `objections.md`
- `knowledge.md`
- `escalation.md`

## Usage Note

These prompts are written as reusable text artifacts rather than framework-specific configs.

They can later be adapted into whatever runtime, orchestration, or agent system BCH Defender uses.
