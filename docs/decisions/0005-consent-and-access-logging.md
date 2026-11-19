# ADR 0005: Consent, visit authorisation and access logging

- **Status:** Accepted; amended 2026-11-18 (care team grantee) and 2026-11-19 (**OTP at
  every visit**, option B). The session length and the OTP fallback are **proposed,
  pending group confirmation**.
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q20, Q27 (partly)

## Context

The PRD does not say who consent is granted to, its scope, its duration or how it is
revoked (§12.2.3, §10.8). It requires an OTP "patient access authorisation" for each
normal-care session (§12.2.1), audit of access (§11.6, §13.1.7, §13.1.8), patient visibility
(§13.1.9) and defined sessions (§12.4.2).

On 18 Nov the group considered two options:
- (A) standing consent alone grants access
- (B) consent plus an OTP at every visit

## Decision

1. Consent is granted **to a care team at a facility**, **until revoked**, with an
   **annual review reminder**. Consent makes the team **eligible**; it does not open the
   record by itself.
2. **OTP at every visit** *(decided 19 Nov, option B)*. A patient OTP opens a
   **time-limited access session for that visit**. Reason: need-to-know access under data
   protection law. The patient takes part in each access, rather than relying on a
   standing grant.
3. *Proposed, pending group confirmation:*
   - The visit session lasts **until the end of the visit, at most 12 hours**.
   - **Fallback when an OTP is impossible** (no phone, no signal, a guardian holds the
     phone): the clinician records the reason, access is granted for that visit, and the
     access is **logged and reviewed like break-glass**.
4. Staff outside the consented care team (e.g. pilot ED staff outside the SCD Clinic team)
   use break-glass (ADR 0004 4b).
5. There are three consent categories:
   - **emergency summary**
   - **full SCD record**
   - **lab results**
6. Granting consent to a **new care team** is also confirmed by an OTP (or a signed form if
   the patient has no phone; open). Break-glass bypasses consent and OTP.
7. **Every record access is logged** with:
   - **who** (user, cadre, facility, care team)
   - **when**
   - **approximate duration**, from when the record is opened until the last activity, or
     until the session times out

## Consequences

- **Data model** (`docs/data-model.md` §3.10–§3.15):
  - `Consent` (eligibility)
  - `VisitAuthorisation` (per-visit window; `otp` or `fallback`, with fallback review)
  - `OtpChallenge` (hashed codes, short expiry, attempt limit)
  - `AccessSession` (basis is a visit authorisation or break-glass)
  - append-only `AccessEvent`
- **SMS** is needed at every visit, and the OTP SMS contains no medical information (ADR
  0004 4c).
- **The PRD's per-session OTP (§12.2.1) stays.** PC-7a records the additions: consent equals
  eligibility, time-limited visits, the fallback.
- **Revoking consent** ends the open visit authorisations for that team at the next
  request; past access stays in the log.
- **Open:**
  - Q-C6: does a visit authorisation cover the whole care team?
  - Q-C7: who ends a visit?
  - Q-C8: fallback cadres, reviewer and SMS
  - Q-C4: consent without a phone
  - the restricted category (prd-review Q21)
  - log granularity (the plan logs sections)
