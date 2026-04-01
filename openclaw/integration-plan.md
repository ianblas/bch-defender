# Integration Plan

## Goal

Integrate BCH Defender with OpenClaw in a way that preserves BCH-first behavior while enabling structured agent execution.

## High-Level Architecture

### BCH Defender remains the policy and logic layer

BCH Defender should continue to define:

- prompts
- routing decisions
- evaluation standards
- support logic
- merchant logic
- objection handling logic
- escalation behavior

### OpenClaw becomes the runtime and tool layer

OpenClaw should be responsible for:

- agent execution
- tool invocation
- browser automation when allowed
- structured sessions
- runtime orchestration

## Recommended Agent Roles

### 1. Support Agent

Primary use:

- payment troubleshooting
- wrong-network triage
- refund support
- wallet restore support
- exchange-at-checkout clarification

Main inputs:

- `prompts/system.md`
- `prompts/support.md`
- `prompts/escalation.md`
- `routing/`

### 2. Merchant Agent

Primary use:

- onboarding guidance
- checkout flow guidance
- pricing and refund policy guidance
- merchant objections

Main inputs:

- `prompts/system.md`
- `prompts/merchant.md`
- `prompts/objections.md`
- `routing/`

### 3. Knowledge Agent

Primary use:

- beginner education
- BCH definitions
- self-custody explanations
- concept clarification

Main inputs:

- `prompts/system.md`
- `prompts/knowledge.md`

### 4. Escalation Mode

Not necessarily a separate agent.

This can be implemented as a stricter mode applied when routing adds an escalation label.

## Integration Sequence

### Phase 1: Design only

Define:

- agent roles
- tool permissions
- session boundaries
- approval boundaries
- routing-to-agent mapping

### Phase 2: Minimal runtime mapping

Connect routing outputs to OpenClaw agent selection.

### Phase 3: Low-risk tool usage

Allow only low-risk assistance such as:

- page reading
- information gathering
- guided research

### Phase 4: Higher-trust tool workflows

Only after validation:

- browser actions
- multi-step agent flows
- tool chaining with explicit approval

## Core Recommendation

Do not begin with a single general-purpose agent that can do everything.

Begin with narrow roles and conservative permissions.

## Success Criteria

An OpenClaw integration is successful when:

- BCH Defender logic remains intact
- prompts and routing are not bypassed
- risky cases are escalated rather than improvised
- tools are used only when they add real value
- browser actions do not outpace policy and approval controls
