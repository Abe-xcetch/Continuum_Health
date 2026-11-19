# PRD change log (to apply in the PRD revision)

`docs/prd.md` is the v0 baseline and is **not edited** until the agreed PRD revision. This
file lists the changes so the revision can apply them in one pass. Each entry links to its
decision and to the disagreement row (D-n) in `docs/data-model.md` §4.

Status values:
- **Decided:** apply in the revision.
- **Provisional:** a team clinical answer; apply after clinical-lead sign-off.
- **Proposed:** pending group confirmation; do not apply yet.

| # | Change | PRD sections affected | Source | Status |
|---|---|---|---|---|
| PC-1 | Verification authority is configurable per cadre and category; remove "only an authorised physician". Defaults: MO and CO everything; lab technologist lab values (may be disabled in the pilot); nurse allergies; pharmacist none | §8.2.1, §10.6, §11.1.2, §11.5.1, §12.2.5, §13.1.3 | ADR 0001; D1 | Mechanism decided; defaults **provisional** |
| PC-2 | Per-item statuses become unverified / clinician-verified / disputed / retracted, plus a source (patient, clinician, import) | §7.4, §7.10, §8.2.1, §8.10 | ADR 0001; D2 | Decided |
| PC-3 | The record-level clinical status is derived from item statuses | §11.1.3 | ADR 0001; D3 | Decided |
| PC-4 | The identifier list (Client Registry ID, national ID / birth certificate, SHA, phone, Continuum ID); confirmed and probable match rules; no registry lookup in the pilot | §7.1, §7.3, §8.2, §10.4, §11.1, §12.2 | ADR 0003; D4 | Decided |
| PC-5 | **Record sex only (required; used for matching and clinical care); remove gender.** Replace "Gender" with "Sex" | §7.1, §7.3, §7.6, §8.2, §9.1.1.1, §11.1, §11.2, §12.2.2 | ADR 0003 (19 Nov); D5 | Decided |
| PC-6 | Remove biometric identification from the MVP; the unconscious patient without documents is out of scope; emergency contacts are not a search method | §8.5.1.1, §9.1.1, §10.4 | ADR 0004 4d; D6, D20 | Decided |
| PC-7 | Consent is granted to a care team at a facility, until revoked, with an annual review; three categories; consent makes the team eligible; staff outside the team use break-glass | §10.8, §12.2.3, §12.4, §12.4.1 | ADR 0005; D7 | Decided |
| PC-7a | **OTP at every visit (option B).** A patient OTP opens a time-limited access session for that visit. Keep the §12.2.1 per-session OTP and add that consent makes the team eligible. *Proposed details:* the session lasts until the visit ends, at most 12 h; when an OTP is impossible, the clinician records a reason, access is granted for that visit, and it is logged and reviewed like break-glass | §12.2.1, §12.2.5 Scenario A, §12.4.2 | ADR 0005 (19 Nov); D8 | **Decided (B)**; session length and fallback **proposed** |
| PC-8 | Emergency access shows the emergency summary only, with unverified items labelled. Content: SCD + genotype, allergies, blood group + Rh, transfusion reactions, current medicines including hydroxyurea, pain management / things to avoid, emergency contact, usual facility | §7.6, §9.3.1.1, §12.2.5, §13.1.6 | ADR 0004 4a; D9 | Scope decided; content **provisional** |
| PC-9 | Break-glass: medical officers and clinical officers only; reason required; 12-hour expiry; logged; patient SMS (no medical information); post-hoc review | §6.3, §9.2, §9.3.1, §9.3.5, §10.9, §12.2.5, §13.1.6 | ADR 0004 4b; D11, D12 | Rules decided; cadres **provisional** |
| PC-10 | Guardian accounts and minor-to-adult transition in the MVP data model; **the pilot enrols adults and children** | §8.8.1.4, §10.1, §14.3 | ADR 0006; D15 | **Provisional** (clinical lead + ethics) |
| PC-11 | Multi-facility design; the pilot tests ED staff opening an SCD-clinic record | §14.2, §14.8, §16.3 | ADR 0007; D16 | Decided |
| PC-12 | Replace the seven SCD categories with the core dataset (ADR 0002 list); blood group and Rh becomes Required | §7.6, §8.3, §14.5, §15.4, §16.5 | ADR 0002; D17, D18 | **Provisional** |
| PC-13 | No card or QR. At enrolment the patient receives their Continuum ID by SMS; **no medical information is ever sent by SMS** | New text in §8.2, §8.5.1.1, §10.4, §10.12 | ADR 0004 4c (19 Nov); D13 | No card: decided. SMS design: **proposed** |
| PC-14 | Hospitalisations: a 12-month count at enrolment, then every new admission recorded (admission date, discharge date, facility, reason); treatment history and treatment responses deferred to phase 2 | §8.3, §14.5, §16.5 | ADR 0002 (Q-D6); D17 | **Proposed** |
