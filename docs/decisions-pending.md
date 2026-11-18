# Pending technical decisions

Decisions that block or shape code but are not product questions in the PRD itself.
Product decisions live in `docs/prd-review.md` §f. Decisions already made are recorded as
ADRs in `docs/decisions/`; the detailed list of open data-model questions is in
`docs/data-model.md` §5.

## Status of prd-review §f after the 16 and 18 Nov 2026 decisions

**Decided (ADRs 0001–0007; PRD changes in `docs/prd-changes.md`):**
- Q9, Q10 verification, amended 18 Nov: `unverified` + `source` (ADR 0001)
- Q5 dataset and Q6 blood group, now the agreed list (ADR 0002)
- Q12, Q13 identifiers and matching; sex required, gender optional (ADR 0003)
- Q14, Q16, Q17, Q18 emergency (ADR 0004)
- Q20 consent to a care team at a facility (ADR 0005, amended 18 Nov)
- Q3 minors in the data model (ADR 0006)
- Multi-facility design (ADR 0007)
- Modelling choices accepted 18 Nov (data-model M2–M5):
  - typed dataset table with guard rails and a reporting view
  - supersession rows for history
  - PostgreSQL triggers created by migrations and tested
  - `pg_trgm`

**Decided but awaiting sign-off or confirmation:**
- ADR 0001 cadre-to-category verification rules: clinical lead.
- ADR 0002 agreed element list: clinical lead. Includes the hydroxyurea dose unit, the
  definition of a hospitalisation, and which elements appear in the emergency summary.
- ADR 0004 4c emergency card / QR: one group member to confirm.
- ADR 0005 item 5, no OTP at each visit under standing consent: **proposed**, pending group
  confirmation.
- ADR 0006 pilot enrolment of children: clinical lead and ethics approval.

**Still open from prd-review §f:**
- Q1 entry points
- Q2 native app vs web
- Q4 hospital integration
- Q7 lab-result structure
- Q8 care-plan structure and review interval
- Q11 which nurse- or lab-entered items need verification (partly covered by the
  configurable rules)
- Q15 search by emergency-contact phone
- Q19 which cadres count as "clinician" for break-glass
- Q21 restricted categories
- Q22, Q23 administrator access to patient data
- Q24 closure / retention
- Q25 deceased / inactive
- Q26 notification channels (SMS is now required for break-glass)
- Q27 audit granularity (plan: per section)
- Q28 medical-records role
- Q29 PRD hygiene

**Still open from the data-model plan** (details in `docs/data-model.md` §5):
- Q-V2 to Q-V5 (verification details)
- Q-I1 to Q-I5 (identifiers; includes encrypting national ID / SHA numbers)
- Q-C3 to Q-C5, Q-A1 to Q-A3 (access)
- Q-E1 to Q-E4 (emergency; includes the break-glass reviewer and deadline)
- Q-G1, Q-G2 (minors)
- Q-T1 (`pg_trgm` privilege in production)
- Q-R1 (who reads the reporting view)
- Q-M6 (app split)
- Choice of SMS provider

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
