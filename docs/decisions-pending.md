# Pending technical decisions

Decisions that block or shape code but are not product questions in the PRD itself.
Product decisions live in `docs/prd-review.md` §f.

## TODO: controlled, audited purge for retention / erasure requests

**Status:** pending a policy decision. **Do not implement until decided.**

The codebase has **no hard-delete path**: `ContinuumModel` soft-deletes on both instance and
queryset `delete()`, there is no `hard_delete()` method, and the admin cannot delete users.
This follows CLAUDE.md ("clinical records are never hard-deleted").

At some point a lawful need to permanently remove or anonymise data may arise, for example:
- a patient's account-closure request once retention periods have passed (PRD §7.9, §6.1)
- a data-subject erasure request under the Kenya Data Protection Act 2019
- test or erroneous records created during the pilot

Before building anything, decide:
1. The retention period for each record type (Kenyan law and the pilot facility's policy).
2. Purge vs anonymisation: delete rows, or strip identifiers and keep clinical history?
3. Who may authorise a purge (two-person approval?), and how it is requested.
4. What audit evidence survives the purge (who, when, why, which records, but no content).
5. How backups are handled.

When decided, implement it as a dedicated, permission-gated service with its own audit
trail and tests. Do not add a generic `hard_delete()` to the base models.

## Patient authentication path

**Status:** open (PRD §11.4; prd-review §f).

`accounts.User` uses email + password and is for **staff/clinician accounts only**. PRD §11.4
describes patients logging in with a Continuum Patient ID or username, with OTP, and many
pilot patients may have no email. Patient login is expected to be a **separate
authentication path** (its own backend and flow). Decide the identifier, the OTP channel
and the account-recovery process before modelling patient accounts.
