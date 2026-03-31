# Bitcoin Cash Protocol Upgrades

Since its launch in August 2017, the Bitcoin Cash network has received regular protocol upgrades focused on improving scalability, security, usability, and smart contract functionality.

## Overview

Bitcoin Cash follows a pattern of scheduled network upgrades, typically activated in May or November. These upgrades have expanded transaction capacity, improved signature handling, strengthened transaction validation rules, introduced new scripting capabilities, enabled token functionality, and improved blocksize management.

This upgrade history is important because it shows that BCH has continued to evolve as a peer-to-peer electronic cash system rather than remaining static.

## Upgrade Timeline

### November 13, 2017 — Improved Difficulty Adjustment Algorithm

Bitcoin Cash replaced the original Emergency Difficulty Adjustment (EDA) with an improved Difficulty Adjustment Algorithm (DAA).

This change was made to stabilize block production and improve the reliability of the network.

### January 9, 2018 — CashAddress Format Enabled

Bitcoin Cash enabled a native address format commonly known as **CashAddress**.

This new format improved usability and helped reduce confusion between BCH and BTC addresses.

### May 15, 2018 — Larger Blocks and Script Reactivation

The network upgrade on this date included several major changes:

- the maximum block size was raised to **32 MB**
- several script opcodes previously disabled by Bitcoin Core were reactivated
- the maximum size of `OP_RETURN` data was increased

This upgrade expanded BCH's transaction capacity and restored useful scripting features.

### November 15, 2018 — CTOR and New Opcodes

Bitcoin Cash implemented **Canonical Transaction Ordering (CTOR)** and enabled two new opcodes:

- `CHECKDATASIG`
- `CHECKDATASIGVERIFY`

These additions improved transaction ordering and expanded scripting possibilities.

### November 2018 — BCH / BSV Split

In November 2018, the network experienced a controversial hard fork that split the project into two separate cryptocurrencies:

- Bitcoin Cash
- Bitcoin SV

This was a major governance and ecosystem event in BCH history.

### May 15, 2019 — Schnorr Signatures and SegWit Recovery Exception

This upgrade enabled **Schnorr signatures** for compatibility with:

- `OP_CHECKSIG`
- `OP_CHECKDATASIG`

It also added an exception to the `CLEANSTACK` rule to allow recovery of some SegWit-related funds.

This improved efficiency and expanded cryptographic support.

### November 15, 2019 — Expanded Schnorr Support and MINIMALDATA

Bitcoin Cash expanded Schnorr signature compatibility to include:

- `OP_CHECKMULTISIG`
- `OP_CHECKMULTISIGVERIFY`

The network also added the **MINIMALDATA** rule, which removed a malleability vector described in BIP 62 and improved the security of most transactions, including the commonly used P2PKH type.

### May 15, 2020 — SigChecks and Other Improvements

This upgrade introduced several changes:

- the limit for chained unconfirmed transactions was increased from **25 to 50**
- SigOps limits were replaced by a new system called **SigChecks**
- the opcode `OP_REVERSEBYTES` was added

These changes improved flexibility and transaction validation.

### November 2020 — BCH / BCHA Split

In November 2020, a second controversial split occurred when Bitcoin ABC separated from the BCH network and launched a new cryptocurrency initially known as **BCHA**, later renamed **eCash (XEC)**.

### November 15, 2020 — ASERTI3-2D Difficulty Algorithm

Bitcoin Cash replaced its previous difficulty adjustment system with **aserti3-2d**.

This change reduced block time variance and improved the consistency of block production.

### May 15, 2021 — Removal of Chained Transaction Limit

Bitcoin Cash removed the limit on chained unconfirmed transactions and allowed multiple `OP_RETURN` outputs in a single transaction.

This further increased transaction flexibility and usefulness.

### May 15, 2022 — Bigger Script Integers and Native Introspection Opcodes

This upgrade expanded the arithmetic range of Script through **Bigger Script Integers** and added **Native Introspection Opcodes**.

These improvements increased the power and flexibility of BCH smart contract capabilities.

### May 15, 2023 — CashTokens, P2SH32, and Transaction Restrictions

This was one of the most important upgrades in BCH history. It introduced:

- **CashTokens**
- transaction version restrictions
- minimum transaction size restrictions
- the **P2SH32** address format

CashTokens significantly expanded BCH's native token and smart contract capabilities.

### May 15, 2024 — Adaptive Blocksize Limit Algorithm (ABLA)

Bitcoin Cash activated the **Adaptive Blocksize Limit Algorithm (ABLA)**.

ABLA automatically adjusts the maximum block size limit according to network usage, helping BCH scale more dynamically over time.

### May 15, 2025 — Targeted VM Limits and BigInt Arithmetic

This upgrade introduced:

- **Targeted VM Limits**
- high-precision **BigInt arithmetic** for contracts

These changes further expanded BCH's contract and virtual machine capabilities.

## Why These Upgrades Matter

The protocol upgrade history of Bitcoin Cash shows a consistent effort to improve the network in three core areas:

- **scalability** — by increasing capacity and improving blocksize management
- **security** — by refining validation rules and difficulty adjustment
- **functionality** — by adding scripting improvements, better cryptography, and token support

This matters because BCH is often described only in terms of the 2017 split, when in reality it has continued to develop as an independent network with ongoing technical progress.

## Notes

Two controversial splits are part of BCH history:

- the 2018 split that created Bitcoin SV
- the 2020 split that led to BCHA, later renamed eCash

Even so, the BCH network continued forward and kept upgrading the protocol.

## Conclusion

Bitcoin Cash has undergone regular protocol upgrades since 2017, with improvements ranging from block production stability and usability enhancements to scripting upgrades, token functionality, and adaptive scaling.

For anyone studying BCH, these upgrades are essential for understanding how the network has evolved beyond its original fork and continued pursuing peer-to-peer electronic cash at scale.
