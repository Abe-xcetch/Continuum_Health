<!--
Source: docs/CONTINUUM_HEALTH_PRD_CLEANED.docx (converted 2026-11-15).
Text is unchanged from the Word file. Conversion changes only:
- Section numbers added to every heading (cite as "PRD §x.y"); numbers typed
  in the original headings (e.g. "7. Patient Record") were replaced by these.
- Word's auto-generated table of contents (page numbers) and empty heading
  paragraphs were omitted.
- The source contains no tables.
If the Word file changes, regenerate this file rather than editing it by hand.
-->

# 1 Product Overview

Continuum Health is a secure, patient-centered digital health system designed to provide patients with a longitudinal health record that can be accessed by authorized healthcare professionals when needed.

The system is initially focused on patients living with Sickle Cell Disease (SCD), particularly those who may experience recurring acute or emergency episodes, receive care from multiple healthcare professionals or facilities, or have complex medical histories that are difficult to repeatedly communicate.

Continuum Health allows relevant patient health information to be recorded, verified and maintained over time, including diagnoses, allergies, treatment history, hospital encounters, care plans and emergency information. Authorized healthcare professionals can access relevant information according to their role and level of access, supporting more informed and efficient care.

The system is designed to work alongside existing hospital systems rather than replace them. During the initial pilot, Continuum Health will be implemented within one participating healthcare facility to test the patient and clinician experience, workflow and integration with the hospital environment.

Continuum Health is designed around the patient rather than a single healthcare facility, with the long-term aim of enabling a patient's health information to remain accessible and continuous as they move between healthcare facilities and, eventually, across regions and countries.

# 2 Problem

Patients living with chronic illnesses such as Sickle Cell Disease often have medical histories that are important to their care but may be fragmented, inaccessible or difficult to communicate when they seek treatment.

When a patient presents for acute or emergency care, healthcare professionals may have limited access to the patient's previous medical history, treatment responses, allergies, previous hospitalizations, care plans or other clinically relevant information. This can result in repeated history-taking, delays in establishing the patient's situation, loss or misunderstanding of important information, and increased burden on the patient to repeatedly explain and advocate for their own care.

The problem Continuum Health seeks to address is the gap between the patient who has an existing medical history and the healthcare professional who needs relevant information from that history to provide timely and informed care.

This problem is particularly important for patients with Sickle Cell Disease and other chronic conditions where repeated healthcare encounters, emergency episodes, multiple healthcare providers and complex treatment histories can make continuity of care difficult.

Continuum Health therefore seeks to improve the availability and continuity of relevant patient information while maintaining patient privacy, security and control over access to their health record.

# 3 Product Goal

The goal of Continuum Health is to enable authorized healthcare professionals to access accurate, verified and clinically relevant patient information when it is needed, particularly during acute and emergency care, while maintaining patient privacy, security and appropriate control over access.

The initial product goal is to test whether providing healthcare professionals with rapid access to a patient's verified longitudinal health record can:

- Reduce the time required to establish a patient's relevant medical history.
- Reduce the burden placed on patients to repeatedly explain or reconstruct their medical history.
- Reduce the loss, misunderstanding or fragmentation of important clinical information.
- Improve continuity of care between healthcare encounters.
- Support healthcare professionals in making more informed and efficient clinical decisions.
- Reduce the time between a patient's arrival for acute or emergency care and the provision of appropriate care.

The product will not replace clinical judgement or the relationship between patients and healthcare professionals. Instead, it will provide healthcare professionals with relevant, verified information to support human clinical decision-making while giving patients greater visibility and control over their health information.

# 4 MVP Definition

A secure digital patient record and clinician-access platform that allows a patient with Sickle Cell Disease to have a verified longitudinal health record that can be accessed by authorized healthcare professionals at one participating hospital, particularly when the patient presents for acute/emergency care.

# 5 Users

- Patient
- Doctor/Clinician
- Nurse
- Laboratory Professional
- Hospital Administrator
- Continuum Health Administrator
- Medical Records/Health Information Professional — **TBC**

# 6 User Roles & Permissions

## 6.1 Patient

**Purpose:** The patient is the owner and primary participant in their Continuum Health record.

The patient can:

1. Create their own Continuum Health account/profile, initially remaining unverified until the required clinical/identity verification is completed.
2. Provide information in the patient-facing portion of their profile.
3. Have an authorized healthcare professional complete/verify the relevant clinical portion of their record.
4. View their own Continuum Health record.
5. View information about who has accessed their record.
6. Request an audit/investigation concerning:
    - Information added, reviewed, updated or amended
    - Records accessed
    - Healthcare professionals who accessed the record
7. Update appropriate personal information.
8. Add/update their healthcare preferences and accessibility requirements.
9. Provide or deny consent for access to applicable portions of their medical record.
10. Request account closure/deactivation, subject to applicable legal and medical-record retention requirements.

**Important:** Patient-provided clinical information should be distinguishable from clinically verified information.

## 6.2 Doctor / Clinician

**Purpose:** Provide and document clinical care.

The clinician can:

1. Create a professional profile.
2. Receive a unique Continuum Health Professional ID.
3. Be associated with an authorized participating healthcare facility.
4. Review and clinically verify relevant patient information.
5. Request access to a patient's record.
6. Access patient information according to their authorized role and permissions.
7. View relevant longitudinal medical history.
8. Add clinical notes and information.
9. Add/update diagnoses, treatment information, allergies and other relevant clinical information within their scope.
10. Create/update clinician-approved treatment plans.
11. Create/update emergency care plans.
12. Amend clinical documentation where authorized, with amendments recorded in the audit trail.
13. Invoke emergency access where the defined emergency-access conditions are met.

## 6.3 Nurse

**Purpose:** Support and document patient care.

The nurse can:

1. Create a nursing professional profile.
2. Receive a unique Continuum Health Professional ID.
3. Be associated with an authorized participating healthcare facility.
4. Request access to a patient's record.
5. Access information according to their authorized role.
6. Access relevant portions of the patient record, including:
    - Emergency care information
    - Allergies/medication reactions
    - Relevant ongoing/current treatment
    - Relevant treatment plan
7. Document treatment or care administered.
8. Invoke emergency access where the defined emergency-access conditions are met.

## 6.4 Laboratory Professional

**Purpose:** Manage and contribute laboratory information to the patient's record.

The laboratory professional can:

1. Create a laboratory professional profile.
2. Receive a unique Continuum Health Professional ID.
3. Be associated with an authorized participating healthcare facility.
4. Request access to a patient's record.
5. Access information necessary to perform their authorized laboratory function.
6. Add/upload laboratory investigations and results.
7. Update/correct laboratory information where authorized, with changes recorded in the audit trail.

## 6.5 Hospital Administrator

**Purpose:** Manage the hospital's participation and implementation of Continuum Health.

The hospital administrator can:

1. Coordinate the linking/onboarding of Continuum Health with the hospital.
2. Coordinate with the Continuum Health Administrator regarding system implementation and operational issues.
3. Support the rollout of Continuum Health within their institution.
4. Coordinate appropriate staff onboarding and facility-level implementation.
5. Support the seamless operation of the system within the participating facility.

**Important:** Hospital administration should not automatically grant unrestricted access to patient clinical information.

## 6.6 Continuum Health Administrator

**Purpose:** Manage the Continuum Health platform and support participating facilities.

The Continuum Health Administrator can:

1. Oversee implementation of Continuum Health at participating hospitals.
2. Maintain the Continuum Health administrative environment.
3. Support participating facilities with system-related issues.
4. Coordinate platform-level operational issues.
5. Have a Continuum Health administrator profile.

**Important:** Being a Continuum Health Administrator should not automatically grant unrestricted access to patient clinical records.

## 6.7 Medical Records / Health Information Professional — TBC

Potential responsibilities could involve:

- Record verification
- Patient-record matching
- Resolving duplicate patient records
- Connecting hospital patient IDs to Continuum IDs
- Supporting record integrity

But whether this is a separate Continuum role or a function performed by an existing hospital role is **TBC**.

# 7 Patient Record

## 7.1 Patient Identity & Demographics

This section contains information used to identify the patient and establish their basic demographic profile.

**Patient identity**

- Full legal name
- Date of birth
- Gender
- Place of birth
- Place of residence
- Contact information
- Emergency contact information
- Government-issued identification number (e.g. national ID/passport) — **TBC**
- Continuum Health Patient ID — **system-generated**
- Hospital-specific patient ID — retained/linked where applicable

**Important design principle**

The **Continuum Health Patient ID will be separate from a hospital's internal patient ID**.

A patient should have one persistent Continuum Health identity that can remain associated with them throughout their healthcare journey, regardless of which participating healthcare facility they visit.

The system should be capable of associating a patient's Continuum Health ID with their patient identifiers at different healthcare facilities.

For example:

**Continuum Patient ID:** CH-XXXXXX  
↳ Hospital A Patient ID: XXXXX  
↳ Hospital B Patient ID: XXXXX  
↳ Hospital C Patient ID: XXXXX

The exact mechanism for linking these identifiers and exchanging information with hospital systems is **TBC** and will be addressed under interoperability/technical requirements.

## 7.2 Continuum Identity

Continuum Health will assign unique identifiers to entities using the platform.

***Patient***

Each patient will receive a **unique Continuum Health Patient ID**.

This ID:

- Is independent of any individual hospital's patient ID
- Remains associated with the patient's Continuum Health account
- Is intended to support portability of the patient's record between participating healthcare facilities
- Can be associated with hospital-specific patient identifiers

***Healthcare professional***

Each healthcare professional using Continuum Health will have a **unique Continuum Health Professional ID**.

The professional ID should be associated with:

- The individual professional
- Their professional role
- Their verified professional credentials
- Their authorized healthcare facility/facilities

The exact structure and verification process for Professional IDs is **TBC** and will be defined under **Identity, Authentication & Professional Verification**.

***Healthcare facility***

Each participating healthcare facility should have a **unique Continuum Health Facility ID**.

The Facility ID will allow Continuum Health to distinguish between participating hospitals/facilities and associate healthcare professionals with the facility where they are authorized to use the system.

The exact structure and management of Facility IDs is **TBC**.

## 7.3 Patient-Provided Information

A patient should be able to create an initial profile and provide relevant personal information themselves.

Patient-provided information may include:

- Name
- Date of birth
- Gender
- Place of birth
- Place of residence
- Contact information
- Emergency contact information
- Government-issued identification information — **TBC**
- Relevant self-reported medical information
- Patient care preferences
- Accessibility/care requirements

Patient-provided clinical information should be distinguishable from **clinically verified information**.

For example:

**Sickle Cell Disease — Patient reported / awaiting clinical verification**

versus:

**Sickle Cell Disease — Clinically verified**

The exact fields that patients can enter themselves versus those requiring professional verification are **TBC** and will be defined throughout the patient-record and permissions requirements.

## 7.4 Clinical Verification

Information within a patient's record should have an identifiable verification status where appropriate.

The system should distinguish between:

- Patient-reported information
- Clinician-documented information
- Clinically verified information
- Information requiring review/update

***Information identified for clinical verification***

Based on the current MVP concept, this may include:

- Primary chronic diagnosis
- Emergency/acute-care plan
- Allergies and medication reactions
- Current/ongoing treatment
- Other clinically relevant treatments
- Relevant medical history
- Other diagnoses

***Verification principle***

Clinical information should be verified by an **appropriately authorized healthcare professional**, rather than automatically requiring a physician for every type of information.

For example, different information may eventually be verified or entered by different authorized professional roles according to their scope of practice.

**The exact verification authority for each information category is TBC.**

## 7.5 Patient Care Preferences & Accessibility Needs

The patient should have a section within their profile where they can provide information about their preferences and requirements relating to their healthcare experience.

This may include:

- Treatment/care preferences
- Communication preferences
- Accessibility requirements
- Other information the patient wants healthcare professionals to be aware of

**Important distinction**

Patient preferences should remain distinguishable from **clinician-approved medical instructions or treatment plans**.

For example:

**Patient preference:** I prefer healthcare professionals to explain procedures before they are performed.

is different from:

**Clinician-approved emergency care plan:** Follow established emergency management plan.

The exact categories of patient preferences and accessibility information are **TBC**.

## 7.6 Emergency Summary

Continuum Health should provide a **rapid-access emergency summary** containing information that may be particularly relevant when a patient presents for acute/emergency care.

The information currently identified for consideration includes:

- Patient name
- Date of birth
- Age — **system-generated from DOB rather than necessarily stored separately**
- Gender
- Primary chronic diagnosis
- Relevant allergies and medication reactions
- Relevant ongoing/current treatments
- Other clinically relevant diagnoses
- Emergency/acute-care treatment plan
- Emergency/acute-care medications where applicable
- Relevant patient care preferences/accessibility requirements
- Short summary of relevant previous hospital stays/clinical encounters
- Treating physician/specialist and contact information where appropriate
- Emergency contact information
- Blood type — **TBC; inclusion and verification requirements to be determined**

**Important design principle**

The Emergency Summary should **not be a separate duplicate medical record**.

It should be a **clinically relevant, rapid-access view of information already contained within the patient's longitudinal record.**

This allows a healthcare professional to quickly see critical information without having to search through the patient's entire history.

## 7.7 Information That Should Not Be Included

Continuum Health should follow a **data minimization principle**.

The system should collect and retain information that is:

- Relevant to patient identification
- Relevant to providing or coordinating healthcare
- Relevant to continuity of care
- Relevant to patient safety
- Necessary for appropriate accountability/auditing
- Otherwise justified by the legitimate function of the system

Information should not be collected simply because it **could** be collected.

The exact categories of information that should be excluded from the MVP are **TBC** as the patient record and regulatory requirements are further developed.

## 7.8 Patient Record Updateability

Some information within the patient's profile will naturally change over time.

**Potentially patient-updatable information**

- Contact information
- Place of residence
- Emergency contact information
- Patient preferences
- Accessibility requirements
- Other appropriate demographic information

**Clinician-managed information**

Clinical information such as:

- Diagnoses
- Medical history
- Emergency care plans
- Allergies/medication reactions
- Current/ongoing treatment
- Treatment history
- Clinical notes

should be managed according to appropriate professional permissions.

**Record integrity**

Where authorized healthcare professionals amend clinical information, the system should retain an **audit trail of the change**, including:

- What was changed
- Who made the change
- When it was changed
- Previous information where appropriate
- Updated information

Clinical records should not be silently overwritten.

## 7.9 Patient Access & Control

This comes directly from what you originally proposed and **I would keep it in the PRD**, although the detailed implementation belongs in the permissions/security section.

Patients should be able to:

- View their own Continuum Health record
- View who has accessed their information
- View relevant access history
- Provide or deny consent where applicable
- Request an audit/investigation of access or changes they believe are inappropriate
- Request correction/review of information
- Manage appropriate patient preferences

***Account deletion***

**Patients may request account closure/deactivation, subject to applicable legal, regulatory and healthcare-record retention requirements.**

Whether information can actually be permanently deleted will need to be determined later.

## 7.10 Record Provenance & Auditability

Every clinically significant piece of information should ideally have identifiable provenance.

The system should be able to establish:

- Who entered the information
- When it was entered
- Which healthcare facility it came from
- Whether it was patient-reported or professionally documented
- Whether it has been clinically verified
- Who subsequently modified it
- When it was modified

This is particularly important because Continuum Health's value depends on healthcare professionals being able to **trust the information they are viewing**.

# 8 Patient Journey

## 8.1 Entry into the Continuum Health System

### 8.1.1 How can a patient first enter Continuum Health?

**Potential entry points:**

1. **After birth / first healthcare appointment**
    - An account may be opened for a newborn at their first healthcare appointment after birth.
    - The account would initially be operated by the parent or legal guardian.
    - The process for transferring control of the account to the patient when they reach adulthood will need to be defined.
2. **Patient-initiated registration**
    - A patient can download the Continuum Health application or access the web platform.
    - They can begin the process of creating their own account.
    - The account can undergo identity verification remotely if the patient has the required identification documents.
    - Clinical information remains clinically unverified until reviewed and verified by an authorized physician.
3. **Registration during a hospital visit**
    - A patient can have a Continuum Health account created during a hospital visit.
    - The account creation process would be completed with the patient and by an authorized hospital representative/healthcare professional.
4. **Existing Continuum Health patient**
    - A patient who already has an account does not need to register again when visiting another participating hospital.
    - They follow the hospital's normal registration process while their existing Continuum Health record can be identified and accessed according to the applicable access and consent requirements.
5. **Emergency presentation**
    - If a patient is unconscious or otherwise unable to participate in the identification/access process, an authorized healthcare professional may attempt to identify the patient within Continuum Health and request emergency access where the defined emergency-access conditions are met.
6. **Continuum Health awareness/registration initiatives**
    - Continuum Health representatives may assist potential patients with beginning the account-registration process.
    - Any account created through this process would remain subject to the appropriate identity and clinical verification requirements.
7. **Post-emergency/hospital enrolment**
    - A patient who receives care at a participating facility without an existing Continuum Health account may be offered the opportunity to create one after receiving emergency treatment or before/at discharge.

**Remaining decision: Which of these entry points will actually be supported in the MVP?**

## 8.2 Account Creation

**Example scenario**

**Patient with Sickle Cell Disease who has never used Continuum Health.**

Potential process:

1. Patient downloads the Continuum Health application.
2. Patient can alternatively access Continuum Health through a web browser.
3. Patient selects **New User / Create Account**.
4. Patient provides the required identifying and account information.
5. The system generates the patient's unique Continuum Health ID.
6. The patient submits the required information for identity verification.
7. The patient can complete identity verification remotely if they have the required accepted documentation.
8. Clinical information provided by the patient remains clinically unverified until reviewed by an authorized physician.
9. The patient receives confirmation when their account has been successfully created and their Continuum Health ID has been assigned.
10. The patient is notified when their identity and/or clinical information has been verified, according to the applicable verification process.

**Potential information provided during registration**

- Full name
- Date of birth
- Age — generated from date of birth
- Gender
- Contact information
- Place of birth
- Citizenship
- Emergency contact information
- Account type
- Primary chronic illness
- National ID/passport number or other approved identifier
- Password/PIN

**Potential optional information**

- Place of residence
- Certain contact information
- National ID/passport number, depending on the final identity-verification requirements

**Remaining decision: Required vs optional registration information.**

**Remaining decision: What forms of identification are acceptable?**

### 8.2.1 Account Status and Clinical Record Verification

Continuum Health should distinguish between:

**Identity verification**

Identity verification confirms that the Continuum Health account belongs to the person claiming it.

- Can potentially be completed remotely.
- Requires appropriate accepted identification/documentation.
- Does not require a physician.
- Once completed, the patient's identity is marked as verified.

**Account status**

The account status describes the state of the patient's Continuum Health account and should remain separate from the verification status of the patient's clinical information.

**Clinical record verification**

Clinical verification confirms that medical information within the patient's record has been reviewed and verified by an authorized physician.

Examples include:

- Primary chronic diagnosis
- Other diagnoses
- Allergies/medication reactions
- Ongoing treatment
- Treatment plans
- Emergency care plans
- Relevant medical history
- Other clinically relevant information

A patient may therefore have:

**A verified identity but a partially or entirely unverified clinical record.**

**Patient-provided medical information**

Information provided by the patient that has not yet been clinically verified should be clearly marked:

#### 8.2.1.1 UNVERIFIED / PENDING CLINICAL VERIFICATION

This distinction should remain visible to authorized healthcare professionals.

## 8.3 Building the Patient's Medical Record

Continuum Health begins building the patient's longitudinal record **from the point of enrolment**, while allowing relevant existing medical history to be incorporated where available and appropriate.

**Information initially provided by the patient**

Potentially:

- Basic identifying information
- Primary chronic diagnosis
- Allergies
- Ongoing treatment
- Treatment/care preferences
- Emergency contacts
- Relevant information for an emergency care plan
- Other patient-reported information

Medical information provided by the patient remains clearly identified as **unverified** until clinically reviewed where verification is required.

**Information added and verified by healthcare professionals**

Potentially:

- Diagnoses
- Treatment
- Prescriptions
- Ongoing treatment
- Emergency care plans
- Treatment plans
- Clinical notes
- Previous visit summaries
- Investigations and results
- Treatment responses
- Relevant hospitalizations

Treatment and care plans are:

- Created by the appropriate clinician
- Approved by the appropriate clinician
- Clinically verified by the appropriate clinician
- Updated by the appropriate clinician where necessary

Patients can participate in decisions where appropriate and can provide their care preferences and relevant patient input.

**Historical information**

Continuum Health does not require the patient's entire lifetime medical history to be reconstructed before an account can be used.

The system should begin building the patient's longitudinal record from enrolment while allowing relevant existing history to be incorporated where available and appropriate.

**Sickle Cell Disease pilot baseline**

For the initial SCD pilot, relevant historical information to establish the patient's baseline record may include:

1. SCD diagnosis
2. Important complications
3. Major hospitalizations
4. Known allergies
5. Relevant treatment history
6. Established emergency/care plans
7. Significant treatment responses

This baseline framework can be adapted when Continuum Health expands to other chronic illnesses.

**Historical records**

Questions to resolve:

- Can previous medical records be uploaded?
- Who can upload them?
- Who verifies them?
- How is the source of the record identified?
- How is information from an old record distinguished from information generated within Continuum?
- Is a complete historical record required?

**Working principle:** Missing historical information should not prevent a patient from having a Continuum Health account.

## 8.4 Patient's Normal Use of Continuum Health

Once appropriately verified, the patient can:

1. Log into their Continuum Health account.
2. View their patient record.
3. View their emergency summary according to their access permissions.
4. Update permitted personal information.
5. Update their care preferences.
6. Provide or update permitted patient-reported information.
7. View their medical history.
8. View who has accessed their record.
9. Request an audit/review.
10. Request correction of information they believe is inaccurate.
11. Manage applicable consent and access preferences.

Patients should not directly edit official clinical information where doing so would alter the official clinical record.

Instead, they should be able to request corrections or provide additional information for clinical review.

## 8.5 Emergency Patient Journey

**Scenario**

**A patient with Sickle Cell Disease presents to the emergency department during an acute episode.**

Potential journey:

**Patient arrives at ED**  
↓  
**Patient identification**  
↓  
**Determine whether patient has a Continuum Health account**  
↓  
**Locate patient's Continuum Health record**  
↓  
**Authenticate/authorize access**  
↓  
**Clinician accesses relevant information**  
↓  
**Emergency information reviewed**  
↓  
**Patient assessed and treated**  
↓  
**Treatment documented**  
↓  
**Relevant record updated**  
↓  
**Patient continues care or is discharged**

**Emergency information**

The system should distinguish between:

**Verified emergency care plan**

- Clinically verified by an authorized physician.
- Available through the appropriate normal access pathway.
- Treated as verified clinical information.

**Patient-provided but unverified emergency information**

- Clearly labelled **UNVERIFIED**.
- Visible according to the applicable access rules.
- Clinician uses professional judgement regarding whether/how it should inform care.

**No emergency plan/information**

- Clinician proceeds according to normal clinical practice.

Continuum Health should communicate the verification status of information but should not make the clinical decision about whether an unverified record should be used.

### 8.5.1 Emergency Access Scenarios

**Scenario A — Patient can provide consent**

- Physician obtains the appropriate initial access.
- The emergency plan can be viewed without requiring additional consent.
- Additional access to other portions of the medical record follows the applicable consent requirements.

**Scenario B — Patient refuses access**

If the patient refuses access to their Continuum Health account:

- The physician should consider the circumstances and clinical necessity.
- If the information is clinically necessary, emergency access can be requested.
- The professional must provide a stated reason for emergency access.

If the patient has refused access to additional portions of their record:

- Their preference should normally be respected.
- If the information becomes clinically necessary during an emergency, emergency access may be requested.
- The reason for accessing the information must be recorded.

**Scenario C — Patient cannot provide consent**

For example, the patient is unconscious or otherwise unable to provide consent:

1. Patient is identified.
2. Authorized professional requests emergency access.
3. Reason for emergency access is recorded.
4. Access is granted according to the emergency-access rules.
5. Access is fully recorded in the audit trail.

**Scenario D — Identity verified but clinical record is unverified**

- The clinician can see that the clinical information is unverified.
- The clinician uses professional judgement regarding whether/how to use it.
- Continuum Health clearly communicates the verification status.
- Continuum Health does not make the clinical decision.

#### 8.5.1.1 Emergency Patient Identification

If the patient cannot communicate, potential identification methods include:

- Personal identification documents
- Continuum Health ID
- Other approved patient identifiers
- Biometrics
- Emergency-contact information
- Other hospital identification mechanisms

If the patient does not remember their Continuum Health ID, the system should provide an alternative method of locating their account using approved identifying information.

**Remaining decision: the exact emergency identification mechanism and acceptable identifiers will be finalized during technical, clinical and legal design.**

#### 8.5.1.2 Patient Cannot Be Found in Continuum Health

If the hospital cannot find the patient's Continuum Health record:

- Treatment and care should continue regardless.
- Continuum Health should not become a prerequisite for receiving treatment.
- The hospital should follow its normal clinical and patient-identification procedures.
- A Continuum Health administrator or appropriate technical support process may be contacted to investigate the issue.

If only part of the patient's record is unavailable:

- The system should clearly indicate what information is available.
- The clinician should use available information according to professional judgement.

## 8.6 Routine / Ongoing Care

For a routine visit:

**Patient arrives**  
↓  
**Patient identified**  
↓  
**Continuum account located**  
↓  
**Healthcare professional requests appropriate access**  
↓  
**Patient provides applicable consent**  
↓  
**Clinician accesses authorised information**  
↓  
**Consultation occurs**  
↓  
**Relevant information is documented**  
↓  
**Record is updated**  
↓  
**Patient leaves/continues care**

Potential updates include:

- Diagnosis
- Ongoing treatment
- Treatment plans
- Investigations
- Allergies
- Emergency care plan
- Clinical notes
- Relevant advice
- Treatment administered

Old information should remain available as historical information rather than simply being overwritten.

## 8.7 Patient Visits Another Participating Hospital

The intended experience should remain substantially the same regardless of the participating healthcare facility:

**Arrival**  
↓  
**Identification**  
↓  
**Continuum account located**  
↓  
**Access requested**  
↓  
**Consent/authorization**  
↓  
**Relevant patient information accessed**  
↓  
**Patient assessed**  
↓  
**Treatment provided**  
↓  
**Treatment documented**  
↓  
**Record updated**  
↓  
**Encounter becomes part of longitudinal history**

The Continuum Health record should remain independent of an individual hospital's patient number.

The system should eventually allow the patient's Continuum ID to be associated with identifiers used by different participating healthcare facilities.

**Potential patient profile information**

The patient may have:

- Primary healthcare facility
- Primary clinician/physician
- Preferred healthcare facility
- Preference regarding whether their primary facility/clinician should be notified when receiving care elsewhere

**Future development: cross-hospital interoperability beyond the initial pilot.**

## 8.8 End of Healthcare Encounter

At the end of an encounter, the system should capture the relevant activity associated with the patient's record.

This may include:

- Healthcare encounter
- Healthcare facility
- Healthcare professionals who accessed the record
- Information accessed
- Access method/reason
- Information added or updated
- Treatments documented
- Investigations/results added
- Changes to care plans
- Changes to emergency care plans
- Relevant patient consent/access decisions

The encounter should become part of the patient's longitudinal medical history.

The patient should be notified of relevant updates/changes according to the final notification rules.

### 8.8.1 Audit Trail / Patient Account Activity

Every interaction with a patient's Continuum Health record should be traceable through a chronological activity log.

The system should capture, where applicable:

- Login/session initiation
- Identity/authentication
- Patient record accessed
- Information viewed
- Information added
- Information edited
- Information updated
- Information uploaded
- Information accessed through emergency privileges
- Access requests
- Access approvals/denials
- Consent actions
- Relevant reasons for access
- Session end/logout

Each activity should be associated with relevant information such as:

- Who performed the action
- Date and time
- Authorized healthcare facility
- Type of action
- Information involved
- Reason where required

The objective is to allow an auditable chronological history of activity on the patient's account.

#### 8.8.1.1 Emergency Care Plan Review

The emergency care plan should not become permanently static.

Questions to resolve:

- How frequently should it be reviewed?
- Who is responsible for reviewing it?
- Does every emergency visit trigger a review?
- Does a major change in treatment trigger a review?
- Should the patient be notified when it changes?

**Potential review interval:** 3–6 months.

**Decision still needed.**

#### 8.8.1.2 Conflicting or Incorrect Information

If a patient reports information that differs from the existing clinical record:

1. The discrepancy should be identified.
2. The relevant healthcare professional should review the information.
3. The information should be clinically verified where necessary.
4. If the patient-provided information is confirmed, the appropriate record should be updated.
5. Previous information should not simply disappear; changes should remain traceable.

For treatment plans and emergency care plans, the responsible healthcare professional retains clinical judgement.

**Core principle**

**Continuum Health should support clinical judgement, not replace or restrict it.**

#### 8.8.1.3 Patient Preferences and Participation in Care

The patient should be able to provide and manage their healthcare preferences within the areas designated for patient input.

This may include:

- Care preferences
- Communication preferences
- Relevant accessibility requirements
- Patient input into emergency-care information
- Other preferences determined to be appropriate for the system

Patient preferences should not override clinical judgement or clinical safety requirements.

Treatment and care plans are created, approved and clinically verified by the appropriate healthcare professional, while the patient participates in decisions where appropriate.

#### 8.8.1.4 Children and Guardians

Potential entry point:

- An account may be created for a child after birth or during childhood.
- The parent or legal guardian initially manages the applicable account access.
- The child's clinical record develops over time.
- The process for transferring control/access to the patient when they reach adulthood must be defined.

**Remaining decision:**

- What happens to the guardian's access when the patient turns 18?
- How is the patient's identity re-verified?
- Which information remains accessible to the guardian?
- Does the patient need to establish independent credentials?

## 8.9 Failure Points / What Could Go Wrong

**Patient identification**

- Two patients with the same name
- Patient has no identification documents
- Patient cannot communicate
- Patient is unconscious
- Patient information is incorrect
- Patient is a child without a parent/legal guardian
- Patient does not remember their Continuum ID

**Record availability**

- Patient's record cannot be found
- Record is incomplete
- Clinical record is unverified
- Important historical information is missing
- Emergency plan is outdated
- Conflicting records exist

**Consent and access**

- Patient refuses access
- Patient cannot provide consent
- Clinician is not authorised
- Emergency access is required
- Appropriate access takes too long

**Technology**

- Internet unavailable
- Electricity unavailable
- Continuum unavailable
- Hospital has no digital system
- Hospital system cannot connect to Continuum
- Patient has no phone

**Patient circumstances**

- Language barrier
- Child reaches adulthood
- Patient becomes deceased
- Patient has been inactive for a long period

## 8.10 Core Principles Emerging from the Patient Journey

**Continuum should support care, not become a barrier to care.**

A patient should not be denied or unnecessarily delayed treatment because Continuum is unavailable, inaccessible, incomplete, or because the patient does not have an account.

**The patient's record should remain longitudinal.**

Information should build over time rather than being replaced every time the patient changes hospitals.

**Identity and clinical verification should be distinct.**

A patient's identity can be verified independently from the verification status of their clinical information.

**Clinical information should have a clear verification status.**

The system should distinguish between patient-reported, clinically verified, and potentially outdated information.

**Emergency access must exist.**

A patient should not need to be conscious and able to provide consent for clinically necessary emergency access to be possible.

**Every interaction should be accountable.**

The system should maintain an auditable chronological record of activity on the patient's account and medical record.

**Continuum should communicate information status, not make clinical decisions.**

The platform provides information and continuity while healthcare professionals retain responsibility for clinical judgement.

**Patient-centered does not mean clinician-replacing.**

Patients should have visibility, participation and control over appropriate aspects of their information and care preferences while clinical decisions remain with qualified healthcare professionals.

# 9 Clinician Journey

## 9.1 Physician Journey

A patient arrives at the hospital and requires clinical assessment.

The physician logs into Continuum Health using their **professional account**, not the patient's account. The physician is authenticated through their Continuum Health professional credentials and their active hospital affiliation.

Each healthcare professional has one unique Continuum Health Professional ID. Their professional account is linked to their professional role, professional registration/licensing information, and hospital affiliation(s). A hospital will also have a unique Continuum Health facility code. A professional's Continuum ID remains the same across hospitals, while their active hospital affiliation identifies the facility from which they are accessing the system.

Once authenticated, the physician can search for a patient using approved patient identifiers.

### 9.1.1 Finding a Patient

A clinician can search for a patient using:

- Continuum Health ID
- Government-issued identification where applicable
- Name and date of birth
- Approved biometric identification
- Other approved identifying information

Name should be used together with date of birth to reduce the likelihood of identifying the wrong patient.

If the patient does not remember their Continuum Health ID and other identification methods are unsuccessful, the system may allow patient-assisted verification through an OTP sent to the patient's registered contact information, where appropriate.

If the patient is unconscious or otherwise unable to participate and has no identification available, an approved biometric search may be used where the hospital and Continuum Health system support it.

If the patient's account cannot be found after the available identification and search methods have been exhausted, the clinician should proceed with treatment without Continuum Health. The incident should be recorded and the Continuum Health Administrator contacted to investigate the issue.

#### 9.1.1.1 Search/Find vs Basic Clinical Access

Searching for and locating a patient should be separate from accessing their clinical information.

**Search/Find**

Before clinical access is granted, the clinician should only be able to see enough information to confirm that the correct patient has been located.

This may include:

- Name
- Date of birth
- Age
- Gender
- Continuum Health ID
- Identity verification status

**Basic Clinical Access**

Once the clinician has been authenticated and granted the first level of access, they may view the patient's basic clinical information necessary to orient themselves and provide immediate care.

This may include:

- Patient identification information
- Primary chronic diagnosis
- Allergies
- Ongoing treatment
- Verified emergency care plan
- Last hospital encounter/visit
- Primary hospital and physician, where applicable
- Identity verification status
- Clinical record verification status

The verified emergency care plan should be available as part of basic clinical access and should not require an additional consent request once the clinician has received this initial authorized access.

Any patient-provided emergency information that has not yet been clinically verified must be clearly labelled as **unverified**. If there is no verified emergency care plan, the clinician should proceed according to normal clinical practice.

**Clinical Access**

Clinical access occurs after the appropriate consent and authorization process.

Once access is granted, the physician may view the relevant parts of the patient's longitudinal record, including:

- Medical history
- Previous hospitalizations
- Previous clinical encounters
- Relevant clinical notes
- Treatment history
- Treatment responses
- Test and investigation summaries
- Previous medical summaries
- Relevant past encounters

Access should be limited according to the clinician's role and the permissions granted.

Where additional or restricted information is required, the clinician may request access to the specific record or category of information.

**Restricted/Sensitive Information**

Certain categories of information may require specific consent or additional authorization.

Potential examples include:

- Mental health records and encounters
- Reproductive health records and encounters
- Detailed historical records
- Detailed investigation or test records
- Detailed notes from other healthcare professionals
- Other information determined to require additional protection

The exact categories of restricted information and the consent requirements for each will be defined under **Consent & Access**.

### 9.1.2 Physician Record Review

Once the physician has the appropriate access, the record should allow them to quickly understand the patient's relevant clinical picture.

**Immediately visible information**

The physician should be able to quickly view:

- Primary chronic diagnosis
- Important complications
- Allergies
- Ongoing treatment
- Verified emergency care plan
- Relevant treatment responses
- Most recent/last encounter

**Information available through the record**

The physician may open and search for:

- Previous hospitalizations
- Previous clinical notes
- Relevant test results and investigation summaries
- Relevant treatment history
- Previous encounter summaries
- Other clinically relevant medical history

The system should prioritize clinically relevant information without requiring the physician to search through the patient's entire history before providing care.

### 9.1.3 What a Physician Can Do

A physician may have authority to:

- View authorized patient information
- Add clinical notes
- Add diagnoses
- Update diagnoses
- Add and update ongoing treatment
- Add and update treatment plans
- Add and update emergency care plans
- Add and update allergy information
- Add visit summaries
- Record relevant clinical findings
- Record treatment administered
- Add clinical interpretations or summaries of investigations
- Verify patient clinical information
- Review information submitted by other professionals
- Request additional access
- Request emergency access where necessary

Clinical information added or changed by a physician should be attributable to the specific physician and subject to the appropriate verification and audit requirements.

Original laboratory results should not simply be overwritten. Where an error is identified, the appropriate professional should be able to request or make a correction through a process that preserves the original record and the audit trail.

## 9.2 Nurse Journey

Nurses will have access appropriate to their role and responsibilities.

**Nurse access**

A nurse may have access to:

- Basic patient information
- Primary chronic diagnosis
- Allergies
- Ongoing treatment
- Treatment plan
- Emergency care plan
- Other information necessary for their role and authorized level of access

A nurse should not automatically have access to the patient's complete longitudinal medical history, detailed clinical notes, or restricted information unless specifically authorized.

**Nurse actions**

A nurse may:

- Record treatment or medication administered
- Add relevant nursing information
- Add a short summary of the nursing encounter where appropriate
- Request additional access where necessary
- Request emergency access where clinically necessary

Information entered by a nurse that requires clinical verification should be clearly identified as pending verification until reviewed by an authorized physician or other appropriate professional.

During an emergency, where a physician is not immediately available, an authorized nurse may request emergency access according to Continuum Health's emergency access rules.

## 9.3 Laboratory Professional Journey

Laboratory professionals will have access limited to information necessary for their laboratory responsibilities.

A laboratory professional may:

- Log into their professional account
- Search for an authorized patient
- Request access to the relevant patient information
- Access information necessary to perform the required test
- Upload laboratory tests and results
- Update or correct laboratory information through an appropriate correction/review process

Laboratory professionals should not automatically have access to the patient's complete medical record.

Original laboratory results should remain part of the patient's longitudinal record and should not simply be deleted or overwritten. If a result is identified as incorrect, false, or otherwise requiring review, the laboratory professional should be able to flag the result and request a review or correction while preserving the original audit trail.

Once a laboratory result has been appropriately uploaded and verified, authorized clinicians should be able to view the result according to their access permissions.

The exact role and permissions of pharmacy professionals remain **TBC** while Continuum Health determines how medication information will be managed.

### 9.3.1 Emergency Access Workflow

Emergency access is intended to ensure that Continuum Health does not prevent or unnecessarily delay treatment when normal consent or access processes cannot reasonably be completed.

Emergency access should be governed by predefined Continuum Health system rules rather than requiring a hospital or Continuum administrator to manually approve every emergency request.

The system should automatically record and flag emergency access for appropriate administrator oversight and later review.

**Scenario A — Patient Can Consent**

1. Patient is identified.
2. Clinician authenticates into their professional account.
3. Clinician requests the appropriate access.
4. Patient provides the required consent.
5. Access is granted.
6. Clinician reviews the relevant information.
7. Treatment is provided.
8. Treatment and relevant clinical information are documented.
9. The encounter and access activity are recorded.
10. Clinician ends the patient session.

**Scenario B — Patient Refuses Access**

If a patient refuses access to their record, their decision should generally be respected.

However, if the clinician determines that specific information is clinically necessary and the situation meets Continuum Health's emergency access criteria, the clinician may request emergency access.

The clinician must provide the reason for the emergency access request.

The system should determine whether the request meets the predefined emergency access rules. If approved, access should be limited to the information necessary for the stated emergency purpose.

If emergency access is not justified, or if Continuum Health cannot be used, the clinician should proceed with treatment according to normal clinical practice.

**Scenario C — Patient Cannot Consent**

Where a patient is unconscious or otherwise unable to provide consent:

1. The clinician attempts to identify the patient using available approved identification methods.
2. The clinician locates the patient's Continuum Health account where possible.
3. The clinician requests emergency access.
4. The clinician provides the reason for the request.
5. The system evaluates the request according to predefined emergency access rules.
6. If approved, the clinician receives access to the information necessary for the emergency.
7. Treatment proceeds.
8. All access and actions are recorded.
9. The patient is notified when appropriate after the emergency.
10. The emergency access is available for administrator oversight and later review.

**Scenario D — Identity Verified but Clinical Record Unverified**

If the patient's identity is verified but their clinical information has not yet been clinically verified, the clinician should be clearly shown that the clinical record is **unverified**.

The clinician may use their professional judgement to determine whether the available information is useful.

Continuum Health should clearly distinguish verified information from patient-provided or otherwise unverified information.

An unverified clinical record should not be treated as equivalent to a verified clinical record.

Emergency access should not be used as a mechanism to verify the patient's clinical record.

#### 9.3.1.1 What Happens During Emergency Access?

When emergency access is granted:

- The access is recorded
- The professional requesting access is recorded
- The hospital/facility from which access occurred is recorded
- The reason for emergency access is recorded
- The information accessed is recorded
- The time of access is recorded
- The actions performed are recorded
- The session end is recorded
- The patient is notified when appropriate
- The access is available for appropriate administrator oversight and later review

Emergency access should provide only the information necessary for the emergency situation and should not automatically unlock the patient's entire record.

### 9.3.2 End-of-Encounter Workflow

At the end of a clinical encounter, the relevant information should be documented in the patient's longitudinal record.

**Required documentation**

Depending on the type of encounter, the clinician should document:

- Summary of the visit
- Relevant findings
- Treatments administered
- Relevant changes to diagnosis
- Changes to ongoing treatment
- Changes to treatment plans
- Changes to the emergency care plan where applicable

**Additional documentation**

Where relevant, the record may also include:

- Detailed consultation notes
- Admission information
- Procedures or surgeries
- Relevant investigations
- Additional diagnoses
- Relevant allergies
- Other clinically significant information

The patient's encounter summary, relevant findings, treatment administered, and applicable treatment plan should become part of their longitudinal medical record.

Historical information should remain accessible while older information is archived appropriately rather than deleted.

### 9.3.3 Audit and Attribution During the Clinical Journey

Continuum Health should capture significant activity throughout the clinician's interaction with a patient record.

This should include:

- Professional login
- Patient search
- Patient record access
- Additional access requests
- Consent requests
- Consent grants and denials
- Emergency access requests
- Emergency access approval
- Emergency access use
- Access to restricted information
- Information viewed where appropriate
- Information added
- Information updated
- Information edited
- Information uploaded
- Clinical verification
- Session start
- Session end/logout

Each relevant action should be attributable to the individual professional who performed it, their professional role, and the hospital/facility from which they accessed the system.

When the clinician ends the patient session, access to that patient's record should close and the clinician should return to their own professional account.

Where required documentation is incomplete, the system may remind the clinician to complete the required documentation before ending the patient encounter.

### 9.3.4 Clinical Journey — Failure and Exception Scenarios

Continuum Health should account for situations where the normal clinical journey cannot be completed.

**Patient cannot be found**

If the patient cannot be identified using available search and verification methods, the clinician should proceed with treatment without Continuum Health and report the incident to the appropriate Continuum Health Administrator.

**Duplicate patient appears**

The clinician should use additional approved identification methods, such as Continuum ID, government identification, or patient-assisted OTP verification, to determine the correct patient account.

**Patient record is incomplete**

During an emergency, the clinician should use their professional judgement and any available information.

Missing historical information should not prevent treatment.

During a routine encounter, the patient and clinician may continue building the record from the information available.

**Record is unverified**

During an emergency, the clinician may use professional judgement regarding whether available unverified information is useful.

During routine care, the clinical information should be appropriately verified by an authorized professional.

**Emergency plan is outdated**

The clinician should use professional judgement during an emergency.

During routine care, the emergency plan should be reviewed and updated where appropriate.

**Patient refuses access**

The patient's decision should generally be respected. Where clinically necessary and where the situation meets the emergency access criteria, the clinician may request emergency access and provide the required justification.

**Patient cannot consent**

The clinician should use the emergency access process.

**Clinician is not authorized**

Unauthorized professionals should not have normal access to Continuum Health. An emergency access mechanism for exceptional circumstances may be considered as a future development but is not part of the initial MVP unless specifically defined and approved.

**Internet connectivity is unavailable**

Continuum Health should not prevent treatment from proceeding when connectivity is unavailable. The patient should be treated according to normal clinical procedures and the encounter should be added to Continuum Health when access is restored.

The exact offline/fallback mechanism remains **TBC**.

**Continuum Health is unavailable**

The clinician should proceed with normal clinical practice and contact the appropriate Continuum Health Administrator or support channel to report the outage.

**Hospital system does not connect to Continuum Health**

The clinician should proceed with treatment according to normal hospital procedures and the issue should be reported to the hospital and Continuum Health administrators.

**Clinician accidentally accesses the wrong patient**

The clinician should immediately end the session and report the incident.

The system should record the incident and notify the appropriate parties according to the security and audit process.

**Clinician accesses information they should not have accessed**

Access should be recorded and the incident reported for review. Appropriate access controls should prevent continued access to information outside the clinician's permissions.

**Clinician requires restricted information**

The clinician should request the required consent or authorization.

If the information is clinically necessary and the situation meets emergency access criteria, emergency access may be requested with the reason clearly stated.

**Multi-Hospital Clinical Access**

Continuum Health is independent of any individual hospital's patient record system.

A patient's Continuum Health account remains the same regardless of which participating hospital they visit.

A clinician working at Hospital A and a clinician working at Hospital B may therefore access the same patient's Continuum Health record, provided they are appropriately authorized and have the required access.

A professional may have multiple hospital affiliations under one Continuum Health Professional ID.

When a professional accesses Continuum Health, the system should identify the active hospital/facility from which they are working so that the access and clinical activity can be appropriately attributed.

A professional's hospital affiliation should be removed or suspended when they no longer work at that facility.

If a professional's registration or license expires, their professional account should be suspended and they should not be able to search for or access patient records until their professional status has been appropriately renewed and verified.

If a professional account is suspected to be compromised, it should be reported and may be suspended pending investigation and resolution.

### 9.3.5 Clinician Journey — Remaining Decisions

The following areas require further definition:

- Exact information included in basic clinical access
- Exact categories of restricted/sensitive information
- Exact rules governing emergency access
- Exact system criteria for automatically approving emergency access
- Administrator oversight and review process
- Professional identity verification requirements
- Professional registration/licensing verification process
- Exact biometric identification process
- Multi-hospital access architecture
- Offline/fallback access
- Pharmacy role and permissions
- Exact rules for clinical verification
- Exact rules for correcting clinical information
- Patient notification requirements for different types of access and record changes
- Rules for child accounts and transition to adulthood
- Rules for deceased patient accounts
- Rules for long-term inactive accounts

# 10 Core Features

Continuum Health's core features are the functions required for the system to support the patient and clinician journeys defined for the initial Sickle Cell Disease (SCD) pilot. Features are divided between those required for the Minimum Viable Product (MVP), those intended for future development, and those that remain to be determined as the system is further designed and tested.

## 10.1 Patient Account Management — MVP

Continuum Health should allow patients to create, access, and manage their accounts.

Key capabilities:

- Patient account creation
- Patient account creation for minors
- Management of minor accounts by parents or legal guardians where applicable
- Transition of a minor account to an adult account when the patient reaches adulthood
- Generation of a unique Continuum Health Patient ID
- Patient account confirmation
- Patient login and logout
- Patient profile viewing
- Editing of permitted personal information
- Addition and management of patient care preferences
- Account deactivation/deletion requests
- Display of account verification status

## 10.2 Patient Identity & Verification — MVP

Continuum Health should allow a patient's identity to be established and verified separately from the verification of their clinical information.

Key capabilities:

- Patient identity verification
- Submission and upload of appropriate identity documents
- Verification of submitted identity information
- Linking of verified identity information to the patient's Continuum Health ID
- Display of identity verification status
- Notification of successful identity verification
- Future biometric registration, where supported
- OTP-based verification or account recovery where appropriate

## 10.3 Professional & Hospital Account Management — MVP

Continuum Health should support secure accounts for authorized healthcare professionals and participating healthcare facilities.

Professional account types for the initial system include:

- Physicians
- Nurses
- Laboratory professionals
- Hospital administrators

Key capabilities:

- Professional account creation
- Generation of a unique Continuum Health Professional ID
- Generation of a unique Continuum Health facility/hospital code
- Professional identity and credential verification
- Professional authorization
- Professional login and logout
- Future professional biometric registration, where supported
- Management of hospital/facility affiliations
- Recording of multiple professional affiliations where applicable
- Professional account suspension and reinstatement
- Removal of hospital affiliations

Pharmacy access and medication-management responsibilities remain **TBC**.

## 10.4 Patient Search & Identification — MVP

Continuum Health should allow authorized healthcare professionals to locate the correct patient account before requesting or receiving access to the patient's medical record.

Key capabilities:

- Patient search
- Search using the Continuum Health Patient ID
- Search using approved identifying information
- Search using appropriate government-issued identification where applicable
- OTP-based patient identification where appropriate
- Biometric patient identification where supported
- Emergency patient search
- Duplicate-patient safeguards
- Confirmation of patient identity before record access

Finding a patient account should be treated as separate from gaining access to the patient's clinical record.

## 10.5 Longitudinal Patient Medical Record — MVP

Continuum Health should create and maintain a longitudinal patient record beginning from the point of enrolment while allowing relevant existing medical history to be incorporated where available and appropriate.

The record should support the storage and organization of:

- Diagnoses and chronic conditions
- Important complications
- Allergies and medication reactions
- Current and ongoing treatments
- Relevant treatment history
- Previous hospitalizations
- Clinical encounters
- Treatment responses
- Clinician-approved treatment and care plans
- Emergency care information
- Relevant investigations and results
- Clinical notes
- Visit and encounter summaries
- Relevant healthcare professionals and facilities

Key capabilities:

- Creation of a longitudinal record
- Viewing of the record according to permissions
- Addition of relevant clinical information
- Updating of clinical information by authorized professionals
- Clinical verification of information
- Review and correction requests
- Archiving of previous information while maintaining appropriate historical access
- Recording the source and verification status of relevant information

## 10.6 Emergency Care Plan — MVP

Continuum Health should provide a dedicated emergency care plan containing clinically relevant information intended to support appropriate care during acute or emergency episodes.

Key capabilities:

- Patient provision of relevant emergency information
- Creation of an emergency care plan by an authorized physician
- Clinical verification of emergency care information
- Viewing of the verified emergency care plan according to the appropriate access level
- Updating and editing of the emergency care plan by authorized physicians
- Review of the emergency care plan
- Clear identification of verified and unverified emergency information
- Identification of outdated emergency information

Patient-provided medical information within an emergency plan should remain clearly marked as unverified until clinically reviewed and verified by an authorized physician.

## 10.7 Clinical Record Management — MVP

Continuum Health should allow authorized healthcare professionals to contribute to and maintain the patient's clinical record according to their professional role and permissions.

Key capabilities include:

- Adding clinical information
- Updating clinical information
- Editing information according to authorized permissions
- Adding diagnoses
- Updating diagnoses
- Adding and updating treatment plans
- Recording ongoing treatment
- Recording allergies
- Adding clinical notes
- Adding encounter summaries
- Recording treatment responses
- Recording treatment administered
- Uploading relevant clinical documents
- Uploading laboratory results by authorized laboratory professionals
- Reviewing clinical information
- Verifying clinical information
- Requesting review or correction of disputed information

The ability to add, edit, update, upload, or verify information should depend on the professional's role and permissions.

## 10.8 Access & Consent Management — MVP

Continuum Health should allow patients and healthcare professionals to manage access to patient information according to defined permissions and consent requirements.

Key capabilities:

- Patient consent management
- Requests for access to patient records
- Requests for access to specific records
- Patient approval or denial of access
- Access permissions based on professional role
- Access permissions based on record type
- Restricted access for sensitive information
- Emergency access requests
- Emergency access approval
- Recording of the reason for emergency access
- Limited permissions for emergency access where appropriate
- Patient notification of relevant access events
- Termination of patient-record access at the end of a session or encounter

## 10.9 Emergency Access Management — MVP

Because emergency care is a primary use case for Continuum Health, the system should provide a defined emergency access process for situations where normal consent or access procedures cannot be followed.

Key capabilities:

- Emergency patient identification
- Emergency access request
- Recording of the reason for emergency access
- System-based emergency access approval
- Appropriate emergency access permissions
- Access to the emergency care plan
- Access to other relevant information where authorized
- Recording of emergency access
- Notification following emergency access
- Administrator oversight and subsequent review
- Emergency access incident reporting

Emergency access should not remove the requirement for accountability. Emergency access events should remain subject to audit and later review.

## 10.10 Healthcare Encounter Management — MVP

Continuum Health should record individual healthcare encounters and incorporate relevant information from those encounters into the patient's longitudinal record.

Key capabilities:

- Creation of a healthcare encounter
- Identification of the healthcare facility
- Identification of the healthcare professional(s) involved
- Recording of encounter type
- Recording of findings
- Recording of treatment administered
- Recording of relevant investigations and results
- Recording of changes to diagnosis, treatment, or care plans
- Creation of a visit/encounter summary
- Closing of the encounter
- Addition of the completed encounter to the patient's longitudinal medical history

## 10.11 Laboratory Information Management — MVP

Continuum Health should allow authorized laboratory professionals to contribute relevant laboratory information to the patient's record.

Key capabilities:

- Laboratory professional account and permissions
- Access to information necessary to perform and document a relevant test
- Linking laboratory results to the correct patient
- Uploading laboratory results
- Verification of uploaded results
- Timestamping and attribution of laboratory results
- Flagging potentially incorrect or disputed results
- Requesting review of previously uploaded results
- Clinician access to verified laboratory results

Original laboratory results should not simply be overwritten. Corrections or disputes should preserve the record of the original result and the subsequent review.

## 10.12 Notifications — MVP

Continuum Health should notify patients and relevant authorized users of important account, verification, access, and security events.

Potential notifications include:

- Account creation confirmation
- Identity verification
- Clinical information verification
- Access requests
- Consent requests
- Relevant record updates
- Emergency access
- Relevant security events
- Account suspension or reinstatement

The exact notification rules will be finalized during the detailed consent, access and security design.

## 10.13 Audit & Activity Tracking — MVP

Continuum Health should maintain a comprehensive record of relevant activity occurring within a patient's account and clinical record.

The system should capture, where applicable:

- Login
- Logout/end of session
- Patient searches
- Patient record access
- Specific records accessed
- Access requests
- Consent requests
- Consent granted or denied
- Emergency access requests
- Emergency access approvals
- Emergency access use
- Information added
- Information updated
- Information edited
- Information uploaded
- Information verified
- Information reviewed
- Correction/review requests
- Account status changes
- Professional account status changes

Relevant activity should be associated with the responsible user/professional, facility, action, affected record, and timestamp.

## 10.14 Patient Audit & Record Review — MVP

Patients should be able to understand and request review of activity associated with their records.

Key capabilities:

- Viewing of relevant access history
- Viewing of who accessed the patient's information
- Audit requests
- Requests for review of disputed activity
- Requests for correction of inaccurate information
- Administrator review of flagged activity
- Review of emergency access
- Recording of actions taken following a review

## 10.15 Hospital & Continuum Administration — MVP

Continuum Health should provide administrative functions necessary to operate and support the system within participating healthcare facilities.

Hospital administrator capabilities include:

- Hospital onboarding
- Coordination of hospital-side implementation
- Coordination of professional affiliations
- Coordination with Continuum Health administrators
- Management of relevant hospital-side issues
- Participation in oversight and incident review

Continuum Health administrator capabilities include:

- Hospital onboarding and implementation support
- System administration
- Professional account administration
- Support for verification processes
- Incident management
- Emergency-access oversight and review
- System issue management
- Permission and account administration
- Pilot monitoring

## 10.16 Hospital System Integration — MVP

The initial pilot should test the practical integration of Continuum Health within one participating healthcare facility.

The pilot should explore and test:

- Connection between Continuum Health and the participating hospital's existing systems and workflows
- Linking of a patient's Continuum Health ID with their hospital patient identifier
- Access to Continuum Health from hospital workstations or other appropriate hospital systems
- How information is entered, updated, and accessed across both systems
- How professional authentication works within the hospital environment
- How discrepancies between Continuum Health and hospital records are identified and managed
- Appropriate pathways for transferring relevant information between systems
- Continuity of care when a patient moves between Continuum Health and the hospital's existing systems

The initial pilot should focus on practical integration with one hospital rather than attempting full interoperability with multiple healthcare systems.

## 10.17 System Reliability & Emergency Fallback — Remaining Decision

Continuum Health should have defined procedures for situations where the system, hospital system, internet connection, or electricity is unavailable.

Potential capabilities include:

- Emergency fallback procedures
- Patient identification fallback
- Access to essential emergency information during temporary system disruption
- Procedures for hospital-system connectivity failure
- Incident reporting when Continuum Health is unavailable

The exact technical mechanism for offline or fallback access remains a future design decision and will be determined through technical, security, and clinical design.

## 10.18 Future Development

The following capabilities are important to Continuum Health's long-term vision but are not required to prove the initial pilot concept:

- Multi-hospital interoperability at scale
- Cross-country and international interoperability
- Advanced data exchange between healthcare systems
- Broader patient populations beyond chronic illness
- Expansion beyond SCD to additional chronic illnesses
- Global patient record accessibility
- Advanced integration with national or regional health systems
- Expanded pharmacy functionality
- Additional healthcare professional roles
- Advanced biometric identification and authentication
- Broader offline functionality
- Advanced analytics and other future technologies

# 11 Identity & Verification

## 11.1 Patient Identity

Each patient will have a unique Continuum Patient ID that identifies their Continuum account and remains associated with them throughout their use of the system. The Continuum Patient ID will be separate from any hospital-specific patient number and will allow the patient's record to remain portable across participating healthcare facilities.

During account creation, the patient will provide basic identifying information, including:

- Full name
- Date of birth
- Gender
- Contact information
- Place of birth
- Citizenship
- Government-issued identification, passport or other accepted identification document
- Emergency contact information
- Primary chronic illness, where applicable

Age will be generated from the patient's date of birth rather than entered separately.

The system will generate the Continuum Patient ID during account creation. The Continuum Patient ID will be unique to one person and cannot be changed or reassigned.

The system will use multiple identifiers when locating a patient record rather than relying on name alone. Where patients have similar names or other identifying information, additional identifiers such as date of birth, government identification or Continuum Patient ID will be used to confirm the correct record.

### 11.1.1 Patient Identity Verification

Identity verification confirms that the person creating or accessing a patient account is the person they claim to be.

Identity verification may be completed remotely through the submission of an accepted identification document. A patient will not necessarily need to visit a hospital solely to verify their identity.

The requirements for acceptable identification documents and the verification process will be confirmed in accordance with applicable legal and regulatory requirements.

Identity verification and clinical verification are separate processes. A patient's identity may be verified while their clinical record remains unverified.

### 11.1.2 Patient Clinical Verification

Clinical verification confirms that information contained in the patient's medical record has been reviewed and verified by an authorized physician.

Patients may provide information about their medical history, diagnosis, allergies, treatment and care needs. Patient-provided clinical information will be clearly marked as unverified until it has been reviewed and verified by an authorized physician.

Only an authorized physician will be able to clinically verify medical information within the Continuum record.

Clinical verification may include verification of:

- Diagnosis and chronic conditions
- Allergies and medication reactions
- Treatment history
- Current or ongoing treatment
- Previous significant hospitalizations
- Important complications
- Treatment responses
- Emergency or care plans
- Other clinically relevant information

Where historical medical information is available, it may be incorporated into the patient's Continuum record by an authorized physician or Continuum Health administrator and subsequently validated by an authorized physician.

A patient does not need to have a complete historical medical record before their Continuum record can be established. The longitudinal record can continue to be built as the patient receives care through participating facilities.

### 11.1.3 Patient Account Status and Clinical Record Status

Continuum will maintain separate statuses for:

**Account status**

- Pending identity verification
- Identity verified
- Suspended
- Deactivated

**Clinical record status**

- Unverified
- Partially verified
- Clinically verified

This distinction ensures that verification of a patient's identity does not automatically mean that all information contained in their medical record is clinically verified.

## 11.2 Professional Identity

Healthcare professionals will have a unique Continuum Professional ID that identifies the individual professional and remains associated with their account.

A professional's Continuum Professional ID will not be tied permanently to one hospital because a professional may work at multiple participating healthcare facilities.

Professional information may include:

- Full name
- Date of birth
- Gender
- Contact information
- Professional role
- Professional registration/license information
- Continuum Professional ID
- Verified hospital/facility affiliation(s)
- Hospital-specific professional identification or credentials, where applicable

Professional identity verification will establish that the account belongs to the claimed individual.

### 11.2.1 Professional Authorization

Professional authorization determines whether a healthcare professional is permitted to access Continuum and what information or functions they are permitted to use.

Authorization will be based on factors including:

- Professional role
- Valid professional registration/license, where applicable
- Verified affiliation with a participating healthcare facility
- The professional's assigned permissions within Continuum

A professional may have more than one verified hospital affiliation.

Where a professional leaves a participating hospital, that hospital affiliation will be removed or deactivated without requiring the professional's Continuum Professional ID to change.

If a professional's required registration or license expires, their Continuum professional access may be suspended until the relevant registration is renewed and verified.

If a professional account is suspected to have been compromised, access may be suspended pending review.

## 11.3 Facility Affiliation

Hospital affiliation will be maintained separately from the Continuum Professional ID.

When a professional accesses Continuum while working at a participating hospital, the system will record the facility from which the professional is accessing the patient record.

This allows a professional to maintain one Continuum Professional ID while working across multiple participating facilities and allows each patient access event to be associated with the relevant facility.

## 11.4 Authentication

Authentication confirms that the person attempting to access an account is the account holder.

Patients will be able to authenticate using approved account credentials, such as their Continuum Patient ID or username and password. OTP-based authentication may also be supported.

Healthcare professionals will authenticate using their professional account credentials and may use additional authentication measures such as two-factor authentication.

Biometric authentication or identification may be considered in future versions of Continuum, particularly for emergency identification. It will not be a requirement for the initial pilot.

## 11.5 Role-Based Access

Access to Continuum will be based on the user's role and the information required for that role.

A user's ability to view, add, edit, verify or request access to information will therefore depend on their assigned professional role and permissions.

For example:

- Physicians may access and clinically verify relevant medical information and update clinical records.
- Nurses may access information required for nursing and emergency care and record care they have administered.
- Laboratory professionals may access the information required to perform laboratory services and add or update laboratory results.
- Hospital administrators will have operational responsibilities but will not have access to patients' clinical records unless specifically authorized under a defined role.
- Pharmacy permissions remain **TBC**.

The principle of minimum necessary access will apply: professionals should only access the information required for their role and the patient's care.

### 11.5.1 Verification of Information Added by Professionals

Information added to Continuum by a healthcare professional will be associated with the professional's identity, role and facility.

Where clinical verification is required, the relevant information will remain clearly identified as pending verification until reviewed by an authorized physician.

Professional roles will only be permitted to modify the areas of the record relevant to their responsibilities. For example, laboratory professionals will add laboratory results rather than edit previously verified clinical information outside their role.

### 11.5.2 Emergency Identification and Unverified Records

Where a patient presents for emergency care, the healthcare professional will attempt to identify the patient using the available identifiers and locate their Continuum record.

If the patient's identity can be sufficiently established but their clinical record is not fully verified, the unverified information will remain clearly labelled. Emergency access will not automatically convert unverified information into verified clinical information.

Clinical decisions will remain the responsibility of the treating healthcare professional.

If a Continuum record cannot be found or cannot be sufficiently identified, treatment will continue according to normal clinical procedures and will not be delayed solely because Continuum cannot be accessed.

## 11.6 Auditability of Identity and Access

All account and patient-record activity will be associated with the relevant user account.

The system will capture information such as:

- User identity and Continuum ID
- Professional role
- Facility/hospital affiliation
- Date and time of activity
- Patient record accessed
- Type of access or action performed
- Consent or access request associated with the action, where applicable
- Emergency access reason, where applicable
- Session start and end

Further audit requirements are defined under **Section 13: Security & Audit**.

# 12 Consent & Access

## 12.1 Purpose

Continuum Health will use a layered access model to ensure that patient information is available to authorized healthcare professionals when clinically necessary, while maintaining patient control over access to their medical information.

Access to a patient's Continuum Health account will not automatically mean unrestricted access to the patient's entire medical record.

The system will distinguish between:

- **Search & Find** — locating and identifying the correct patient account
- **Patient Access Authorization** — confirming that the patient authorizes the professional to proceed with access during a normal care encounter
- **Basic Access** — limited, predefined information available to an authorized healthcare professional after access authorization
- **Clinical Record Access** — broader access to the patient's medical record following appropriate patient consent
- **Restricted/Sensitive Access** — access to information requiring specific consent
- **Emergency Access** — a controlled exception to the normal consent process when information is clinically necessary and normal access or consent cannot be obtained

The purpose of this model is to balance **timely clinical access, patient autonomy, privacy, and clinical safety.**

## 12.2 Search & Find

Search & Find is the process through which an authorized healthcare professional locates a patient's Continuum Health account.

Search & Find does not provide access to the patient's clinical information.

A healthcare professional may search for a patient using available identifying information, including:

- Continuum Patient ID
- Name and date of birth
- Approved government identification where applicable
- Other approved identification methods
- Patient Access Authorization/OTP where required
- Biometrics in future versions where available and appropriately implemented

The system should use multiple identifiers where necessary to reduce the risk of selecting the wrong patient, particularly where patients have similar or identical names.

Once the correct patient account has been identified, the professional may proceed to the appropriate access process.

### 12.2.1 Patient Access Authorization

For normal care, finding a patient's account will not by itself provide access to their clinical information.

The patient should authorize the professional to proceed with access to their account.

This may be achieved through an OTP or another approved authentication/authorization mechanism.

The purpose of the OTP is to confirm that the patient is participating in and authorizing the access session.

The OTP should be treated as an **access authorization mechanism rather than clinical consent**.

Patient access authorization confirms that the professional may proceed to the patient's account. It does not automatically constitute consent to access every part of the patient's medical record.

Where a patient is unable to provide access authorization, the Emergency Access process may be used where clinically justified.

### 12.2.2 Basic Access

Following appropriate patient identification and access authorization, an authorized healthcare professional may receive Basic Access.

Basic Access is intended to provide sufficient information to understand the patient's immediate clinical context without exposing the patient's entire longitudinal record.

Basic Access may include:

**Patient information**

- Name
- Date of birth
- Age
- Gender where relevant
- Continuum Patient ID
- Identity verification status
- Clinical record verification status

**Essential clinical information**

- Verified primary chronic diagnosis
- Important complications
- Verified allergies and medication reactions
- Current/ongoing treatment
- Verified emergency care plan
- Relevant patient care preferences
- Most recent encounter or relevant recent encounter summary
- Primary healthcare facility and/or primary healthcare professional where applicable and where the patient has chosen to provide this information

The exact information available through Basic Access will be defined according to the professional's role and the clinical context.

Basic Access does not provide unrestricted access to the patient's complete medical history.

### 12.2.3 Clinical Record Access

Where a healthcare professional requires information beyond Basic Access, they may request access to the relevant portion of the patient's clinical record.

The patient may provide consent for broader access.

Clinical Record Access may include:

- Previous hospitalizations
- Previous clinical encounters
- Medical history
- Previous treatment history
- Treatment responses
- Previous clinical notes
- Relevant investigations and test result summaries
- Previous diagnoses
- Treatment plans
- Other clinically relevant information required for the patient's care

Access should be limited to information relevant to the professional's role and the patient's care.

Continuum Health should avoid requiring patients to approve every individual piece of information where a broader category of access is appropriate.

### 12.2.4 Restricted and Sensitive Information

Certain information may require additional or specific consent because of its sensitive nature.

Examples may include:

- Mental health diagnoses and encounters
- Reproductive health information
- Detailed clinical histories
- Detailed clinical notes
- Detailed investigation or test results
- Other information specifically classified as sensitive by the patient or according to applicable policy or law

A patient may request that certain records be classified as sensitive/restricted.

Access to restricted information should require specific authorization and/or consent according to the applicable access rules.

Where restricted information is clinically necessary during an emergency, the Emergency Access process may be used where justified.

### 12.2.5 Emergency Access

Emergency Access is a controlled exception to the normal consent and access process.

It is intended for situations where clinically relevant information is required and:

- The patient cannot provide consent or access authorization
- The patient is unconscious or otherwise unable to communicate
- The patient refuses access but the healthcare professional determines that specific information may be clinically necessary in an emergency
- Normal access procedures cannot be completed within the circumstances of the emergency
- Restricted information is required for immediate clinical decision-making

Emergency Access should not provide unrestricted access by default.

The healthcare professional requesting Emergency Access must provide a reason for the request and identify the information required.

Where possible, the system should approve access according to predefined emergency access rules. Administrator oversight and subsequent review should be used to ensure appropriate use.

Emergency Access should provide only the information necessary for the stated emergency.

**Emergency Access Scenarios**

**Scenario A — Patient can provide consent**

The normal access process applies:

**Search & Find → Patient Access Authorization → Basic Access → Consent for additional information where required → Treatment → Documentation → End session**

The patient may grant or deny access to additional parts of their record.

**Scenario B — Patient refuses access**

If a patient refuses access to their account, their decision should normally be respected.

However, where a healthcare professional determines that specific information is clinically necessary in an emergency, they may request Emergency Access and must provide the reason for the request.

The request and outcome will be recorded for subsequent review.

**Scenario C — Patient cannot provide consent**

If the patient cannot provide access authorization or consent, the healthcare professional may use the Emergency Access process.

The professional should first use available identifying information to locate the patient's account.

If the account is found and Emergency Access is approved, the professional receives the information permitted under the emergency access rules.

If the patient cannot be identified or the account cannot be located, treatment should continue according to normal clinical practice without Continuum Health.

**Scenario D — Patient identity is verified but clinical information is unverified**

Where the patient's identity is verified but their clinical record has not yet been clinically verified, the information must be clearly labelled as **Unverified**.

In an emergency, the clinician may use their professional judgement regarding whether the available information is useful.

Continuum Health should clearly communicate that unverified information should not be treated as confirmed clinical information.

Emergency Access cannot be used to convert or verify unverified clinical information.

Clinical verification must be completed separately by an authorized physician.

## 12.3 Access by Professional Role

Access will be role-based.

**Physician**

A physician may:

- Receive Basic Access
- View the patient's emergency care plan
- Request broader clinical record access
- Request access to restricted information where clinically necessary
- Add, update and edit appropriate clinical information
- Add and update diagnoses
- Add and update treatment information
- Add and update treatment plans
- Add and update emergency care plans
- Add and update allergies
- Add clinical notes and encounter summaries
- Upload relevant historical medical information
- Verify clinical information
- Request Emergency Access
- Access information granted through Emergency Access

All clinical information added or changed by a physician must be attributed to that physician and captured in the audit trail.

**Nurse**

A nurse may:

- Receive Basic Access appropriate to their role
- View the emergency care plan
- View relevant ongoing treatment and allergies
- View information necessary for their clinical responsibilities
- Record treatment administered
- Record relevant nursing information
- Add a short encounter summary where appropriate
- Request Emergency Access where necessary

Nurses should not independently modify verified diagnoses, treatment plans, emergency care plans or other physician-verified clinical information.

Any necessary changes should be referred for appropriate clinical review.

**Laboratory Professional**

A laboratory professional may:

- Access the patient's relevant identifying information
- Access the laboratory/test section required for their work
- Upload test results
- Update the status of tests/results where appropriate

Laboratory professionals should not have access to the patient's broader medical history unless specifically authorized according to their role and the applicable access rules.

Previously finalized test results should not simply be deleted or overwritten. Where a result is identified as incorrect, the system should preserve the original record and allow the result to be flagged for review or correction according to the applicable clinical governance process.

**Hospital Administrator**

A hospital administrator should have administrative access rather than clinical access.

They may:

- Manage the hospital's Continuum Health institutional setup
- Manage hospital-level Continuum configuration
- Monitor professional affiliations and institutional access
- Monitor Emergency Access requests and events
- Receive system and access-related alerts
- Coordinate with Continuum Health administrators
- Assist with institutional issues and incidents
- Participate in appropriate review of Emergency Access events

A hospital administrator should not have access to a patient's clinical record solely because they hold an administrative role.

Patient clinical information should remain inaccessible unless the individual also holds an appropriately authorized clinical role.

**Continuum Health Administrator**

The Continuum Health Administrator may:

- Manage Continuum Health system-level administration
- Manage institutional onboarding and configuration
- Support participating hospitals
- Review system incidents
- Review Emergency Access activity where required
- Manage professional account status and suspension
- Support access and authorization issues
- Coordinate investigations of inappropriate access
- Manage system-level permissions according to defined governance rules

Continuum Health administrators should not routinely access patient clinical information unless their specific role and circumstances require it and such access is appropriately authorized and audited.

## 12.4 Patient Control Over Access

Patients should have meaningful visibility and control over access to their information.

Patients can:

- View their own medical record
- View who has accessed their account
- View the healthcare facility associated with an access event
- View relevant access history
- Manage consent for broader record access
- Request an audit or review
- Request correction or review of information
- Request that certain information be classified as sensitive/restricted
- Receive notifications regarding significant access or changes to their record

Patients cannot directly edit verified clinical information.

They may request that information be reviewed, corrected or updated by an appropriately authorized healthcare professional.

Patients may update their basic profile information and care preferences within the permissions provided by the system.

### 12.4.1 Access Across Healthcare Facilities

Continuum Health is not intended to permanently attach a patient's record to one healthcare facility.

A patient's Continuum Health account is independent of individual hospital patient numbers.

Where a patient visits another participating healthcare facility, an appropriately authorized professional at that facility should be able to locate the patient's Continuum Health account and follow the same access, authorization, consent and emergency access processes.

This allows the patient's longitudinal record to follow them across participating healthcare facilities while maintaining appropriate access controls.

The system should record the healthcare facility from which each access event occurs.

### 12.4.2 End of Access Session

Access to a patient's account should be treated as a defined session.

At the end of the encounter, the professional should:

1. Complete required clinical documentation.
2. Record relevant treatment and findings.
3. Save any appropriate updates to the patient's record.
4. End the patient access session.
5. Return to their professional account.
6. Log out of their professional account when their work session is complete.

The patient's account should not remain open after the professional ends the patient session.

All access, changes and relevant actions will be captured in the system audit trail.

# 13 Security & Audit

## 13.1 Security, Privacy & Audit

### 13.1.1 Purpose

Continuum Health must protect the confidentiality, integrity and availability of patient information while ensuring that access to patient records is controlled, appropriate and traceable.

Finding a patient on the system must not automatically mean having access to their medical record. Patient identification, basic access, clinical access, consent and emergency access must remain separate stages of the access process.

Every action taken on a patient account must be attributable to the person who performed it and recorded in the system.

### 13.1.2 Confidentiality & Privacy

Patient information must only be accessible to authorized users and according to their role and level of access.

The system must:

- Require secure authentication for patients and healthcare professionals.
- Apply role-based access controls.
- Limit patient searches to the minimum information required for identification.
- Ensure that searching for a patient does not automatically expose their medical record.
- Require patient authorization for basic account access where applicable, including OTP confirmation.
- Require appropriate consent before broader access to the medical record.
- Apply additional controls to sensitive or restricted information.
- Allow emergency access when clinically necessary and when normal consent cannot be obtained or has been denied, subject to the emergency access process.
- Ensure that access is limited to information necessary for the user's role and purpose.
- Protect information while being stored and transmitted.
- Control access to active sessions and prevent unauthorized use of accounts.

An OTP used to authorize basic access is not considered equivalent to consent to access the patient's full medical record.

### 13.1.3 Data Integrity

Patient information must remain accurate, traceable and protected from unauthorized modification.

The system must:

- Record who entered, uploaded, edited or verified information.
- Clearly distinguish verified clinical information from information that has not yet been clinically verified.
- Ensure that clinical information requiring verification is reviewed and verified by an authorized physician.
- Prevent unauthorized users from altering clinical records.
- Maintain a traceable history of significant changes to records.
- Allow patients to request review or correction of information where they believe it is inaccurate.
- Preserve previous information in a traceable form rather than silently replacing historical records.

Patient-provided clinical information must remain clearly labelled as unverified until it has been clinically reviewed.

### 13.1.4 Role-Based Access

Access to patient information must be based on the user's role and the minimum information required to perform their responsibilities.

**Physician**

Physicians may:

- Access the patient's basic profile after appropriate authorization.
- View the emergency care plan.
- View relevant clinical information according to consent and access permissions.
- Verify clinical information.
- Add, edit and update clinical records.
- Add or incorporate relevant historical information.
- Update diagnoses, treatment information, allergies and care plans.
- Request additional access where required.
- Request emergency access where clinically necessary.

**Nurse**

Nurses may:

- Access the patient's basic profile and emergency information.
- View information relevant to the patient's care.
- Record administered treatment and relevant nursing information.
- Add short clinical or nursing summaries where appropriate.
- Request review or revision of information that requires physician input.
- Request emergency access where necessary.

Nurses should not have unrestricted access to the patient's entire medical history by default.

**Lab Professional**

Lab professionals may:

- Access the information necessary to identify the patient.
- Access the patient's tests and results section.
- Upload or add new laboratory results.
- Flag or request review of a potentially incorrect result.

Lab professionals should not silently alter previously recorded laboratory results.

**Hospital Administrator**

Hospital administrators may:

- Access basic identifying information required for administrative functions.
- Coordinate the hospital's participation and integration with Continuum Health.
- Monitor emergency access requests and provide administrative oversight.
- Coordinate system-related issues with the Continuum Health Administrator.

Hospital administrators must not have access to the patient's clinical record unless a separate authorized clinical role applies.

**Continuum Health Administrator**

Continuum Health Administrators may:

- Oversee system rollout and operation at participating facilities.
- Coordinate technical or operational issues.
- Monitor system activity for administrative and security purposes.
- Review audit information where required.
- Support the investigation of access or security incidents.

Administrative access must not automatically provide access to patient clinical information.

### 13.1.5 Sensitive & Restricted Information

Certain information may require additional access controls.

This may include:

- Mental health information.
- Reproductive health information.
- Patient-requested sensitive records.
- Other information identified by Continuum Health policy as requiring restricted access.

Sensitive information should require specific consent or appropriate authorization before access.

Where sensitive information is clinically necessary during an emergency, a healthcare professional may request emergency access in accordance with the emergency access process.

The detailed classification and access rules for sensitive information will be further developed as part of the system's policy and technical design.

### 13.1.6 Emergency Access

Emergency access is intended for situations where a healthcare professional believes that access to information is necessary for patient care and normal consent cannot be obtained or has been denied.

The system must:

- Require the healthcare professional to provide a reason for requesting emergency access.
- Record the professional, facility, time and information accessed.
- Limit emergency access to information relevant to the emergency.
- Clearly identify that the access occurred under emergency provisions.
- Notify the appropriate administrator for review.
- Make emergency access visible to the patient through their access history where appropriate.
- Maintain a complete audit trail of the emergency access.

For the pilot, emergency access may be automatically approved by the system once the required conditions and reason have been provided, with administrative review afterwards.

A future version may consider a human-and-system approval process for certain emergency access situations.

Emergency access must not allow a physician to treat unverified clinical information as verified. Clinical verification remains a separate process.

### 13.1.7 Session Controls

Every interaction with a patient record should form part of a traceable user session.

The system should record, where applicable:

- Login/session start.
- Professional identity and role.
- Hospital or facility affiliation.
- Date and time of access.
- Patient record accessed.
- Information viewed.
- Access or consent requests.
- Emergency access requests.
- Information added, edited or updated.
- Clinical verification actions.
- Session end/logout.

Sessions should be controlled to reduce the risk of unauthorized access after a user has finished working with a patient record.

### 13.1.8 Audit Trail

Continuum Health must maintain an audit trail of significant activity involving patient records.

The audit trail should capture:

- Who accessed the record.
- When the record was accessed.
- Which facility the user was associated with.
- What type of access occurred?
- What information was viewed.
- What information was added, edited or updated.
- Consent given, denied or changed.
- Emergency access requests and approvals.
- Verification actions.
- Significant security or access events.
- End of session where applicable.

Audit information must be protected from unauthorized alteration.

### 13.1.9 Patient Audit Visibility

Patients should be able to see who has accessed their information and when.

The patient should have access to:

- A summary of recent access activity.
- The professional or role that accessed their information.
- The facility associated with the access.
- The type of access.
- Emergency access events.
- Significant changes made to their record.

Patients may request a more detailed audit where they want to understand exactly what information was accessed or what action was taken.

The level of detail visible to patients may be refined during the technical and policy design stages.

### 13.1.10 Accountability & Notifications

All activity involving patient information must be attributable to a specific user account.

The system should notify patients of significant activity involving their records, including where appropriate:

- Significant changes to their clinical information.
- Changes to their emergency care plan.
- Significant access events.
- Emergency access to their record.
- Other security or account events requiring patient awareness.

Emergency access should also trigger an administrative notification for review.

### 13.1.11 Availability & Continuity of Care

Continuum Health should be designed to support availability of patient information when it is needed, but the system must never become a prerequisite for receiving medical care.

If:

- The Continuum system is unavailable.
- Internet connectivity is unavailable.
- Hospital integration is unavailable.
- A patient record cannot be found.
- A patient's identity cannot be sufficiently established.

the healthcare professional must continue providing care according to normal clinical procedures.

The pilot should identify and test an appropriate fallback approach for situations where Continuum cannot be accessed. A fully functional offline emergency system does not need to be implemented in the initial pilot unless it is technically and operationally feasible.

### 13.1.12 Security Incidents

If a patient record is accessed incorrectly or by the wrong person:

- The session should be ended as soon as the issue is identified.
- The incident must be recorded.
- The relevant access must be included in the audit trail.
- The patient should be notified where appropriate.
- The incident should be reviewed by the appropriate administrator.
- Any unauthorized changes should be identified and addressed.

Compromised professional accounts should be suspended immediately and reviewed before access is restored.

### 13.1.13 Pilot Security Considerations

The pilot should test whether Continuum Health can securely support:

- Patient identification and controlled search.
- Basic access and patient authorization.
- Role-based access.
- Consent-based access.
- Emergency access.
- Access to sensitive information.
- Clinical verification.
- Secure user sessions.
- Audit trails.
- Patient visibility of access activity.
- Notifications.
- Administrative oversight.
- Handling of incorrect or unauthorized access.
- Continuity of care when Continuum or hospital integration is unavailable.

Specific technical security measures, infrastructure, encryption standards and implementation details will be defined during the technical design and system architecture stages.

# 14 Pilot Environment

## 14.1 Pilot Purpose

The initial Continuum Health pilot will test the feasibility and practical use of the system within a real healthcare environment.

The pilot will assess whether Continuum Health can provide patients living with Sickle Cell Disease with a secure, portable longitudinal health record and enable authorized healthcare professionals to access relevant patient information when needed, particularly during emergency and ongoing care.

The pilot will also assess how Continuum Health can operate alongside and connect with the participating hospital's existing information systems without unnecessarily duplicating clinical work.

## 14.2 Pilot Setting

The initial pilot will be conducted within **one participating healthcare facility**.

The pilot will be limited to the participating facility rather than attempting to introduce Continuum Health across multiple hospitals during the first implementation.

The participating facility will provide the clinical environment in which patient registration, verification, record access, clinical documentation, emergency access and hospital-system integration can be tested.

## 14.3 Pilot Patient Population

The initial pilot population will consist of approximately **50 patients living with Sickle Cell Disease (SCD)**.

The pilot will include a mixture of patients with different levels of interaction with the healthcare system, including patients who:

- Have existing or established SCD medical histories
- Have frequent hospital or emergency department encounters
- Have less frequent healthcare encounters
- Are newly enrolled into Continuum Health?
- Have existing medical information that can be incorporated into their Continuum Health record where available and appropriate

The purpose of including a range of patients is to test Continuum Health across different patient circumstances rather than limiting the pilot to one type of healthcare user.

The initial pilot will focus primarily on **adolescents and adults with SCD**, with the inclusion of younger patients to be considered in accordance with the pilot facility's clinical, ethical and operational requirements.

## 14.4 Pilot Healthcare Users

The pilot will involve the following user groups:

**Patients**

Patients with SCD participating in the pilot will create or be enrolled into Continuum Health accounts, complete identity verification, participate in clinical verification where required, manage their consent and care preferences, and interact with their longitudinal record.

**Physicians**

Physicians will be the primary clinical users responsible for:

- Clinical verification
- Reviewing patient records
- Adding and updating clinical information
- Developing and updating treatment and emergency care plans
- Accessing relevant patient history
- Requesting additional or emergency access where necessary

**Nurses**

Nurses will participate in relevant patient care workflows, particularly emergency and ongoing care, including:

- Accessing information relevant to patient care
- Reviewing emergency information
- Recording administered treatment
- Adding relevant nursing information
- Requesting emergency access where necessary

**Laboratory Professionals**

Laboratory professionals will participate in the limited laboratory component of the pilot by:

- Accessing information necessary for laboratory activities
- Uploading relevant test results
- Adding new laboratory information
- Flagging results requiring review

**Hospital Administrator**

The hospital administrator will provide institutional oversight and coordinate:

- Hospital participation
- Hospital-system integration
- User onboarding and institutional processes
- Operational issues arising during the pilot
- Coordination with the Continuum Health Administrator

**Continuum Health Administrator**

The Continuum Health Administrator will oversee the Continuum Health side of the pilot, including:

- System rollout
- User and system support
- Operational issues
- Audit and access oversight
- Coordination with the participating hospital
- Documentation of issues and lessons learned during the pilot

## 14.5 Pilot Clinical Scope

The pilot will focus on the clinically relevant information required to demonstrate Continuum Health's value for patients with Sickle Cell Disease.

The initial clinical scope will include:

- SCD diagnosis
- Important complications
- Major hospitalizations
- Known allergies
- Relevant treatment history
- Established emergency and care plans
- Significant treatment responses

Continuum Health will not require the patient's entire historical medical record to be reconstructed before the patient can participate in the pilot.

The longitudinal record will begin developing from the point of enrolment, while relevant existing medical history may be incorporated where available and appropriate.

## 14.6 Pilot System Scope

The pilot will test the core functions required to demonstrate the Continuum Health model, including:

- Patient account creation
- Identity verification
- Continuum Health ID generation
- Clinical verification
- Patient record creation and management
- Emergency care information
- Patient search and identification
- Basic patient access
- OTP-based patient authorization
- Consent management
- Role-based professional access
- Emergency access
- Clinical record viewing
- Clinical record creation and updating
- Laboratory result upload
- Patient access history
- Audit trails
- Notifications
- Session tracking
- Administrative oversight

The pilot will focus on whether these functions work together as a coherent clinical workflow rather than testing each feature in isolation.

## 14.7 Hospital System Integration

Hospital-system integration will form part of the initial pilot.

The purpose of this component is to understand how Continuum Health can operate alongside the participating hospital's existing information system and how relevant patient information can be exchanged between the systems.

The pilot will explore:

- How Continuum Health connects with the hospital's existing system
- What information should be exchanged between the systems
- How patient records can be linked without creating unnecessary duplication
- How clinical information entered during a patient encounter can be appropriately reflected across systems
- How Continuum Health can fit into existing clinical workflows
- What technical, operational or workflow challenges arise during integration

The pilot will not attempt to establish interoperability with multiple hospitals or national healthcare systems at this stage.

The lessons from the pilot will inform the design of future interoperability and multi-facility integration.

## 14.8 Pilot Workflow

The pilot will follow the patient and clinician journeys defined within this PRD.

At a high level:

**Patient enrolment** → **Identity verification** → **Clinical verification** → **Record creation** → **Patient authorization/consent** → **Clinical access** → **Patient care** → **Clinical documentation** → **Record update** → **Audit and notification**

Emergency scenarios will additionally test:

**Patient identification** → **Emergency access request** → **Authorization** → **Relevant information accessed** → **Care provided** → **Encounter documented** → **Emergency access recorded** → **Administrative review**

The pilot will test both routine/ongoing care and emergency care scenarios where feasible.

## 14.9 Pilot Limitations

The initial pilot will intentionally remain limited in scope.

The pilot will not:

- Attempt to support every chronic illness
- Attempt to include every healthcare facility
- Attempt to establish international interoperability
- Replace the participating hospital's existing health information system
- Require the complete reconstruction of every patient's historical medical record
- Establish the final national or international operating model for Continuum Health
- Establish the final technical architecture required for global deployment
- Determine the final legal and regulatory framework for international operation

The pilot is intended to generate evidence, identify challenges and validate the core Continuum Health model before expansion.

## 14.10 Pilot Learning Objectives

The pilot will seek to determine:

- Whether patients can be enrolled and verified effectively
- Whether healthcare professionals can identify patients efficiently
- Whether patients can control access to their information appropriately
- Whether authorized professionals can access relevant information without unnecessary exposure to unrelated records
- Whether emergency access can function appropriately
- Whether clinical information can be verified and maintained accurately
- Whether the system fits naturally into existing clinical workflows
- Whether hospital-system integration is feasible
- Whether Continuum Health reduces the burden of repeatedly reconstructing a patient's medical history
- What operational, technical and clinical challenges must be addressed before expansion

The findings from the pilot will inform subsequent development of Continuum Health and future pilots across additional facilities and patient populations.

# 15 Success Metrics

The success of the Continuum Health pilot will be measured by whether the system can provide authorized healthcare professionals with the right patient information at the right time, while reducing the burden placed on patients and maintaining appropriate control, security and accountability over health information.

The pilot will assess the following areas:

## 15.1 Patient Access and Experience

The pilot will assess whether patients are able to successfully use and understand the system.

Metrics will include:

- Number and percentage of pilot patients who successfully create an account.
- Number and percentage of patients who successfully complete identity verification.
- Number and percentage of patients who understand whether their account and clinical record are verified or unverified.
- Successful use of patient login and account access.
- Successful management of consent and care preferences.
- Patient ability to view their access history.
- Patient ability to request a review, correction or audit of their record.
- Patient-reported reduction in the burden of repeatedly explaining their medical history.
- Patient-reported sense of control over who accesses their health information.

## 15.2 Clinical Usefulness

The pilot will assess whether Continuum Health provides information that is useful to healthcare professionals during patient care.

Metrics will include:

- Percentage of patient searches that successfully identify the correct patient.
- Percentage of authorized clinicians who are able to access the information they require.
- Percentage of clinicians who report that the emergency information provided was useful during care.
- Clinician assessment of whether the longitudinal record provides a more complete understanding of the patient's history.
- Percentage of clinical records successfully verified by an authorized physician.
- Ability of physicians to add, update and verify relevant clinical information.
- Ability of healthcare professionals to document relevant information without unnecessary duplication.

## 15.3 Efficiency and Patient Burden

The pilot will assess whether access to Continuum Health can improve the efficiency of accessing relevant patient information and reduce unnecessary repetition.

Metrics will include:

- Time taken to search for and identify a patient.
- Time from patient arrival to relevant Continuum Health information being accessed.
- Time required for a clinician to establish relevant medical history using Continuum Health.
- Time required to access emergency care information.
- Frequency with which patients are required to repeat information that is already available in their verified record.
- Time required to document and update relevant information after an encounter.
- Comparison of relevant measures with the participating hospital's existing workflow or baseline, where baseline information is available.

## 15.4 Record Quality and Continuity

The pilot will assess whether Continuum Health is able to build and maintain a useful longitudinal patient record.

Metrics will include:

- Percentage of pilot patients with a clinically verified record.
- Percentage of pilot records containing the core SCD information defined for the pilot.
- Percentage of relevant encounters that result in the patient's record being updated.
- Availability of relevant previous encounters when a patient returns for care.
- Availability of relevant treatment history, complications and treatment responses.
- Number of identified missing or conflicting records requiring review.
- Extent to which relevant information is carried forward between encounters.
- Accuracy and completeness of information following physician verification.

## 15.5 Safety, Access Control and Accountability

The pilot will assess whether the system appropriately controls access to patient information and provides a clear record of activity.

Metrics will include:

- Percentage of access attempts in which healthcare professionals are limited to information appropriate to their role and authorized access level.
- Successful use of patient authorization and consent processes.
- Successful use of the emergency access process when required.
- Percentage of emergency access events that are recorded and available for review.
- Percentage of patient record changes that are correctly attributed to the professional who made them.
- Successful recording of patient searches, access requests, consent decisions, emergency access, record changes and sessions.
- Successful delivery of important patient notifications.
- Number of incorrect-patient access incidents.
- Number of unauthorized access incidents.
- Number of unresolved access, verification or record-integrity issues.
- Number and type of incidents requiring administrative intervention.

## 15.6 Technical and Operational Performance

The pilot will assess whether the system can function reliably within the participating healthcare facility and fit into existing workflows.

Metrics will include:

- Successful patient search and identification rate.
- Successful access-request rate.
- Successful consent and authorization rate.
- System availability during the pilot.
- Successful connection and information exchange with the participating hospital's existing system.
- Number and type of hospital-system integration issues identified.
- Number of system or workflow issues requiring Continuum Health administrator intervention.
- Time required to resolve identified technical or operational issues.
- Successful operation of the agreed emergency fallback approach, where applicable.

## 15.7 Primary Success Indicators

The primary success of the pilot will be assessed through the following questions:

1. Can the right patient be found and correctly identified?
2. Can an authorized healthcare professional access the right information at the right time?
3. Can the system provide useful verified information during emergency and routine care?
4. Does access to the longitudinal record reduce the burden on patients to repeatedly explain their medical history?
5. Can relevant patient information be maintained and carried forward between healthcare encounters?
6. Can Continuum Health maintain appropriate consent, access control, security and accountability?
7. Can the system operate within the workflow of a participating healthcare facility and connect with its existing system?

Specific numerical targets for these metrics will be established during pilot planning where appropriate, using available hospital baselines, system testing and pilot observations. The pilot will focus not only on whether targets are met, but also on identifying usability, workflow, clinical, technical and safety issues that need to be addressed before wider implementation.

# 16 Out of Scope

The following functions, populations, integrations and capabilities are outside the scope of the Continuum Health MVP and initial pilot. These may be considered for future development once the core system has been tested and validated.

## 16.1 Clinical Decision-Making Functions

Continuum Health will not:

- Diagnose patients independently.
- Prescribe medication or treatment.
- Provide independent medical advice.
- Replace clinical judgement or the patient–healthcare professional relationship.
- Make autonomous clinical decisions.
- Provide autonomous clinical decision support or treatment recommendations.

Continuum Health may support healthcare professionals by making relevant verified information available, but responsibility for clinical decisions remains with the authorized healthcare professional.

## 16.2 Expansion Beyond Sickle Cell Disease

The initial pilot will focus on patients living with Sickle Cell Disease.

The following are therefore outside the scope of the initial pilot:

- Supporting all chronic illnesses.
- Supporting the general patient population.
- Expanding to additional chronic conditions unless deliberately included in a later phase.
- Developing condition-specific workflows for conditions other than Sickle Cell Disease.

The system will, however, be designed with future expansion in mind.

## 16.3 Multi-Hospital Deployment

The MVP will be implemented and tested within one participating healthcare facility.

A full multi-hospital deployment is outside the scope of the initial pilot. The pilot will instead be used to understand how Continuum Health can integrate with a hospital environment and existing workflows before expanding to multiple facilities.

## 16.4 National and International Interoperability

The pilot will explore integration and information exchange with the participating hospital's existing system.

However, the following are outside the scope of the initial pilot:

- National health information exchange.
- Integration across multiple healthcare facilities.
- Cross-border health information exchange.
- International interoperability.
- Global deployment.

These will be considered as part of future development.

## 16.5 Complete Historical Medical Record Digitization

Continuum Health will not require the complete reconstruction of a patient's lifetime medical history before the record can become useful.

The MVP will focus on building the longitudinal record from enrolment while incorporating relevant existing medical history where it is available and can be appropriately verified.

The pilot will prioritize clinically important Sickle Cell Disease information, including:

- Important complications.
- Major hospitalizations.
- Known allergies.
- Relevant treatment history.
- Established emergency or care plans.
- Significant treatment responses.

Complete historical digitization and reconstruction of every previous medical encounter is outside the scope of the MVP.

## 16.6 Advanced Biometric Identification

Biometric identification and authentication, including fingerprint or other biometric methods for patient identification, are outside the scope of the initial MVP.

The MVP will rely on defined identification and authentication methods such as Continuum ID, approved identifying information and OTP-based authorization where applicable.

Biometric identification may be introduced in a future phase once the appropriate technical, security, privacy and regulatory requirements have been established.

## 16.7 Advanced Offline Functionality

A fully functional offline version of Continuum Health is outside the scope of the initial MVP.

The pilot may be used to design and test how Continuum Health should operate when connectivity or system availability is limited. However, healthcare delivery must not depend on Continuum Health being available.

If Continuum Health is unavailable, healthcare professionals will continue to provide care using existing hospital procedures.

## 16.8 Advanced Artificial Intelligence

Artificial intelligence features that independently influence clinical decisions are outside the scope of the MVP.

This includes:

- AI diagnosis.
- AI-generated treatment decisions.
- Autonomous treatment recommendations.
- Predictive clinical decisions.
- Autonomous clinical decision-making.

The potential use of AI for appropriate future functions may be explored after the core system has been validated.

## 16.9 Billing and Financial Functions

The MVP will not include:

- Patient billing.
- Insurance claims processing.
- Payments.
- Financial management.
- Medical financing.
- Other healthcare payment functions.

These functions may be considered for future integration where appropriate.

## 16.10 Pharmacy as a Full System Role

Pharmacy integration and the full definition of pharmacy permissions are not finalized for the MVP and remain to be determined.

The initial system may contain basic medication information as part of the patient record, but a dedicated pharmacy workflow, pharmacy-specific access permissions and medication management functions will be determined in a later phase.

## 16.11 Advanced Patient Services

The MVP will focus on the secure patient record, authorized access and continuity of care.

The following services are outside the scope of the initial pilot:

- Appointment booking.
- Telemedicine.
- Direct patient–clinician messaging.
- Medication purchasing or delivery.
- Integration with personal health devices.
- Wellness tracking.
- Broader lifestyle or health-management features.

These may be considered as future patient-facing services.

## 16.12 Expanded Sensitive and Restricted Health Information

The MVP will establish defined controls for sensitive or restricted information, including information relating to mental health, reproductive health and information specifically designated as sensitive by the patient.

More advanced management of sensitive records, additional categories of restricted information and more complex access policies are outside the scope of the initial pilot and may be developed as the system matures.

## 16.13 Purpose of the Scope Limitations

These limitations are intended to keep the MVP focused on the core problem Continuum Health is designed to solve: **making relevant, verified patient information securely accessible to authorized healthcare professionals when it is needed, particularly during acute and emergency care.**

The features excluded from the MVP are not necessarily excluded from the long-term vision of Continuum Health. They are being deferred so that the initial pilot can establish whether the core system is useful, safe, practical and capable of integrating into real healthcare workflows before significant expansion.

# 17 Future Development

The future development of Continuum Health will focus on expanding the system beyond the initial Sickle Cell Disease pilot while maintaining its core principles of patient-centered care, secure access, clinical verification, interoperability, privacy and patient control.

Future development will be guided by lessons from the pilot, user feedback, technical feasibility, healthcare-system requirements, legal and regulatory requirements, and the needs of patients and healthcare professionals.

## 17.1 Expansion to Additional Healthcare Facilities

Following successful evaluation of the pilot, Continuum Health may be expanded to additional healthcare facilities.

Future development may include:

- Onboarding multiple hospitals and healthcare facilities.
- Supporting different types of healthcare facilities and levels of care.
- Allowing patients to access their Continuum record across participating facilities.
- Establishing processes for onboarding and managing participating facilities.
- Improving integration between Continuum Health and existing hospital information systems.
- Supporting the exchange of relevant patient information between participating facilities while maintaining appropriate access controls.

**National and International Interoperability**

The long-term vision of Continuum Health is to allow a patient's health information to remain accessible and continuous even when they move between healthcare facilities, regions or countries.

Future development may therefore include:

- Integration with national health information systems where appropriate.
- Interoperability with different electronic medical record and hospital information systems.
- Standardized exchange of patient information between healthcare systems.
- Support for patients receiving care outside their primary country of residence.
- Cross-border access to relevant patient information where legally and technically possible.
- Development of mechanisms that allow the patient's Continuum ID to remain consistent across different healthcare systems.

The exact technical standards, infrastructure and partnerships required for this level of interoperability will be determined as the system develops.

## 17.2 Expansion Beyond Sickle Cell Disease

Sickle Cell Disease will be the initial clinical focus of Continuum Health.

Following evaluation of the SCD implementation, the platform may be expanded to support other chronic illnesses and conditions where longitudinal medical history and continuity of care are particularly important.

Potential future areas may include:

- Other chronic diseases.
- Patients with multiple chronic conditions.
- Disabilities requiring long-term or specialized care.
- Conditions requiring frequent emergency or hospital visits.
- Eventually, broader patient populations beyond chronic illness.

Expansion will be based on evidence from the pilot and the ability of the platform to support the clinical and information requirements of additional conditions safely.

## 17.3 Advanced Identity and Biometric Authentication

Future versions may introduce additional methods of identifying and authenticating patients and healthcare professionals.

Potential developments may include:

- Biometric patient identification.
- Fingerprint or other approved biometric authentication.
- Additional identity verification methods.
- Improved identification of patients who cannot communicate or do not have access to their phone or Continuum credentials.
- Integration with appropriate national or institutional identity systems where permitted.

Any biometric functionality will be developed with particular attention to privacy, security, consent and the risks associated with biometric information.

## 17.4 Advanced Offline and Emergency Access

The pilot will allow Continuum Health to identify the challenges associated with connectivity, electricity and access to digital systems within healthcare facilities.

Future development may include more advanced offline or low-connectivity functionality that allows essential patient information to remain available during temporary system or network disruptions.

Potential developments may include:

- Secure offline access to limited emergency information.
- Synchronization of information once connectivity is restored.
- Additional emergency access mechanisms.
- Improved continuity of care during infrastructure or connectivity failures.

Emergency functionality will remain subject to strict access controls and audit requirements.

## 17.5 Research, Public Health and Population Health Data

As Continuum Health develops a longitudinal database of clinically verified Sickle Cell Disease information, the system may eventually support the responsible secondary use of health data for research, public health and health-system planning.

The primary purpose of the Continuum Health record will remain the provision and continuity of patient care. Research and population-health use will therefore be treated as a separate and appropriately governed use of information rather than allowing researchers direct access to individual patient records.

Future development may include a dedicated research and population-health data environment that can use appropriately governed data from Continuum Health records.

Potential future capabilities may include:

- Development of a structured Sickle Cell Disease research database derived from Continuum Health records.
- Analysis of longitudinal patterns such as complications, hospitalizations, treatments, treatment responses and healthcare encounters.
- Supporting research into Sickle Cell Disease outcomes and patterns of care.
- Supporting approved research partnerships with universities, healthcare institutions and other appropriate organizations.
- Generation of aggregated population-level information for public health planning and policy development.
- Supporting healthcare resource planning and identification of areas requiring additional services or intervention.
- Development of dashboards and analytical tools using appropriately aggregated data.
- Creation of appropriately de-identified or otherwise lawfully governed datasets for approved research purposes.
- Establishment of processes through which patients can understand how their information may be used for secondary purposes and, where applicable, exercise their available choices regarding such use.
- Maintaining appropriate governance, security, privacy, transparency and auditability throughout the secondary-use data lifecycle.

The specific governance, consent or other lawful basis, de-identification requirements, data access procedures and research approval processes will be determined before this functionality is implemented.

## 17.6 Artificial Intelligence and Advanced Analytics

Artificial intelligence and advanced analytics may be explored as future capabilities of Continuum Health.

Potential applications may include:

- Identifying patterns within longitudinal patient data.
- Supporting population-health analysis.
- Identifying trends in hospitalizations, complications and treatment responses.
- Supporting research and health-system planning.
- Assisting healthcare professionals in locating relevant information within a patient's record.

Any future AI functionality must support, rather than replace, clinical judgement. Continuum Health will not use AI to independently diagnose patients, prescribe treatment or make autonomous clinical decisions.

## 17.7 Patient-Centered Expansion

Future development may expand the services available directly to patients while maintaining the core purpose of Continuum Health.

Potential future features may include:

- Improved patient dashboards.
- Greater control over personal health information and sharing preferences.
- Patient-generated health information.
- Notifications and reminders relating to care.
- Improved access to personal health history.
- Patient education and information resources.
- Additional accessibility features for patients with disabilities or communication barriers.

These features will only be introduced where they support the core purpose of improving continuity, accessibility and patient-centered care.

## 17.8 Additional Healthcare Professional Roles

As Continuum Health expands, additional professional roles may be incorporated into the platform.

This may include:

- Pharmacists and pharmacy systems.
- Allied health professionals.
- Specialists and other clinical professionals.
- Additional laboratory and diagnostic roles.
- Other healthcare workers whose access is necessary for continuity of care.

Each role will have defined permissions based on the information and actions required for that role.

## 17.9 Advanced Data Governance and Patient Control

As the platform expands, Continuum Health will require more comprehensive governance mechanisms for the management and use of health information.

Future development may include:

- More detailed patient control over different categories of information.
- Advanced sensitive-record controls.
- More detailed access and audit reports.
- Data-sharing preferences.
- Research and secondary-use preferences where applicable.
- Expanded mechanisms for correcting or challenging information.
- Formal data governance structures and policies.
- Mechanisms for managing data when patients become inactive, move between jurisdictions or die.

## 17.10 Long-Term Vision

The long-term development of Continuum Health is to evolve from a system initially designed to support patients with Sickle Cell Disease into a patient-centered health information infrastructure that can support continuity of care across healthcare facilities, regions and countries.

The long-term vision is for a patient to maintain one trusted longitudinal health record that can follow them throughout their healthcare journey, while ensuring that healthcare professionals only access the information they are authorized and clinically permitted to access.

Future development will therefore be guided by one central principle:

**The patient's health record should follow the patient, not remain trapped within a single healthcare facility.**
