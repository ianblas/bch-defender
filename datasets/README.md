# Datasets

## Purpose

This directory contains structured evaluation cases for BCH Defender.

The goal is to turn the repo's FAQ, playbooks, examples, and edge cases into reusable test material for:

- prompt iteration
- routing design
- evaluation
- future integration work

## Design Principles

Each dataset case should be:

- BCH-first
- operational when needed
- clear about expected behavior
- explicit about dangerous or wrong behavior
- reusable across prompts and model versions

## Recommended Fields

A case may include:

- `id`
- `category`
- `subcategory`
- `user_message`
- `context`
- `expected_behavior`
- `good_answer`
- `bad_answer`
- `must_say`
- `must_not_say`
- `tags`

Not every field is required for every case, but the structure should stay consistent enough for evaluation.

## Initial Datasets

- `support-gold.jsonl`
- `objections-gold.jsonl`
- `knowledge-gold.jsonl`
- `adversarial-cases.jsonl`
