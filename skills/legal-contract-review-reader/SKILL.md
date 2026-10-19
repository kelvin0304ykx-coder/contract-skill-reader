---
name: legal-contract-review-reader
description: Use this skill for Chinese contract review, contract redlining, review comments, clause-risk analysis, negotiation positions, contract-finalization checks, reconciling user-edited review versions, producing clause-by-clause change explanations tied to a reviewed contract, and comparing a contract against procurement, response, award, framework, or attachment documents. Trigger when the user says 合同审查, 审合同, 修订合同, 合同批注, 红线稿, 风险条款, 签署前核对, 站在甲方/乙方角度, 用户调整后再审, 逐条说明修改理由, or provides a DOCX/PDF contract for review. Focus on an existing contract. New-contract drafting and litigation are outside this package; source-dependent legal conclusions require an available authorized original-text research channel.
---
Read [portable runtime and DOCX handling](references/portable-runtime.md) first. Use only dependencies actually available in the reader environment. No other private Skill or database account is bundled.



# Legal Contract Review

Keep original matter files read-only, separate facts from missing information and proposals, and use only authorized materials and research channels. Do not disclose client materials to other services without scope. The author, contract-number, subject-information, and intentionally deleted comment rules below apply unless the current user instructs otherwise. Source verification is defined in [research sources](references/research-sources.md).

## Position

Act as the contract-review workflow for an existing Chinese contract or draft. Produce work that a lawyer can use in negotiation, internal approval, or finalization. Review from the user's actual side of the transaction; do not produce a neutral clause summary unless asked.

Use the included references and validator for ordinary review. Read
[portable-runtime.md](references/portable-runtime.md) for actual DOCX handling
and visual QA; read [research-sources.md](references/research-sources.md) when a
conclusion depends on current law. Existing document software and an authorized
research provider are capabilities the reader supplies, not hidden Skill names.
For procurement comparison, use only supplied procurement/award/response files.
For new drafting, litigation or external filing, identify the separate scope
instead of assuming another legal Skill exists or has been executed.

Do not claim that an external lawyer, separate agent, second model, or legal database reviewed the contract unless that review actually occurred in the current task.

## Select The Review Mode

Choose one mode from the request and available files:

- `quick scan`: identify only material signing blockers and high-risk clauses; do not create a full redline unless asked.
- `full redline`: review clause by clause, apply tracked revisions and targeted comments, and report unresolved material risks. Use this as the default when the user provides an editable contract and asks for review.
- `finalization`: check an already negotiated draft for residual contradictions, missing blanks, numbering, cross-references, attachments, comments, revisions, and signature readiness. Do not reopen settled commercial points without a material reason.
- `negotiation`: produce preferred wording, acceptable fallback, negotiation bottom line, and the counterparty's likely response for each material issue.

State the selected mode in the working notes or delivery summary. Do not silently reduce a full review to a quick scan.

## Establish The Review Brief

Determine before substantive editing:

- Reviewing party and role: Party A/B, buyer/seller, employer/contractor, licensor/licensee, hospital/supplier, principal/service provider, or another role.
- Transaction objective and stage: pre-award, first draft, negotiation, internal approval, signing, performance amendment, renewal, or termination.
- Source hierarchy: procurement file, response, award notice, framework agreement, main contract, order, statement of work, annex, technical specification, or later written confirmation.
- Requested deliverables: risk view, DOCX redline, comments, clean version, negotiation table, or signing check.
- Material unknowns: price, dates, licenses, authority, budget, technical standards, tax treatment, acceptance process, data handling, or business-approved exceptions.

Infer the reviewing side only when the request or current materials make it clear, and state the inference. If the side is genuinely ambiguous and would reverse the risk allocation, ask one targeted question before finalizing; continue with file inventory and neutral fact extraction while waiting.

## Protect The Source Files

- Inventory current files before editing. Identify the mother contract, supporting documents, duplicates, prior versions, scans, and existing redlines.
- Treat original business files as read-only. Create clearly named outputs beside or under the matter folder without overwriting the source.
- Let current-matter documents and the user's latest instructions override templates, memory, and prior drafting habits.
- Preserve absolute source paths in the working source record.
- Preserve existing tracked changes and comments unless the user asks to accept, reject, remove, or consolidate them.
- For PDF-only or scanned inputs, state whether reliable editable redlining is possible. Do not present reconstructed text as the untouched original.

Before editing a DOCX, read [matter-identity-gate.md](references/matter-identity-gate.md)
and lock its user-confirmed identity, current mother path/hash, and exact output
path. Reuse that intake record at QA and handoff; never derive expected identity
from the candidate output just to make validation pass.

## Build The Transaction Map

Before changing clauses, map the contract as a connected transaction rather than a list of headings:

1. `role and authority`: who signs, performs, instructs, accepts, pays, invoices, guarantees, owns, or bears third-party responsibility;
2. `performance flow`: subject matter, scope, milestones, dependencies, delivery, cooperation, change control, subcontracting, and completion;
3. `money flow`: price, tax, invoice, payment conditions, retention, set-off, deductions, reconciliation, and refund;
4. `acceptance flow`: standards, evidence, procedure, time limit, objections, deemed acceptance, re-performance, and consequences;
5. `risk and exit`: title/risk transfer, warranty, breach, indemnity, liability cap, suspension, termination, settlement, handover, and survival;
6. `evidence and dispute`: notices, service, records, signatures, system data, audit, governing law, jurisdiction/arbitration, and preservation.

Use the map to find broken loops and cross-clause contradictions. A clause can look reasonable alone while making payment, acceptance, termination, or proof impossible when combined with another clause.

## Run The Review

For `full redline` or `finalization`, read [review-matrix.md](references/review-matrix.md) before completing the review. Scale the matrix to the transaction; do not add irrelevant boilerplate.

Review in this order:

1. Confirm document integrity, version, hierarchy, blanks, annexes, defined terms, numbering, internal references, and template residue.
2. Test legality, authority, mandatory rules, special qualifications, enforceability, and dispute-resolution validity.
3. Test the performance, money, acceptance, change, breach, termination, settlement, evidence, and dispute loops.
4. Test risk allocation from the user's side under ordinary performance, delay, defect, non-payment, third-party claim, regulatory change, force majeure, and early exit.
5. Compare the contract against controlling procurement or transaction documents and record any silent expansion, omission, or contradiction.
6. Convert each material issue into a concrete redline, comment, business decision, or research item.

Do not rewrite for style alone. Preserve useful negotiated language and change wording only when it improves legality, operability, evidence, risk allocation, or clarity.

## Enforce Precision Redlining

Every Word redline must be a precision edit. Keep all unchanged wording as
ordinary text and wrap tracked-change markup only around the smallest continuous
unit that actually changes: usually a word, amount, date, phrase, punctuation
mark, or individual sentence.

The following is a delivery-blocking prohibition:

- Never delete the full original paragraph and insert a full replacement
  paragraph merely because that is easier to implement.
- Never use a near-total delete-and-insert pair when unchanged wording can be
  preserved outside the revision markup.
- Never treat a correct accepted-changes view as sufficient when the all-markup
  view presents the user with a large block deletion and a large block insertion.
- Never use whole-paragraph replacement to conceal a batch rewrite, formatting
  reconstruction, or tooling limitation.

This rule still applies when the clause is substantially restructured. Split the
revision into sentence- or phrase-level changes, preserve reusable text and the
clause structure, and let the reader compare old and new language locally. A
wholly new clause may be inserted as one tracked insertion, and a clause removed
without replacement may be one tracked deletion. Replacing an old clause with a
new clause is not an exception.

If the available editing method cannot produce precision revisions, do not
deliver the file. Change the implementation and rerun the DOCX validation and
all-markup visual review required by [docx-delivery.md](references/docx-delivery.md).

## Maintain An Internal Clause-Issue Record

Track material issues internally using this shape:

| Location | Classification | Severity | Adverse Scenario | Proposed Action | Fallback / Input | Source Status |
|---|---|---|---|---|---|---|
| clause / page / annex | must change / recommend / business decision / fact check | critical / high / medium / low | practical consequence | redline / comment / research | fallback or missing fact | checked / user-stated / needs check |

Apply these distinctions:

- `must change`: signing blocker, invalid or materially unenforceable term, uncontrolled major liability, payment/acceptance trap, missing essential right, or contradiction that defeats performance.
- `recommend`: meaningful but negotiable improvement to allocation, remedy, procedure, proof, or clarity.
- `business decision`: multiple legally workable options depend on price, leverage, operations, relationship, or risk appetite. Present the choice; do not decide silently.
- `fact check`: the correct text depends on identity, authority, amount, date, qualification, account, technical standard, attachment, or another fact not established by the source.

Use severity to describe consequence, not editing preference. Do not mark every drafting improvement as high risk.

The optional research-chain and private experience-index workflow is not part
of this reader package. Do not initialize or query private indexes. Continue the
ordinary review workflow below; normal source verification remains necessary
for conclusions that actually depend on current authority.

## Build The Contract Change Mapping Sheet

Read [change-mapping.md](references/change-mapping.md) when:

- the redline will feed a legal opinion, clause-by-clause change explanation, negotiation matrix, or signing checklist;
- the user returns a reviewed contract or opinion with further edits; or
- multiple dependent outputs must remain consistent.

Create the mapping sheet as an internal temporary work product for one contract inside the existing client or matter workflow. Do not create a separate client project or a new client-facing file by default. Give each substantive change a stable change ID and use the current mapping as the single source for dependent outputs.

Do not equate raw tracked-change node counts with substantive changes. Group related insertions and deletions that implement one clause-level objective, and exclude purely mechanical changes from the client-facing count with an internal reason.

Use the same change ID wherever a material issue appears across requested, applicable deliverables. Do not create a redundant comment, redline, or report item merely to carry a change ID. A user-deleted or abandoned change must not remain current in another deliverable; record its disposition only in internal version reconciliation.

For a user-deleted fact-check or metadata comment, do not mention its subject matter in any current issue or client-facing deliverable, even to say that it will not be restored. Put only its identifier and noncurrent disposition in internal version reconciliation. This prevents a negative reminder from recreating the deleted comment in substance.

## Enforce Dependent-Deliverable Correspondence

Treat correspondence between the latest contract and every legal opinion,
change explanation, negotiation table, or signing check as a delivery-blocking
requirement. Read [change-mapping.md](references/change-mapping.md) and run its
hard correspondence and freshness gate.

- Record the controlling mother contract path and a current version fingerprint
  before drafting any dependent deliverable.
- Make every client-facing item identify the exact current article, paragraph,
  item, table row, or annex location, then state the main change and reason. A
  topic label such as `payment risk` or `breach liability` is not a location.
- Derive every item from the current mapping. Do not reconstruct the opinion
  from an earlier opinion, memory, or theme-level summary.
- Treat a dependent deliverable as stale immediately after any later contract
  edit. Reconcile the contract, rebuild affected mapping rows, refresh the
  dependent deliverable, and rerun a full-document consistency check.
- Keep unresolved comments tied to their exact clause and label them as a fact
  check or decision. Never describe an unresolved comment as a completed edit.
- Require `current substantive change groups = included explanation groups +
  documented exclusions`. Record the counts internally.

Do not deliver when the equation fails, an item lacks an exact current location,
the contract version is newer than the mapping or opinion, or any clause number,
amount, date, defined term, or annex reference differs from the latest contract.
Substantive similarity is not a substitute for correspondence.

## Reconcile A User-Edited Version

Treat the user's latest file as the current authority. Compare it with prior versions to classify mapped changes as retained, user-reworded, user-deleted, newly added, or superseded. Update the mapping and dependent outputs to match the latest contract.

Do not restore user-deleted text or comments. If a deletion removes a critical substantive protection or creates a signing blocker, preserve the user's current text and raise only the consequence once in the delivery note or signing check for lawyer or business confirmation; do not reproduce the deleted wording or present the deleted change as current.

## Decide Between Redline And Comment

Read [docx-delivery.md](references/docx-delivery.md) whenever producing or modifying a Word contract.

- Use tracked revisions when the legal or commercial wording can be responsibly corrected from the available materials.
- Use comments when the answer depends on a missing fact, user approval, operational choice, negotiation authority, source-document mismatch, or current external verification.
- For a material issue, prefer a usable replacement clause over a long lecture. Add a short comment only when the user needs the consequence, decision, or fallback explained.
- For high or critical risk, do not leave only a risk label when a concrete redline is possible.
- Do not silently fill names, dates, amounts, bank accounts, qualifications, technical standards, or annex contents.
- Keep acceptable clauses quiet unless the user asks for a full clause-by-clause report.

Apply these standing Word-review defaults unless the user gives matter-specific instructions:

- Set all new tracked-change and comment author names to `审阅人`.
- Do not proactively revise or manage the contract-number field.
- Do not directly revise party/entity subject information by default; comment for verification or supplementation of identity, authority, licenses, unified social credit code, legal representative, account information, and consistency with source documents.
- Do not re-add fact-check comments the user intentionally removed, including contract-number, signing-place, party-information, or subject-information comments.

## Apply The Research Gate

Form the transaction and clause judgment before external research. Then use an available authorized original-text legal research channel to verify current rules, exceptions and adverse authority. Apply [research-sources.md](references/research-sources.md): exact original, applicable version, validity, locator and actual query time. Complete verified originals do not require duplicate searches; record any unresolved gap or conflict. Research supplies authority and counterevidence; it does not replace the final contract judgment.

Use the source-verification gate in [research-sources.md](references/research-sources.md) when a material conclusion depends on:

- current statute or judicial-interpretation wording, article number, validity, or mandatory rule;
- special regulation in procurement, medical, employment, construction, data, IP, finance, safety, food/drug, state-assets, or another regulated field;
- a formal legal basis, case, or adjudicative rule that will appear in an external review memo.

Ordinary contract review must not proactively query counterparty company facts, including registration, penalties, enforcement, litigation, company-specific qualifications, licenses, or signing authority. Check party and qualification facts only against the current contract and supplied source documents; use a targeted fact-check comment when information is absent or inconsistent. Separate company due diligence requires a specific request and an authorized source; it is not part of ordinary review.

If research is unavailable, continue every review step that does not depend on a current external source. Mark only the affected legal point `需检索确认`, identify the unavailable source or question precisely, and do not block local analysis of payment, acceptance, performance, remedies, termination, evidence, or cross-clause consistency.

Keep source status disciplined: use the contract or supplied source document for established text and facts; identify missing facts as fact checks; distinguish transaction-structure analysis from verified external authority; and use verified authority only for a current rule or adverse authority actually supported by the completed research. Keep tool/channel attribution in internal records, not production labels in artifacts. Do not add decorative law citations to routine comments.

For every issue marked as verified authority, preserve the exact authority-ledger source ID in the internal issue record. If an adverse-authority check is material, record the exact adverse source IDs actually reviewed. A Boolean, status label, or generic citation without a resolvable source ID is not verification.

When several issues are marked as verified authority under the same regulated legal topic, verify and cite each issue separately. A topic-matching source attached to one issue cannot substitute for a missing or wrong-topic source on another issue. Keep a conclusion grounded solely in the contract or supplied documents labeled as source-document rather than adding a decorative legal citation.

Match the authority to the proposition actually made: use IP authority for ownership, license scope, warranty, and third-party material rights; contract-remedy authority may support the notification, defense control, settlement, causation, loss, and cap mechanics of an IP indemnity issue.

## Run The Contract Final Gate

Before delivery, perform an internal skeptical pass from the counterparty, dispute, and enforcement perspectives:

- Can the user prove performance, delivery, acceptance, notice, breach, and loss with the records the contract requires?
- Can a payment condition, acceptance mechanism, unilateral discretion, set-off, liability exclusion, or termination condition be controlled solely by the counterparty?
- Do remedies work together, or do caps, exclusions, cure periods, exclusive-remedy language, and termination settlement cancel them out?
- Are time periods tied to observable trigger events and compatible across clauses?
- Are defined terms, amounts, dates, annexes, numbering, and cross-references consistent?
- Did the contract silently depart from procurement, response, award, technical, or authorization documents?
- Did any edit change an established fact without support or exceed the user's requested scope?
- Are unresolved business decisions, missing facts, and unverified law visible?
- Does every current material issue use one stable change ID across every requested deliverable?
- Has every user-deleted, abandoned, or superseded change been removed from the current risk summary, explanation, negotiation table, and signing check?
- Does every replacement preserve unchanged wording outside tracked-change markup and avoid a long full-paragraph delete-and-insert pair?

For Word outputs, also complete the mechanical and visual checks in [docx-delivery.md](references/docx-delivery.md). Record the actual review method only in internal notes or the chat handoff; never insert a model/provider name or internal review label into the reviewed contract or another delivered artifact.

Run the bundled read-only OOXML validator before delivering a reviewed DOCX:

```bash
python3 scripts/validate_contract_ooxml.py "<reviewed-contract.docx>" \
  --baseline "<current-mother.docx>" --identity "<internal-matter-identity.json>" \
  --require-identity --mode review --json
```

Require `identity_gate: pass`, resolve every error and review every warning.
Use `--mode finalization` for signing readiness. Without identity inputs the
legacy invocation is structural-only (`not_checked`), not delivery acceptance.
Finalization prepares a draft for real signing; it does not certify execution.
Only unchanged source fields explicitly labeled as signatures, seals or signing
dates may remain as `placeholder.signing_blank` warnings. Review them and identify
who completes them at signing. Amounts, performance/payment dates, parties,
contract numbers, new blanks and drafting prompts remain blocking. Do not fill
signature fields with invented names or dates merely to silence a validator.
Contract-number checks distinguish explicit contract/agreement identifiers and
standalone document-number labels from project/procurement numbers.
The validator checks the locked mother, number/title/parties and output path,
new or changed tracked-change/comment authors, precision-redline violations,
comment relationships, contract-number value changes, current-text placeholders,
and malformed OOXML targets. Record the report's output hash in the current
change mapping and recheck it before linking or submitting the exact file. A
`revision.block_replacement` error is delivery-blocking: rebuild that paragraph
as phrase- or sentence-level tracked changes. The validator never rewrites the
document.
Rendering and visual inspection remain mandatory because structural validation
cannot detect clipping, pagination, or visual redline defects.

When a clause-by-clause explanation or another dependent deliverable is requested, run the coverage gate in [change-mapping.md](references/change-mapping.md). Confirm that every current substantive change is accounted for, every explanation matches the latest contract, and any exclusion is documented internally.

The gate must return `pass` before delivery. A stale opinion, theme-only
explanation, missing exact clause location, or count mismatch is a
delivery-blocking failure even when the legal analysis is otherwise correct.

## Deliver The Result

Match the deliverable to the review mode:

- `quick scan`: concise blocker/high-risk list, affected clauses, practical consequence, and immediate action.
- `full redline`: reviewed DOCX with tracked revisions/comments plus a concise delivery note listing only material unresolved points.
- `finalization`: residual-issue list and signing check; provide a clean version only when the user asks to accept revisions or prepare one.
- `negotiation`: issue, preferred wording, acceptable fallback, bottom line, rationale, and expected counterargument.
- `clause-by-clause explanation`: when expressly requested, derive the clause-by-clause change explanation from the current mapping sheet and the included [change-mapping.md](references/change-mapping.md). A broader formal legal opinion is separate scope. Follow contract order and state which clause changed, the main change, and why it changed; distinguish completed redlines from unresolved comments and fact checks.

Do not create a second report that merely duplicates every Word comment unless requested. An express request for a legal opinion explaining each change is a request for the clause-by-clause explanation deliverable. State:

- reviewing side and mode;
- mother contract and controlling supporting files;
- generated outputs;
- critical/high unresolved items;
- facts or approvals still needed;
- legal points and source-document facts still needing verification;
- actual review method;
- final status: `可进入谈判`, `需业务确认`, `需补充材料`, `需检索确认`, `需律师确认`, or `可进入签署前定稿`.

The preceding review method, final status, and any AI-assistance or lawyer-confirmation note belong only in internal notes or the chat handoff. All delivered contracts, opinions, explanations, clean copies, redlines, comments, filenames, document properties and revision authors omit production labels. If a verified mandatory disclosure requirement conflicts with this, explain it in chat and resolve that boundary before delivery; do not silently add a label or suppress required disclosure.

Do not add `Codex`, `Claude`, `AI生成`, `AI辅助`, `复核方式`, `已复核`, `未复核`, `非多模型复核`, or equivalent production/review labels to artifacts. This is a production-label rule, not a ban on subject matter: retain AI-related contract provisions, product names and evidence when substantively relevant. Keep necessary legal caveats, assumptions, evidence gaps, and conventional signature/effectiveness language in professional form without naming internal workflow status.

Once the user says they edited, revised, finalized, or took over an artifact, treat that file as user-controlled and authoritative. Do not edit, regenerate, overwrite, or restore text to it without a new express request.
