# ADR 0006: Minors and guardians

- **Status:** Accepted for the data model. **The pilot enrols adults and children**
  (19 Nov): *provisional, awaiting clinical-lead sign-off and ethics approval*.
- **Date:** 2026-11-16; amended 2026-11-19 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q3

## Context

PRD §10.1 puts minor accounts, guardian management and minor-to-adult transition in the MVP.
§14.3 focuses the pilot on adolescents and adults. §8.8.1.4 leaves the guardian's access at
18, re-verification and independent credentials open. Most people with SCD in Kenya are
diagnosed in childhood.

## Decision

1. Guardian relationships and the minor-to-adult transition are in the **data model now**.
2. **The pilot enrols adults and children** (*provisional*, 19 Nov). Final approval rests
   with the clinical lead and the ethics committee.

## Consequences

- **Data model:** `GuardianRelationship` and `Patient.adult_transition_at`
  (`docs/data-model.md` §3.5).
- **OTPs and SMS for a minor** can go to the guardian's phone (`OtpChallenge` /
  `SmsMessage` `sent_to_guardian`).
- **Consent** may be given by a guardian on a minor's behalf.
- **Enrolment of minors** can be switched off by configuration if ethics approval excludes
  children.
- **PRD change:** PC-10 (§14.3 changes from "adolescents and adults" to adults and children,
  provisional).
- **Open:**
  - **Q-G1** (PRD §8.8.1.4): guardian access after 18, re-verification, credentials.
  - **Q-G2:** more than one active guardian at once?
  - **Q-G3:** where an adolescent's OTPs go by default.
  - The age of majority is 18 (Children Act 2022). Should adolescents get any
    self-management before 18?
