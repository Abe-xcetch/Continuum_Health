# PRD change log (to apply in the PRD revision)

`docs/prd.md` is the v0 baseline and is **not edited** until the agreed PRD revision. This
file lists the changes the group has decided so far, so the revision can apply them in one
pass. Each entry links to its decision and to the disagreement row (D-n) in
`docs/data-model.md` §4.

Status values:
- **Decided:** apply in the revision.
- **Awaiting sign-off:** apply after the named sign-off.
- **Proposed:** not yet agreed; do not apply.

| # | Change | PRD sections affected | Source | Status |
|---|---|---|---|---|
| PC-1 | Verification authority is configurable per cadre and category; remove "only an authorised physician" wording | §8.2.1, §10.6, §11.1.2, §11.5.1, §12.2.5, §13.1.3 (§7.4 already agrees) | ADR 0001; D1 | Decided (the rules themselves await clinical-lead sign-off) |
| PC-2 | Per-item statuses become unverified / clinician-verified / disputed / retracted, plus a separate source (patient, clinician, import) | §7.4, §7.10, §8.2.1, §8.10 | ADR 0001 (amended 18 Nov); D2 | Decided |
| PC-3 | The record-level clinical status (§11.1.3) is derived from item statuses, not maintained separately | §11.1.3 | ADR 0001; D3 | Decided |
| PC-4 | Identifiers: Client Registry ID, national ID / birth certificate, SHA number, phone, Continuum ID, in a separate identifier list; confirmed and probable match rules; no registry lookup in the pilot | §7.1, §7.3, §8.2, §10.4, §11.1, §12.2 | ADR 0003; D4 | Decided (which identifiers are required at registration is still open) |
| PC-5 | **Record sex (required; used for matching and clinical care) and gender (optional) as separate fields.** Replace "Gender" in the identity, search-result and Basic Access lists with "Sex" and add "Gender (optional)" | §7.1, §7.3, §7.6, §8.2, §9.1.1.1, §11.1, §11.2, §12.2.2 | Group decision 18 Nov 2026; ADR 0003; D5 | Decided |
| PC-6 | Remove biometric identification from the MVP; the unconscious patient without documents is out of MVP scope | §8.5.1.1, §9.1.1, §10.4 (consistent with §11.4, §16.6) | ADR 0004 4d; D6, D20 | Decided |
| PC-7 | Consent is granted to a care team at a facility, until revoked, with an annual review; three categories (emergency summary, full SCD record, lab results); staff outside the team use break-glass | §10.8, §12.2.3, §12.4, §12.4.1 | ADR 0005 (amended 18 Nov); D7 | Decided |
| PC-7a | No OTP at each visit under standing consent; OTP only for granting consent to a new care team and for patient login | §12.2.1, §12.2.5 Scenario A | ADR 0005 item 5; D8 | **Proposed**, pending group confirmation |
| PC-8 | Emergency access shows the emergency summary only, with unverified items labelled | §7.6, §9.3.1.1, §12.2.5, §13.1.6 | ADR 0004 4a; D9 | Decided |
| PC-9 | Break-glass: any authenticated clinician at a registered facility; reason required; 12-hour expiry; logged; patient SMS; post-hoc review | §9.3.1, §9.3.5, §10.9, §12.2.5, §13.1.6 | ADR 0004 4b; D11, D12 | Decided ("clinician" cadres still open) |
| PC-10 | Guardian accounts and minor-to-adult transition are in the data model; pilot enrolment of children is decided by the clinical lead and ethics | §8.8.1.4, §10.1, §14.3 | ADR 0006; D15 | Decided |
| PC-11 | Multi-facility design; the pilot tests ED staff opening an SCD-clinic record | §14.2, §14.8, §16.3 | ADR 0007; D16 | Decided |
| PC-12 | Replace the seven SCD categories with the agreed core dataset; blood group and Rh becomes Required (was TBC) | §7.6, §8.3, §14.5, §15.4, §16.5 | ADR 0002; D17, D18 | **Awaiting clinical-lead sign-off** |
| PC-13 | Patient card / QR showing "Sickle Cell Disease" + Continuum ID only | New text in §8.5.1.1 and §10.4 | ADR 0004 4c; D13 | **Proposed** (one member to confirm) |
