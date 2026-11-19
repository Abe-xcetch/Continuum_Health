# Continuum Health: data model plan (draft for approval)

- **Status:** PLAN ONLY. No models or migrations exist yet. Each model still goes through
  plan → tests → implementation under `continuum-dev-workflow` (CLAUDE.md §5).
- **Updated:** 2026-11-19
- **Based on:** `docs/prd.md` (v0, unrevised), `docs/prd-review.md`, ADRs 0001–0007 in
  `docs/decisions/`, and the group's answers of 16, 18 and 19 Nov 2026.
- **Status labels used below:**
  - **Decided:** the group agreed it.
  - **Provisional:** a clinical answer from the team, *awaiting clinical-lead sign-off*.
  - **Proposed:** pending group confirmation.
- **Where the PRD and an ADR disagree,** the model follows the ADR (§4). Decided PRD changes
  are in `docs/prd-changes.md`. Open questions are in §5.

All examples use synthetic data. Nothing here changes `docs/prd.md`.

---

## 1. Conventions

### 1.1 Apps (one per domain)

| App | Models |
|---|---|
| `apps/facilities` | Facility, CareTeam |
| `apps/staff` | Cadre, StaffProfile, FacilityMembership, CareTeamMembership, VerificationPermission |
| `apps/patients` | Patient, PatientIdentifier, EmergencyContact, GuardianRelationship |
| `apps/clinical` | CodeSystem, Code, DatasetElement, CoreDatasetItem, Allergy, PatientComplication, Medication, GenotypeTest, TransfusionAlert, Admission, UsualCareProvider, EmergencyCarePlan, VerificationEvent; reporting view `clinical_scd_dataset_wide` |
| `apps/access` | Consent, VisitAuthorisation, OtpChallenge, BreakGlassAccess, AccessSession, AccessEvent, SearchEvent |
| `apps/notifications` | SmsMessage |

`apps/accounts.User` stays as it is: staff log in with email. Patients and guardians have
**no login yet** (`docs/decisions-pending.md`). Patient-side accounts will link to
`Patient` / `GuardianRelationship` later through a nullable FK, and none of these models
depends on them.

### 1.2 Base classes and what each model uses

Base classes:
- `ContinuumModel` (exists), which combines:
  - **P** = `PublicIdModel`: UUID `public_id`, used in URLs and APIs
  - **T** = `TimeStampedModel`: `created_at`, `updated_at`
  - **A** = `AuditedModel`: `created_by`, `updated_by` (who typed the entry)
  - **S** = `SoftDeleteModel`: `deleted_at`, `deleted_by`, `objects` (live rows only) and
    `all_objects`

New, proposed:
- **V** = `VerifiableMixin` (abstract, `apps/clinical`): per-item verification fields
  (§3.7).
- **C** = `ClinicalItem` (abstract) = ContinuumModel + V + provenance (`source`,
  `source_facility`, supersession) (§3.7).
- **L** = `AppendOnlyModel` (abstract, `apps/core`): P + `created_at` only. `save()` refuses
  updates and `delete()` raises an error. A **PostgreSQL trigger** blocks `UPDATE` and
  `DELETE` (PRD §13.1.8). The trigger is created by a migration and tested (M4, accepted).
- **G** = **guarded columns**: the row may be updated, but a trigger allows only a named set
  of columns to change after insert (e.g. review fields on `BreakGlassAccess`). It shares
  the trigger helper with L.

### 1.3 Rules applied everywhere

- **`on_delete`:**
  - `PROTECT` for every FK to patients, clinical items, staff, users and facilities.
  - **No `CASCADE`** anywhere.
- **Integer primary keys stay internal;** URLs use `public_id`.
- **Nothing identifying goes into application logs or `SearchEvent`:** no identifier
  value, name, phone number, OTP code or clinical value.
- **No medical information is ever sent by SMS** (ADR 0004). SMS bodies are fixed, reviewed
  templates, and message bodies are never stored (§3.14).
- **Coded values** use `TextChoices` when the list is fixed by the software, and the `Code`
  reference table when clinicians maintain the list.
- **Measured values** use `DecimalField`; **counts** use integers.
- **Live-row uniqueness** uses partial `UniqueConstraint(..., condition=Q(deleted_at=None))`.
- **Clinical values are never overwritten** (PRD §7.8; M3, accepted). A change creates a new
  row that `supersedes` the old one.
- **Rules a `CHECK` can't express** (they need a lookup in another table) are enforced with
  PostgreSQL triggers created in migrations and covered by tests (M4).

---

## 2. Entity-relationship diagram

```mermaid
erDiagram
    User ||--o| StaffProfile : "has (staff only)"
    Cadre ||--o{ StaffProfile : classifies
    Cadre ||--o{ VerificationPermission : "may verify"
    StaffProfile ||--o{ FacilityMembership : "works at"
    Facility ||--o{ FacilityMembership : employs
    Facility ||--o{ CareTeam : contains
    FacilityMembership ||--o{ CareTeamMembership : "belongs to"
    CareTeam ||--o{ CareTeamMembership : has

    Patient ||--o{ PatientIdentifier : "identified by"
    Facility ||--o{ PatientIdentifier : "issues (hospital no.)"
    Patient ||--o{ EmergencyContact : has
    Patient ||--o{ GuardianRelationship : "minor in"

    DatasetElement ||--o{ CoreDatasetItem : defines
    CodeSystem ||--o{ DatasetElement : "value set"
    CodeSystem ||--o{ Code : lists
    Code ||--o{ CoreDatasetItem : "coded value"
    Patient ||--o{ CoreDatasetItem : has
    Patient ||--o{ Allergy : has
    Patient ||--o{ PatientComplication : has
    Patient ||--o{ Medication : takes
    Patient ||--o{ GenotypeTest : had
    Patient ||--o{ TransfusionAlert : has
    Patient ||--o{ Admission : "admitted (from enrolment)"
    Patient ||--o{ UsualCareProvider : "usually seen by"
    Patient ||--o{ EmergencyCarePlan : has
    VerificationEvent }o--|| User : by

    Patient ||--o{ Consent : gives
    CareTeam ||--o{ Consent : "made eligible"
    CareTeam ||--o{ VisitAuthorisation : "authorised for visit"
    Patient ||--o{ VisitAuthorisation : "authorises"
    OtpChallenge |o--o| VisitAuthorisation : "confirms"
    OtpChallenge |o--o| Consent : "confirms grant"
    Patient ||--o{ OtpChallenge : "receives"
    Patient ||--o{ BreakGlassAccess : "subject of"
    StaffProfile ||--o{ BreakGlassAccess : invokes
    Patient ||--o{ AccessSession : "opened in"
    User ||--o{ AccessSession : opens
    VisitAuthorisation |o--o{ AccessSession : basis
    BreakGlassAccess |o--o{ AccessSession : basis
    AccessSession ||--o{ AccessEvent : records
    User ||--o{ SearchEvent : searches
    Patient ||--o{ SmsMessage : "sent to"

    Patient {
        uuid public_id UK
        string continuum_id UK
        date date_of_birth
        string sex "required; no gender field"
        string account_status
    }
    CoreDatasetItem {
        fk value_code
        decimal value_decimal
        int value_integer
        date value_date
        bool value_boolean
        string null_reason "none|unknown"
        bool is_current
    }
    VisitAuthorisation {
        string method "otp|fallback"
        datetime started_at
        datetime expires_at "max 12h (proposed)"
        datetime ended_at
    }
    BreakGlassAccess {
        string reason_code
        datetime started_at
        datetime expires_at "max 12h"
        datetime reviewed_at
    }
    AccessSession {
        string basis
        datetime opened_at
        datetime last_activity_at
        datetime closed_at
    }
```

The clinical item models (`CoreDatasetItem`, `Allergy`, `PatientComplication`, `Medication`,
`GenotypeTest`, `TransfusionAlert`, `Admission`, `EmergencyCarePlan`) all carry the
`ClinicalItem` fields (§3.7). They are omitted from the diagram for space.

---

## 3. Models

### 3.1 Facility (`apps/facilities`)

**Purpose:** a healthcare facility. Participating facilities are `active`.
**Implements:** PRD §7.2, §11.3, §12.4.1; ADR 0007. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `facility_code` | `CharField(12)`, unique | Continuum Facility ID, generated, immutable; format TBC (PRD §7.2) |
| `name` | `CharField(200)` | |
| `kmhfl_code` | `CharField(20)`, null, unique | Kenya Master Health Facility List code |
| `county` | `TextChoices` | The 47 counties |
| `status` | `TextChoices` | `onboarding`, `active`, `suspended`, `withdrawn` |
| `registered_at` | `DateTimeField`, null | Set when status first becomes `active` |

- **Constraints:** `registered_at` is set when the status is `active`.
- **Indexes:** `status`.

### 3.2 CareTeam (`apps/facilities`)

**Purpose:** a named team within a facility (e.g. "SCD Clinic", "Emergency Department").
Consent makes a care team **eligible** (ADR 0005).
**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `facility` | FK Facility, `PROTECT` | |
| `name` | `CharField(100)` | |
| `kind` | `TextChoices` | `scd_clinic`, `emergency`, `inpatient`, `laboratory`, `outpatient`, `other` |
| `is_active` | `BooleanField` | |

- **Constraints:** unique `(facility, name)` among live rows.

### 3.3 Staff: Cadre, StaffProfile, FacilityMembership, CareTeamMembership, VerificationPermission (`apps/staff`)

#### Cadre

**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `code` | `SlugField`, unique | |
| `name` | `CharField(100)` | |
| `regulator` | `TextChoices` | `KMPDC`, `COC`, `NCK`, `KMLTTB`, `PPB`, `none` |
| `may_break_glass` | `BooleanField` | ADR 0004 4b |

**Seed** (*provisional, awaiting clinical-lead sign-off*):

| `code` | Name | Regulator | `may_break_glass` |
|---|---|---|---|
| `medical_officer` | Medical officer | KMPDC | **yes** |
| `clinical_officer` | Clinical officer | COC | **yes** |
| `nurse` | Nurse | NCK | no |
| `lab_technologist` | Laboratory technologist | KMLTTB | no |
| `pharmacist` | Pharmacist | PPB | no |

The team's answers do not mention consultants or specialists (Q-V6).

#### StaffProfile

**Implements:** PRD §7.2, §11.2, §11.2.1. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `user` | OneToOne `accounts.User`, `PROTECT` | |
| `professional_id` | `CharField(12)`, unique | Continuum Professional ID, generated, immutable |
| `full_name` | `CharField(200)` | |
| `work_phone` | `CharField(16)`, blank | Shown as the "usual clinician" contact |
| `cadre` | FK Cadre, `PROTECT` | |
| `registration_number` | `CharField(50)`, blank | |
| `registration_expires_on` | `DateField`, null | PRD §11.2.1 |
| `registration_verified_at` / `_by` | `DateTimeField` / FK User, `PROTECT`, null | |
| `status` | `TextChoices` | `pending`, `active`, `suspended`, `deactivated` |

#### FacilityMembership

**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `staff` | FK StaffProfile, `PROTECT` | |
| `facility` | FK Facility, `PROTECT` | |
| `role` | `TextChoices` | `clinical`, `facility_admin` (no clinical access, PRD §12.3) |
| `starts_on` / `ends_on` | `DateField` / `DateField`, null | Ended, never deleted |
| `verified_by` / `verified_at` | FK User, `PROTECT` / `DateTimeField` | |

- **Constraints:** one open membership per `(staff, facility, role)`; `ends_on >= starts_on`.

#### CareTeamMembership

**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `membership` | FK FacilityMembership, `PROTECT` | |
| `care_team` | FK CareTeam, `PROTECT` | Same facility (trigger) |
| `starts_on` / `ends_on` | dates | |

#### VerificationPermission

**Implements:** ADR 0001. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `cadre` | FK Cadre, `PROTECT` | |
| `category` | `TextChoices` `ItemCategory` | `clinical`, `lab_value`, `allergy`, `complication`, `medication`, `transfusion`, `admission`, `care_plan` |
| `is_enabled` | `BooleanField` | Lets a rule be switched off for the pilot without deleting it |
| `approved_by` / `approved_on` | FK User / date | |

- **Constraints:** unique `(cadre, category)` among live rows.

**Seed** (*provisional, awaiting clinical-lead sign-off*). These are written as a data
migration; in production they are enabled only after sign-off.

| Cadre | Categories |
|---|---|
| Medical officer | all |
| Clinical officer | all |
| Lab technologist | `lab_value` (blood group and Rh, baseline Hb, other lab values), **`is_enabled` may be off in the pilot** |
| Nurse | `allergy` only |
| Pharmacist | none |

Which category each element or model belongs to is in §3.6 and §3.8.

### 3.4 Patient, PatientIdentifier, EmergencyContact (`apps/patients`)

#### Patient

**Implements:** PRD §7.1, §7.2, §11.1, §11.1.3; ADR 0003, 0006, 0007. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `continuum_id` | `CharField(12)`, unique | Generated, immutable, never reassigned. `CH-XXXXXX` with no O/0 or I/1 and a check character (proposal). Sent to the patient by SMS at enrolment (§3.14) |
| `given_name`, `middle_names`, `family_name` | `CharField` | |
| `date_of_birth` | `DateField` | Age is computed |
| `dob_is_estimated` | `BooleanField` | |
| `sex` | `TextChoices`, **required** | `female`, `male`, `intersex`. Used for matching and clinical care. **There is no gender field (decided 19 Nov; PC-5)** |
| `place_of_birth` | `CharField`, blank | |
| `county_of_residence`, `residence_detail` | `TextChoices` / `CharField`, blank | |
| `citizenship` | `CharField(2)`, blank | ISO 3166 |
| `preferred_language` | `TextChoices` | `en`, `sw`, `other` |
| `account_status` | `TextChoices` | `pending_identity`, `identity_verified`, `suspended`, `deactivated` |
| `identity_verified_at` / `_by` | `DateTimeField` / FK User, `PROTECT`, null | |
| `is_deceased`, `date_of_death` | `BooleanField`, `DateField` null | |
| `adult_transition_at` | `DateTimeField`, null | ADR 0006 |

- **Constraints:**
  - `identity_verified_at` is set when `account_status = identity_verified`.
  - `date_of_death` is null unless `is_deceased`.
  - `sex` is never blank.
- **Indexes:** `(family_name, date_of_birth)`; `pg_trgm` GIN indexes on `given_name` and
  `family_name` (M5, accepted). The extension is created by Django's `TrigramExtension()`
  migration operation (Q-T1).

#### PatientIdentifier

**Implements:** ADR 0003; PRD §7.1, §10.4, §12.2. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `id_type` | `TextChoices` | `client_registry`, `national_id`, `birth_certificate`, `sha_number`, `phone`, `continuum_id`, `facility_mrn` |
| `value` | `CharField(64)` | Normalised (phone in E.164; IDs uppercased, separators removed) |
| `issuing_facility` | FK Facility, `PROTECT`, null | `facility_mrn` only |
| `verification_method` | `TextChoices` | `unverified`, `self_declared`, `document_sighted`, `document_uploaded`, `otp_confirmed`, `registry_lookup` (future) |
| `verified_at` / `verified_by` | `DateTimeField` / FK User, `PROTECT`, null | |
| `is_primary` | `BooleanField` | The primary phone receives OTPs and SMS |

- **Strong types:** all except `phone` (Q-I1).
- **Constraints:**
  - Unique `(id_type, value)` among live rows for strong types except `facility_mrn`.
  - Unique `(issuing_facility, value)` for `facility_mrn`.
  - `issuing_facility` is set if and only if the type is `facility_mrn`.
  - `verified_at` is set for document, OTP and registry methods.
  - One live `is_primary` per `(patient, id_type)`.
- **Indexes:** `(id_type, value)`.
- **Matching** (ADR 0003):
  - **confirmed:** a strong identifier agrees, plus the name or DOB agrees.
  - **probable:** names + DOB + **sex** agree, with no strong identifier; shown with a
    warning.

#### EmergencyContact

**Uses:** P T A S. Required by the dataset (§3.6). Not searchable. Not verified (Q-V5).

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `name`, `relationship` | `CharField` | |
| `phone` | `CharField(16)` | E.164 |
| `priority` | `PositiveSmallIntegerField` | |

### 3.5 GuardianRelationship (`apps/patients`)

**Implements:** ADR 0006 (the pilot enrols adults **and children**, *provisional*); PRD
§8.8.1.4, §10.1. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | The minor |
| `guardian_name` | `CharField(200)` | |
| `guardian_phone` | `CharField(16)` | Receives OTPs and SMS for a minor (Q-G3) |
| `guardian_id_type` / `guardian_id_value` | `TextChoices` / `CharField`, blank | |
| `relationship` | `TextChoices` | `mother`, `father`, `legal_guardian`, `other_relative`, `other` |
| `legal_basis` | `TextChoices` | `parent`, `court_order`, `other_documented` |
| `verified_by` / `verified_at` | FK User / `DateTimeField`, null | |
| `starts_on` / `ends_on` | `DateField` / `DateField`, null | |
| `end_reason` | `TextChoices`, blank | `patient_reached_majority`, `revoked`, `guardian_changed`, `deceased` |

- **Constraints:** `end_reason` is set if and only if `ends_on` is set; `ends_on >= starts_on`.
- **Transition:** a service ends open relationships at 18 and sets
  `Patient.adult_transition_at`. A daily task lists patients turning 18 within 90 days.

### 3.6 SCD core dataset (`apps/clinical`)

**Implements:** ADR 0002, ADR 0001; PRD §8.3, §14.5, §15.4. **Design (M2, accepted)** with
these guard rails:
1. **Typed value columns:** `code`, `decimal`, `integer` (counts), `date`, `boolean`. The
   `integer` column was added 19 Nov for counts.
2. An **element-definition table** (`DatasetElement`) holding each element's data type.
3. A **`CHECK`**: exactly one value column **or** a null reason is set.
4. A **partial unique index**: one current row per patient + element.
5. A **PostgreSQL view**: one row per patient, for reporting.

Elements with structure are `linked`: their entries live in a dedicated model, and the
`CoreDatasetItem` row only records `none` / `unknown` when there are no entries.

#### CodeSystem and Code

**Uses:** P T A S.

| Model | Fields |
|---|---|
| `CodeSystem` | `key` (`SlugField`, unique), `name` |
| `Code` | `system` FK `PROTECT`, `code` (`SlugField`), `label`, `sort_order`, `is_active`, `external_ref` (blank) |

- **Constraints:** unique `(system, code)`. Codes are retired with `is_active=False` and
  never deleted.

**Seeded code systems** (*provisional, awaiting clinical-lead sign-off*):

| `CodeSystem.key` | Codes |
|---|---|
| `scd_genotype` | `hbss` HbSS · `hbsc` HbSC · `hbs_beta0` HbSβ⁰ · `hbs_beta_plus` HbSβ⁺ · `other` |
| `blood_group` | `a_pos` `a_neg` `b_pos` `b_neg` `ab_pos` `ab_neg` `o_pos` `o_neg` |
| `genotype_test_method` | `hb_electrophoresis` Hb electrophoresis · `hplc` HPLC · `isoelectric_focusing` Isoelectric focusing · `point_of_care` Point-of-care rapid test · `dna_genetic` DNA / genetic · `newborn_screening` Newborn screening · `sickling_solubility` Sickling / solubility screen · `other` |
| `complication` | `stroke` · `acute_chest_syndrome` · `splenic_sequestration` · `avascular_necrosis` · `other` (with a description) |
| `admission_reason` | *Proposed (Q-D6):* `vaso_occlusive_crisis` · `acute_chest_syndrome` · `fever_infection` · `severe_anaemia` · `stroke` · `splenic_sequestration` · `priapism` · `other` |

"Unknown" (genotype, blood group, …) is always `null_reason = unknown`, never a code.
"None" for complications or other medicines is `null_reason = none`.

#### DatasetElement

**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `key` | `SlugField`, unique | |
| `label` | `CharField` | |
| `data_type` | `TextChoices` | `code`, `decimal`, `integer`, `date`, `boolean`, `linked` |
| `linked_model` | `CharField`, blank | e.g. `clinical.Allergy` |
| `code_system` | FK CodeSystem, `PROTECT`, null | |
| `unit` | `CharField(20)`, blank | e.g. `g/dL`, `mg/day` |
| `min_value` / `max_value` | `DecimalField`, null | For `decimal` and `integer` |
| `requirement` | `TextChoices` | `required`, `optional`, `conditional` |
| `required_if_element` | FK self, `PROTECT`, null | For `conditional` |
| `required_if_rule` | `TextChoices`, blank | `is_true`, `greater_than_zero` |
| `verification_category` | `TextChoices` `ItemCategory`, null | Which `VerificationPermission` category applies; null = not verified |
| `in_emergency_summary` | `BooleanField` | |
| `sort_order` | `PositiveSmallIntegerField` | |
| `is_active` | `BooleanField` | |

- **Constraints:**
  - `code_system` is set if and only if the type is `code`.
  - `linked_model` is set if and only if the type is `linked`.
  - Both `required_if_*` fields are set if and only if the requirement is `conditional`.
  - The min/max values are set only for numeric types.

**Element list.** *Provisional, awaiting clinical-lead sign-off* (team answers of 19 Nov).
Every element accepts `none` or `unknown`.

*Required:*

| Key | Label | Type | Req | Verify category | Summary |
|---|---|---|---|---|---|
| `scd_confirmed` | SCD confirmed | boolean | required | clinical | ✓ |
| `scd_genotype` | Genotype | code | required ⚑1 | clinical ⚑5 | ✓ |
| `blood_group` | Blood group and Rh | code | required | lab_value | ✓ |
| `baseline_hb` | Baseline haemoglobin (g/dL, 2.0–20.0; `observed_on` = date) | decimal | required | lab_value | — |
| `transfusion_count` | Number of transfusions ⚑2 | integer (0–999) | required | transfusion | — |
| `last_transfusion` | Date of last transfusion | date | conditional (`transfusion_count` > 0) | transfusion | — |
| `transfusion_alerts` | Transfusion reactions or antibodies | linked → `TransfusionAlert` | required | transfusion | ✓ |
| `hydroxyurea` | On hydroxyurea | boolean | required | medication | ✓ |
| `hydroxyurea_dose` | Hydroxyurea dose (**mg/day**) | integer (0–4000) | conditional (`hydroxyurea` true) | medication | ✓ |
| `hydroxyurea_start` | Hydroxyurea start date | date | conditional (`hydroxyurea` true) | medication | — |
| `folic_acid` | On folic acid | boolean | required | medication | ✓ ⚑3 |
| `allergies` | Allergies | linked → `Allergy` | required | allergy | ✓ |
| `hospitalisations_12m` | Hospitalisations in the last 12 months (**any ward admission**), stated at enrolment | integer (0–99) | required | clinical | — |
| `pain_management` | Pain management that usually works / things to avoid | linked → `EmergencyCarePlan` | required | care_plan | ✓ |
| `usual_care` | Usual facility and clinician | linked → `UsualCareProvider` | required | (not verified) | ✓ (facility) |
| `emergency_contact` | Emergency contact | linked → `EmergencyContact` | required | (not verified) | ✓ |

*Optional:*

| Key | Label | Type | Req | Verify category | Summary |
|---|---|---|---|---|---|
| `genotype_test` | Test method, date and facility | linked → `GenotypeTest` | optional | lab_value | — |
| `penicillin_prophylaxis` | Penicillin prophylaxis | boolean | optional | medication | ✓ ⚑3 |
| `other_medicines` | Other medicines (none or list) | linked → `Medication` | optional | medication | ✓ |
| `complications` | Complications (fixed list + none + other) | linked → `PatientComplication` | optional | complication | — ⚑4 |

Flags for the clinical lead:
- **⚑1** The team said genotype is *Optional*; it is kept *Required* (with `unknown`
  allowed), on JK's instruction.
- **⚑2** The meaning of "number of transfusions" is unclear: lifetime episodes, units, or
  the last 12 months?
- **⚑3** The emergency summary lists "current medicines incl. hydroxyurea". Folic acid and
  penicillin prophylaxis are read as current medicines and shown when "yes".
- **⚑4** Complications and baseline Hb are **not** in the provisional summary list.
  Intended?
- **⚑5** Is genotype a lab value, so that a lab technologist may confirm it, or clinical?
  Also, a **sickling/solubility screen cannot establish the genotype** (it doesn't
  separate HbAS from HbSS). Should a genotype supported only by that method be blocked from
  verification?

**Completeness (§15.4):** applicable elements are the required ones, plus conditional ones
whose condition holds. An element counts as complete when it has a current value, a current
linked entry, or a `null_reason`. Completeness is computed from the reporting view.

#### CoreDatasetItem

**Uses:** C.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `element` | FK DatasetElement, `PROTECT` | |
| `value_code` | FK Code, `PROTECT`, null | |
| `value_decimal` | `DecimalField(7,2)`, null | |
| `value_integer` | `IntegerField`, null | Counts and doses (added 19 Nov) |
| `value_date` | `DateField`, null | |
| `value_boolean` | `BooleanField`, null | |
| `null_reason` | `TextChoices`, blank | `none`, `unknown` |
| `observed_on` | `DateField`, null | Metadata, not a value column |

Constraints:
1. **`CHECK` exactly one:**
   `num_nonnulls(value_code_id, value_decimal, value_integer, value_date, value_boolean) + (null_reason <> '')::int = 1`.
2. **Partial unique index:** `(patient, element)` where `is_current AND deleted_at IS NULL`.
3. **Trigger `clinical_dataset_item_type_check`:**
   - The value column must match `element.data_type`.
   - A code must come from the element's code system.
   - A numeric value must be within min/max.
   - A `linked` element accepts only a `null_reason`.

   Tested.

**Indexes:** `(patient, is_current)`, `(element, is_current)`.

#### Reporting view `clinical_scd_dataset_wide`

- **Shape:** one row per live patient, keyed by `public_id` only (no names, identifiers or
  contacts).
- **Columns:** per scalar element, `<key>`, `<key>_status` (`value` / `none` / `unknown` /
  `missing`) and `<key>_verification`; per linked element, `<key>_count` and
  `<key>_status`.
- **Generated SQL:** the view's SQL is generated from the active elements by
  `apps/clinical/reporting.py` and created by `RunSQL`. Any data migration that changes
  elements recreates it, and a test asserts that the columns match the active elements.
- **Who reads it:** reporting only (Q-R1); the clinical UI never uses it.

### 3.7 Verification: VerifiableMixin, ClinicalItem, VerificationEvent (`apps/clinical`)

**Implements:** ADR 0001; PRD §7.4, §7.8, §7.10, §11.5.1, §13.1.3.

#### `VerifiableMixin`

| Field | Type | Notes |
|---|---|---|
| `verification_status` | `TextChoices` | `unverified`, `clinician_verified`, `disputed`, `retracted` |
| `verified_by` / `verified_at` / `verified_at_facility` | FK User `PROTECT` / `DateTimeField` / FK Facility `PROTECT`, all null | Set when `clinician_verified` (`CHECK`) |

#### `ClinicalItem` = ContinuumModel + VerifiableMixin + provenance

| Field | Type | Notes |
|---|---|---|
| `source` | `TextChoices`, required | `patient`, `clinician`, `import`. A guardian's entry is `patient` |
| `source_facility` | FK Facility, `PROTECT`, null | Required when the source is `clinician` |
| `recorded_by_cadre` | FK Cadre, `PROTECT`, null | |
| `is_current` | `BooleanField` | |
| `supersedes` | OneToOne self, `PROTECT`, null | M3 |

Each concrete model declares its `ItemCategory`; for `CoreDatasetItem` it comes from the
element.

#### VerificationEvent

**Uses:** L.

| Field | Type | Notes |
|---|---|---|
| `content_type` / `object_id` | FK ContentType `PROTECT` / `PositiveBigIntegerField` | |
| `patient` | FK Patient, `PROTECT` | |
| `from_status` / `to_status` | `TextChoices` | |
| `actor` / `actor_cadre` / `facility` | FK User / FK Cadre / FK Facility (null), `PROTECT` | |
| `reason` | `TextField`, blank | Required for `disputed` and `retracted` |

- **Service rule:** `clinician_verified` requires an **enabled** `VerificationPermission`
  for the actor's cadre and the item's category, and an active clinical membership at the
  acting facility.

### 3.8 Linked clinical entries (`apps/clinical`)

**Uses:** C (except `UsualCareProvider`).

| Model | Category | Fields (besides ClinicalItem) | Constraints |
|---|---|---|---|
| `Allergy` | allergy | `patient`; `substance`; `category` (`drug`, `food`, `environmental`, `other`); `reaction`; `severity` (`mild`, `moderate`, `severe`, `unknown`) | — |
| `PatientComplication` | complication | `patient`; `complication` FK Code; `description` (required for `other`); `onset_date` (null); `onset_precision` | Code system (trigger); partial unique `(patient, complication)` except `other` |
| `Medication` | medication | `patient`; `name`; `dose_text`; `frequency_text`; `route`; `started_on` / `stopped_on` | `stopped_on >= started_on`. "Other" medicines: hydroxyurea, folic acid and penicillin prophylaxis are elements and aren't repeated here |
| `GenotypeTest` | lab_value | `patient`; `method` FK Code; `tested_on` (null); `tested_on_precision`; `facility` FK Facility (null); `facility_name_text` | Never both `facility` and `facility_name_text` |
| `TransfusionAlert` | transfusion | `patient`; `kind` (`reaction`, `alloantibody`); `description`; `identified_on` (null) | — |
| `Admission` | admission | `patient`; `admitted_on`; `discharged_on` (null); `facility` FK Facility (null) or `facility_name_text`; `reason` FK Code (`admission_reason`); `reason_detail` | `discharged_on >= admitted_on`; exactly one of `facility` / `facility_name_text`. **Proposed (Q-D6)** |
| `UsualCareProvider` | — | `patient`; `facility` FK (null) or `facility_name_text`; `clinician` FK StaffProfile (null) or `clinician_name_text`; `clinician_phone` | One current per patient. **Uses P T A S + `source`, not verified** |

**Q-D6, proposed resolution:**
- `hospitalisations_12m` is the count **stated at enrolment**.
- From enrolment on, **every new admission is recorded** as an `Admission` row, with
  admission date, discharge date, facility and reason.
- **Treatment history and treatment responses (PRD §8.3) are deferred to phase 2.**

### 3.9 EmergencyCarePlan (`apps/clinical`)

**Purpose:** holds the required `pain_management` element and other acute-care guidance;
versioned.
**Category:** care_plan. **Uses:** C.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `pain_relief_that_works` | `TextField`, blank | In the emergency summary |
| `pain_relief_to_avoid` | `TextField`, blank | In the emergency summary |
| `fluids_oxygen_guidance` / `other_instructions` | `TextField`, blank | Not in the provisional summary list (Q-D7) |
| `review_due_on` | `DateField` | Overdue plans show as "outdated" (PRD §10.6) |
| `last_reviewed_at` / `_by` | `DateTimeField` / FK User, null | |

- **Constraints:** one current, live plan per patient; at least one pain field is
  non-empty.

**Emergency summary** (ADR 0004 4a). *Content provisional, awaiting clinical-lead
sign-off.* A selector, not a model, showing:
- SCD confirmed and genotype
- allergies
- blood group and Rh
- transfusion reactions or antibodies
- current medicines, including hydroxyurea (and its dose), folic acid and penicillin
  prophylaxis when "yes", plus other medicines
- pain management and things to avoid
- emergency contact
- usual facility

Each item shows its verification status and source. The selector has a fixed number of
queries, tested.

### 3.10 Consent (`apps/access`)

**Purpose:** standing consent that makes **a care team at a facility eligible** for access
in one category. **Consent alone opens nothing:** each visit also needs a
`VisitAuthorisation` (§3.11).
**Implements:** ADR 0005; PRD §10.8, §12.2.3, §12.4. **Uses:** P T A. **No S** (revoked,
never deleted).

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `grantee_team` | FK CareTeam, `PROTECT` | |
| `category` | `TextChoices` | `emergency_summary`, `full_scd_record`, `lab_results` |
| `granted_at` | `DateTimeField` | |
| `granted_by_guardian` | FK GuardianRelationship, `PROTECT`, null | |
| `capture_method` | `TextChoices` | `otp`, `signed_form` (no phone; Q-C4) |
| `otp_challenge` | OneToOne OtpChallenge, `PROTECT`, null | Set when the method is `otp` |
| `recorded_by` | FK User, `PROTECT` | |
| `review_due_on` | `DateField` | +1 year; a reminder only |
| `last_reviewed_at` | `DateTimeField`, null | |
| `revoked_at` / `revocation_note` | `DateTimeField`, null / `TextField` | |

- **Constraints:**
  - One active consent per `(patient, grantee_team, category)`.
  - `revoked_at >= granted_at`.
  - `otp_challenge` is set if and only if the method is `otp`.

### 3.11 VisitAuthorisation (`apps/access`)

**Purpose:** the patient's per-visit authorisation (ADR 0005, **decided 19 Nov: OTP at every
visit**). It opens a time-limited access window for an eligible care team.
**Implements:** ADR 0005; PRD §12.2.1, §12.4.2. **Uses:** P T, plus G (only the end and review
columns may change).

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `care_team` | FK CareTeam, `PROTECT` | Must hold an active consent at creation (service) |
| `requested_by` | FK StaffProfile, `PROTECT` | Member of `care_team` |
| `method` | `TextChoices` | `otp`, `fallback` |
| `otp_challenge` | OneToOne OtpChallenge, `PROTECT`, null | Required for `otp` |
| `fallback_reason_code` | `TextChoices`, blank | `no_phone`, `no_signal`, `guardian_holds_phone`, `patient_unable`, `other` (**proposed**) |
| `fallback_reason_text` | `TextField`, blank | Required for `fallback` |
| `started_at` / `expires_at` | `DateTimeField` | **Proposed:** until the visit ends, at most 12 h |
| `ended_at` / `end_reason` | `DateTimeField`, null / `TextChoices` | `visit_ended`, `expired`, `consent_revoked` |
| `reviewed_by` / `reviewed_at` / `review_outcome` / `review_notes` | as `BreakGlassAccess` | **Fallback only**, reviewed like break-glass (proposed) |

- **Constraints:**
  - `method = otp` ⇔ `otp_challenge` is set and the fallback fields are blank.
  - `method = fallback` ⇔ `fallback_reason_text` isn't empty and there's no
    `otp_challenge`.
  - `started_at < expires_at <= started_at + 12 h`.
  - The review fields are all set or all null, and are set only for `fallback`.
- **Indexes:** `(patient, care_team, expires_at)`, partial `(reviewed_at)` where the method
  is `fallback` (the review queue).
- **Access rule:** a user acts under consent only when **all** of these hold:
  - they are an active member of `care_team`
  - the team holds an active consent for the category being viewed
  - there's an unended, unexpired `VisitAuthorisation` for `(patient, care_team)`
- **Proposed:** the authorisation covers the whole care team for that visit, not only the
  requester (Q-C6).

### 3.12 OtpChallenge (`apps/access`)

**Purpose:** a one-time code sent to the patient (or a minor's guardian) to grant consent to
a new care team or to authorise a visit. Patient login will reuse it later.
**Uses:** P T, plus G (only `attempts` and `verified_at` change).

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `purpose` | `TextChoices` | `consent_grant`, `visit_access` (`patient_login` later) |
| `sent_to_identifier` | FK PatientIdentifier (phone), `PROTECT`, null | |
| `sent_to_guardian` | FK GuardianRelationship, `PROTECT`, null | For minors |
| `code_hash` | `CharField(64)` | HMAC-SHA256 of the code with a server secret; the code is never stored or logged |
| `expires_at` | `DateTimeField` | Short (e.g. 10 min; setting) |
| `attempts` | `PositiveSmallIntegerField` | Locked after a maximum (setting, e.g. 5) |
| `verified_at` | `DateTimeField`, null | |
| `requested_by` / `facility` | FK User / FK Facility, `PROTECT` | |

- **Constraints:**
  - Exactly one of `sent_to_identifier` / `sent_to_guardian` is set.
  - `expires_at > created_at`.
- **Rate limit:** requests per patient per hour are rate-limited (Q-S3).

### 3.13 BreakGlassAccess (`apps/access`)

**Purpose:** emergency override (ADR 0004 4b). The only cadres allowed are **medical
officers and clinical officers** (*provisional*), via `Cadre.may_break_glass`.
**Uses:** P T, plus G.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `invoked_by` | FK StaffProfile, `PROTECT` | `may_break_glass` cadre, with an active clinical membership at `facility` |
| `facility` | FK Facility, `PROTECT` | `active` |
| `reason_code` / `reason_text` | `TextChoices` / `TextField` (required) | |
| `scope` | `TextChoices` | `emergency_summary` |
| `started_at` / `expires_at` / `ended_at` | `DateTimeField` | `expires_at <= started_at + 12 h` |
| `patient_notified_at` / `notification` | `DateTimeField`, null / OneToOne SmsMessage, `PROTECT`, null | The SMS contains **no medical information** (§3.14) |
| `reviewed_by` / `reviewed_at` / `review_outcome` / `review_notes` | | |

- **Constraints:**
  - `started_at < expires_at <= started_at + 12 h`.
  - `reason_text` isn't empty.
  - The review fields are all set or all null.
- **Indexes:** `(patient, started_at)`, `(reviewed_at)`, `(facility, started_at)`.

### 3.14 SmsMessage (`apps/notifications`)

**Purpose:** a record of every SMS sent. **The SMS design is proposed, pending group
confirmation** (ADR 0004 4c).
**Uses:** P T, plus G (only status fields change).

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `purpose` | `TextChoices` | `enrolment_continuum_id`, `otp`, `break_glass_notice`, `fallback_access_notice`, `consent_review_reminder` |
| `template_key` | `CharField(50)` | One of the fixed templates in code |
| `sent_to_identifier` / `sent_to_guardian` | as `OtpChallenge` | |
| `provider` / `provider_message_id` | `CharField` | |
| `status` | `TextChoices` | `queued`, `sent`, `delivered`, `failed` |
| `sent_at` / `status_at` | `DateTimeField`, null | |
| `error_code` | `CharField`, blank | |

- **The message body is never stored.** It is rebuilt from `template_key` if needed.
  - OTP codes reach the provider only.
  - The Continuum ID is the only patient data in any template.
- **Templates** (proposed wording; **no medical information, ever**):
  - `enrolment_continuum_id`: "Your Continuum ID is CH-XXXXXX. Keep this message and show it
    when you visit a clinic."
  - `otp`: "Your Continuum code is NNNNNN. It expires in 10 minutes. Do not share it."
  - `break_glass_notice` / `fallback_access_notice`: "Your Continuum record was opened on
    DD/MM/YYYY. If you have questions, call 07XX XXX XXX."
- **Test:** every template is checked against a list of banned words (diagnosis, sickle,
  SCD, genotype, drug names, facility names), so a medical term can't slip into a template.
- **Sender ID and brand:** if Continuum is known as an SCD-only service, the sender name
  itself reveals the diagnosis (Q-S1).
- **Sending** goes through a Celery task (provider network call, retries); the request never
  waits on it.

### 3.15 AccessSession, AccessEvent, SearchEvent (`apps/access`)

**Implements:** ADR 0005; PRD §11.6, §12.4.2, §13.1.7–§13.1.9.

#### AccessSession

**Uses:** P, `created_at`, plus G (only `last_activity_at`, `closed_at` and `close_reason`
change).

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `user` / `staff_cadre` / `facility` | FK User / FK Cadre / FK Facility, `PROTECT` | Copied at open time |
| `basis` | `TextChoices` | `visit_authorisation`, `break_glass`, `self`, `guardian`, `administrative` |
| `visit_authorisation` / `break_glass` | FK, `PROTECT`, null | |
| `opened_at` / `last_activity_at` / `closed_at` | `DateTimeField` | |
| `close_reason` | `TextChoices`, blank | `user_ended`, `logout`, `idle_timeout`, `authorisation_expired`, `consent_revoked` |

- **Approximate duration** = `(closed_at or last_activity_at) − opened_at`.
- **Constraints:**
  - The basis requires its matching FK.
  - `closed_at >= opened_at`.
  - `close_reason` is set if and only if `closed_at` is set.

#### AccessEvent

**Uses:** L.

| Field | Type | Notes |
|---|---|---|
| `session` | FK AccessSession, `PROTECT` | |
| `action` | `TextChoices` | `view`, `create`, `update`, `verify`, `dispute`, `retract`, `export` |
| `section` | `TextChoices` | `emergency_summary`, `scd_dataset`, `allergies`, `complications`, `medications`, `transfusion`, `admissions`, `care_plan`, `usual_care`, `identifiers`, `consent` |
| `object_public_id` | `UUIDField`, null | |

#### SearchEvent

**Uses:** L.

| Field | Type | Notes |
|---|---|---|
| `user` / `facility` | FK, `PROTECT` | |
| `method` | `TextChoices` | `continuum_id`, `identifier`, `name_dob_sex` |
| `identifier_type` | `TextChoices`, blank | The type only, never the value |
| `result_count` | `PositiveSmallIntegerField` | |
| `selected_patient` | FK Patient, `PROTECT`, null | |
| `match_level` | `TextChoices`, blank | `confirmed`, `probable` |

---

## 4. Where the PRD and the ADRs still disagree

| # | Topic | PRD says | ADR / model says | State |
|---|---|---|---|---|
| D1 | Who verifies | Physician only (§8.2.1, §10.6, §11.1.2, §11.5.1, §12.2.5, §13.1.3) | Configurable; defaults MO/CO all, lab tech lab values, nurse allergies | Decided (mechanism) → PC-1; defaults *provisional* |
| D2 | Verification statuses | §7.4 four statuses; §8.10 "outdated" | `unverified` / `clinician_verified` / `disputed` / `retracted` + `source` | Decided → PC-2 |
| D3 | Record-level status | Maintained (§11.1.3) | Derived | Decided → PC-3 |
| D4 | Identifiers | Inconsistent (§7.1, §8.2, §11.1) | Identifier table (ADR 0003) | Decided → PC-4 |
| D5 | Sex vs gender | "Gender" everywhere | **Sex only** (required); no gender field | **Decided 19 Nov** → PC-5 |
| D6 | Biometrics | In MVP features | Removed | Decided → PC-6 |
| D7 | Consent grantee | Undefined | A care team at a facility (eligibility) | Decided → PC-7 |
| D8 | Per-visit OTP | OTP each session (§12.2.1) | **Kept**: OTP at every visit; session until visit end, max 12 h, and OTP fallback are *proposed* | **Decided 19 Nov (B)** → PC-7a; details proposed |
| D9 | Emergency access scope | Requester picks; restricted reachable | Emergency summary only, content *provisional* | Decided → PC-8 |
| D10 | Unverified items at Basic Access | "Verified" items only (§12.2.2) | Undecided for Basic Access | Open (Q-C3) |
| D11 | Who may invoke emergency access | Nurses conditionally / unconditionally | MO and CO only | *Provisional* → PC-9 |
| D12 | Emergency duration and notification | No limit; "when appropriate" | 12 h; SMS with no medical information | Decided → PC-9 |
| D13 | Emergency card / QR | Not in the PRD | **No card or QR.** Continuum ID sent by SMS at enrolment | **Decided 19 Nov** (no card); SMS design *proposed* → PC-13 |
| D14 | Restricted information | A restricted layer | No restricted category | Open (prd-review Q21) |
| D15 | Minors in the pilot | §10.1 in the MVP; §14.3 adolescents and adults | The pilot enrols adults **and children** | *Provisional* (clinical lead + ethics) → PC-10 |
| D16 | Multi-facility | One facility | Multi-facility model | Decided → PC-11 |
| D17 | SCD dataset | Seven categories (§8.3, §14.5) | Element list §3.6; admissions recorded from enrolment; treatment history/responses deferred to phase 2 | List *provisional*; Q-D6 *proposed* → PC-12, PC-14 |
| D18 | Blood group | TBC (§7.6) | Required | *Provisional* → PC-12 |
| D19 | Hospital patient ID | Linked (§7.1, §10.16) | `facility_mrn` type | Open (Q-I5) |
| D20 | Emergency contacts as an identification method | §8.5.1.1 | Not searchable | Decided → PC-6 |
| D21 | Product scope | SCD-only (§16.2), with expansion as future (§17.2) | Should the design anticipate other chronic illnesses? | Open (scope question, `decisions-pending.md`) |

---

## 5. Open questions

Resolved since the last version:
- Q-C2: OTP every visit
- Q-E1: MO / CO, provisional
- Q-E2: no card
- Q-D1: mg/day, provisional
- Q-D2: any ward admission, provisional
- D5: sex only

Q-D6 is now *proposed*.

### Dataset (clinical lead)
- **Q-D3.** Confirm the emergency summary content, including ⚑3 and ⚑4 in §3.6.
- **Q-D4.** Blood group: verifiable by a lab technologist only from a lab report?
- **Q-D5.** ⚑5: genotype as a lab value; sickling/solubility screen as evidence.
- **Q-D6.** *Proposed:* admissions recorded from enrolment; treatment history and responses
  in phase 2. Also confirm the `admission_reason` list.
- **Q-D7.** Are care-plan fields other than pain management (fluids/oxygen, other) shown in
  emergencies, or kept at all?
- **Q-D8.** ⚑1: genotype Required vs Optional.
- **Q-D9.** ⚑2: what "number of transfusions" means.

### Verification
- **Q-V2.** Is "requiring review/update" (PRD §7.4) a status or derived?
- **Q-V3.** Who can set `disputed`, and who resolves it?
- **Q-V4.** May a clinician verify their own entry?
- **Q-V5.** Confirm that usual care and emergency contact are not verified.
- **Q-V6.** Consultants/specialists: a cadre of their own, or included with medical
  officers? (Not in the 19 Nov answers.)

### Identifiers
- **Q-I1.** Is phone strong? The plan says no.
- **Q-I2.** Encrypt national ID / SHA numbers?
- **Q-I3.** Continuum ID mirrored in the identifier table: OK?
- **Q-I4.** Which identifiers are required at registration?
- **Q-I5.** The hospital patient number (`facility_mrn`).

### Consent, visits and access
- **Q-C3.** Basic Access content and labelling (D10).
- **Q-C4.** Consent capture without a phone (signed form?).
- **Q-C5.** Administrator access (prd-review Q22, Q23).
- **Q-C6.** *Proposed:* a visit authorisation covers the whole care team for that visit.
  Confirm.
- **Q-C7.** *Proposed:* session until the visit ends, maximum 12 h. Who ends the visit, and
  is it ended automatically at discharge?
- **Q-C8.** *Proposed:* the OTP fallback. Which cadres may use it? Who reviews it, and
  within how long? Is the patient notified by SMS afterwards (template
  `fallback_access_notice`)?
- **Q-A1.** Idle timeout for record sessions.
- **Q-A2.** Who sees a patient's access history?
- **Q-A3.** Log per section (plan) or per field?

### Emergency and SMS
- **Q-E3.** Break-glass reviewer and deadline.
- **Q-E4.** Break-glass on a minor: SMS to the guardian, the patient, or both?
- **Q-S1.** *Proposed SMS design:* the sender ID and wording must not reveal SCD. Is
  "Continuum" itself revealing if the service is SCD-only (see D21)?
- **Q-S2.** SMS provider (e.g. an aggregator with a Kenyan sender ID).
- **Q-S3.** OTP expiry, attempt limit and resend limit.

### Minors
- **Q-G1.** PRD §8.8.1.4: the guardian's access after 18, re-verification, credentials.
- **Q-G2.** More than one active guardian at once?
- **Q-G3.** For a minor, do OTPs go to the guardian's phone by default? The 19 Nov fallback
  reason "guardian holds phone" suggests the patient's own phone is the default. Clarify
  for adolescents.

### Technical
- **Q-T1.** `pg_trgm` extension privilege in production.
- **Q-R1.** Access to the reporting view.
- **Q-M6.** The app split (`apps/patients`, `apps/staff`, `apps/notifications`).

---

## 6. Proposed build order (after approval)

Each step is its own plan → tests (RED) → implementation → verification report cycle:

1. **The append-only base and trigger helpers** (`apps/core`): L and G, with tests.
2. Facilities, care teams, cadres (provisional seed), staff profiles and memberships.
3. Patient (sex only), identifiers, emergency contacts, `pg_trgm`, search and matching,
   and `SearchEvent`.
4. Access sessions and events.
5. Code systems, dataset elements (provisional seed), `CoreDatasetItem` with its `CHECK`,
   unique index and trigger, the reporting view, and verification (provisional
   permissions, disabled in production until sign-off).
6. Linked entries (including `Admission`, once Q-D6 is confirmed), the care plan and the
   emergency summary selector.
7. SMS (`SmsMessage`, templates, provider) and `OtpChallenge`.
8. Consent, `VisitAuthorisation` (OTP and fallback), then break-glass.
9. Guardians and the transition.
