# Runner v1

## Purpose

This directory defines a first evaluation runner design for BCH Defender.

The goal is to connect:

- prompts
- routing
- datasets
- evaluation rubrics
- iteration workflow

into a repeatable evaluation process.

## What This Runner Is

This runner is a design and spec layer.

It defines:

- what an evaluation run should look like
- how results should be recorded
- how baseline and candidate prompts should be compared

## What This Runner Is Not Yet

This is not a framework-specific implementation.

It does not assume a specific SDK, orchestration runtime, or model provider.

## Included Files

- `eval-run-spec.md`
- `result-schema.md`
- `sample-run.md`

## Design Principle

The runner should make it easy to answer questions like:

- did the prompt improve support verification?
- did it regress on safety?
- did it weaken BCH-first framing?
- did it perform differently on merchant, objections, or multi-turn cases?
