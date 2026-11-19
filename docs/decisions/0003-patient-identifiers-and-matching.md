# ADR 0003: Patient identifiers and matching rules

- **Status:** Accepted; amended 2026-11-19 (record sex only).
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q12, Q13

## Context

The PRD lists identifiers inconsistently (§7.1, §8.2, §11.1, §12.2) and defines no rule for
confirming that a search result is the right person. Kenya is introducing a national Client
Registry and the Social Health Authority (SHA) number; neither is in the PRD. The PRD
records "gender" throughout and never sex.

## Decision

1. Store the following identifiers in a **separate identifier table**:
   - Client Registry ID
   - national ID or birth certificate number
   - SHA number
   - phone number
   - Continuum ID

   Each row holds type, value, verification method and verified-at (and verifier).
2. The table is designed so that a Client Registry lookup can be added later without a
   schema change. There is **no registry lookup in the pilot**.
3. Matching:
   - **Confirmed match:** one strong identifier agrees, plus name or date of birth agrees.
   - **Probable match:** name + date of birth + sex agree, with no strong identifier. It is
     shown with a warning and must be confirmed deliberately.
4. **Record sex only** (required: used for matching and clinical care). **Do not record
   gender.** *(Decided 19 Nov; replaces the 18 Nov "sex required, gender optional".)*

## Consequences

- The data model has `PatientIdentifier`, and `Patient.sex` is required with no gender
  field (`docs/data-model.md` §3.4).
- Strong identifiers are unique across live patients; this is the main duplicate safeguard.
- The match level is stored on every search audit event.
- **PRD change:** replace "Gender" with "Sex" throughout (PC-5); the identifier list
  (PC-4).
- **Open:**
  - Q-I1: whether phone counts as a strong identifier (the plan says no)
  - Q-I5: the hospital patient number
  - Q-I4: which identifiers are required at registration
