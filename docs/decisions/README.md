# Architecture / product decision records (ADRs)

One short record per decision: context, decision, consequences, status. ADRs record what
the group decided; they do **not** change `docs/prd.md`. Where an ADR and the PRD disagree,
the disagreement is listed in the ADR and in `docs/data-model.md` §4 until the PRD revision
resolves it.

| # | Decision | Status | Decided |
|---|---|---|---|
| [0001](0001-clinical-verification.md) | Per-item verification (`unverified` + `source`), configurable cadre rules | Accepted; default rules *provisional* (clinical lead) | 16 Nov; amended 18 and 19 Nov |
| [0002](0002-scd-core-dataset.md) | SCD core dataset | Accepted; element list *provisional* (clinical lead); admissions from enrolment *proposed* | 16 Nov; list 18 and 19 Nov |
| [0003](0003-patient-identifiers-and-matching.md) | Patient identifiers and matching; sex only | Accepted | 16 Nov; amended 19 Nov |
| [0004](0004-emergency-access.md) | Emergency summary, break-glass (MO/CO), no card: Continuum ID by SMS, unconscious patients | Accepted; summary content and cadres *provisional*; SMS design *proposed* | 16 Nov; amended 19 Nov |
| [0005](0005-consent-and-access-logging.md) | Consent to a care team, OTP at every visit, access logging | Accepted (option B); session length and fallback *proposed* | 16 Nov; amended 18 and 19 Nov |
| [0006](0006-minors-and-guardians.md) | Minors and guardians; the pilot enrols adults and children | Accepted (data model); enrolment *provisional* (clinical lead + ethics) | 16 Nov; amended 19 Nov |
| [0007](0007-multi-facility.md) | Multi-facility design from the start | Accepted | 16 Nov |

Status labels:
- *provisional*: a team clinical answer awaiting clinical-lead sign-off.
- *proposed*: pending group confirmation.

**Deciders:** JK, FK (project group meeting, 16 Nov 2026; follow-up answers 18 and 19 Nov 2026).

PRD changes that follow from these decisions are logged in `docs/prd-changes.md`, to be
applied in the PRD revision.

New ADRs: copy the shape of an existing one and take the next number. The follow-up answers
of 18 and 19 Nov were recorded as dated amendments, because the ADRs had not yet been merged.
Once merged, an accepted ADR is not rewritten: supersede it with a new ADR and update the
old one's status line. Confirming a *provisional* or *proposed* item may be recorded as a
dated status change.
