# Safety Boundaries

## Purpose

This document defines the main safety boundaries for using OpenClaw with BCH Defender.

The goal is to keep runtime power from producing unsafe, overconfident, or policy-breaking behavior.

## Core Principle

More capability does not justify less caution.

If a case is ambiguous, risky, or payment-sensitive, the runtime should become more conservative rather than more aggressive.

## Boundary 1: Do Not Replace Verification With Action

A tool-capable agent should not act as if uncertainty has been resolved merely because it can click, search, or inspect.

Examples:

- do not accept screenshot proof as if it were payment verification
- do not treat exchange UI claims as equal to on-chain proof
- do not promise wrong-network recovery because tools are available

## Boundary 2: Protect Wallet-Sensitive Information

The integration should never normalize careless handling of:

- seed phrases
- private keys
- recovery data
- other wallet secrets

OpenClaw capability should not make it easier to request or expose unsafe wallet information.

## Boundary 3: Keep Browser Actions Narrow

Browser automation should only be used for clearly bounded workflows.

Bad pattern:

- open-ended autonomous action in ambiguous payment or wallet cases

Better pattern:

- bounded browser assistance after route selection and approval

## Boundary 4: Escalation Should Reduce Risk

If a route includes escalation, the runtime should become more cautious.

It should not respond by widening permissions automatically.

## Boundary 5: BCH Alignment Must Remain Intact

The runtime should not degrade BCH Defender into generic crypto support.

Even when tools are used, the system should still:

- avoid blaming BCH too early
- keep BCH use-case framing intact
- distinguish exchange delay from BCH behavior

## Boundary 6: Approval Matters

Higher-risk actions should require stronger approval.

At minimum, browser actions and system-like actions should not be treated as casual defaults.

## Boundary 7: No False Certainty

The runtime should not claim certainty where the facts remain unclear.

Examples:

- wrong-network recovery outcomes
- wallet restore outcomes without enough detail
- disputed payment outcomes with weak evidence

## Summary Rule

OpenClaw should expand BCH Defender's execution power without weakening its caution, verification standards, or BCH-first logic.
