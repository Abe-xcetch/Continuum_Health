# ADR 0004: Emergency access

- **Status:** Accepted for 4a, 4b and 4d. **4c is proposed: one member still to confirm.**
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q14, Q16, Q17, Q18 (partly Q19); prd-review §d gaps 1, 2, 6

## Context

The PRD does not say what emergency access shows (§7.6 vs §12.2.2 vs §12.2.5), what the
automatic approval rules are (§9.3.5), whether unverified items are visible (§12.2.2 says
"verified" while §12.2.5 Scenario D says unverified items are shown, labelled), or how a
clinician learns that a patient has SCD before searching (prd-review §d gap 1). Biometrics
appear in MVP features (§10.4) but are out of scope (§11.4, §16.6).

## Decision

**4a. What emergency access shows.** The **emergency summary only** (PRD §7.6). Unverified
items are shown, clearly **labelled as unverified**; they are never hidden and never
presented as verified.

**4b. Break-glass.**
- **Who:** any authenticated clinician acting at a registered facility.
- **Requires** a reason.
- **Expires** after 12 hours.
- **Logged** in full.
- The **patient is notified by SMS**.
- Every use is **reviewed afterwards** (post-hoc review).
- Approval is automatic once the conditions and reason are given (PRD §13.1.6 pilot rule).

**4c. Patient card / QR.** *Proposed, one member to confirm.* Patients may carry a card
whose face and QR code show only "**Sickle Cell Disease**" and the **Continuum ID**. No
name, no other clinical data.

**4d. Unconscious patient without documents** is **out of MVP scope**. Biometric
identification is **removed** from the MVP. Treatment proceeds as normal care without
Continuum (PRD §8.5.1.2, §11.5.2).

## Consequences

- Data model: `BreakGlassAccess` (12-hour expiry enforced by a database check),
  `EmergencyCard` (revocable token), and the emergency summary as a **view** over existing
  records, never a copy (PRD §7.6).
- An SMS provider becomes an MVP dependency. A patient with no phone (PRD §8.9) gets no SMS;
  the event still appears in their access history.
- Biometric items in PRD §8.5.1.1, §9.1.1 and §10.4 must be removed in the revision.
- **Open:** which cadres count as "clinician" for break-glass (nurses? clinical officers?
  never lab staff?). PRD §6.3 / §9.2 restrict nurses to when no physician is available.
- **Open:** whether break-glass can ever reach beyond the summary. PRD §12.2.5 allows
  emergency access to restricted information; 4a does not.
- **Open:** who performs the post-hoc review, and within how long.
- **Open (4c):** printing "Sickle Cell Disease" on a card discloses a diagnosis to anyone who
  sees it. Issuing a card should need the patient's (or guardian's) explicit agreement.
