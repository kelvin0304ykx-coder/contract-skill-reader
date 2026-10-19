# Contract Change Mapping And Version Reconciliation

## Contents

- Purpose And Boundary
- Build The Mapping Sheet
- Reconcile A User-Edited Version
- Produce A Clause-By-Clause External Explanation
- Hard Correspondence And Freshness Gate
- Run The Coverage Gate

Use this reference when a contract review has more than one dependent deliverable, when the user asks for a clause-by-clause explanation of changes, or when the user returns a reviewed contract or legal opinion with further edits.

## Purpose And Boundary

Create a `contract change mapping sheet` as an internal, temporary work product for one contract. Keep it inside the existing client or matter workflow; do not create a new client project, and do not deliver it as a separate file unless the user asks.

Use the mapping sheet as the single source for the redline, clause-by-clause legal opinion, negotiation matrix, and signing checklist. Do not independently reconstruct those outputs from memory.

## Build The Mapping Sheet

Create one row for each substantive clause change. Group related insertions and deletions that implement one legal or commercial change; do not count raw XML revision nodes as separate changes.

| Field | Required Content |
|---|---|
| Change ID | stable sequential identifier within the contract review |
| Location | current article, paragraph, item, table, or annex |
| Original problem | adverse scenario or defect in the source wording |
| Main change | concise summary of the current revised wording |
| Edit granularity | word, phrase, sentence, whole new clause, or whole deletion; never paragraph replacement |
| Reason | why the change protects the reviewing side or makes performance workable |
| Basis | checked law, controlling transaction document, user instruction, or stated inference |
| Classification / severity | must change, recommend, business decision, or fact check; critical, high, medium, or low |
| Action | redline, comment, research, signing check, or no external action |
| Version status | retained, user-reworded, user-deleted, newly added, or superseded |
| External explanation | include, exclude with reason, or needs update |

Exclude purely mechanical formatting, punctuation, numbering repair, and non-substantive style changes from the client-facing count. Record the exclusion rule or a short exception list internally when coverage could otherwise be questioned.

Keep comments for missing facts and decisions in the same mapping when they materially affect signing, but distinguish them from completed textual changes.

Use the same change ID only where the issue actually appears in a requested, applicable deliverable. Do not create a redundant client-facing artifact solely to carry a change ID.

## Reconcile A User-Edited Version

Treat the latest file supplied or saved by the user as the current authority. Compare it with the prior mother contract and prior Codex output only to identify what changed; do not overwrite it with an earlier version.

Classify each prior mapped item as:

- `retained`: the user kept the substantive change;
- `user-reworded`: the user changed the wording but retained or altered the objective;
- `user-deleted`: the user removed the change or comment;
- `newly added`: the user introduced a new substantive change;
- `superseded`: a later clause or document made the item obsolete.

Update the mapping and every dependent deliverable to the current version. Do not re-add user-deleted fact-check comments or contract text. Never repeat the subject matter of a deleted fact-check or metadata comment in a current output, including as a negative reminder. If a user deletion removes a critical substantive protection or creates a new signing blocker, leave the user's text intact and surface only the consequence once in the delivery note or signing check for lawyer or business confirmation; do not reproduce the deleted wording.

Keep the deleted or superseded item itself only in the internal version reconciliation. It must not remain as a current mapping, comment, redline, or change. A consequence-only warning about deletion of a critical substantive protection is a new current issue and must use its own change ID; this exception never applies to deleted fact-check or metadata comments.

When the user edits only an external legal opinion, preserve the user's tone, structure, deletions, and accepted language. Update only the rows or conclusions affected by the contract mapping unless a broader inconsistency requires repair.

## Produce A Clause-By-Clause External Explanation

When the user asks for a legal opinion or client explanation stating which clause changed and why, derive the explanation from the current mapping sheet using the workflow in this package. A broader formal legal opinion needs an expressly defined scope.

Use this default structure unless the user's template controls:

1. concise review conclusion;
2. clause-by-clause change explanation;
3. unresolved comments or signing checks;
4. verified legal basis;
5. final status and lawyer-confirmation note in the internal mapping or chat handoff only, never embedded in the delivered artifact unless expressly requested.

For each substantive change, state at least:

- the current contract location;
- the main change;
- the practical or legal reason for the change.

Add the original problem, verified legal basis, risk level, or remaining confirmation only when useful. Follow the current contract's clause order. Summarize the change rather than copying the full replacement clause; the redline remains the controlling wording.

Distinguish a completed redline from a comment, fact check, business choice, or research item. Do not describe an unresolved point as if it had already been amended in the contract.

## Hard Correspondence And Freshness Gate

This gate is mandatory and delivery-blocking for every legal opinion, change
explanation, negotiation table, or signing check that depends on a reviewed
contract.

### Lock The Controlling Version

Before drafting, record the absolute path of the latest mother contract and a
version fingerprint such as its content hash and modification time. Compare all
candidate user-edited contracts and prior outputs; do not select a mother file
only because its filename says `final`, `reviewed`, or `refined`.

For DOCX review, use [matter-identity-gate.md](matter-identity-gate.md). Bind the
mapping to both the current mother SHA-256 and the reviewed contract's
`output_sha256`; every dependent artifact and the final handoff must refer to
that same reviewed version. A timestamp or an earlier zero-error report cannot
replace the current content hash or a passed identity gate.

Any contract edit made after the mapping or dependent deliverable was generated
makes that mapping and deliverable stale. Treat this as true even when the later
edit appears small or unrelated. Reconcile the latest contract, refresh affected
rows, and run the full gate again.

### Require Exact Item Shape

Each client-facing explanation item must contain, in this order:

1. the exact current article, paragraph, item, table row, or annex location;
2. the main completed change, or the expressly labeled unresolved comment;
3. the practical or legal reason.

A broad theme, heading, or risk category without the current clause location is
not a clause-by-clause explanation. Do not combine unrelated clauses merely to
reduce the item count. Group clauses only when they implement one connected
objective, and list every included location in the item heading.

### Prove Coverage

Calculate and record internally:

`current substantive change groups = included explanation groups + documented exclusions`

Document only mechanical formatting, punctuation, numbering repair, or other
non-substantive changes as exclusions. An unresolved contract comment is not an
exclusion: map it to its exact clause, mark it as `fact check`, `business
decision`, or `needs verification`, and keep it distinct from completed edits.

The gate fails if any of the following is true:

- the controlling contract is not the latest user-authoritative version;
- the contract changed after the mapping or dependent deliverable;
- a current substantive change has no mapping or explanation disposition;
- an explanation lacks an exact current location or uses only a theme label;
- an explanation duplicates, contradicts, or describes a deleted or superseded change;
- a pending comment is presented as an implemented amendment;
- the coverage equation does not balance;
- a clause number, amount, date, defined term, party label, annex name, or
  cross-reference differs from the latest contract.

Do not deliver on failure. Refresh the mapping and dependent deliverable until
the gate passes; legal or thematic similarity does not cure a failed gate.

## Run The Coverage Gate

Before delivering a clause-by-clause explanation or a revised set of dependent documents, verify:

- every current substantive change has one mapping row;
- every requested client-facing explanation maps to a current substantive change or an expressly identified unresolved comment;
- the substantive-change count matches the included explanation count after documented exclusions;
- no explanation describes a user-deleted or superseded change as current;
- clause numbers, defined terms, amounts, dates, annex names, and cross-references match the latest contract;
- each stated legal basis is live-verified or marked `needs verification`;
- material unresolved comments appear in the signing check when they require action before signature;
- affected explanations were refreshed after user edits, followed by a full-document consistency check.
- every replacement change is implemented at the smallest workable word, phrase, or sentence level; no mapping row is implemented as a long full-paragraph delete-and-insert pair.

Report the counts and any exclusions in the internal QA note. Do not burden the client-facing opinion with production metrics unless the user asks.

Record the final result as `correspondence_gate: pass` or `fail`. Only `pass` is
deliverable.
