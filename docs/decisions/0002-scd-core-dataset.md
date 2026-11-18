# ADR 0002: SCD core dataset

- **Status:** Accepted by the group. The element list awaits **clinical-lead sign-off**.
- **Date:** 2026-11-16; agreed element list recorded 2026-11-18 · **Deciders:** JK, FK
- **Resolves:** prd-review §f Q5, Q6 (blood group)

## Context

The PRD names seven categories of SCD baseline information (§8.3, §14.5), with no fields,
types, value sets or required/optional rules. §15.4 measures the percentage of records
containing "the core SCD information defined for the pilot", so a defined dataset is
needed. prd-review §c proposed SCD-specific items for the clinical lead to consider.

## Decision

The SCD core dataset is the following agreed list.

**Required**
- SCD confirmed (yes / no)
- Genotype: HbSS, HbSC, HbSβ⁰, HbSβ⁺, other, unknown
- Blood group and Rh
- Baseline haemoglobin
- Hydroxyurea: yes / no, dose, start date
- Folic acid
- Allergies
- Hospitalisations in the last 12 months
- Usual facility and clinician
- Emergency contact

**Optional**
- Genotype test method, date and facility
- Transfusion history: count, last date, reactions or antibodies
- Penicillin prophylaxis
- Other current medicines
- Major complications, from a fixed list: stroke, acute chest syndrome, splenic
  sequestration, avascular necrosis, others
- Pain management that usually works, and things to avoid

**Required elements must accept an explicit "none" or "unknown"** value. A required
element is complete when it holds a value, "none" or "unknown"; it is incomplete only when
nothing has been recorded. Staff should never have to invent a value to get past a form.

## Consequences

- **Reference data:** elements are held as data (`DatasetElement`), each with a data type,
  so the clinical lead's changes become a reviewed data migration, not a schema change
  (`docs/data-model.md` §3.6). The modelling guard rails were accepted on 18 Nov 2026: typed
  value columns, a CHECK for exactly one value or a null reason, one current row per
  patient and element, and a pivoted reporting view.
- **Hydroxyurea dose and start date** are *conditionally* required, only when hydroxyurea =
  yes.
- **"Unknown" genotype** is stored as the shared null reason `unknown`, not as a genotype
  code.
- **Structured elements** are linked records rather than single values: allergies,
  complications, other medicines, genotype test details, transfusion reactions or
  antibodies, usual facility and clinician, emergency contacts, pain management. Pain
  management lives in the emergency care plan.
- **§15.4 completeness** is computed exactly from the reporting view.
- **Each element is verifiable on its own** (ADR 0001), except usual facility/clinician and
  emergency contact (to confirm, data-model Q-V5).
- **PRD change:** PRD §8.3 / §14.5 items not in the list (hospitalisation details,
  treatment history, treatment responses) must be dropped or deferred in the revision
  (data-model D17, Q-D6). Blood group moves from "TBC" (§7.6) to Required.
- **Open for sign-off** (data-model §5):
  - hydroxyurea dose unit
  - the definition of a hospitalisation
  - which elements appear in the emergency summary
  - the genotype test-method list
