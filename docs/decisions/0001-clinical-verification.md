# ADR 0001: Per-item clinical verification with configurable cadre rules

- **Status:** Accepted; amended 2026-11-18 (status renamed; `source` added). The
  default cadre rules (19 Nov) are **provisional, awaiting clinical-lead sign-off**.
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q9, Q10 (partly Q11)

## Context

The PRD disagrees with itself on who may verify clinical information. §7.4 says an
"appropriately authorized healthcare professional … rather than automatically requiring a
physician", and leaves authority per category TBC. §8.2.1, §10.6, §11.1.2, §11.5.1, §12.2.5
and §13.1.3 say only an authorised physician may verify. The PRD also mixes per-item
statuses (§7.4) with a whole-record status (§11.1.3). In Kenyan practice, clinical officers
and nurses deliver much SCD care.

## Decision

1. Verification status is stored **per clinical item**, with one of:
   - `unverified`
   - `clinician-verified`
   - `disputed`
   - `retracted`

   *(Amended 18 Nov: originally `self-reported`.)*
2. Each item records its **source** separately from its status: `patient`, `clinician` or
   `import`. A guardian's entry counts as `patient`, and the user who typed the entry is
   recorded separately. *(Added 18 Nov.)*
3. Every status change records the **verifier** (user, cadre, facility) and a **timestamp**,
   in an append-only history.
4. **Which cadres may verify which categories of information is configuration, not code.**
   Each rule can be enabled or disabled without being deleted, and every change is audited.
5. The whole-record status (PRD §11.1.3) is **derived** from item statuses; it is not
   stored.

### Default rules: *provisional, awaiting clinical-lead sign-off* (19 Nov)

| Cadre | May confirm |
|---|---|
| Medical officer (MO) | everything |
| Clinical officer (CO) | everything |
| Laboratory technologist | blood group and Rh, baseline Hb and other lab values (**may be disabled in the pilot**) |
| Nurse | allergies only |
| Pharmacist | nothing |

## Consequences

- The data model has `VerifiableMixin`, `VerificationEvent` and `VerificationPermission`
  (with an `is_enabled` flag), and each element or model has a verification category
  (`docs/data-model.md` §3.3, §3.6–§3.8).
- The defaults are written as a data migration. In production they are enabled only after
  sign-off.
- Emergency access never changes a status (PRD §11.5.2, §13.1.6).
- **PRD change:** remove the physician-only wording (PC-1); adopt the new statuses and
  source (PC-2).
- **Open:**
  - Q-V2: "requiring review/update" (§7.4)
  - Q-V4: whether clinicians may verify their own entries
  - Q-V6: where consultants and specialists fit
  - Q-D5: whether genotype is a lab value that a lab technologist may confirm
