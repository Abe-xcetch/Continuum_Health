# ADR 0002: SCD core dataset

- **Status:** Accepted by the group (16 Nov), with the agreed list recorded on 18 Nov. The
  element list and its details from 19 Nov are **provisional, awaiting clinical-lead
  sign-off**.
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q5, Q6

## Context

The PRD names seven categories of SCD baseline information (§8.3, §14.5), with no fields,
types, value sets or required/optional rules. §15.4 measures the percentage of records
containing "the core SCD information defined for the pilot".

## Decision

**Required elements accept an explicit "none" or "unknown".** A required element is
complete when it holds a value, "none" or "unknown". Staff should never have to invent a
value to get past a form.

### Element list: *provisional, awaiting clinical-lead sign-off* (19 Nov)

**Required**
- SCD confirmed (yes / no)
- Genotype: HbSS, HbSC, HbSβ⁰, HbSβ⁺, other, unknown ⚑1
- Blood group and Rh
- Baseline haemoglobin
- Transfusion history: number ⚑2, date of last transfusion, reactions or antibodies
- Hydroxyurea: yes / no; if yes, dose **in mg/day** and start date
- Folic acid
- Allergies
- Hospitalisations in the last 12 months, counting **any ward admission**
- Pain management that usually works / things to avoid
- Usual facility and clinician
- Emergency contact

**Optional**
- Genotype test method, date and facility. Methods:
  - Hb electrophoresis
  - HPLC
  - isoelectric focusing
  - point-of-care rapid test
  - DNA / genetic
  - newborn screening
  - sickling / solubility screen
  - other
- Penicillin prophylaxis (yes / no)
- Other medicines (none, or a list)
- Complications: a fixed list (stroke, acute chest syndrome, splenic sequestration,
  avascular necrosis), plus none and other

**Flags for the clinical lead**
- ⚑1 The team said genotype is *Optional*; JK keeps it *Required*, with "unknown" allowed.
- ⚑2 The meaning of "number" of transfusions is unclear: lifetime episodes, units, or the
  last 12 months?
- A sickling/solubility screen cannot establish the genotype. Should it count as
  supporting evidence for verifying one? (data-model Q-D5)

### Hospitalisation history (Q-D6): *proposed, pending group confirmation* (19 Nov)

- At enrolment, record the **number of hospitalisations in the last 12 months**.
- From then on, record **every new admission**: admission date, discharge date, facility
  and reason.
- **Treatment history and treatment responses** (PRD §8.3) are **deferred to phase 2**.

## Consequences

- **Design:** elements are reference data (`DatasetElement`), with typed value columns
  `code`, `decimal`, `integer` (counts, added 19 Nov), `date` and `boolean`. A `CHECK`
  requires exactly one value or a null reason, there is one current row per patient and
  element, and a pivoted reporting view supports reporting (`docs/data-model.md` §3.6).
- **Conditional elements:** the hydroxyurea dose and start date are required only when
  hydroxyurea is "yes"; the date of last transfusion only when the number is above 0.
- **Structured elements** are linked models:
  - allergies, complications, other medicines
  - genotype test, transfusion reactions/antibodies
  - usual care, emergency contact
  - pain management (in the emergency care plan)
- **Admissions:** a new `Admission` model, pending confirmation of Q-D6.
- **§15.4 completeness** is computed from the reporting view.
- **PRD change:** replace the §8.3 / §14.5 categories (PC-12); record admissions going
  forward, and defer treatment history and responses (PC-14, proposed). Blood group moves
  from TBC (§7.6) to Required.
