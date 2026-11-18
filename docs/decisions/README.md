# Architecture / product decision records (ADRs)

One short record per decision: context, decision, consequences, status. ADRs record what
the group decided; they do **not** change `docs/prd.md`. Where an ADR and the PRD disagree,
the disagreement is listed in the ADR and in `docs/data-model.md` §4 until the PRD revision
resolves it.

| # | Decision | Status | Decided |
|---|---|---|---|
| [0001](0001-clinical-verification.md) | Per-item clinical verification, configurable cadre rules | Accepted (amended 18 Nov: `unverified` + `source`); cadre rules await clinical-lead sign-off | 2026-11-16 |
| [0002](0002-scd-core-dataset.md) | SCD core dataset (agreed list) | Accepted; element list awaits clinical-lead sign-off | 2026-11-16, list 2026-11-18 |
| [0003](0003-patient-identifiers-and-matching.md) | Patient identifiers and matching rules (sex required, gender optional) | Accepted | 2026-11-16 |
| [0004](0004-emergency-access.md) | Emergency summary, break-glass, card/QR, unconscious patients | Accepted, except 4c (one member to confirm) | 2026-11-16 |
| [0005](0005-consent-and-access-logging.md) | Consent to a care team, and access logging | Accepted (amended 18 Nov); no per-visit OTP is proposed, pending confirmation | 2026-11-16 |
| [0006](0006-minors-and-guardians.md) | Minors and guardians | Accepted (data model); pilot enrolment of children pending | 2026-11-16 |
| [0007](0007-multi-facility.md) | Multi-facility design from the start | Accepted | 2026-11-16 |

**Deciders:** JK, FK (project group meeting, 16 Nov 2026; follow-up answers 18 Nov 2026).

PRD changes that follow from these decisions are logged in `docs/prd-changes.md`, to be
applied in the PRD revision.

New ADRs: copy the shape of an existing one, take the next number, and never rewrite an
accepted ADR; supersede it with a new one and update the status line of the old one.
