# Session Flow

## Purpose

This document describes how a BCH Defender session should flow inside an OpenClaw runtime.

## Standard Flow

### 1. Receive the user request

The system receives the raw user message.

### 2. Route the request

Use the routing layer to identify:

- primary route
- secondary labels
- whether escalation applies

### 3. Select the prompt stack

Based on routing, assemble the right prompt combination.

Examples:

- system + support
- system + merchant
- system + objections
- system + knowledge
- add escalation when needed

### 4. Determine whether tool use is needed

Do not use tools by default when explanation alone is sufficient.

Use tools only when they materially improve the answer or complete the task.

### 5. Apply permission policy

Before any non-trivial action, confirm that the selected agent role and route allow that tool use.

### 6. Produce the response or action

The agent should answer or act in a way that remains aligned with BCH Defender behavior standards.

### 7. Evaluate later if needed

The response pattern should remain compatible with later dataset-based evaluation.

## Example Session Types

### Support-only session

- route: `support`
- prompts: `system` + `support`
- tools: none or verification-only

### Merchant guidance session

- route: `merchant`
- prompts: `system` + `merchant`
- tools: usually none, sometimes read-only

### Knowledge session

- route: `knowledge`
- prompts: `system` + `knowledge`
- tools: usually none

### Ambiguous risky support session

- route: `support`
- secondary: `escalation`
- prompts: `system` + `support` + `escalation`
- tools: restricted until key facts are clarified

### Browser-assisted merchant session

- route: `merchant`
- secondary: possibly `checkout` or `exchange`
- prompts: `system` + `merchant`
- tools: browser actions only if the workflow is clearly bounded and approved

## Session Rule

Routing comes before tools.

Prompt stack comes before action.

Safety boundaries remain in effect throughout the session.
