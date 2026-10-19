# DOCX Contract Review Delivery

Use this reference whenever producing or modifying a Word contract.

## Editing Roles

Use tracked revisions for language that can be responsibly corrected from verified text and available transaction materials. Use comments for facts, approvals, commercial choices, missing source documents, and verification items.

Prefer this pattern:

- Redline the clause with usable language.
- Add a short comment only when the user must understand the consequence, choose an option, supply a fact, or approve a fallback.
- Keep comments actionable and tied to the exact text.
- Avoid long legal essays, generic warnings, repeated risk descriptions, and comments on clauses that require no action.

Use compact comment labels when helpful:

- `[需业务确认]`
- `[需补充材料]`
- `[需核对]`
- `[需检索确认]`
- `[谈判建议]`

Do not use a label as a substitute for explaining the actual decision or missing item.

## Standing User Defaults

- Set the author of every new tracked revision and comment to `审阅人`.
- Leave the contract-number field untouched unless the user expressly asks to revise it.
- For party/entity identity, authority, qualification, license, unified social credit code, legal representative, account, and source-document consistency, add a verification comment instead of silently editing the body.
- Do not re-add contract-number, signing-place, party-information, subject-information, or other fact-check comments the user intentionally deleted.
- Do not silently fill or normalize party names, dates, amounts, tax rates, bank accounts, technical standards, or annex data without a controlling source.

## Preserve The Mother Document

- Work from the identified mother contract and save to a new output path.
- Preserve page size, margins, headers, footers, logos, fonts, styles, numbering, tables, fields, page numbers, section breaks, signature blocks, annex layout, and existing revision state.
- Preserve existing comments and revisions unless the user asks to remove or resolve them.
- Avoid converting native numbering, fields, or tables into plain text.
- Avoid global formatting cleanup unrelated to the review.
- Do not accept all changes or generate a clean version unless the user expressly requests acceptance of changes or a clean copy. Finalization checking alone does not authorize either action.

## Resume From A User-Edited Review Version

- Treat the latest file supplied or saved by the user as the new mother document for the next output.
- Inventory its current revisions and comments before editing; compare with prior outputs only to identify user choices and dependent materials that need updating.
- Do not reconstruct the current document from an earlier Codex output or re-add user-deleted text, revisions, or comments.
- Preserve user-reworded clauses and update only what the current request requires. If a user deletion creates a critical unresolved risk, keep the user's text and flag the consequence in the delivery note or signing check.
- When a legal opinion, negotiation table, or signing check depends on the redline, reconcile it through [change-mapping.md](change-mapping.md).

## Precision Redline Iron Rule

- Keep unchanged wording as ordinary, unmarked text. Place `w:del` and `w:ins`
  only around the smallest continuous text unit that actually changes.
- Prefer word-, phrase-, amount-, date-, punctuation-, or single-sentence
  revisions. A reader using “show all markup” must be able to identify the exact
  legal change without comparing two long blocks manually.
- Prohibit deleting the complete old paragraph and inserting the complete new
  paragraph in the same location. This remains prohibited when the net text is
  legally correct, when most of the clause changes, or when block replacement is
  easier for the production tool.
- For a substantially restructured clause, retain reusable words and structure,
  then split the redline into sentence- or phrase-level revision pairs. Keeping
  only the clause number or a few punctuation marks does not make an otherwise
  complete paragraph replacement a precision edit.
- A wholly new clause may be one tracked insertion. A clause removed without any
  replacement may be one tracked deletion. An old clause exchanged for a new
  clause is a replacement and must still be precision-redlined.
- If precision markup cannot be produced safely, stop delivery and change the
  editing method. Do not solve the limitation with a broad delete-and-insert.

## Revision Quality

- Preserve defined terms and use them consistently.
- Keep inserted clauses compatible with the document's numbering, indentation, punctuation, and drafting style.
- Check that comments anchor to the intended text and remain readable after edits.
- Remove accidental duplicate comments and duplicate revisions.
- Ensure no comment exposes internal reasoning, file paths, model/tool instructions, credentials, or unrelated client information.
- Ensure the document contains no unresolved drafting artifacts such as TODO, placeholder prompts, template project names, or internal production notes unless intentionally left for the user.

## Mechanical Verification

Run the [mother and identity gate](matter-identity-gate.md) with the locked
intake record and current mother, not a candidate-derived fingerprint. Retain
the output hash for the final file and dependent-deliverable handoff.

Use the available document tooling to verify:

- the file opens without repair warnings;
- new or changed tracked changes/comments are authored by `审阅人`; unchanged
  inherited authors remain intact;
- existing revisions/comments were not unintentionally removed;
- clause numbering, cross-references, tables, headers/footers, page numbers, and signature areas survived;
- the output path differs from the source path;
- the clean visible text does not contain duplicated or missing fragments caused by revision markup;
- the validator reports zero `revision.block_replacement` errors and zero block replacements in the summary;
- no unintended metadata or comments from another matter remain.
- any clause-by-clause explanation requested by the user passes the change-coverage gate in [change-mapping.md](change-mapping.md).

## Visual QA

Render the reviewed DOCX to page images or PDF before delivery. Inspect every page for:

- clipped text, missing fonts, blank pages, shifted tables, broken numbering, overflow, orphaned headings, and damaged signature areas;
- comments or revision balloons obscuring content where visible in the selected render mode;
- header/footer, logo, page-number, and section-break integrity;
- inconsistent spacing or formatting introduced by edited clauses;
- long consecutive strike-through and insertion blocks in the all-markup view; inspect that view in addition to the accepted-changes view;
- annex and table legibility.

If the render differs materially from Word behavior, state the limitation and inspect through the best available renderer. Do not call the deliverable final without a visual check.

## Delivery Set

Default to the smallest useful set:

- full review: one redline DOCX plus a concise delivery note listing material unresolved issues;
- finalization: redline DOCX and, only when requested, a clean DOCX with changes accepted;
- quick scan: no modified DOCX unless requested;
- negotiation: redline DOCX or negotiation matrix according to the user's stated use.

Do not create a separate report that repeats every comment. Create a risk memo only when the user asks, when the document format cannot carry useful comments, or when multiple critical/high risks need a management-level decision.
