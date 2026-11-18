# Continuum Health: data model plan (draft for approval)

- **Status:** PLAN ONLY. No models or migrations exist yet. Each model still goes through
  plan → tests → implementation under `continuum-dev-workflow` (CLAUDE.md §5).
- **Date:** 2026-11-18
- **Based on:** `docs/prd.md` (v0, unrevised), `docs/prd-review.md`, ADRs 0001–0007 in
  `docs/decisions/`, and the group's answers of 18 Nov 2026:
  - Q-V1: `unverified` + `source` (decided)
  - Q-C1 / Q-M1: care teams (decided)
  - D5: sex and gender (decided)
  - Q-C2: no OTP under standing consent (**proposed**, pending group confirmation)
  - M2–M5: modelling choices (accepted)
  - SCD dataset: the agreed list (awaiting clinical-lead sign-off)
- **Where the PRD and an ADR disagree,** the model follows the ADR. The disagreement is
  listed in §4, and decided PRD changes are logged in `docs/prd-changes.md`. Open questions
  are in §5.

All examples use synthetic data. Nothing here changes `docs/prd.md`.

---

## 1. Conventions

### 1.1 Apps (one per domain)

| App | Models |
|---|---|
| `apps/facilities` | Facility, CareTeam |
| `apps/staff` | Cadre, StaffProfile, FacilityMembership, CareTeamMembership, VerificationPermission |
| `apps/patients` | Patient, PatientIdentifier, EmergencyContact, GuardianRelationship, EmergencyCard |
| `apps/clinical` | CodeSystem, Code, DatasetElement, CoreDatasetItem, Allergy, PatientComplication, Medication, GenotypeTest, TransfusionAlert, UsualCareProvider, EmergencyCarePlan, VerificationEvent; reporting view `clinical_scd_dataset_wide` |
| `apps/access` | Consent, BreakGlassAccess, AccessSession, AccessEvent, SearchEvent |

`apps/accounts.User` stays as it is: staff log in with email. Patients and guardians have
**no login yet** (`docs/decisions-pending.md`). Patient-side accounts will link to
`Patient` / `GuardianRelationship` later through a nullable FK; none of these models
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
  `DELETE` (PRD §13.1.8). The trigger is created by a migration and tested (M4,
  accepted). No soft delete, because nothing is ever deleted.

### 1.3 Rules applied everywhere

- **`on_delete`:**
  - `PROTECT` for every FK to patients, clinical items, staff, users and facilities.
  - **No `CASCADE`** anywhere.
- **Integer primary keys stay internal;** URLs use `public_id`.
- **Nothing identifying goes into application logs or `SearchEvent`:** no identifier
  value, name, phone number or clinical value.
- **Coded values** use `TextChoices` when the list is fixed by the software, and the `Code`
  reference table when clinicians maintain the list.
- **Measured values** use `DecimalField`.
- **Live-row uniqueness** uses partial `UniqueConstraint(..., condition=Q(deleted_at=None))`.
- **Clinical values are never overwritten** (PRD §7.8; M3, accepted). A change creates a new
  row that `supersedes` the old one, and the old row stops being `is_current`.
  Verification-status changes go to `VerificationEvent`. There is no history-table library.
- **Rules the database can't express with a `CHECK`** (they need a lookup in another table)
  are enforced with PostgreSQL triggers created in migrations, each with tests for allowed
  and rejected writes (M4).

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
    Patient ||--o{ EmergencyCard : carries

    DatasetElement ||--o{ CoreDatasetItem : defines
    CodeSystem ||--o{ DatasetElement : "value set"
    CodeSystem ||--o{ Code : lists
    Code ||--o{ CoreDatasetItem : "coded value"
    Patient ||--o{ CoreDatasetItem : has
    Patient ||--o{ Allergy : has
    Patient ||--o{ PatientComplication : has
    Code ||--o{ PatientComplication : complication
    Patient ||--o{ Medication : takes
    Patient ||--o{ GenotypeTest : had
    Patient ||--o{ TransfusionAlert : has
    Patient ||--o{ UsualCareProvider : "usually seen by"
    Facility |o--o{ UsualCareProvider : "usual facility"
    StaffProfile |o--o{ UsualCareProvider : "usual clinician"
    Patient ||--o{ EmergencyCarePlan : has
    VerificationEvent }o--|| User : by

    Patient ||--o{ Consent : gives
    CareTeam ||--o{ Consent : receives
    Patient ||--o{ BreakGlassAccess : "subject of"
    StaffProfile ||--o{ BreakGlassAccess : invokes
    Facility ||--o{ BreakGlassAccess : at
    Patient ||--o{ AccessSession : "opened in"
    User ||--o{ AccessSession : opens
    Facility ||--o{ AccessSession : "acting at"
    Consent |o--o{ AccessSession : basis
    BreakGlassAccess |o--o{ AccessSession : basis
    AccessSession ||--o{ AccessEvent : records
    User ||--o{ SearchEvent : searches

    Patient {
        uuid public_id UK
        string continuum_id UK
        date date_of_birth
        string sex "required"
        string gender "optional"
        string account_status
    }
    DatasetElement {
        string key UK
        string data_type "code|decimal|date|boolean|linked"
        string requirement
    }
    CoreDatasetItem {
        fk value_code
        decimal value_decimal
        date value_date
        bool value_boolean
        string null_reason "none|unknown"
        bool is_current
        string verification_status
    }
    Consent {
        string category
        datetime granted_at
        datetime revoked_at
        date review_due_on
    }
    BreakGlassAccess {
        string reason_code
        text reason_text
        datetime started_at
        datetime expires_at
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
`GenotypeTest`, `TransfusionAlert`, `EmergencyCarePlan`) all carry the `ClinicalItem`
fields (§3.7). They are omitted from the diagram for space.

---

## 3. Models

### 3.1 Facility (`apps/facilities`)

**Purpose:** a healthcare facility. Participating facilities are `active`. Non-participating
facilities can appear as free text on the clinical models that allow it.
**Implements:** PRD §7.2 (Facility ID), §11.3, §12.4.1; ADR 0007. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `facility_code` | `CharField(12)`, unique | Continuum Facility ID, system-generated, immutable. Format TBC (PRD §7.2); proposed `FAC-XXXXXX` |
| `name` | `CharField(200)` | |
| `kmhfl_code` | `CharField(20)`, null, unique | Kenya Master Health Facility List code, if known |
| `county` | `TextChoices` | The 47 counties |
| `status` | `TextChoices` | `onboarding`, `active`, `suspended`, `withdrawn` |
| `registered_at` | `DateTimeField`, null | Set when status first becomes `active` |

- **"Registered facility"** (ADR 0004 4b) means `status = active`.
- **Constraints:** `CheckConstraint`: `registered_at` is set when the status is `active`.
- **Indexes:** `status`.

### 3.2 CareTeam (`apps/facilities`)

**Purpose:** a named team within a facility (e.g. "SCD Clinic", "Emergency Department").
It is the **consent grantee** (ADR 0005; Q-C1 and Q-M1 decided).
**Implements:** ADR 0005, 0007; PRD §12.2.3. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `facility` | FK Facility, `PROTECT` | |
| `name` | `CharField(100)` | |
| `kind` | `TextChoices` | `scd_clinic`, `emergency`, `inpatient`, `laboratory`, `outpatient`, `other` |
| `is_active` | `BooleanField` | |

- **Constraints:** unique `(facility, name)` among live rows.
- **Access rule:** consent covers only users with an **active `CareTeamMembership`** in the
  grantee team. Pilot ED staff are not in the SCD Clinic team, so they need break-glass
  (ADR 0004 4b) unless the patient grants consent to the ED team.

### 3.3 Staff: Cadre, StaffProfile, FacilityMembership, CareTeamMembership, VerificationPermission (`apps/staff`)

#### Cadre

**Purpose:** a professional cadre. It is **reference data, not code**, so verification rules
can be configured (ADR 0001).
**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `code` | `SlugField`, unique | e.g. `medical_officer`, `consultant`, `clinical_officer`, `nurse`, `lab_technologist` |
| `name` | `CharField(100)` | |
| `regulator` | `TextChoices` | `KMPDC`, `COC`, `NCK`, `KMLTTB`, `none` |
| `is_clinician` | `BooleanField` | Whether the cadre may invoke break-glass (ADR 0004 4b). The value for each cadre is **open** (Q-E1) |

#### StaffProfile

**Purpose:** the professional identity of a staff `User`.
**Implements:** PRD §7.2, §11.2, §11.2.1. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `user` | OneToOne `accounts.User`, `PROTECT` | |
| `professional_id` | `CharField(12)`, unique | Continuum Professional ID, generated, immutable. Format TBC (PRD §7.2) |
| `full_name` | `CharField(200)` | |
| `work_phone` | `CharField(16)`, blank | Shown as the "usual clinician" contact (§3.8) |
| `cadre` | FK Cadre, `PROTECT` | |
| `registration_number` | `CharField(50)`, blank | Licence number with the regulator |
| `registration_expires_on` | `DateField`, null | PRD §11.2.1: access is suspended on expiry |
| `registration_verified_at` / `_by` | `DateTimeField` / FK User, `PROTECT`, null | |
| `status` | `TextChoices` | `pending`, `active`, `suspended`, `deactivated` |

#### FacilityMembership

**Purpose:** verified affiliation with a facility; there can be more than one (PRD
§11.2.1, §11.3).
**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `staff` | FK StaffProfile, `PROTECT` | |
| `facility` | FK Facility, `PROTECT` | |
| `role` | `TextChoices` | `clinical`, `facility_admin` |
| `starts_on` / `ends_on` | `DateField` / `DateField`, null | When a professional leaves, the membership is ended, not deleted |
| `verified_by` / `verified_at` | FK User, `PROTECT` / `DateTimeField` | |

- **Constraints:** one open membership per `(staff, facility, role)` (partial unique where
  `ends_on IS NULL` and the row is live); `ends_on >= starts_on`.
- **Rule:** a `facility_admin` membership grants **no** clinical access (PRD §12.3).

#### CareTeamMembership

**Purpose:** puts a facility member in a care team.
**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `membership` | FK FacilityMembership, `PROTECT` | |
| `care_team` | FK CareTeam, `PROTECT` | Same facility as the membership (enforced by a trigger, M4) |
| `starts_on` / `ends_on` | dates | |

- **Constraints:** one open row per `(membership, care_team)`.

#### VerificationPermission

**Purpose:** which cadre may verify which category of information.
**Implements:** ADR 0001. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `cadre` | FK Cadre, `PROTECT` | |
| `category` | `TextChoices` `ItemCategory` | `scd_dataset`, `allergy`, `complication`, `medication`, `genotype_test`, `transfusion_alert`, `emergency_care_plan` (`lab_result` is added when lab results are modelled) |
| `approved_by` / `approved_on` | FK User / date | The clinical governance sign-off |

- **Constraints:** unique `(cadre, category)` among live rows.
- **Ships empty.** Pilot rules come as a reviewed data migration after the clinical lead
  signs them off.

### 3.4 Patient, PatientIdentifier, EmergencyContact (`apps/patients`)

#### Patient

**Purpose:** a person with SCD enrolled in Continuum. Not owned by any facility.
**Implements:** PRD §7.1, §7.2, §11.1, §11.1.3; ADR 0003, 0006, 0007. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `continuum_id` | `CharField(12)`, unique | System-generated, immutable, never reassigned (PRD §11.1). `CH-XXXXXX`, with no O/0 or I/1 and a check character (proposal) |
| `given_name`, `middle_names`, `family_name` | `CharField` | |
| `date_of_birth` | `DateField` | Age is computed, never stored |
| `dob_is_estimated` | `BooleanField` | |
| `sex` | `TextChoices`, **required** | `female`, `male`, `intersex`. Used for matching (ADR 0003) and clinical care. **Decided (D5)** |
| `gender` | `CharField(50)`, blank | **Optional**, self-described. **Decided (D5)**; PRD change PC-5 |
| `place_of_birth` | `CharField`, blank | |
| `county_of_residence`, `residence_detail` | `TextChoices` / `CharField`, blank | |
| `citizenship` | `CharField(2)`, blank | ISO 3166 code |
| `preferred_language` | `TextChoices` | `en`, `sw`, `other` |
| `account_status` | `TextChoices` | `pending_identity`, `identity_verified`, `suspended`, `deactivated` (PRD §11.1.3) |
| `identity_verified_at` / `_by` | `DateTimeField` / FK User, `PROTECT`, null | Identity verification, separate from clinical verification (PRD §11.1.1) |
| `is_deceased`, `date_of_death` | `BooleanField`, `DateField` null | |
| `adult_transition_at` | `DateTimeField`, null | ADR 0006 |

- **Not stored:** the whole-record clinical status (PRD §11.1.3) is derived (ADR 0001).
- **Constraints:**
  - `identity_verified_at` is set when `account_status = identity_verified`.
  - `date_of_death` is null unless `is_deceased`.
  - `sex` is never blank.
- **Indexes:**
  - `(family_name, date_of_birth)`.
  - **`pg_trgm` GIN trigram indexes** on `given_name` and `family_name` for fuzzy name
    search (M5, accepted). The extension is created with Django's `TrigramExtension()`
    migration operation, which needs a database role allowed to create extensions (Q-T1).

#### PatientIdentifier

**Purpose:** every external or system identifier, one per row (ADR 0003).
**Implements:** ADR 0003; PRD §7.1, §10.4, §12.2. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `id_type` | `TextChoices` | `client_registry`, `national_id`, `birth_certificate`, `sha_number`, `phone`, `continuum_id`, `facility_mrn` (hospital patient number) |
| `value` | `CharField(64)` | Normalised: phone in E.164 (`+2547…`), IDs uppercased with spaces and hyphens removed |
| `issuing_facility` | FK Facility, `PROTECT`, null | Required only for `facility_mrn` |
| `verification_method` | `TextChoices` | `unverified`, `self_declared`, `document_sighted`, `document_uploaded`, `otp_confirmed`, `registry_lookup` (future; not used in the pilot) |
| `verified_at` / `verified_by` | `DateTimeField` / FK User, `PROTECT`, null | |
| `is_primary` | `BooleanField` | e.g. the primary phone for SMS |

- **Strong types:** `client_registry`, `national_id`, `birth_certificate`, `sha_number`,
  `continuum_id` and `facility_mrn`. `phone` is **not strong** (Q-I1).
- **Constraints:**
  - Unique `(id_type, value)` among live rows for strong types except `facility_mrn`.
  - Unique `(issuing_facility, value)` for `facility_mrn`.
  - `issuing_facility` is set if and only if `id_type = facility_mrn`.
  - `verified_at` is set for methods other than `unverified` and `self_declared`.
  - One live `is_primary` per `(patient, id_type)`.
- **Indexes:** `(id_type, value)`.
- **Continuum ID:** canonical on `Patient.continuum_id`, mirrored here as one immutable row
  created in the same transaction (Q-I3).
- **Matching** (ADR 0003, in a selector):
  - **confirmed:** a strong identifier agrees, plus the name or DOB agrees.
  - **probable:** given + family name + DOB + **sex** agree, with no strong identifier;
    shown with a warning.

#### EmergencyContact

**Purpose:** people to contact in an emergency. The dataset requires at least one, or an
explicit `none` / `unknown` (§3.6).
**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `name`, `relationship` | `CharField` | |
| `phone` | `CharField(16)` | E.164 |
| `priority` | `PositiveSmallIntegerField` | |

- **Not searchable** (prd-review Q15 open).

### 3.5 GuardianRelationship (`apps/patients`)

**Purpose:** a parent or legal guardian managing a minor's record (ADR 0006).
**Implements:** ADR 0006; PRD §8.8.1.4, §10.1. **Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | The minor |
| `guardian_name` | `CharField(200)` | |
| `guardian_phone` | `CharField(16)` | For SMS, including break-glass notifications |
| `guardian_id_type` / `guardian_id_value` | `TextChoices` / `CharField`, blank | |
| `relationship` | `TextChoices` | `mother`, `father`, `legal_guardian`, `other_relative`, `other` |
| `legal_basis` | `TextChoices` | `parent`, `court_order`, `other_documented` |
| `verified_by` / `verified_at` | FK User / `DateTimeField`, null | |
| `starts_on` / `ends_on` | `DateField` / `DateField`, null | |
| `end_reason` | `TextChoices`, blank | `patient_reached_majority`, `revoked`, `guardian_changed`, `deceased` |

- **Constraints:** `end_reason` is set if and only if `ends_on` is set; `ends_on >= starts_on`.
- **Transition:** a service ends open relationships with `patient_reached_majority` and sets
  `Patient.adult_transition_at`. A daily task lists patients turning 18 within 90 days; it
  never ends access by itself.

### 3.6 SCD core dataset (`apps/clinical`)

**Implements:** ADR 0002 (**agreed list; awaiting clinical-lead sign-off**), ADR 0001; PRD
§8.3, §14.5, §15.4. **Design:** M2, accepted with guard rails:
1. **Typed value columns** only: `code`, `decimal`, `date`, `boolean`.
2. An **element-definition reference table** (`DatasetElement`) holding each element's data
   type.
3. A **`CHECK`** that exactly one value column **or** a null reason is set.
4. A **partial unique index**: one current row per patient + element.
5. A **PostgreSQL view** that pivots to one row per patient for reporting.

Elements that need more structure than one typed value (allergies, complications, other
medicines, genotype test details, transfusion reactions/antibodies, usual facility and
clinician, emergency contacts, pain management) have `data_type = linked`. Their entries
live in a dedicated model (§3.8, §3.9, §3.4). The `CoreDatasetItem` row for a linked element
exists **only** to record an explicit `none` or `unknown` when there are no entries.

#### CodeSystem and Code

**Uses:** P T A S.

| Model | Fields |
|---|---|
| `CodeSystem` | `key` (`SlugField`, unique), `name` |
| `Code` | `system` FK CodeSystem `PROTECT`; `code` (`SlugField`); `label`; `sort_order`; `is_active`; `external_ref` (blank, e.g. an ICD-11 code for future mapping) |

- **Constraints:** unique `(system, code)`.
- **Retiring a code:** `is_active=False`; codes are never deleted.

**Seeded code systems** (agreed list):

| `CodeSystem.key` | Codes |
|---|---|
| `scd_genotype` | `hbss` HbSS · `hbsc` HbSC · `hbs_beta0` HbSβ⁰ · `hbs_beta_plus` HbSβ⁺ · `other` Other |
| `blood_group` | `a_pos`, `a_neg`, `b_pos`, `b_neg`, `ab_pos`, `ab_neg`, `o_pos`, `o_neg` (ABO + Rh as one value) |
| `genotype_test_method` | `hplc`, `electrophoresis`, `isoelectric_focusing`, `point_of_care`, `newborn_screen`, `molecular`, `other` (proposed; not in the agreed list) |
| `complication` | `stroke` Stroke · `acute_chest_syndrome` Acute chest syndrome · `splenic_sequestration` Splenic sequestration · `avascular_necrosis` Avascular necrosis · `other` Other (with a description) |

"Unknown" genotype or blood group is recorded as `null_reason = unknown`, not as a code,
so "unknown" means the same thing for every element. The agreed list's "unknown" genotype
is preserved this way.

#### DatasetElement

**Purpose:** the element-definition reference table.
**Uses:** P T A S.

| Field | Type | Notes |
|---|---|---|
| `key` | `SlugField`, unique | |
| `label` | `CharField` | |
| `data_type` | `TextChoices` | `code`, `decimal`, `date`, `boolean`, `linked` |
| `linked_model` | `CharField`, blank | For `linked`: the app label of the model holding entries, e.g. `clinical.Allergy` |
| `code_system` | FK CodeSystem, `PROTECT`, null | Required if and only if `data_type = code` |
| `unit` | `CharField(20)`, blank | e.g. `g/dL` |
| `decimal_places` | `PositiveSmallIntegerField`, null | `0` makes a decimal element a whole-number count |
| `min_value` / `max_value` | `DecimalField`, null | Plausibility range |
| `requirement` | `TextChoices` | `required`, `optional`, `conditional` |
| `required_if_element` / `required_if_boolean` | FK self, `PROTECT`, null / `BooleanField`, null | For `conditional`: e.g. the hydroxyurea dose is required when `hydroxyurea = yes` |
| `in_emergency_summary` | `BooleanField` | Drives the summary (ADR 0004 4a) |
| `sort_order` | `PositiveSmallIntegerField` | |
| `is_active` | `BooleanField` | |

- **Constraints:**
  - `code_system` is set if and only if `data_type = code`.
  - `linked_model` is set if and only if `data_type = linked`.
  - Both `required_if_*` fields are set if and only if `requirement = conditional`.
  - `decimal_places`, `min_value` and `max_value` are set only for `decimal`.

**Agreed element list.** ⚠ **Awaiting clinical-lead sign-off.** Every element accepts
`none` or `unknown` (ADR 0002).

*Required:*

| Key | Label | Data type | Stored in | Req | Summary* |
|---|---|---|---|---|---|
| `scd_confirmed` | SCD confirmed | boolean | CoreDatasetItem | required | yes |
| `scd_genotype` | Genotype | code (`scd_genotype`) | CoreDatasetItem | required | yes |
| `blood_group` | Blood group and Rh | code (`blood_group`) | CoreDatasetItem | required | yes |
| `baseline_hb` | Baseline haemoglobin (g/dL; `observed_on` = date measured) | decimal (1 dp, 2.0–20.0) | CoreDatasetItem | required | yes |
| `hydroxyurea` | On hydroxyurea | boolean | CoreDatasetItem | required | yes |
| `hydroxyurea_dose` | Hydroxyurea dose (unit: Q-D1) | decimal | CoreDatasetItem | conditional (`hydroxyurea = yes`) | yes |
| `hydroxyurea_start` | Hydroxyurea start date | date | CoreDatasetItem | conditional (`hydroxyurea = yes`) | no |
| `folic_acid` | On folic acid | boolean | CoreDatasetItem | required | yes |
| `allergies` | Allergies | linked → `Allergy` | Allergy (none / unknown in CoreDatasetItem) | required | yes |
| `hospitalisations_12m` | Hospitalisations in the last 12 months | decimal (0 dp, 0–99) | CoreDatasetItem | required | yes |
| `usual_care` | Usual facility and clinician | linked → `UsualCareProvider` | UsualCareProvider | required | yes |
| `emergency_contact` | Emergency contact | linked → `EmergencyContact` | EmergencyContact | required | yes |

*Optional:*

| Key | Label | Data type | Stored in | Req | Summary* |
|---|---|---|---|---|---|
| `genotype_test` | Genotype test method, date and facility | linked → `GenotypeTest` | GenotypeTest | optional | no |
| `transfusion_count` | Number of transfusions (lifetime) | decimal (0 dp, 0–999) | CoreDatasetItem | optional | yes |
| `last_transfusion` | Date of last transfusion | date | CoreDatasetItem | optional | yes |
| `transfusion_alerts` | Transfusion reactions or red-cell antibodies | linked → `TransfusionAlert` | TransfusionAlert | optional | yes |
| `penicillin_prophylaxis` | On penicillin prophylaxis | boolean | CoreDatasetItem | optional | no |
| `other_medicines` | Other current medicines | linked → `Medication` | Medication | optional | yes |
| `complications` | Major complications (fixed list) | linked → `PatientComplication` | PatientComplication | optional | yes |
| `pain_management` | Pain management that usually works / things to avoid | linked → `EmergencyCarePlan` | EmergencyCarePlan (pain fields) | optional | yes |

\* The "Summary" column (shown in the emergency summary) is a **proposal** for the clinical
lead; the agreed list did not specify it.

**§15.4 completeness** = required elements, plus conditional elements whose condition is
met, that have a current value, a current linked entry, or a `null_reason`; divided by the
number of applicable elements. It is computed from the reporting view.

#### CoreDatasetItem

**Purpose:** one patient's current (and past) value for one element.
**Uses:** C (= P T A S + V + provenance).

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `element` | FK DatasetElement, `PROTECT` | |
| `value_code` | FK Code, `PROTECT`, null | |
| `value_decimal` | `DecimalField(7,2)`, null | |
| `value_date` | `DateField`, null | |
| `value_boolean` | `BooleanField`, null | |
| `null_reason` | `TextChoices`, blank | `none`, `unknown` |
| `observed_on` | `DateField`, null | When the value was true or measured (e.g. the baseline Hb date). Metadata, not a value column |

Constraints (guard rails):
1. **`CHECK` exactly one:** either exactly one of `value_code`, `value_decimal`,
   `value_date`, `value_boolean` is set and `null_reason` is blank, or all four are null and
   `null_reason` is `none` or `unknown`. In SQL:
   `num_nonnulls(value_code_id, value_decimal, value_date, value_boolean) + (null_reason <> '')::int = 1`.
2. **Partial unique index:** `(patient, element)` where `is_current AND deleted_at IS NULL`.
3. **Trigger `clinical_dataset_item_type_check`** (M4):
   - The value column set must match `element.data_type`.
   - `value_code` must belong to `element.code_system`.
   - A decimal must respect `decimal_places` and the min/max range.
   - A `linked` element accepts only a `null_reason`.

   A `CHECK` can't do these because they need to read `DatasetElement`. Tests cover each
   rejection.

**Indexes:** `(patient, is_current)`, `(element, is_current)`.

**Linked elements:** adding the first entry (e.g. an `Allergy`) supersedes a `none` /
`unknown` row for that element in the same transaction (service rule).

#### Reporting view `clinical_scd_dataset_wide`

**Purpose:** one row per live patient, one group of columns per active element, for
reporting and §15.4 completeness. **Not used by the clinical UI**, which goes through
selectors with access checks.

- **Created by a `RunSQL` migration.** The SQL is generated from the active elements by a
  function in `apps/clinical/reporting.py`, with conditional aggregation over current, live
  `CoreDatasetItem`s (`max(...) FILTER (WHERE element_key = 'baseline_hb')`).
- **Columns per scalar element:** `<key>` (the value; codes as their `code` slug),
  `<key>_status` (`value` / `none` / `unknown` / `missing`) and `<key>_verification`.
- **Columns per linked element:** `<key>_count` and `<key>_status`.
- **Identifies patients by `public_id` only:** no names, identifiers or contact details
  (data minimisation).
- **When elements change,** the data migration that changes them must also
  `DROP VIEW` / `CREATE VIEW`. A test asserts that the view's columns match the active
  elements, so a forgotten rebuild fails CI.
- **Optional:** an unmanaged model (`managed = False`) for ORM reads in reports.
- **Who may read it:** reporting roles only (Q-R1).

### 3.7 Verification: VerifiableMixin, ClinicalItem, VerificationEvent (`apps/clinical`)

**Implements:** ADR 0001 (as amended 18 Nov 2026); PRD §7.4, §7.8, §7.10, §11.5.1, §13.1.3.

#### `VerifiableMixin` (abstract)

| Field | Type | Notes |
|---|---|---|
| `verification_status` | `TextChoices` | **`unverified`**, `clinician_verified`, `disputed`, `retracted` |
| `verified_by` | FK User, `PROTECT`, null | |
| `verified_at` | `DateTimeField`, null | |
| `verified_at_facility` | FK Facility, `PROTECT`, null | |

- **Constraint (on each concrete model):** `verified_by` and `verified_at` are set when the
  status is `clinician_verified`.

#### `ClinicalItem` (abstract) = ContinuumModel + VerifiableMixin + provenance

| Field | Type | Notes |
|---|---|---|
| `source` | `TextChoices`, required | **`patient`**, **`clinician`**, **`import`**: where the information came from (Q-V1, decided). A guardian's entry is `patient`; `created_by` records who typed it |
| `source_facility` | FK Facility, `PROTECT`, null | Required when `source` is `clinician` (`CHECK`) |
| `recorded_by_cadre` | FK Cadre, `PROTECT`, null | Cadre at the time of entry (PRD §11.5.1) |
| `is_current` | `BooleanField` | |
| `supersedes` | OneToOne self, `PROTECT`, null | The previous version (M3) |

- **Display:** "Unverified — reported by patient" vs "Unverified — entered by clinician"
  vs "Verified by <cadre>, <facility>, <date>". This covers PRD §7.4's "patient-reported"
  and "clinician-documented".

#### VerificationEvent

**Purpose:** append-only history of every status change.
**Uses:** L.

| Field | Type | Notes |
|---|---|---|
| `content_type` / `object_id` | FK ContentType, `PROTECT` / `PositiveBigIntegerField` | The item (several models) |
| `patient` | FK Patient, `PROTECT` | Copied onto the row, so a patient's events can be queried directly |
| `from_status` / `to_status` | `TextChoices` | |
| `actor` | FK User, `PROTECT` | |
| `actor_cadre` | FK Cadre, `PROTECT` | |
| `facility` | FK Facility, `PROTECT`, null | |
| `reason` | `TextField`, blank | Required for `disputed` and `retracted` |

- **Indexes:** `(content_type, object_id)`, `(patient, created_at)`.
- **Service rule:** a user may set `clinician_verified` only with a
  `VerificationPermission` for their cadre and the item's category, while holding an active
  clinical membership at the acting facility.
- **Open:** whether a clinician who can verify an item's category may verify their own
  entry (Q-V4).

### 3.8 Linked clinical entries (`apps/clinical`)

**Implements:** ADR 0002 (agreed list); PRD §7.6, §8.3, §11.1.2. **Uses:** C, except
`UsualCareProvider` (see below).

| Model | Fields (besides ClinicalItem) | Constraints |
|---|---|---|
| `Allergy` | `patient`; `substance` (`CharField`); `category` (`drug`, `food`, `environmental`, `other`); `reaction` (text); `severity` (`mild`, `moderate`, `severe`, `unknown`) | — |
| `PatientComplication` | `patient`; `complication` FK Code (`complication` system), `PROTECT`; `description` (required when the code is `other`); `onset_date` (null); `onset_precision` (`day`, `month`, `year`, `unknown`) | Code system checked by a trigger (M4); partial unique `(patient, complication)` where current and live, except `other` |
| `Medication` | `patient`; `name`; `dose_text`; `frequency_text`; `route`; `started_on` / `stopped_on` (null) | `stopped_on >= started_on`. These are **other** current medicines: hydroxyurea and folic acid are dataset elements and are not repeated here (service check). Coded dosing is out of scope (PRD §16.10) |
| `GenotypeTest` | `patient`; `method` FK Code (`genotype_test_method`); `tested_on` (null); `tested_on_precision`; `facility` FK Facility `PROTECT`, null; `facility_name_text` (for non-participating labs) | `facility` or `facility_name_text` (or neither, if unknown), never both |
| `TransfusionAlert` | `patient`; `kind` (`reaction`, `alloantibody`); `description` (e.g. "anti-K"; "febrile reaction"); `identified_on` (null) | — |
| `UsualCareProvider` | `patient`; `facility` FK Facility `PROTECT`, null; `facility_name_text`; `clinician` FK StaffProfile `PROTECT`, null; `clinician_name_text`; `clinician_phone` | One current per patient; `facility` or `facility_name_text` is set |

**`UsualCareProvider` uses** P T A S + `source` + supersession, **without** verification.
It is a care-coordination fact, not clinical information to verify (Q-V5). When
`clinician` is set, the summary shows the clinician's `work_phone`, and the
`clinician_phone` field is left blank.

Hospitalisation details, treatment history and treatment responses (PRD §8.3) are **not**
in the agreed dataset (D17). The count is the `hospitalisations_12m` element. Encounters
(PRD §10.10) and lab results (§10.11) are later plans.

### 3.9 EmergencyCarePlan (`apps/clinical`)

**Purpose:** a clinician-authored plan for acute episodes, versioned. Its pain fields hold
the dataset's `pain_management` element.
**Implements:** PRD §7.6, §8.8.1.1, §10.6; ADR 0002, 0004 4a. **Uses:** C.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `pain_relief_that_works` | `TextField`, blank | Dataset element `pain_management` |
| `pain_relief_to_avoid` | `TextField`, blank | Dataset element `pain_management` |
| `fluids_oxygen_guidance` | `TextField`, blank | |
| `other_instructions` | `TextField`, blank | |
| `review_due_on` | `DateField` | Interval TBC (PRD suggests 3–6 months). An overdue plan shows as "outdated" (PRD §10.6) |
| `last_reviewed_at` / `_by` | `DateTimeField` / FK User, null | |

- **Constraints:**
  - One current, live plan per patient.
  - At least one text field is non-empty.
- **Patient-reported pain information:** if a patient reports what works before any
  clinician plan exists, it's stored as a plan with `source = patient`, `unverified`.

**Emergency summary (ADR 0004 4a).** This is **not a model**. A selector builds it from:
- `Patient`, `EmergencyContact` and `UsualCareProvider`
- current `CoreDatasetItem`s for elements with `in_emergency_summary`
- current `Allergy`, `PatientComplication`, `Medication` and `TransfusionAlert` entries
- the current `EmergencyCarePlan`

Every item shows its verification status and source. The selector has a fixed number of
queries, tested.

### 3.10 Consent (`apps/access`)

**Purpose:** standing consent from a patient (or guardian) to **a care team at a facility**,
for one category.
**Implements:** ADR 0005 (as amended 18 Nov 2026); PRD §7.9, §10.8, §12.2.3, §12.4.
**Uses:** P T A. **No S:** consent is revoked, never deleted.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `grantee_team` | FK CareTeam, `PROTECT` | |
| `category` | `TextChoices` | `emergency_summary`, `full_scd_record`, `lab_results` |
| `granted_at` | `DateTimeField` | |
| `granted_by_guardian` | FK GuardianRelationship, `PROTECT`, null | |
| `capture_method` | `TextChoices` | `otp_to_patient_phone` (proposed default, Q-C2), `signed_form` (fallback when there's no phone; Q-C4), `patient_app` (future) |
| `otp_verified_at` | `DateTimeField`, null | Required when `capture_method = otp_to_patient_phone` |
| `recorded_by` | FK User, `PROTECT` | |
| `review_due_on` | `DateField` | `granted_at` + 1 year: a reminder is sent; consent does **not** lapse |
| `last_reviewed_at` | `DateTimeField`, null | |
| `revoked_at` / `revocation_note` | `DateTimeField`, null / `TextField` | |

- **Constraints:**
  - One active consent per `(patient, grantee_team, category)`.
  - `revoked_at >= granted_at`.
  - `otp_verified_at` is set if and only if the method is OTP.
- **Indexes:** `(patient, revoked_at)`, `(grantee_team, revoked_at)`, `review_due_on`.
- **Rule:** a user acts under consent only with an active `CareTeamMembership` in
  `grantee_team`. **There's no OTP at each visit** under standing consent (Q-C2, *proposed,
  pending group confirmation*).

### 3.11 BreakGlassAccess (`apps/access`)

**Purpose:** an emergency override of consent (ADR 0004 4b). In the pilot this is the path
for **ED staff outside the SCD Clinic team**.
**Implements:** PRD §9.3.1, §10.9, §12.2.5, §13.1.6. **Uses:** P T. **No S.**

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `invoked_by` | FK StaffProfile, `PROTECT` | Clinician cadre, with an active clinical membership at `facility` |
| `facility` | FK Facility, `PROTECT` | Must be `active` |
| `reason_code` | `TextChoices` | `unconscious`, `unable_to_communicate`, `refused_but_clinically_necessary`, `normal_access_not_possible`, `other` |
| `reason_text` | `TextField` | Required, with a minimum length |
| `scope` | `TextChoices` | `emergency_summary` only (ADR 0004 4a) |
| `started_at` / `expires_at` | `DateTimeField` | `expires_at = started_at + 12h` |
| `ended_at` | `DateTimeField`, null | |
| `patient_notified_at` / `notification_status` | `DateTimeField`, null / `TextChoices` | `pending`, `sent`, `failed`, `no_phone` |
| `reviewed_by` / `reviewed_at` | FK User, `PROTECT`, null / `DateTimeField` | |
| `review_outcome` / `review_notes` | `TextChoices` / `TextField` | `appropriate`, `inappropriate`, `needs_follow_up` |

- **Constraints:**
  - `started_at < expires_at <= started_at + interval '12 hours'`.
  - `reason_text` isn't empty.
  - The review fields are all set or all null.
  - A trigger (M4) blocks changes to the core columns after insert.
- **Indexes:** `(patient, started_at)`, `(reviewed_at)`, `(facility, started_at)`.

### 3.12 AccessSession, AccessEvent, SearchEvent (`apps/access`)

**Implements:** ADR 0005; PRD §11.6, §12.4.2, §13.1.7, §13.1.8, §13.1.9.

#### AccessSession

**Purpose:** one opening of one patient's record.
**Uses:** P, `created_at`.

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `user` | FK User, `PROTECT` | |
| `staff_cadre` | FK Cadre, `PROTECT`, null | Copied at open time |
| `facility` | FK Facility, `PROTECT`, null | The acting facility |
| `care_team` | FK CareTeam, `PROTECT`, null | The team whose consent is used |
| `basis` | `TextChoices` | `consent`, `break_glass`, `self`, `guardian`, `administrative` |
| `consent` / `break_glass` | FK Consent / FK BreakGlassAccess, `PROTECT`, null | |
| `opened_at` / `last_activity_at` / `closed_at` | `DateTimeField` (`closed_at` null) | `last_activity_at` is updated at most once a minute |
| `close_reason` | `TextChoices`, blank | `user_ended`, `logout`, `idle_timeout`, `break_glass_expired`, `consent_revoked` |

- **Approximate duration** = `(closed_at or last_activity_at) − opened_at`, computed.
- **Constraints:**
  - `basis = consent` requires `consent` and `care_team`.
  - `basis = break_glass` requires `break_glass`.
  - `closed_at >= opened_at`.
  - `close_reason` is set if and only if `closed_at` is set.
  - A trigger allows only `last_activity_at`, `closed_at` and `close_reason` to change.
- **Indexes:** `(patient, opened_at)`, `(user, opened_at)`, a partial index on open sessions.

#### AccessEvent

**Uses:** L.

| Field | Type | Notes |
|---|---|---|
| `session` | FK AccessSession, `PROTECT` | |
| `action` | `TextChoices` | `view`, `create`, `update`, `verify`, `dispute`, `retract`, `export` |
| `section` | `TextChoices` | `emergency_summary`, `scd_dataset`, `allergies`, `complications`, `medications`, `transfusion`, `care_plan`, `usual_care`, `identifiers`, `consent` |
| `object_public_id` | `UUIDField`, null | Never a value |

#### SearchEvent

**Uses:** L.

| Field | Type | Notes |
|---|---|---|
| `user` | FK User, `PROTECT` | |
| `facility` | FK Facility, `PROTECT` | |
| `method` | `TextChoices` | `continuum_id`, `identifier`, `name_dob_sex`, `emergency_card` |
| `identifier_type` | `TextChoices`, blank | The type only, **never the value** |
| `result_count` | `PositiveSmallIntegerField` | |
| `selected_patient` | FK Patient, `PROTECT`, null | |
| `match_level` | `TextChoices`, blank | `confirmed`, `probable` |

### 3.13 EmergencyCard (`apps/patients`)

**Purpose:** a card or QR code showing only "Sickle Cell Disease" + the Continuum ID.
**Implements:** ADR 0004 4c (**pending one member's confirmation**). **Uses:** P T A. **No S.**

| Field | Type | Notes |
|---|---|---|
| `patient` | FK Patient, `PROTECT` | |
| `token_hash` | `CharField(64)`, unique | SHA-256 of a random 128-bit token. The QR encodes `https://<host>/e/<token>`; the raw token is never stored |
| `issued_at` / `issued_by` | `DateTimeField` / FK User, `PROTECT` | |
| `patient_agreed_at` | `DateTimeField` | The card discloses the diagnosis, so explicit agreement is required |
| `revoked_at` / `revoke_reason` | `DateTimeField`, null / `TextChoices` | `lost`, `replaced`, `patient_request`, `deceased` |

- **Constraints:** one unrevoked card per patient.
- **Scanning:**
  - **Without a login:** the page shows only what is printed on the card, plus a login
    prompt. It is rate-limited, and the response is the same for revoked and unknown
    tokens.
  - **A logged-in clinician:** gets a confirmed Search & Find result, logged as
    `SearchEvent(method=emergency_card)`. No clinical access without consent or
    break-glass.

---

## 4. Where the PRD and the ADRs still disagree

The PRD has not been revised. Decided changes are logged in `docs/prd-changes.md` (PC-n).

| # | Topic | PRD says | ADR / model says | State |
|---|---|---|---|---|
| D1 | Who verifies | Only an authorised **physician** (§8.2.1, §10.6, §11.1.2, §11.5.1, §12.2.5, §13.1.3) | Configurable per cadre and category (ADR 0001); §7.4 agrees | Decided → PC-1 |
| D2 | Verification statuses | §7.4: patient-reported, clinician-documented, clinically verified, requiring review/update; §8.10 "potentially outdated" | `unverified` / `clinician_verified` / `disputed` / `retracted`, plus `source` (patient, clinician, import) | Decided → PC-2; "requiring review" open (Q-V2) |
| D3 | Record-level status | §11.1.3: maintained | Derived | Decided → PC-3 |
| D4 | Identifiers | Government ID TBC / optional / required (§7.1, §8.2, §11.1); no Client Registry or SHA | Identifier table (ADR 0003) | Decided → PC-4; required set open (Q-I4) |
| D5 | Sex vs gender | "Gender" everywhere | `sex` required (matching, clinical care); `gender` optional | **Decided 18 Nov** → PC-5 |
| D6 | Biometrics | In MVP features (§8.5.1.1, §9.1.1, §10.4) | Removed (ADR 0004 4d) | Decided → PC-6 |
| D7 | Consent grantee and duration | Undefined | A care team at a facility, until revoked, with annual review | **Decided 18 Nov** → PC-7 |
| D8 | Per-visit OTP | OTP each normal-care session (§12.2.1) | No OTP per visit under standing consent; OTP only to grant consent to a new care team, and for patient login | **Proposed**, pending group confirmation |
| D9 | Emergency access scope | Requester identifies the information needed; restricted information reachable (§12.2.4, §12.2.5) | Emergency summary only | Decided → PC-8 |
| D10 | Unverified items at Basic Access | §12.2.2: "*verified*" items only | Shown and labelled in emergency; Basic Access not yet decided | Open (Q-C3) |
| D11 | Who may invoke emergency access | Nurses conditionally (§9.2) or unconditionally (§6.3) | Any clinician at a registered facility; "clinician" cadres undefined | Open (Q-E1) |
| D12 | Emergency duration and notification | No limit; notified "when appropriate" | 12-hour expiry; SMS always | Decided → PC-9 |
| D13 | Emergency card / QR | Not mentioned | Card with SCD + Continuum ID | Pending one member (4c) |
| D14 | Restricted information | A restricted/sensitive layer (§12.1, §12.2.4, §13.1.5) | Three consent categories, no restricted layer | Open (prd-review Q21) |
| D15 | Minors in the pilot | §10.1 in the MVP; §14.3 adolescents and adults | In the data model; enrolment by the clinical lead and ethics | Decided (model) → PC-10 |
| D16 | Multi-facility | One facility (§14.2, §16.3) | Multi-facility model; ED-vs-SCD-clinic test via care teams | Decided → PC-11 |
| D17 | SCD dataset | Seven categories (§8.3, §14.5): diagnosis, complications, major hospitalisations, allergies, treatment history, care plans, treatment responses | Agreed list (§3.6). **Not in it:** hospitalisation details, treatment history, treatment responses, emergency care plan as a whole. **Added:** genotype, blood group, baseline Hb, hydroxyurea, folic acid, transfusions, usual facility/clinician, emergency contact | Agreed; awaits clinical-lead sign-off → PC-12 |
| D18 | Blood group | §7.6: TBC | Required element | Agreed (with D17) → PC-12 |
| D19 | Hospital patient ID | §7.1, §10.16: retained and linked | `facility_mrn` identifier type | Open (Q-I5) |
| D20 | Emergency contacts as an identification method | §8.5.1.1 | Not searchable; unconscious patients without documents are out of scope | Decided (4d) → PC-6 |

---

## 5. Open questions

Resolved on 18 Nov 2026 and removed from this list:
- Q-V1 (`unverified` + `source`)
- Q-C1 and Q-M1 (care teams)
- D5 (sex and gender)
- Q-M2 to Q-M5 (EAV-lite with guard rails, supersession, triggers, `pg_trgm`)
- The former Q-D1 to Q-D4 (replaced by the agreed list)

Q-C2 is now *proposed*.

### Dataset (for clinical-lead sign-off)
- **Q-D1.** Hydroxyurea dose unit: mg/kg/day or mg/day?
- **Q-D2.** What counts as a "hospitalisation" in the last 12 months: an admission of 24
  hours or more? ED visits?
- **Q-D3.** Which elements appear in the emergency summary (the "Summary" column in §3.6
  is a proposal).
- **Q-D4.** Blood group: may only a lab report or a clinician verify it?
- **Q-D5.** The test-method code list for `GenotypeTest` is proposed, not agreed.
- **Q-D6.** Are hospitalisation details, treatment history and treatment responses (PRD
  §8.3) deliberately dropped from the MVP, or deferred to encounters (D17)?

### Verification
- **Q-V2.** Is "requiring review/update" (PRD §7.4) a status, or derived from review dates?
- **Q-V3.** Who can set `disputed`, and who resolves a dispute?
- **Q-V4.** May a clinician verify an item they entered themselves?
- **Q-V5.** Confirm that `UsualCareProvider` and `EmergencyContact` need no clinical
  verification.

### Identifiers
- **Q-I1.** Is phone a strong identifier? The plan says no.
- **Q-I2.** Field-level encryption for national ID / SHA numbers?
- **Q-I3.** The Continuum ID is canonical on `Patient` and mirrored in `PatientIdentifier`.
  OK?
- **Q-I4.** Which identifiers are required at registration? Children often have only a
  birth certificate.
- **Q-I5.** Hospital patient number (`facility_mrn`): include it, and is it strong?

### Consent and access
- **Q-C2.** *Proposed:* no OTP at each visit under standing consent; OTP only for granting
  consent to a new care team and for patient login. **Pending group confirmation.**
- **Q-C3.** What does a consented clinician see first (PRD "Basic Access"), and does
  `emergency_summary` consent equal Basic Access?
- **Q-C4.** Consent capture for patients with no phone: a signed form? Who checks it?
- **Q-C5.** Administrative access by hospital or Continuum admins (prd-review Q22, Q23).
  The plan allows none until decided.
- **Q-A1.** Idle timeout for a patient-record session (30 minutes like login, or shorter)?
- **Q-A2.** Who may see a patient's access history inside the system?
- **Q-A3.** Log views per section (plan) or per field?

### Emergency
- **Q-E1.** Which cadres are "clinicians" for break-glass?
- **Q-E2.** Card QR: revocable token (plan) or the plain Continuum ID?
- **Q-E3.** Who reviews break-glass events, and within how many days?
- **Q-E4.** Break-glass on a minor: SMS to the guardian, the patient, or both?

### Minors
- **Q-G1.** PRD §8.8.1.4: the guardian's access after 18, re-verification, credentials.
- **Q-G2.** More than one active guardian at once? The plan allows it.

### Technical
- **Q-T1.** `pg_trgm` needs a role that can create extensions. Local and CI use `postgres`;
  confirm the production database allows it, or have the extension pre-created by the
  database administrator.
- **Q-R1.** Who may read `clinical_scd_dataset_wide`? Proposal: a separate read-only
  reporting database role, granted later, with no access from the web app's reporting
  pages until reporting permissions are designed.
- **Q-M6.** Patients and staff split into `apps/patients` and `apps/staff`, rather than
  extending `apps/accounts`.

---

## 6. Proposed build order (after approval)

Each step is its own plan → tests (RED) → implementation → verification report cycle:

1. The append-only base and trigger helpers (`apps/core`), with tests.
2. Facilities, care teams, cadres, staff profiles and memberships.
3. Patient (with sex and gender), identifiers, emergency contacts, `pg_trgm`, search and
   matching, and `SearchEvent`.
4. Access sessions and events.
5. Code systems, dataset elements, `CoreDatasetItem` with its `CHECK`, partial unique index
   and type trigger, the reporting view, and verification (rules stay empty until
   sign-off).
6. Linked entries, the emergency care plan and the emergency summary selector.
7. Consent, then break-glass and the SMS notification (needs an SMS provider decision).
8. Guardians and the transition.
9. The emergency card, if 4c is confirmed.
