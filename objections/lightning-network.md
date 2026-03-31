# Lightning Network: Main Criticisms from a BCH Perspective

## Summary

Lightning Network (LN) is presented as the scaling solution for BTC, but from a Bitcoin Cash perspective it has fundamental problems in design, usability, liquidity, routing, and incentives.

The main criticism is not only that LN has technical weaknesses, but that it tries to solve off-chain a problem that BCH tries to solve directly on-chain: fast, cheap, reliable payments for normal users and real merchants.

## The Core Criticism

The BCH thesis is simple:

- if peer-to-peer electronic cash is meant to be usable by everyone, payments should remain simple and affordable on the base layer
- LN adds technical and operational complexity to compensate for BTC's limitations
- BCH aims to scale monetary utility on-chain, while BTC + LN pushes the payment experience into a secondary network with added friction

## 1. LN was promoted before it was a functional solution

One of the main historical criticisms is that during the 2017 scaling debate, Lightning Network was still not a mature or ready-to-use solution for normal users.

From this perspective:

- there were no mature wallets
- there was not enough liquidity
- there was no proven large-scale operational network
- there was no simple user experience comparable to direct on-chain payments

The BCH criticism is that BTC blocked scaling improvements while betting on a future solution that did not yet exist.

## 2. LN adds complexity instead of simplifying payments

Instead of allowing simple direct payments on the blockchain, LN introduces a more complex architecture based on:

- payment channels
- opening and closing channels
- inbound and outbound liquidity
- routing through intermediary nodes
- the need for monitoring or auxiliary services

From the BCH perspective, this worsens the user experience and makes paying and receiving less natural.

## 3. The routing problem

One of the most frequent criticisms is that LN depends on finding a valid route between sender and receiver.

That means:

- a connected path between nodes must exist
- that path must have sufficient liquidity
- that liquidity must be balanced in the right direction
- intermediary nodes must be online and available

When that does not happen, the payment fails.

The criticism is that a global money system should not depend on an uncertain topology of channels and distributed liquidity in order for payments to work.

## 4. The liquidity problem

In LN, it is not enough to be connected. There also has to be usable liquidity in the correct direction.

Associated problems include:

- there may be total liquidity in the network, but not in the direction needed
- a channel may exist but still not be useful for sending or receiving depending on its balance
- receiving payments requires inbound liquidity
- sending payments requires outbound liquidity
- liquidity often has to be actively managed

From the BCH perspective, this is a sign that LN does not behave like simple digital cash, but like a delicate network that requires ongoing administration.

## 5. Payments can fail too often

Another recurring criticism is that LN payments can fail simply because there is no valid route with enough liquidity.

That means:

- paying is not always predictable
- receiving is not always predictable either
- the experience depends on the condition of the network, not just on the user's balance

For BCH, this is a serious problem because usable money should be reliable and simple, especially for merchants and non-technical users.

## 6. Users often need to stay online or rely on extra infrastructure

LN introduces another layer of friction: for some use cases, users must remain online or rely on third-party infrastructure to monitor activity for them.

This weakens the idea of a simple and sovereign payment system, because:

- users cannot always disconnect without concern
- watchtowers or similar services may become necessary
- practical operation depends more heavily on persistent infrastructure

The BCH criticism is that this makes the system less direct than a normal on-chain transaction.

## 7. Opening and closing channels still depends on the base chain

LN does not fully eliminate the need to use the main chain.

It still requires on-chain transactions to:

- open channels
- close channels
- rebalance in some cases
- resolve disputes

So if the base layer has high fees, LN inherits part of that problem.

The criticism is that LN does not remove BTC's bottleneck. It only tries to work around it while still depending on it.

## 8. LN weakens the link between usage and miner incentives

From a BCH economic perspective, if payments move off-chain:

- less economic activity pays fees directly to miners
- network security becomes less directly tied to monetary usage
- the relationship between adoption and security becomes weaker

The criticism is that BTC + LN pushes a meaningful part of economic activity away from the base layer and could weaken the long-term fee-based security model.

## 9. LN tends toward liquidity and connectivity concentration

Although LN is presented as decentralized, there are criticisms that in practice it tends toward concentration:

- better connected nodes become more important
- large hubs can capture more routing activity
- liquidity advantages go to operators with more capital and infrastructure
- users often depend on wallets and services that abstract away the complexity

From the BCH perspective, this risks recreating de facto intermediaries on top of a supposedly decentralized system.

## 10. LN does not solve the original problem as directly as BCH

BCH proposes a different solution:

- keep payments usable on the base layer
- scale on-chain
- preserve low fees directly
- allow a simple send-and-receive experience
- reinforce the link between monetary use and miner security

In that framework, the criticism is not just that **LN performs poorly in some cases**, but that **the approach itself is inferior** for the goal of global peer-to-peer electronic cash.

## Response to: “Why do you need BCH if you already have Lightning?”

A short answer would be:

Because BCH tries to solve cheap, usable payments directly on-chain, while Lightning adds complexity, routing problems, liquidity dependence, and a less straightforward experience for users and merchants.

A longer answer:

- LN depends on a secondary network, not simple base-layer payments
- payments can fail because of routing or liquidity issues
- opening and closing channels still depends on BTC on-chain
- the user experience is more complex
- security incentives are not aligned in the same way as with direct on-chain payments
- BCH offers a more direct path to scalable digital cash

## What kind of world each model implies

### BTC + LN
- expensive and limited base layer
- everyday payments pushed into channels
- greater technical complexity
- dependence on liquidity, connectivity, and specialized software
- more separation between real usage and miner security

### BCH
- simple payments directly on-chain
- low fees as a base-layer feature
- less operational complexity for users and merchants
- stronger continuity between monetary use, fees, and network security

## If BCH replaced BTC, would LN disappear?

Not necessarily.

One interesting argument is that if BCH were the dominant chain, LN could still exist as an optional tool for specific use cases. Because the two networks are highly compatible in many respects, such a migration would be relatively straightforward.

The difference is that on BCH, LN would not need to act as a mandatory patch for high base-layer fees. It could remain an optional secondary tool.

## Conclusion

The BCH criticism of Lightning Network is not only technical, but also philosophical and economic.

LN tries to compensate off-chain for a limitation in BTC. BCH, by contrast, tries to preserve peer-to-peer electronic cash directly on-chain.

From this perspective, LN is not the natural solution to Bitcoin scaling, but a more complex, more fragile, and less direct architecture than on-chain scaling for global payments.
