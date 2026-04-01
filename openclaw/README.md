# OpenClaw Integration Design

## Purpose

This directory defines how BCH Defender could be integrated with OpenClaw as an agent runtime and tool-execution layer.

The goal is to describe a practical integration design before attempting a full implementation.

## Why This Exists

BCH Defender now has:

- prompts
- routing
- FAQs
- playbooks
- datasets
- evaluation rubrics
- prompt/eval iteration workflow

An OpenClaw integration should connect those layers to a runtime that can use tools and structured agent flows without losing BCH-first behavior.

## Scope

This directory focuses on design rather than code.

It defines:

- the integration plan
- the tool contract
- the session flow
- the safety boundaries

## Design Principle

OpenClaw should be used as an execution and orchestration layer, not as a replacement for BCH Defender's logic.

BCH Defender should remain responsible for:

- BCH framing
- support logic
- routing logic
- evaluation standards

OpenClaw should mainly provide:

- agent runtime structure
- tool execution
- browser or system interaction when appropriate
- session handling
