# ADR 0004: Emergency access

- **Status:** Accepted for 4a, 4b, 4c and 4d. The 4a summary content and the 4b cadres are
  **provisional, awaiting clinical-lead sign-off**. The 4c SMS design is **proposed,
  pending group confirmation**.
- **Date:** 2026-11-16; amended 2026-11-19 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q14, Q16, Q17, Q18, Q19; prd-review §d gaps 1, 2, 6

## Context

The PRD does not say what emergency access shows (§7.6 vs §12.2.2 vs §12.2.5), what the
automatic approval rules are (§9.3.5), whether unverified items are visible, or how a
clinician learns that a patient has SCD before searching. Biometrics appear in the MVP
features (§10.4) but are out of scope (§11.4, §16.6).

## Decision

**4a. What emergency access shows:** the **emergency summary only**. Unverified items are
shown, clearly labelled as unverified.

*Summary content, provisional (19 Nov):*
- SCD and genotype
- allergies
- blood group and Rh
- transfusion reactions
- current medicines, including hydroxyurea
- pain management / things to avoid
- emergency contact
- usual facility

**4b. Break-glass:**
- **Who:** an authenticated clinician at a registered facility. **Only medical officers and
  clinical officers** may invoke it (*provisional, 19 Nov*).
- **Requires** a reason.
- **Expires** after 12 hours.
- **Logged** in full.
- The **patient is notified by SMS**.
- Every use gets a **post-hoc review**.
- Approval is automatic once the conditions and reason are given.

**4c. No card or QR** *(decided 19 Nov; replaces the proposed card/QR).* Instead:
- *Proposed, pending group confirmation:* at enrolment the patient receives their
  **Continuum ID by SMS**.
- **No medical information is ever sent by SMS**, in any message.

**4d. An unconscious patient without documents** is out of MVP scope, and biometric
identification is removed. Treatment proceeds as normal care without Continuum.

## Consequences

- **Data model** (`docs/data-model.md`):
  - `BreakGlassAccess`, with the 12-hour limit enforced by the database
  - `Cadre.may_break_glass` (MO and CO true)
  - `SmsMessage` with fixed templates and no stored message body
- **The `EmergencyCard` model is removed** from the plan.
- **The emergency summary is a view over existing records**, never a copy.
- **The break-glass SMS** says only that the record was opened, and when, with a contact
  number. It names no diagnosis and no facility.
- **An SMS provider** becomes an MVP dependency. A patient with no phone gets no SMS; the
  event still appears in their access history.
- **PRD change:**
  - remove biometrics (PC-6)
  - emergency summary scope (PC-8)
  - break-glass rules (PC-9)
  - Continuum ID by SMS (PC-13, proposed)
- **Open:**
  - Q-E3: who reviews break-glass events, and within how long
  - Q-E4: SMS recipient for a minor
  - Q-S1: whether the sender name "Continuum" itself reveals SCD if the service is
    SCD-only
  - whether restricted information can ever be reached in an emergency (prd-review Q21)
