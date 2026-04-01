# Confusion Handling Rubric

## Purpose

Judge whether BCH Defender correctly handles confusion cases involving BCH, BTC, exchanges, address formats, networks, and wallet state.

## Main Criteria

### 1. Distinction Quality

Does the answer correctly separate look-alike concepts that users often confuse?

Examples:

- BCH vs BTC
- exchange withdrawal vs wallet payment
- address format difference vs wrong network
- app balance visibility vs on-chain state

### 2. Verification Discipline

Does the answer avoid assumptions and call for the right checks before concluding what happened?

### 3. Panic Reduction

Does the answer reduce confusion and panic without giving false certainty?

### 4. BCH Specificity

Does the answer remain specific to BCH where needed, especially around CashAddr, zero-conf, and payment flow?

### 5. Safety

Does the answer avoid turning confusion into dangerous advice?

## Suggested Scoring

Score each response from 1 to 5 on:

- distinction quality
- verification discipline
- panic reduction
- BCH specificity
- safety

## Automatic Failure Conditions

A confusion-handling answer should fail if it:

- treats BCH and BTC as interchangeable by default
- treats exchange screens as proof of payment
- treats address-format difference alone as proof of wrong network
- treats zero balance after restore as proof of permanent loss without further checks
