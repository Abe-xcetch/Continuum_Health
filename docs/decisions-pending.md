# Pending technical decisions

Decisions that block or shape code but are not product questions in the PRD itself.
Product decisions live in `docs/prd-review.md` §f. Decisions already made are recorded as
ADRs in `docs/decisions/`; the detailed list of open data-model questions is in
`docs/data-model.md` §5.

## Scope question: SCD-only, or other chronic illnesses?

**Status:** open (raised 19 Nov 2026). **Decide before build step 5** (the dataset).

PRD §16.2 puts other diseases out of scope, and §17.2 lists them as future work. Should the
pilot design stay **SCD-only**, or **anticipate other chronic illnesses** (e.g. diabetes,
HIV, hypertension)?

What changes:
- **Dataset:** `DatasetElement` would need a condition/programme key (e.g. `scd`), with
  per-condition required elements and completeness. This is cheap to add now, and a
  migration later.
- **Patient:** "SCD confirmed" would become one entry in a list of the patient's
  conditions.
- **Emergency summary and verification categories:** they would become per condition.
- **Privacy:** if Continuum is known as an SCD-only service, then being in it, receiving
  its SMS or being on its lists reveals the diagnosis (data-model Q-S1). A multi-condition
  service reduces that.
- **Consent categories:** "full SCD record" would need generalising.

Recommendation, for the group to decide:
- Keep the **pilot SCD-only**.
- Add only the cheap hooks now: a `condition` key on dataset elements, and neutral
  branding and SMS wording.

## Status of prd-review §f after the 16, 18 and 19 Nov 2026 decisions

Status labels:
- *provisional*: a team clinical answer awaiting clinical-lead sign-off.
- *proposed*: pending group confirmation.

**Decided (ADRs 0001–0007; PRD changes in `docs/prd-changes.md`):**
- Q9, Q10 verification: `unverified` + `source` (ADR 0001)
- Q5, Q6 dataset and blood group (ADR 0002; list *provisional*)
- Q12, Q13 identifiers and matching; **sex only** (ADR 0003)
- Q14 no card or QR (ADR 0004 4c); Q16, Q17, Q18 emergency (ADR 0004)
- Q19 break-glass cadres: MO and CO (*provisional*)
- Q20 consent to a care team, with **OTP at every visit** (ADR 0005, option B)
- Q3 minors in the data model; **the pilot enrols adults and children** (ADR 0006;
  *provisional*)
- Multi-facility design (ADR 0007)
- Modelling choices M2–M5: typed dataset table, now including `integer`; supersession
  history; triggers; `pg_trgm`

**Awaiting clinical-lead sign-off** (*provisional*):
- Verification defaults (ADR 0001)
- The dataset element list and its flags (ADR 0002; data-model §3.6 ⚑1–⚑5):
  - genotype Required vs Optional
  - the meaning of the transfusion "number"
  - genotype as a lab value / the sickling screen
  - emergency summary content
- Hydroxyurea dose in mg/day; hospitalisation = any ward admission
- Break-glass cadres MO and CO; emergency summary content (ADR 0004)
- Enrolling children (ADR 0006; also needs ethics approval)

**Proposed, pending group confirmation:**
- Visit session until the visit ends, at most 12 h; OTP fallback with break-glass-style
  review (ADR 0005)
- The SMS design: Continuum ID at enrolment, fixed templates, no medical information
  (ADR 0004 4c)
- Q-D6: admissions recorded from enrolment; treatment history and responses in phase 2
  (ADR 0002)

**Still open from prd-review §f:**
- Q1 entry points
- Q2 native app vs web
- Q4 hospital integration
- Q7 lab-result structure
- Q8 care-plan structure and review interval
- Q11 (partly covered by the configurable rules)
- Q15 emergency-contact search
- Q21 restricted categories
- Q22, Q23 administrator access
- Q24 closure / retention
- Q25 deceased / inactive
- Q26 notification channels (SMS is now required)
- Q27 audit granularity
- Q28 medical-records role
- Q29 PRD hygiene

**Still open from the data-model plan** (`docs/data-model.md` §5):
- Q-D3 to Q-D9: dataset details
- Q-V2 to Q-V6: verification, including consultants
- Q-I1 to Q-I5: identifiers
- Q-C3 to Q-C8, Q-A1 to Q-A3: consent, visits, access
- Q-E3, Q-E4, Q-S1 to Q-S3: emergency and SMS, including the SMS provider
- Q-G1 to Q-G3: minors
- Q-T1, Q-R1, Q-M6: technical

## TODO: controlled, audited purge for retention / erasure requests

**Status:** pending a policy decision. **Do not implement until decided.**

The codebase has **no hard-delete path**: `ContinuumModel` soft-deletes on both instance and
queryset `delete()`, there is no `hard_delete()` method, and the admin cannot delete users.
This follows CLAUDE.md ("clinical records are never hard-deleted").

At some point a lawful need to permanently remove or anonymise data may arise, for example:
- a patient's account-closure request once retention periods have passed (PRD §7.9, §6.1)
- a data-subject erasure request under the Kenya Data Protection Act 2019
- test or erroneous records created during the pilot

Before building anything, decide:
1. The retention period for each record type (Kenyan law and the pilot facility's policy).
2. Purge vs anonymisation: delete rows, or strip identifiers and keep clinical history?
3. Who may authorise a purge (two-person approval?), and how it is requested.
4. What audit evidence survives the purge (who, when, why, which records, but no content).
5. How backups are handled.

When decided, implement it as a dedicated, permission-gated service with its own audit
trail and tests. Do not add a generic `hard_delete()` to the base models.

## Patient authentication path

**Status:** open (PRD §11.4; prd-review §f).

`accounts.User` uses email + password and is for **staff/clinician accounts only**. PRD §11.4
describes patients logging in with a Continuum Patient ID or username, with OTP, and many
pilot patients may have no email. Patient login is expected to be a **separate
authentication path** (its own backend and flow). Decide the identifier, the OTP channel
and the account-recovery process before modelling patient accounts.
