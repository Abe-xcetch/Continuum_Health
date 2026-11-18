# ADR 0001: Per-item clinical verification with configurable cadre rules

- **Status:** Accepted, amended 2026-11-18 (status renamed; `source` added). The
  cadre-to-category rules await **clinical-lead sign-off**.
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q9, Q10 (partly Q11)

## Context

The PRD disagrees with itself on who may verify clinical information. §7.4 says an
"appropriately authorized healthcare professional … rather than automatically requiring a
physician" and leaves authority per category TBC. §8.2.1, §10.6, §11.1.2, §11.5.1, §12.2.5
and §13.1.3 say only an authorised physician may verify. The PRD also mixes per-item
statuses (§7.4) with a whole-record status (§11.1.3). In Kenyan practice, clinical officers
and nurses deliver much SCD care, so a physician-only rule may not fit the pilot facility.

## Decision

1. Verification status is stored **per clinical item**, not per record, with one of:
   - `unverified`
   - `clinician-verified`
   - `disputed`
   - `retracted`

   *Amended 18 Nov 2026:* the first status was originally `self-reported`. It was renamed
   because an unverified item entered by a clinician is not self-reported.
2. Each item also records its **source**, meaning where the information came from:
   `patient`, `clinician` or `import`. This is separate from the status. A guardian's
   entry counts as `patient`, and the user who typed the entry is recorded separately.
   *(Added 18 Nov 2026.)*
3. Every status change records the **verifier** (user, cadre, facility) and a **timestamp**,
   and is kept in an append-only history.
4. **Which cadres may verify which categories of information is configuration, not code.**
   It is held as data (cadre × category) that an authorised administrator can change, with
   each change audited. No cadre, including physicians, is hard-coded as a verifier.
5. The whole-record status in PRD §11.1.3 (Unverified / Partially / Clinically verified)
   is **derived** from the item statuses for display; it is not stored.

## Consequences

- Every clinical item model carries the same verification fields; see
  `docs/data-model.md` (`VerifiableMixin`, `VerificationEvent`, `VerificationPermission`).
- Until the clinical lead signs off the rules, the permission table ships **empty**, so
  nobody can verify. Seed data for the pilot is a separate, reviewed data migration.
- Emergency access never changes a status (PRD §11.5.2, §13.1.6 still hold).
- The PRD's physician-only wording must change in the revision (§8.2.1, §10.6, §11.1.2,
  §11.5.1, §12.2.5, §13.1.3).
- PRD §7.4's "patient-reported" and "clinician-documented" are expressed as `unverified`
  plus the `source` (patient or clinician).
- **Open:** "requiring review/update" (§7.4): a status, or derived from review dates
  (data-model Q-V2)? Also open: whether a clinician may verify their own entry (Q-V4).
