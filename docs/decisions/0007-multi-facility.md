# ADR 0007: Multi-facility design from the start

- **Status:** Accepted.
- **Date:** 2026-11-16 · **Deciders:** JK, FK
- **Resolves:** prd-review §d gap 4 (partly)

## Context

The pilot is one facility (PRD §14.2, §16.3), but the product's value is a record that
follows the patient across facilities (§7.1, §8.7, §12.4.1). With only one facility the
cross-facility emergency case cannot be tested (prd-review §d gap 4).

## Decision

1. The data model is **multi-facility from the start**:
   - Facilities are records.
   - Staff have memberships at one or more facilities.
   - Every access and every clinical entry records the facility it happened at.
2. Patient records are **not owned by a facility** (PRD §12.4.1).
3. The pilot tests the emergency flow as **Emergency Department staff opening a record held
   by the SCD clinic**.

## Consequences

- Single-facility shortcuts are not allowed, such as a global "the hospital" setting or a
  facility-less access log.
- Staff choose (or are assigned) an **acting facility** per login session; it is recorded on
  every access (PRD §11.3).
- A full multi-hospital deployment is still out of scope (§16.3); this decision is about
  the data model, not the rollout.
- For the ED test to mean anything, the ED must not already hold consent from the SCD
  clinic's patients. *Resolved 18 Nov 2026:* consent is granted to a **care team** (ADR 0005
  as amended). ED staff outside the SCD Clinic team must use break-glass, so the pilot
  exercises the emergency path within one facility.
