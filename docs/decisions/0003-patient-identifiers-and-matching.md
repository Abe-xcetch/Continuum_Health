# ADR 0003: Patient identifiers and matching rules

- **Status:** Accepted.
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q12, Q13

## Context

The PRD lists identifiers inconsistently (§7.1, §8.2, §11.1, §12.2) and defines no rule for
confirming that a search result is the right person (§10.4 "duplicate-patient safeguards"
are undefined). Kenya is introducing a national Client Registry (master patient index) and
the Social Health Authority (SHA) number; neither is mentioned in the PRD.

## Decision

1. The following identifiers are stored in a **separate identifier table**, one row per
   identifier:
   - Client Registry ID
   - national ID or birth certificate number
   - SHA number
   - phone number
   - Continuum ID
2. Each row holds: type, value, verification method, verified-at (and verifier).
3. This is designed so that a **Client Registry lookup can be added later without a schema
   change**. There is **no registry lookup in the pilot**.
4. Matching rules for Search & Find:
   - **Confirmed match:** one **strong identifier** agrees, plus **name or date of birth**
     agrees.
   - **Probable match:** name + date of birth + sex agree, with no strong identifier. The
     result is shown **with a warning** and the user must confirm it deliberately.
   - Anything weaker is not shown as a match.

## Consequences

- `PatientIdentifier` replaces per-identifier columns on `Patient`
  (`docs/data-model.md` §3.4).
- Strong identifiers are unique across live patients (database constraint), which is also
  the main duplicate-record safeguard.
- The probable-match rule needs a recorded **sex**, which the PRD does not have (it
  records "gender" throughout). *Decided 18 Nov 2026:* the patient record stores **sex
  (required**; used for matching and clinical care) and **gender (optional)** as separate
  fields. This is a PRD change (`docs/prd-changes.md` PC-5).
- The match level (confirmed or probable) is stored on every search audit event.
- **Open:** which identifier types count as "strong". Phone numbers are often shared or
  recycled in Kenya, so the data model treats phone as **not strong**. Needs confirmation.
- **Open:** the hospital patient number (PRD §7.1, §10.16) is not in the list above. The
  data model adds it as a facility-scoped identifier type for confirmation.
