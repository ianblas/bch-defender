# Prompt / Eval Iteration

## Purpose

This directory defines how BCH Defender should improve prompts using the repo's datasets and evaluation rubrics.

The goal is to make prompt improvement systematic rather than intuitive or random.

## Core Idea

A prompt change should not be accepted just because it sounds better.

It should be tested against representative BCH cases and judged with explicit evaluation criteria.

## What This Directory Contains

- `workflow.md`
- `experiment-template.md`
- `scorecard-template.md`

## Principles

Prompt/eval iteration should be:

- BCH-first
- case-driven
- explicit about failure modes
- tied to the repo's datasets and rubrics
- conservative about accepting regressions in safety or BCH alignment
