# First Live Checklist

## Purpose

This checklist is for the first practical BCH Defender OpenClaw runtime test.

## Workspace Checks

- [ ] Workspace root is correct
- [ ] `skills/` directory exists
- [ ] all four core `SKILL.md` files exist
- [ ] referenced prompt files exist
- [ ] `openclaw/openclaw.example.json` paths match the repo layout

## Profile Checks

- [ ] Merchant Operations profile can be tested with a focused merchant question
- [ ] Comparative Objections profile can be tested with a focused comparison question
- [ ] Privacy and Network profile can be tested with a focused privacy/tooling question
- [ ] Record Anchoring profile can be tested with a focused OP_RETURN or timestamping question

## Behavior Checks

- [ ] session behavior is focused rather than overly broad
- [ ] the answer reflects the expected dominant skill
- [ ] the answer reflects the expected prompt stack direction
- [ ] read-only-first behavior is preserved by default
- [ ] no unsafe wallet-secret handling language appears

## Mapping Checks

- [ ] the session can be mapped back to a runner manifest
- [ ] the session can be mapped back to an iteration slice
- [ ] neighboring regression checks are identified if the profile changed recently

## Success Condition

The first live config is successful when BCH Defender can run a focused OpenClaw session whose behavior is:

- traceable
- skill-aligned
- prompt-stack consistent
- policy-consistent
- easy to evaluate afterward
