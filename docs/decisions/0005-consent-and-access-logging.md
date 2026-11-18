# ADR 0005: Consent and access logging

- **Status:** Accepted; amended 2026-11-18 (care team grantee). Item 5 (no per-visit OTP)
  is **proposed, pending group confirmation**.
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q20, Q27 (partly)

## Context

The PRD does not say who consent is granted to, its scope, its duration or how it is
revoked (§12.2.3, §10.8), and it asks that patients not approve every piece of information
individually. It requires that access, including "what information was viewed", be audited
(§11.6, §13.1.7, §13.1.8) and visible to patients (§13.1.9), and that sessions end
(§12.4.2). It also requires an OTP "patient access authorisation" for each normal-care
session (§12.2.1).

## Decision

1. Consent is granted **to a care team at a facility** (for example, the SCD Clinic at the
   pilot hospital). It lasts **until revoked**, with an **annual review reminder**.
   *(Amended 18 Nov 2026: "a facility's care team" now means a named care team, not the
   whole facility.)*
2. Only members of that care team act under the consent. **Staff outside the team, such as
   pilot ED staff outside the SCD Clinic team, must use break-glass** (ADR 0004 4b), unless
   the patient grants consent to their team.
3. There are three consent categories:
   - **emergency summary**
   - **full SCD record**
   - **lab results**
4. **Break-glass bypasses consent.**
5. *Proposed, pending group confirmation:* **no OTP at each visit** under standing consent.
   OTP is used to **grant consent to a new care team** and for **patient login**.
6. **Every record access is logged** with:
   - **who** (user, cadre, facility, care team)
   - **when**
   - **approximate duration**, from when the record is opened until the last activity, or
     until the session times out

## Consequences

- Data model (`docs/data-model.md` §3.2, §3.10–§3.12):
  - `CareTeam` and `CareTeamMembership`
  - `Consent`, whose grantee is a care team
  - `AccessSession`, which records the care team whose consent was used
  - append-only `AccessEvent`
- This is what makes the pilot's ED test meaningful (ADR 0007): ED access to SCD-clinic
  patients goes through break-glass.
- Revoking consent ends access from the next request; past access stays in the log.
- **Access logs are append-only,** enforced by database triggers (PRD §13.1.8).
- **PRD change:** consent grantee and duration (PC-7). If item 5 is confirmed, PRD §12.2.1's
  per-session OTP also changes (D8).
- **Open:**
  - The PRD's restricted/sensitive layer (§12.2.4) has no category. Is it out of the MVP?
  - How consent is captured for patients with no phone (a signed form?).
  - Whether the log records sections viewed or every field (the plan: sections).
