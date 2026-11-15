# PRD Review: Continuum Health

- **Reviewed:** `docs/prd.md` (converted from `docs/CONTINUUM_HEALTH_PRD_CLEANED.docx`)
- **Date:** 2026-11-15
- **Purpose:** find what is defined, what is missing and what conflicts before designing
  the data model.

Section references (§) use the numbering in `docs/prd.md`. This review quotes and
interprets the PRD; it does not change it.

---

## a. Summary

Continuum Health is a patient-centred longitudinal health record for people living with
sickle cell disease (SCD). Its purpose is to give authorised healthcare professionals fast
access to verified, clinically relevant information, especially during acute and emergency
care, without replacing hospital systems or clinical judgement (§1–§3). The MVP is one
participating hospital and about 50 adolescent and adult SCD patients (§4, §14.2–§14.3).

Patients self-register or are enrolled, and they get a permanent Continuum Patient ID that
is separate from hospital numbers (§7.1–§7.2, §11.1). Identity verification is kept separate
from clinical verification: patient-reported information stays marked "unverified" until a
physician verifies it (§8.2.1, §11.1.2–§11.1.3).

Professionals have one Professional ID and can be affiliated with more than one facility
(§11.2–§11.3). They reach records through a layered model (§12.1):
1. Search & Find, which shows identification details only.
2. Patient access authorisation by OTP.
3. Basic Access, a limited predefined view.
4. Consent-based Clinical Record Access.
5. Restricted/Sensitive access.
6. A system-approved, audited Emergency Access exception.

Every action is attributed and audited, and patients can see who accessed their record
(§8.8.1, §13.1.8–§13.1.9). The system must never become a precondition for receiving care
(§8.10, §13.1.11).

---

## b. Table of contents

- **1** Product Overview
- **2** Problem
- **3** Product Goal
- **4** MVP Definition
- **5** Users
- **6** User Roles & Permissions
  - 6.1 Patient · 6.2 Doctor / Clinician · 6.3 Nurse · 6.4 Laboratory Professional ·
    6.5 Hospital Administrator · 6.6 Continuum Health Administrator ·
    6.7 Medical Records / Health Information Professional (TBC)
- **7** Patient Record
  - 7.1 Patient Identity & Demographics · 7.2 Continuum Identity · 7.3 Patient-Provided
    Information · 7.4 Clinical Verification · 7.5 Patient Care Preferences & Accessibility
    Needs · 7.6 Emergency Summary · 7.7 Information That Should Not Be Included ·
    7.8 Patient Record Updateability · 7.9 Patient Access & Control · 7.10 Record
    Provenance & Auditability
- **8** Patient Journey
  - 8.1 Entry into the Continuum Health System (8.1.1 How can a patient first enter?)
  - 8.2 Account Creation (8.2.1 Account Status and Clinical Record Verification;
    8.2.1.1 UNVERIFIED / PENDING CLINICAL VERIFICATION)
  - 8.3 Building the Patient's Medical Record
  - 8.4 Patient's Normal Use of Continuum Health
  - 8.5 Emergency Patient Journey (8.5.1 Emergency Access Scenarios; 8.5.1.1 Emergency
    Patient Identification; 8.5.1.2 Patient Cannot Be Found)
  - 8.6 Routine / Ongoing Care
  - 8.7 Patient Visits Another Participating Hospital
  - 8.8 End of Healthcare Encounter (8.8.1 Audit Trail / Patient Account Activity;
    8.8.1.1 Emergency Care Plan Review; 8.8.1.2 Conflicting or Incorrect Information;
    8.8.1.3 Patient Preferences and Participation in Care; 8.8.1.4 Children and Guardians)
  - 8.9 Failure Points / What Could Go Wrong
  - 8.10 Core Principles Emerging from the Patient Journey
- **9** Clinician Journey
  - 9.1 Physician Journey (9.1.1 Finding a Patient; 9.1.1.1 Search/Find vs Basic Clinical
    Access; 9.1.2 Physician Record Review; 9.1.3 What a Physician Can Do)
  - 9.2 Nurse Journey
  - 9.3 Laboratory Professional Journey (9.3.1 Emergency Access Workflow; 9.3.1.1 What
    Happens During Emergency Access?; 9.3.2 End-of-Encounter Workflow; 9.3.3 Audit and
    Attribution; 9.3.4 Failure and Exception Scenarios; 9.3.5 Remaining Decisions)
- **10** Core Features
  - 10.1 Patient Account Management · 10.2 Patient Identity & Verification ·
    10.3 Professional & Hospital Account Management · 10.4 Patient Search &
    Identification · 10.5 Longitudinal Patient Medical Record · 10.6 Emergency Care Plan ·
    10.7 Clinical Record Management · 10.8 Access & Consent Management · 10.9 Emergency
    Access Management · 10.10 Healthcare Encounter Management · 10.11 Laboratory
    Information Management · 10.12 Notifications · 10.13 Audit & Activity Tracking ·
    10.14 Patient Audit & Record Review · 10.15 Hospital & Continuum Administration ·
    10.16 Hospital System Integration · 10.17 System Reliability & Emergency Fallback
    (Remaining Decision) · 10.18 Future Development
- **11** Identity & Verification
  - 11.1 Patient Identity (11.1.1 Identity Verification; 11.1.2 Clinical Verification;
    11.1.3 Account Status and Clinical Record Status)
  - 11.2 Professional Identity (11.2.1 Professional Authorization)
  - 11.3 Facility Affiliation · 11.4 Authentication
  - 11.5 Role-Based Access (11.5.1 Verification of Information Added by Professionals;
    11.5.2 Emergency Identification and Unverified Records)
  - 11.6 Auditability of Identity and Access
- **12** Consent & Access
  - 12.1 Purpose
  - 12.2 Search & Find (12.2.1 Patient Access Authorization; 12.2.2 Basic Access;
    12.2.3 Clinical Record Access; 12.2.4 Restricted and Sensitive Information;
    12.2.5 Emergency Access)
  - 12.3 Access by Professional Role
  - 12.4 Patient Control Over Access (12.4.1 Access Across Healthcare Facilities;
    12.4.2 End of Access Session)
- **13** Security & Audit
  - 13.1 Security, Privacy & Audit: 13.1.1 Purpose · 13.1.2 Confidentiality & Privacy ·
    13.1.3 Data Integrity · 13.1.4 Role-Based Access · 13.1.5 Sensitive & Restricted
    Information · 13.1.6 Emergency Access · 13.1.7 Session Controls · 13.1.8 Audit Trail ·
    13.1.9 Patient Audit Visibility · 13.1.10 Accountability & Notifications ·
    13.1.11 Availability & Continuity of Care · 13.1.12 Security Incidents ·
    13.1.13 Pilot Security Considerations
- **14** Pilot Environment
  - 14.1 Purpose · 14.2 Setting · 14.3 Patient Population · 14.4 Healthcare Users ·
    14.5 Clinical Scope · 14.6 System Scope · 14.7 Hospital System Integration ·
    14.8 Workflow · 14.9 Limitations · 14.10 Learning Objectives
- **15** Success Metrics
  - 15.1 Patient Access and Experience · 15.2 Clinical Usefulness · 15.3 Efficiency and
    Patient Burden · 15.4 Record Quality and Continuity · 15.5 Safety, Access Control and
    Accountability · 15.6 Technical and Operational Performance · 15.7 Primary Success
    Indicators
- **16** Out of Scope
  - 16.1 Clinical Decision-Making · 16.2 Expansion Beyond SCD · 16.3 Multi-Hospital
    Deployment · 16.4 National and International Interoperability · 16.5 Complete
    Historical Record Digitization · 16.6 Advanced Biometric Identification ·
    16.7 Advanced Offline Functionality · 16.8 Advanced AI · 16.9 Billing and Financial ·
    16.10 Pharmacy as a Full System Role · 16.11 Advanced Patient Services ·
    16.12 Expanded Sensitive and Restricted Information · 16.13 Purpose of the Scope
    Limitations
- **17** Future Development
  - 17.1 Additional Healthcare Facilities · 17.2 Beyond SCD · 17.3 Advanced Identity and
    Biometrics · 17.4 Advanced Offline and Emergency Access · 17.5 Research, Public Health
    and Population Health Data · 17.6 AI and Advanced Analytics · 17.7 Patient-Centered
    Expansion · 17.8 Additional Professional Roles · 17.9 Advanced Data Governance and
    Patient Control · 17.10 Long-Term Vision

---

## c. SCD core dataset

**Verdict: PARTIAL.** No section defines an SCD core dataset as fields. The PRD names
**categories** of SCD information in three places, but gives no field definitions, data
types, value sets or required/optional rules.

| Section | What it names |
|---|---|
| **§8.3** "Sickle Cell Disease pilot baseline" | 1. SCD diagnosis · 2. Important complications · 3. Major hospitalizations · 4. Known allergies · 5. Relevant treatment history · 6. Established emergency/care plans · 7. Significant treatment responses |
| **§14.5** Pilot Clinical Scope | The same seven items as §8.3 (wording: "Established emergency and care plans") |
| **§16.5** Complete Historical Medical Record Digitization | Six of the seven; **"SCD diagnosis" is left out** of this list |

Supporting references:
- **§15.4** measures the "percentage of pilot records containing the core SCD information
  defined for the pilot". This assumes a defined dataset exists, and the closest candidate
  is §14.5.
- **§7.6** (Emergency Summary), **§9.1.1.1** (Basic Clinical Access) and **§12.2.2** (Basic
  Access) list fields shown to clinicians: primary chronic diagnosis, allergies and
  medication reactions, current/ongoing treatment, important complications, emergency care
  plan, last encounter, primary hospital/physician, and so on. These are generic chronic-
  disease fields, not SCD-specific ones.
- **§7.6** lists "Blood type — TBC; inclusion and verification requirements to be
  determined".

**What is missing to build it.** These are SCD-specific items the PRD does not mention. They
are listed for your clinical lead to accept or reject, not as recommendations:
- SCD genotype (e.g. HbSS, HbSC, HbS/β-thalassaemia) and how it was confirmed
- Baseline haemoglobin and other baseline laboratory values
- Disease-modifying therapy (e.g. hydroxyurea), with dose and start date
- Transfusion history, red-cell alloantibodies and transfusion reactions
- Pain-crisis history and frequency, and the patient's usual effective analgesia
- History of specific complications: stroke, acute chest syndrome, splenic sequestration,
  avascular necrosis, priapism, leg ulcers
- Splenectomy or functional asplenia, and vaccination/prophylaxis status
- Blood group (marked TBC in §7.6)

Also undecided: whether "Important complications" is a coded list or free text, and whether
each item needs a date, source and verification status (§7.10 implies it does).

---

## d. Emergency identification

### What the PRD says

| Section | Content |
|---|---|
| **§8.5** | Emergency flow: *Patient arrives → Patient identification → Determine whether patient has a Continuum Health account → Locate record → Authenticate/authorize access → …* |
| **§8.5.1.1** | If the patient cannot communicate, possible methods: personal identification documents, Continuum Health ID, other approved patient identifiers, **biometrics**, **emergency-contact information**, other hospital identification mechanisms. If the patient doesn't remember their ID, there should be an alternative lookup using approved identifying information. "Remaining decision: the exact emergency identification mechanism and acceptable identifiers will be finalized…" |
| **§9.1.1** | Search by Continuum ID, government ID, name + DOB, approved biometric identification, other approved information. Patient-assisted OTP when other methods fail. **Biometric search for an unconscious patient with no ID** "where the hospital and Continuum Health system support it". |
| **§9.1.1.1** | Search results show only name, DOB, age, gender, Continuum ID and identity-verification status. |
| **§10.4** (headed "MVP") | Lists "Biometric patient identification where supported", "OTP-based patient identification" and "Emergency patient search". |
| **§11.4** | Biometrics "will not be a requirement for the initial pilot". |
| **§11.5.2** | The professional "will attempt to identify the patient using the available identifiers". If the record can't be found or sufficiently identified, treatment continues normally. |
| **§12.2** | Search & Find identifiers: Continuum ID, name + DOB, government ID, other approved methods, OTP, "Biometrics in future versions". |
| **§16.6** | Biometric identification is **out of scope** for the MVP. The MVP relies on Continuum ID, approved identifying information and OTP. |
| **§8.5.1.2, §9.3.4, §13.1.11** | If the patient isn't found, treat normally, record the incident and contact the Continuum administrator. |
| **§12.4.1, §8.7** | At another participating facility, the same process applies. |

### Gaps

1. **Nothing tells a clinician the patient has SCD before a search.** Every pathway assumes
   the clinician already suspects a Continuum account exists and searches for it. The PRD
   names no patient-carried signal: no card, wristband, QR code, phone lock-screen
   information or alert. At an unfamiliar facility this is the main problem, and the PRD
   doesn't address it.
2. **An unconscious patient without documents cannot be identified in the MVP.** Biometrics
   are out of scope (§11.4, §16.6) and OTP needs the patient to take part. Name + DOB needs
   someone who knows them. The patient can then only be found if a companion knows their
   details.
3. **Emergency-contact lookup is mentioned but not searchable.** §8.5.1.1 lists
   emergency-contact information as an identification method, but it isn't among the
   search identifiers in §9.1.1, §10.4 or §12.2. The PRD doesn't say whether searching by
   an emergency contact's phone number is allowed, or how.
4. **There is no "unfamiliar facility" in the MVP.** The pilot is one facility (§14.2,
   §16.3). A clinician at a non-participating facility has no Continuum account, and §9.3.4
   ("Clinician is not authorized") rules out emergency access for unauthorised professionals
   in the MVP. Cross-facility emergency identification is therefore described (§8.7,
   §12.4.1) but can't happen in the pilot.
5. **No acceptable identifiers or matching rules are defined.** §8.5.1.1 defers the
   identifiers; §8.2 asks "What forms of identification are acceptable?". There's no rule
   for confirming a match, such as how many identifiers must agree. §10.4 lists
   "Duplicate-patient safeguards" without defining them.
6. **SCD status may be hidden at Basic Access when it's unverified.** §12.2.2 lists
   "*Verified* primary chronic diagnosis" and "*Verified* allergies". A newly enrolled
   patient who self-reported SCD might show no diagnosis at Basic Access, even though §8.5,
   §9.1.1.1 and §12.2.5 Scenario D say unverified information should be visible and
   labelled.

### Contradictions

| Topic | Conflict |
|---|---|
| Biometrics | MVP features (§10.4, headed "MVP") and the journeys (§8.5.1.1, §9.1.1) include biometric identification, but §11.4 and §16.6 exclude it from the pilot/MVP. |
| What emergency access shows | §7.6 defines an "Emergency Summary" view. §12.2.2 defines Basic Access, which includes the verified emergency plan. §12.2.5 says the requester must "identify the information required". §9.3.1.1 and §13.1.6 say "only the information necessary". None of these say whether emergency access shows the §7.6 summary, the Basic Access set, or a per-request selection. §7.6 is not mentioned in any access section. |
| Who may invoke emergency access | §6.3 gives nurses emergency access with no condition; §9.2 limits it to "where a physician is not immediately available". |
| Emergency access approval | Approval is automatic, against "predefined emergency access rules" (§9.3.1, §10.9, §12.2.5, §13.1.6), but those rules are listed as undefined (§9.3.5). |
| Patient notification | "When appropriate" (§9.3.1, §9.3.1.1, §13.1.6) is never defined. |
| Structure | The Emergency Access Workflow and other clinician-wide sections (§9.3.1–§9.3.5) sit under §9.3 *Laboratory Professional Journey*. This looks like a heading-level slip in the Word file; citations will read oddly (e.g. "§9.3.1 Emergency Access Workflow"). |

---

## e. Other gaps that would block the data model

**Verification**
- **Who can verify clinical information** is contradictory:
  - §7.4 says "appropriately authorized healthcare professional … rather than automatically
    requiring a physician", and calls verification authority per category "TBC".
  - §8.2.1, §10.6, §11.1.2, §11.5.1, §12.2.5 and §13.1.3 say **only an authorised
    physician** may verify.
  - §10.11 needs "verification of uploaded [lab] results" but doesn't say by whom.
- **How detailed verification status is:**
  - §7.4 gives statuses per piece of information: patient-reported, clinician-documented,
    clinically verified, requiring review/update.
  - §11.1.3 gives a whole-record status: Unverified, Partially verified, Clinically
    verified.
  - §8.10 adds "potentially outdated".
  - The PRD doesn't define whether status is stored per item, derived for the record, or
    both, and the set of values doesn't match across sections.
- **Information entered by nurses or labs:** §9.2 and §11.5.1 say it is "pending
  verification" until a physician reviews it, but don't say which of it needs verification.

**Account and identity**
- **Account status mixes two things.** §8.2.1 says account status is separate from
  identity verification, but §11.1.3's account statuses ("Pending identity verification",
  "Identity verified", Suspended, Deactivated) combine them. Several states from elsewhere
  in the PRD are missing: deceased, long-term inactive, closure requested, guardian-managed
  minor.
- **Registration fields don't match between sections.** §7.1, §7.3, §8.2 and §11.1
  disagree on:
  - citizenship (only in §8.2 and §11.1)
  - place of residence (required in §7.1, optional in §8.2)
  - government ID (TBC in §7.1/§7.3, optional in §8.2, required in §11.1)
  - "Account type" (§8.2, undefined)
- **"Gender" is used everywhere.** The PRD never asks whether biological sex should be
  recorded separately.
- **Identifier formats:** Professional ID and Facility ID formats are TBC (§7.2). The
  Continuum Patient ID format is shown only as `CH-XXXXXX` (§7.1).
- **Hospital patient ID linking** is described (§7.1, §10.16) but its mechanism is TBC.

**Roles and permissions**
- **The role list isn't consistent.**
  - §10.3's professional account types leave out the Continuum Health Administrator.
  - The Medical Records role is TBC (§6.7). Duplicate merging and ID linking depend on it.
  - Pharmacy is TBC (§9.3, §10.3, §11.5, §16.10).
- **Patient data visible to hospital administrators:** §13.1.4 lets them "access basic
  identifying information", but §6.5 and §12.3 give them no patient data at all.
- **Continuum administrators:** §11.1.2 lets them incorporate historical clinical
  information, but §12.3 and §13.1.4 say they shouldn't routinely access clinical
  information.
- **Individual permissions** (view, add, edit or verify for each role and each category of
  information) are described in prose across §6, §9, §11.5, §12.3 and §13.1.4. They're
  never consolidated, and the lists differ. For example, the lab role can "update status
  of tests" in §12.3 but only "flag" results in §13.1.4.

**Consent and access sessions**
- **Consent** is undefined in several ways:
  - who it's granted to (one professional, a role or a facility)
  - its scope (which categories of information)
  - how long it lasts (one session, one encounter, or until revoked)
  - how it's revoked
  - "Avoid approving every individual piece of information" (§12.2.3) needs a defined set
    of categories.
- **OTP access authorisation** has no defined lifetime, retry limits or channel.
- **Access sessions and encounters:** the PRD doesn't say whether an access session (§12.4.2,
  §13.1.7) is the same thing as an encounter (§8.8, §10.10), or how they relate (one-to-one,
  many-to-one). It doesn't say who opens and closes each.
- **Restricted categories** are only examples (§12.2.4, §13.1.5). How the patient marks a
  record as sensitive, and who confirms it, is undefined.

**Clinical content**
- **Encounters:** encounter types, required fields, and what "closing" means are undefined
  (§10.10). §9.3.2 lists the required documentation but not its structure.
- **Emergency care plan:**
  - Its structure is undefined: free text, or structured items such as analgesia,
    fluids and oxygen?
  - The review interval is undecided; §8.8.1.1 suggests "3–6 months".
  - What "outdated" means (§10.6) is undefined.
- **Medications and prescriptions** appear in §8.3 and §16.10 ("basic medication
  information") with no structure.
- **Laboratory results** have no test catalogue, units, reference ranges or result
  structure. "Uploading results" (§6.4, §10.11) doesn't say whether results are structured
  data or file uploads.
- **Historical records:** six open questions in §8.3 (upload, who uploads, who verifies,
  source, how old records are distinguished, completeness).
- **Corrections and disputes** (§8.8.1.2, §10.14) have no workflow states or owner.

**Lifecycle and compliance**
- **Minors and guardians:**
  - §10.1 puts minor accounts and guardians in the MVP, but §14.3 focuses on adolescents
    and adults.
  - The guardian relationship, proxy access and transfer at 18 are all open (§8.8.1.4).
- **Deceased and long-term inactive accounts** are undefined (§9.3.5).
- **Deletion versus retention:** whether "account deletion" ever removes data is TBC
  (§7.9). This affects soft delete and archiving across every model. CLAUDE.md already
  forbids hard-deleting clinical records.
- **Notifications** have no defined channel (SMS, email, in-app) or rules (§10.12). "Patient
  has no phone" is a known failure point (§8.9).
- **Audit detail:** "Information viewed where appropriate" (§9.3.3) doesn't say whether
  every field view or every page view is recorded.
- **Kenyan law:** the PRD doesn't cite the Data Protection Act 2019, the Health Act or
  retention periods. §11.1.1 and §7.7 defer to "applicable legal and regulatory
  requirements".

**Platform**
- **Mobile app versus web:** §8.1.1 and §8.2 have the patient "download the Continuum
  Health application" or use a web browser. The decided stack is server-rendered web plus
  DRF, so the PRD doesn't say whether a native app is in the MVP.
- **Hospital integration** is "MVP" (§10.16) but described as "explore and test". The
  hospital system and what data is exchanged are unknown.

**Editorial issues** (the text was left unchanged in `prd.md`)
- §7.9 opens with a leftover drafting note: "This comes directly from what you originally
  proposed and **I would keep it in the PRD**…".
- §8.2.1.1 "UNVERIFIED / PENDING CLINICAL VERIFICATION" is formatted as a heading but is
  really a label example.
- Stray question marks appear in §13.1.8 ("What type of access occurred?") and §14.3 ("Are
  newly enrolled into Continuum Health?").
- §13 has only one subsection (13.1), so every security citation is §13.1.x.

---

## f. Decisions you need to make

**Scope and platform**
1. Which entry points from §8.1.1 are in the MVP? (Self-registration, registration at the
   hospital, post-emergency enrolment, newborn/guardian, outreach.)
2. Is a native mobile app in the MVP, or is the patient side a mobile-friendly web app
   only?
3. Are minors in the pilot? If yes, from what age, and does the guardian/proxy model have
   to be in the MVP data model?
4. What does "hospital system integration" mean for the MVP: manual entry of the hospital
   patient ID, a CSV import, or a live API? Which hospital system is it?

**SCD dataset**
5. What exactly is the SCD core dataset: the fields, which are required, and which value
   sets (for genotype, complications, and so on) apply? Who on the clinical side signs it
   off?
6. Is blood group included (§7.6), and does it need verification?
7. Are lab results structured values with units, uploaded documents, or both?
8. Is the emergency care plan structured, free text, or a structured template with free
   text, and what is its review interval?

**Verification**
9. Is verification authority physician-only (as most of the PRD says), or set per category
   of information (as §7.4 says)?
10. Is verification status stored per item, with the record status derived from it? Which
    set of status values do we use?
11. Which information entered by nurses or labs needs physician verification, and which
    counts as authoritative straight away?

**Identity and emergency identification**
12. Which identifiers are acceptable for registration and for search? Is the national ID
    number required or optional?
13. What makes a "confirmed match" in search? For example, Continuum ID alone, or name +
    DOB plus one more identifier.
14. How does an unfamiliar or busy ED know the patient has SCD before searching? A card, QR
    code, wristband or phone lock-screen information? Is any of this in the MVP?
15. Can clinicians search by emergency-contact phone number for an unconscious patient?
16. Should Basic Access and emergency views show **unverified** SCD diagnosis and allergies
    (labelled), or verified items only?

**Access and consent**
17. What exactly does emergency access show: the §7.6 Emergency Summary, the Basic Access
    set, or categories the clinician selects?
18. What are the automatic approval rules for emergency access (§9.3.5)? Is there a time
    limit on each grant?
19. Can nurses invoke emergency access unconditionally, or only when no physician is
    available? Can lab staff ever invoke it?
20. Who is consent granted to (a professional, a role or a facility), how long does it
    last, and what are the consent categories?
21. Which information categories are restricted in the MVP? Can the patient mark any item
    as sensitive, and does anyone have to approve that?
22. Can hospital administrators see basic patient identifiers (§13.1.4) or none at all
    (§12.3)?
23. Can Continuum administrators enter historical clinical information (§11.1.2)?

**Lifecycle and compliance**
24. What happens on an account-closure request: deactivation only, or anonymisation after
    a retention period? What retention period applies under Kenyan law?
25. How are deceased and long-term inactive patients handled?
26. Which notification channels are in the MVP (SMS, email, in-app), and which events
    notify the patient?
27. How detailed must audit of "information viewed" be: every field, or every
    page/section?
28. Who has the Medical Records role (§6.7) for duplicate merging and ID linking in the
    pilot: a separate role, the hospital's records officer, or a Continuum administrator?

**Document hygiene**
29. Should the PRD be corrected (the §7.9 drafting note, the misplaced §9.3.x headings,
    §8.2.1.1 as a heading) before we start citing section numbers? Section numbers would
    change if the heading levels change.
