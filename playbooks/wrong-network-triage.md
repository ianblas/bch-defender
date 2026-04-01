# Wrong Network Triage

## Goal

Identify wrong-network BCH payment cases clearly and avoid false promises.

## Core Rule

A wrong-network send is not the same thing as a delayed BCH payment.

Treat it as a routing problem first.

## First Questions

### 1. What asset was sent?

Do not assume it was BCH.

### 2. What network was used?

The customer may have used another chain while thinking they were paying with BCH.

### 3. What address format was involved?

Address-format confusion can contribute to routing mistakes.

### 4. Who controls the receiving keys, if anyone?

Recovery possibilities depend on key control and compatibility.

## Triage Procedure

### 1. Separate three different possibilities

Determine whether the problem is:

- a real BCH payment that is merely delayed in the merchant view
- a wrong-network send
- a wrong-address send

### 2. Verify the transaction details before discussing recovery

Support should understand what actually happened before saying whether recovery is possible.

### 3. Do not promise recovery early

Self-custodial mistakes do not guarantee recovery.

### 4. Escalate if key control or chain compatibility matters

If the case involves recovery theory, it should go to a knowledgeable operator.

## Staff Rules

- do not call it a pending BCH payment if the network was wrong
- do not guess about recovery steps casually
- do not confuse address-format issues with guaranteed recoverability

## Escalate When

Escalate if:

- the asset is unclear
- the network is unclear
- the receiving keys may be controlled by the business
- the user asks about technical recovery paths

## Short Answer

Wrong-network triage starts by identifying the asset, network, address context, and key control. Do not treat it as a normal delayed BCH payment or promise recovery too early.