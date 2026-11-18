# ADR 0006: Minors and guardians

- **Status:** Accepted for the data model. **Pilot enrolment of children** is to be decided
  by the clinical lead and ethics approval.
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q3 (data-model part)

## Context

PRD §10.1 puts minor accounts, guardian management and minor-to-adult transition in the MVP.
§14.3 focuses the pilot on adolescents and adults, with younger patients "to be
considered". §8.8.1.4 leaves the guardian's access at 18, re-verification and independent
credentials open. Most people with SCD in Kenya are diagnosed in childhood, so adding
guardians later would mean reworking consent and access.

## Decision

1. **Guardian relationships** and the **minor-to-adult transition** are in the **data model
   now**.
2. Whether **children are enrolled in the pilot** is decided by the clinical lead and the
   ethics approval, not by the software.

## Consequences

- Data model: `GuardianRelationship` (who, legal basis, verified, start/end, end reason)
  and a transition record on the patient (`docs/data-model.md` §3.5).
- Consent and break-glass notifications may be given to or sent to a guardian on behalf of
  a minor.
- Enrolment of minors can be switched off by configuration until approved.
- **Open (PRD §8.8.1.4):**
  - What the guardian may still see after the patient turns 18.
  - How the patient's identity is re-verified at transition.
  - Whether the patient must set up independent credentials (depends on the patient-login
    decision in `docs/decisions-pending.md`).
- **Open:** the age of majority for this purpose is 18 (Kenyan Children Act). Are
  adolescents allowed any self-management before 18?
