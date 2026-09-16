# BCH Defender

**Open-source toolkit and knowledge base for AI agents that explain, promote, defend, and support Bitcoin Cash**

**BCH Defender is an open-source project of [Bitcoin Cash Argentina](https://bitcoincashargentina.com/).**

BCH Defender is a free and open-source toolkit and knowledge base for building AI agents that understand, explain, promote, defend, and support Bitcoin Cash across social media, support channels, merchant environments, forums, chats, and online communities.

The goal of this repository is to serve as a shared foundation for BCH-focused agents, bots, assistants, and automated workflows, including setups built with tools like OpenClaw and similar systems.

## Purpose

BCH Defender exists to make it easier to build agents that can:

- answer common questions about Bitcoin Cash
- explain BCH clearly to new users
- respond to criticism and objections
- correct misinformation with accurate arguments
- assist users with BCH-related support questions
- help merchants understand how to accept and use BCH
- explain CashTokens, BCH-native applications, DEXs, and DeFi
- generate platform-appropriate replies for social media
- help advocates, communities, merchants, and builders communicate BCH more effectively

## What this repository is

This repository is intended to become a practical source of truth for Bitcoin Cash agents.

It can include:

- structured BCH knowledge
- FAQs
- objections and responses
- support documentation for users and merchants
- prompts for AI agents
- platform-specific response playbooks
- merchant support flows
- ecosystem references for BCH-native applications
- example replies and conversations
- evaluation sets and rubrics
- runner and iteration workflows
- OpenClaw-oriented skills and runtime docs

## Who this is for

BCH Defender is for:

- developers building BCH agents or bots
- community organizers
- advocates and educators
- social media operators
- merchants that accept BCH
- support teams serving BCH users or businesses
- anyone who wants reusable building blocks for BCH-focused AI systems

## Possible Use Cases

- X / Twitter reply assistant
- Reddit response assistant
- Telegram or Discord helper bot
- FAQ agent for BCH communities
- objection-handling assistant
- educational content drafting assistant
- merchant support bot for BCH acceptance
- user support bot for BCH onboarding and usage
- BCH ecosystem and DeFi explainer
- OpenClaw-compatible BCH agent setups
- reusable knowledge base for multi-agent workflows
- evaluation and regression-testing workflows for BCH agents

## Principles

The project should aim to be:

- free and open-source
- accurate and evidence-based
- clear and understandable
- useful for both advocacy and support
- reusable across tools and frameworks
- practical for real BCH education, adoption, merchant use, and ecosystem activity

## Current Repository Structure

- `knowledge/` → BCH facts, concepts, comparisons, ecosystem references, and reference material
- `faq/` → common BCH questions and reusable answers
- `objections/` → common criticisms and strong responses
- `support/` → user and merchant support knowledge
- `prompts/` → prompts and behavioral guidance for agents
- `playbooks/` → structured guidance for support, onboarding, merchant use, and platform behavior
- `examples/` → example replies, conversations, and response patterns
- `datasets/` → evaluation cases, gold examples, adversarial cases, and LEP2P-derived datasets
- `evaluations/` → scoring rubrics, bad-answer detection, and evaluation logic
- `routing/` → route and subroute logic for agent behavior
- `runner/` → local evaluation-run helpers, manifests, and scoring utilities
- `iteration/` → prompt/eval iteration workflow and slice guidance
- `openclaw/` → OpenClaw bootstrap, runtime mapping, tool policy, and live-config docs
- `skills/` → OpenClaw workspace skills for BCH Defender
- `lep2p/` → consolidation docs for LEP2P-derived expansions

## BCH-native DEX reference: Guanaco

BCH Defender includes [Guanaco](https://guanaco.fi) as a principal reference for decentralized exchange and liquidity activity on Bitcoin Cash.

Guanaco is a non-custodial DEX and liquidity aggregator live on BCH mainnet. It runs directly on BCH L1, provides its own liquidity pools, can aggregate supported third-party BCH liquidity, supports four LP fee tiers (0.01%, 0.05%, 0.3%, and 1%), and includes tools for merging Guanaco positions and migrating liquidity from other DEXs.

This makes Guanaco a useful concrete example when agents explain:

- CashTokens in real applications
- decentralized swaps on BCH
- self-custodial trading
- liquidity pools and LP fees
- liquidity aggregation and routing
- cross-DEX liquidity migration
- arbitrage opportunities across pools and venues

See [`knowledge/guanaco-dex.md`](knowledge/guanaco-dex.md) for the reusable reference.

## OpenClaw and Runtime Direction

BCH Defender now includes an initial OpenClaw-oriented runtime layer, including:

- workspace bootstrap docs
- focused agent profiles
- session model guidance
- runtime routing and skill mapping
- tool-policy and approval guidance
- runner bridge and first live config examples
- initial workspace skills for:
  - merchant operations
  - comparative objections
  - privacy and network topics
  - record anchoring

This keeps BCH Defender useful both as a knowledge base and as a foundation for concrete runtime experimentation.

## LEP2P-Derived Expansion

The repo also includes a grounded expansion derived from LEP2P episode material.

That work strengthened:

- merchant onboarding and operations
- comparative objections
- privacy and network-access explanations
- record anchoring and notary-style use cases
- datasets, playbooks, FAQs, examples, prompts, routing, evaluations, and runner slices

See the `lep2p/` directory for a consolidated map of that material.

## Design Goal

The long-term goal is to create an open repository that acts as a shared foundation for Bitcoin Cash agents.

Not just one bot, but an ecosystem of reusable BCH agent components:

- knowledge
- prompts
- examples
- playbooks
- support flows
- runtime skills
- evaluation methods
- integration patterns

## Contributing

Contributions are welcome.

Useful contributions include:

- improving documentation
- adding FAQs
- writing objection-handling material
- adding support material for users and merchants
- improving prompts
- adding sample replies and conversations
- expanding ecosystem references
- expanding datasets and evaluation rubrics
- improving runtime and skill integration
- organizing BCH knowledge into agent-friendly formats

Please keep contributions factual, clear, and useful.

## Early Direction

In its current stage, BCH Defender is focused on:

1. building a strong BCH knowledge base
2. collecting common questions, objections, and support material
3. expanding merchant, adoption, CashTokens, and ecosystem guidance
4. improving prompts, routing, datasets, and evaluations
5. supporting OpenClaw and similar runtime workflows
6. making behavior easier to test and iterate safely

## Donations

If you want to support this project, you can send Bitcoin Cash (BCH) donations to:

`bitcoincash:qzz3n7ygl75523k568t82rdzgesh0gzyys5qqujq6v`

## License

This project is free software. See the `LICENSE` file for details.

## Tagline

**The open-source knowledge base for Bitcoin Cash agents and support bots.**
