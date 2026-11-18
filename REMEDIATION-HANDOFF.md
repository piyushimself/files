# Reading Room remediation handoff

Last updated: 2026-11-18 (Asia/Kolkata)

This file is the durable continuation point for the ongoing Reading Room remediation in this repository. Read it before doing work in a new chat. Then inspect live GitHub state because workflow/PR statuses may have changed since this checkpoint.

## User's standing instruction

The user explicitly authorized autonomous repository work: make necessary changes, test, create PRs, and merge safe fixes. Continue until every actionable finding is corrected and validated or clearly recorded as blocked by evidence, permissions, or an external dependency. Do not ask the user to restate context. Do not claim completion from a successful build alone.

Quality bar:
- Treat each page and source document as its own deliverable.
- Review mobile and desktop, typography, contrast, layout, controls, accessibility, content accuracy and readability.
- Correct root causes; run real browser QA and inspect screenshots/reports.
- Distinguish automated checks from visual/editorial review, factual verification, rights clearance, and external testing.
- Never invent facts, licences, permissions, TradingView results, or source data.

## Repository

- Repo: https://github.com/piyushimself/files
- Pages site: https://piyushimself.github.io/files/
- Default branch: main
- Public repository. Withholding originals from Pages does NOT make them private; originals remain accessible in GitHub and its history. Do not change repository visibility or rewrite history without a specific, informed confirmation.

## Latest completed UI fix

PR #12, “Fix mobile collection navigation overflow”, was merged:
- PR: https://github.com/piyushimself/files/pull/12
- Head: 8706ae97ddeef1873881c5aa63b0b5f88a39a813
- Merge commit: 347fc95e5d5610723eef7e4bc56f5f508074d74d
- Change: hide duplicate Previous/Next reader shortcuts on phone widths; collection browsing remains available through Browse collections.
- PR workflow #225 / run 44355644772 completed successfully (build/browser QA job passed); deploy was skipped as expected for a PR event.
- Main deployment workflow after merge: run 44357926956, URL https://github.com/piyushimself/files/actions/runs/44357926956. At checkpoint it was in progress. Poll it and verify deployment/live site.
- A subsequent main run 44358098251 was queued for commit ded46cb8ac707b9403252ae19504f6fdfcc80a80 (“Record post-merge mobile browser QA evidence”). Poll that too.
- Earlier main run 44356951764 for commit 3719ade5ba3dab09cc4e66d612dc0eff5d884d8e completed successfully.

## Source-document inventory and review

- 48 source files extracted: 43 PDFs, 3 DOCX, 1 TXT, 1 Pine file.
- One exact duplicate PDF pair: All_Film_Collections_Combined_compressed.pdf and All_Film_Collections_Combined_compressed (1).pdf. 47 unique source docs.
- Extracted text review artifact has 48 docs, no extraction errors; OCR needed for Aag_Ki_Kavitayen.pdf pages 27 and 90 and 1000_Creative_Educational_Cultural_Links.pdf page 82.
- Pattern scan found no common sensitive-data matches, but this is not proof of absence.
- All 48 original files remain withheld from the Pages build; none is cleared for publication. Rights/licensing/ownership remain unproven. Never publish poems, descriptions, quotes, or other substantial third-party material without documented permission/licence.
- Current editorial review: DOCUMENT-CONTENT-REVIEW.md
  https://github.com/piyushimself/files/blob/main/DOCUMENT-CONTENT-REVIEW.md
- Latest known blob SHA before handoff commit: 6c845462fb05042faef8a28097ac28437d84acee. Fetch fresh before updating.

## High-priority source findings to fix

1. Count/scope mismatches:
   - 1000_Greatest_Fictional_Books.pdf: 36 sections vs cover 26; 857 unique titles / 143 repeats; includes non-fiction/memoir.
   - 1000_Inspirations.pdf: 1,001 numbered items and one section 201 vs 1,000 claim.
   - 1000_Writing_Prompts.docx: 835 prompts, not 1,000.
   - 2000_Inspirations (1).pdf: ten section counts total 1,462, not 2,000.
   - 200_Films_Like_Frida.pdf: 220 numbered entries, 218 unique title lines.
   - 300_Films_Filmography.pdf: 298 extracted entry lines though numbering reaches 300; repair names/diacritics.
   - Cinema 900: cover says 100 x 3 = 300 while body says 300 x 3 = 900; regional subtotals support 900. library-3 reports 835 for corresponding collection; reconcile dedupe policy.
   - complete_movie_ratings.pdf: actual section counts 98 + 33 + 87 = 218, but labels imply 100 + 50 + 100.
   - complete_movie_ratings_647.pdf: named sections total 238 (100 + 50 + 88); claimed 647 unique needs a reproducible manifest and reconciliation with library-3's 649.
   - complete_movie_encyclopedia.pdf: 647 vs library-3's 649; streaming verification statement dated 2025 is stale in 2026.
2. Factual/editorial:
   - asian_books_curriculum.pdf contains “Not Asian — replace with …” placeholder and non-Asian entries in Asian list.
   - masters_of_e_art_cinema.pdf falsely claims Jane Campion is the only woman Palme d'Or winner.
   - definitive_anime_encyclopedia.pdf and ultimate_anime_guide.pdf contain known misquoted/misattributed Miyazaki line.
   - sensitive_cinema.pdf has harmful framing implying love containing violence is still love; rewrite and add specific content warnings.
   - Three_Year_Old_Reading_Guide and World_Stories_3YearOld_Guide include unsupported neuroscience claim about daily reading creating more neural pathways; remove. Reading direction guidance must be language-aware.
   - Cybersecurity_Stories_For_Your_Teams.pdf oversimplifies GDPR/NIS2/DORA incident reporting timelines; correct against official sources already cited in DOCUMENT-CONTENT-REVIEW.md.
   - Other resource directories have unverified links, outdated availability, cultural framing and attribution issues as recorded in the review.
3. Layout/visual:
   - visually inspect ratings PDFs where extraction may scramble row/column alignment; do not assume extraction defects are source defects.
   - Personal_Reference_Film_Books_Art.pdf rating glyphs extracted as ####I; inspect actual rendered pages.
   - Global kids guides and some other table PDFs have extraction ordering issues; inspect rendered pages before edits.
   - Aag_Ki_Kavitayen.pdf must preserve Hindi poetry line/stanza structure; high rights risk.
4. Pine scripts:
   - ATH - Pine.txt: timeframe mismatch (monthly logic/weekly exit), stop/target displayed but not enforced, invalid account-level compounding/CAGR/drawdown metrics; indicator, not Strategy Tester strategy.
   - Crypto_Trend_Rider_4H.pine: signals/alerts not consistently barstate.isconfirmed, Chandelier stop may loosen, initial sizing stop not enforced, partial exits distort position-level stats, no fees/slippage/spread/funding; indicator, not Strategy Tester strategy.
   - Both were only statically reviewed; not compiled/backtested in TradingView. Never claim they were.

## Immediate next actions

1. Poll workflow run 44357926956 (main deployment after PR #12 merge) and queued run 44358098251. Verify successful Pages deployment and inspect live mobile reader at phone widths.
2. Fetch fresh repository tree and current DOCUMENT-CONTENT-REVIEW.md. Continue source-level remediation, not just report annotations.
3. Reconcile film counts with reproducible title manifests. Normalize titles carefully; document alias/duplicate rules and show exact mismatches before changing claims.
4. Obtain original PDF page renderings for table/glyph problems; correct only verified defects.
5. Correct high-confidence factual/editorial issues in source documents, preserve formatting, and update review table with evidence.
6. Fix Pine code only after establishing intended semantics; add tests where possible. Compile/backtest only if a real TradingView path is available.
7. Keep source docs withheld until rights and factual/layout requirements are resolved.
8. Keep DOCUMENT-CONTENT-REVIEW.md and this handoff current. For each finding record: source, exact issue, correction commit, validation evidence, status (fixed/verified/blocked).
9. Run site-wide regression and inspect screenshots/artifacts before declaring completion.

## Automation / notification

An hourly condition-watch automation titled “Reading Room Completion Watch” is active. It checks repo commits, PRs, workflow runs, browser QA artifacts and deployment, and should notify only when all correctable work is genuinely complete or clearly blocked and documented. The automation is a status watch; it does not itself perform the repairs.



## Latest continuation checkpoint — 18 November 2026, 23:25 IST

### Deployment and CI status

- Main run [#228](https://github.com/piyushimself/files/actions/runs/44357926956) completed successfully, including deployment of the PR #12 mobile navigation fix.
- Main run [#229](https://github.com/piyushimself/files/actions/runs/44358098251) completed successfully, including deployment of the post-merge browser evidence update.
- Main run [#231](https://github.com/piyushimself/files/actions/runs/44358176598) completed successfully, including deployment of this handoff file.
- Main run [#230](https://github.com/piyushimself/files/actions/runs/44358148370) built and passed Chromium QA but its deploy job failed only because GitHub Pages was already deploying commit 3ddb7d1d30bfc3dcc574ba798e96289934073012; later runs #229 and #231 deployed successfully. This was a deployment concurrency conflict, not a site-build/browser failure.
- Latest downloaded browser artifact from run #231 reports 34 collections, 32 apps, 96 iframe loads, 20 search, 14 select, 15 filter, 3 tabs, 4 shell controls, 63 filter disclosures and zero automated issues. Contact sheets of all 34 collection mobile screenshots, 34 desktop screenshots, and the mobile app screenshots were reviewed. Selected individual screenshots were inspected at full size.

### Additional mobile reader finding and fix in progress

Visual inspection found that the collection reader toolbar's horizontally scrollable rail clipped the System font selector and text-size controls in the initial 390px mobile viewport. Although technically swipeable, those controls were not discoverable. PR [#13](https://github.com/piyushimself/files/pull/13) changes the phone layout to wrap controls into visible rows and extends Chromium QA to assert all required controls are visible, the toolbar has no horizontal overflow, Previous/Next remain hidden, and Browse collections exposes all 34 catalogue links.

- PR #13 head: cfc2d03d0a7fa94cb9e640de4c5552a6189a3043
- Workflow run #232: [44364534543](https://github.com/piyushimself/files/actions/runs/44364534543) — was in progress at checkpoint; poll before merge.
- Do not merge until the new assertions pass and its screenshots are visually inspected.

### Pine remediation in progress

PR [#14](https://github.com/piyushimself/files/pull/14) contains a proposed correction to Crypto_Trend_Rider_4H.pine:
- confirmed-bar gating for entries, add-ons, exits and alerts;
- ratcheted Chandelier stop and prior-bar stop evaluation;
- enforced initial/shared stop and gap-fill assumption;
- target high-touch fills with stop priority;
- partial P&L rolled into completed-leg metrics;
- configurable fee/slippage/funding estimates; and
- closed-leg drawdown labeling.

A static CI invariant check was added. It is not a Pine compiler or Strategy Tester run. TradingView compile/backtest and actual exchange-cost calibration remain external acceptance steps. PR #14 workflow is queued/running; poll the check run before deciding whether to merge.

ATH - Pine.txt remains unresolved. Its monthly signal and weekly exit timing, stop/target semantics, and account-level metrics need a coherent execution model; no speculative code edit has been made. Keep both Pine sources withheld.

## Next actions from this checkpoint

1. Poll PR #13 run #232; inspect report and mobile screenshots. If the wrap layout passes and looks correct, merge, then verify the main deployment.
2. Poll PR #14's workflow/check run. Inspect the static validator output. Review the Pine diff carefully; do not describe it as compiled or backtested. If CI passes and the code review is sound, merge the source correction while keeping it withheld; record TradingView validation as externally blocked.
3. Continue source-document corrections and count reconciliation. Rights evidence remains unproven for all source documents, so none is cleared for Pages publication.
4. Continue visual PDF page inspection for table/column extraction and rating glyph defects. Do not alter source entries based only on garbled text extraction.
5. Continue resolving the ATH Pine execution model, count discrepancies and factual/editorial issues listed above.



## Continuation checkpoint — 19 November 2026, 00:32 IST

### Current verified state
- PR #13 “Keep all reader controls visible on mobile” is merged. Its workflow #232 (run 44364534543) FAILED the new navigation test on seven mature-content pages: the age-gate modal intercepted the Browse collections click. The report was downloaded and inspected. The failures are genuine test failures; the rest of the run exercised 34 catalog items, 34 wrappers, 32 apps, 68 mobile page loads, 89 iframe loads and 204 reader controls.
- Root cause under investigation: QA's age-confirmation handling is not reliably dismissing the wrapper's modal before it clicks the navigation menu. The actual wrapper gate uses #age-gate and #age-confirm; the app iframe has a separate #rr-app-age-gate/#rr-app-age-confirm. The parent wrapper gate must be dismissed and verified before testing parent navigation.
- PR #17 “Fix mature age-gate handling in mobile browser QA” is open:
  https://github.com/piyushimself/files/pull/17
  Branch `fix-mature-gate-mobile-qa`, head `78b9977f7abbb66daae94491f79112964efcdc4e`.
  It uses the actual visible confirmation control, force-clicks only after checking visibility, and verifies the modal is hidden with display:none. Run #234 / 44376472525 was queued at checkpoint. Poll and inspect the resulting report/screenshots. Do not merge until the seven cases pass and no new issues are introduced.
- PR #14 “Correct Crypto Trend Rider risk and trade metrics” is merged. It remains an indicator simulation, not a Strategy Tester strategy. PR #16 “Model spread costs and guard partial exits” is open:
  https://github.com/piyushimself/files/pull/16
  Branch head `d17224f32f30cc57c4c238ac2a02bd51d1c147a6`.
  Adds configurable per-side spread cost and caps partial target percentage at 99%. Workflow run #233 / 44375453170 was still in progress at checkpoint. Poll; inspect full static validation and browser QA. Do not merge until all checks pass.
- PR #15 “Replace unreliable ATH indicator with weekly strategy” is merged as `dd07e4eeb75a06460136ca7aa18fd711fd370b56`; main workflow #231 / 44375319576 completed successfully including deployment. New source `ATH_Weekly_Confirmed_Strategy.pine` uses weekly chart guard, previous confirmed monthly data, confirmed weekly exit, real strategy.exit stop/limit orders and TradingView Strategy Tester metrics. `ATH - Pine.txt` is now marked deprecated and points to replacement. TradingView compilation/backtest, Bar Magnifier review and broker cost calibration remain unperformed; do not claim performance validation or live readiness.
- Latest source PDF correction runner run #235 / 44376439524 completed successfully on branch `source-pdf-corrections`, head `d282243ca22d119fc2e9ca6e6bd4ddcb42a67b8a`. Artifact `reading-room-corrected-source-pdfs` (ID 14461588246) was downloaded and inspected. It contains corrected versions of many PDFs plus `FILM-RATINGS-647-AUDIT.json` and `FILM-RATINGS-647-MANIFEST.csv`. The 647 ranked rows resolve to 629 unique films under title+director+year matching, across 18 duplicate groups. Calculated unique-film stats: IMDb mean 7.58, RT mean 88%, 26 IMDb 8.5+, 184 IMDb 8.0+, 53 films at 100% RT (55 ranked rows). The manifest is an artifact only so far, not yet committed to main. The source-correction branch was previously 20 commits ahead / 4 behind main; inspect its latest state and create a clean PR/rebase. Do not merge wholesale without inspecting every changed PDF page and the two exact duplicate PDFs.
- PR #16 and #17 are both open and mergeable at checkpoint.
- Latest Actions run list included #234 (PR17, queued), #233 (PR16, in progress), #235 (source PDF correction runner, completed success).

### Immediate next actions
1. Poll run #234 (44376472525) for PR #17. Inspect QA report; confirm mature wrapper gate dismissed before menu interaction on all seven mature collections. If test still fails, diagnose selectors/overlay precisely and correct before merge.
2. Poll run #233 (44375453170) for PR #16. Review spread/funding math, especially partial exit allocation and remaining position quantity, as well as static validator and full browser QA. Merge only if clean.
3. Create a new correction PR from the source-pdf-corrections branch after bringing it up to date with main. Include the reproducible 647-row manifest, parser/audit source, and corrected PDFs. Inspect every changed page, not only cover pages; ensure original files are preserved or replaced only where correction is justified. Do not publish any of these PDFs on Pages pending documented rights clearance.
4. Review corrected PDF pages for count/title labels and typography. Audit 647 manifest rows against source page images and rating sources/as-of date. The 647/629 counts are now supported by a row-level manifest but rating provenance still needs date/source evidence.
5. Continue fixing high-confidence factual/editorial findings (Asian book placeholders/scope, Palme d'Or claim, Miyazaki quote attribution, sensitive-cinema abuse framing, reading neuroscience claim, GDPR/NIS2/DORA reporting timelines, resource URL validation, stale streaming availability).
6. Continue checking source documents for visual table defects and Hindi poetry layout. Preserve rights-sensitive material withheld.
7. Update DOCUMENT-CONTENT-REVIEW.md with per-finding correction commits and validation evidence; update this handoff at every meaningful checkpoint.
8. Keep TradingView external validation clearly separated from repository static checks.


## Continuation checkpoint — 19 November 2026, 00:36 IST

### Source-PDF correction PR preparation
- A clean branch `source-pdf-corrections-clean` was created from current main commit `6cab6377a5e0234ff0f8a0a7a7c61994b1ad55bf` to avoid merging the stale/diverged 31-commit correction branch wholesale.
- It contains 10 corrected source PDFs, `tools/correct_source_pdfs.py`, the strict 647-row parser, CSV manifest, JSON audit and deduplication report. The temporary correction workflow is deliberately not included.
- The final correction workflow run [44377163391](https://github.com/piyushimself/files/actions/runs/44377163391) succeeded and produced artifact `reading-room-corrected-source-pdfs`. The parser verifies 647 rows, 629 unique films, 18 duplicate groups, 18 repeated category records, IMDb mean 7.58, RT mean 88%, 26 IMDb 8.5+, 184 IMDb 8.0+, and 53 unique 100% RT films (55 ranked rows).
- The parser's normalization was tightened after a failed run: it strips only known trailing year/category/director/“Laputa” labels; other parenthetical text is preserved. The final successful run validates the strict parser.
- The first toddler-guide heading pass produced replacement question marks because Helvetica did not support the em dash in that insertion. A second pass replaced those with colons; the final page 15 was visually inspected and now renders correctly.

### Open PRs and CI
- PR #16 `Model spread costs and guard partial exits` is open. It adds per-side spread cost to the fee/slippage/funding model and prevents 100% “partial” exits from leaving zero-quantity legs open. Its full browser QA was still running at checkpoint; poll before merge. The dashboard cost label should also be checked so per-side costs are not described as “per 8h”.
- PR #17 `Fix mature age-gate handling in mobile browser QA` is open. It addresses seven test failures caused by the mature wrapper modal intercepting Browse collections clicks. Its full Chromium QA was still running; inspect all seven cases and screenshots before merge.
- Main run [44375319576](https://github.com/piyushimself/files/actions/runs/44375319576) after PR #15 completed successfully including deployment.
- Main run [44376623677](https://github.com/piyushimself/files/actions/runs/44376623677) is running the updated QA and handoff commit; inspect its final report.
- The corrected PDFs are not publication-cleared. No licence or ownership evidence has been provided. Keep them withheld.

### Next actions
1. Poll PR #16 and #17 workflows; inspect browser reports/screenshots. Correct the PR #16 cost-label wording before merge if still inaccurate.
2. Open a PR from `source-pdf-corrections-clean`; confirm all 10 binary PDFs and audit files are in the diff, no temporary workflow is included, and no rights-sensitive files are added to the Pages artifact.
3. Inspect all changed PDF pages, not only the sampled pages; keep all originals withheld.
4. Continue the remaining count, cultural scope, placeholder, quote, URL, table layout, rating provenance, and rights findings.


## 19 November 2026 — source PDF correction refinement

- The 647-rating PDF page 21 heading was found to still say “All 647 Films Ranked” after the cover/footer correction. It has now been corrected to “All 647 Ranked Entries by IMDb Score”.
- The correction script was made idempotent per section after a partial-run failure exposed that a global completion check could re-edit already corrected cover/page-2/stat blocks. The latest correction run [44378251873](https://github.com/piyushimself/files/actions/runs/44378251873) passed and produced a fresh artifact. The page 21 rendering was visually inspected.
- All ranking table pages 21–35 were reviewed together in a contact sheet for consistent column geometry; pages 21, 26 and 34 received additional high-resolution review. The extraction concerns about Peter Mullan and the anime score columns were false positives in the high-resolution samples.
- The clean source-PDF PR branch has been updated to commit `70a0bdcf08378922cc9414b6981be872db57be93`; it includes the latest corrected 647 PDF, manifest, audit JSON and repeatable correction script.
- Rights/ownership evidence remains unavailable; all source PDFs remain withheld.


## Automation checkpoint — 19 November 2026, 00:56 IST

### Latest site QA and deployment
- PR [#17](https://github.com/piyushimself/files/pull/17) was squash-merged as `1903c3787156523193380affa23b13ed4c6d2e11`. It fixes the mature-wrapper age-gate handling in Chromium QA.
- PR #17 workflow [#246](https://github.com/piyushimself/files/actions/runs/44376472525) passed: 34 collections, 32 apps, 34 wrappers, 34 desktop pages, 68 mobile pages, 96 iframe loads, 204 mobile reader controls, 34 reader navigation menus, 7 direct mature-app gate tests, and zero automated issues.
- The #246 mobile contact sheet and all seven mature collection mobile screenshots were reviewed. Reader controls are visible in the initial 390px viewport. The direct age-gate screenshot clearly labels the prompt as self-declaration, not identity/age verification.
- Main run [#251](https://github.com/piyushimself/files/actions/runs/44380872713) for merge commit #17 was still running at this checkpoint. Its build/deployment result and live Pages state must be checked before marking the fix deployed.
- The latest previously completed main deployment was run [#247](https://github.com/piyushimself/files/actions/runs/44376623677) for commit `6cab6377a5e0234ff0f8a0a7a7c61994b1ad55bf`; it passed and deployed, but predates PR #17.

### Pine follow-up
- PR [#16](https://github.com/piyushimself/files/pull/16) remains open. Workflow [#245](https://github.com/piyushimself/files/actions/runs/44375453170) passed the Chromium suite with zero issues (same 34/32/96/204 coverage) and the static Pine invariant checks passed in the build.
- The diff adds per-side spread assumptions to entry, partial-exit and final-exit costs, caps partial target allocation at 99%, and fixes the dashboard label so spread/fee/slippage are per-side while funding is per 8-hour interval.
- Pine cost inputs remain user-calibrated assumptions, not historical exchange data. TradingView compilation/backtesting remains an external dependency. PR #16's branch is two commits behind current main and GitHub reports mergeability as unknown; refresh/recheck before merge.

### Source-PDF follow-up
- PR [#18](https://github.com/piyushimself/files/pull/18) remains open. Its latest PR workflow [#250](https://github.com/piyushimself/files/actions/runs/44378477884) passed the full Chromium suite with zero issues; its source-PDF visual-review artifact was downloaded and 19 modified pages were rendered for inspection.
- The corrections are high-confidence but do not constitute full-page editorial or rights clearance. The PDF artifact inspection found additional layout defects not yet recorded by the previous sampled review:
  1. On page 15 of `Three_Year_Old_Reading_Guide (1).pdf`, the “10” badge is rendered as vertically separated “1” and “0”; the closing teal panel also shows two missing-glyph squares after “Happy reading.”
  2. On page 15 of `World_Stories_3YearOld_Guide.pdf`, the “10” badge likewise wraps into two lines.
- These visual defects must be corrected and re-rendered before accepting the source-PDF PR. The correction script also contains two whitespace-normalization expressions written as `r'\\s+'` instead of `r'\s+'`; review/fix this idempotence-check defect before relying on repeat runs.
- All source PDFs remain withheld from GitHub Pages and no ownership/licence/permission evidence has been established. The public repository remains public; Pages withholding does not make root-level source files private.
- The source-document inventory still contains unresolved count/scope, factual, attribution, URL, table-layout, rating-provenance and rights findings. The 647-row/629-distinct-film audit is a documented rule-based result, not a global film-identity resolver.

### Completion state
Not complete. PR #17's QA is green but post-merge deployment still needs verification; PR #16 is pending branch refresh and merge; PR #18 has visual follow-up defects; multiple source-document findings and external TradingView validation remain outstanding. Do not notify completion from a passing build or merged PR alone.


## Continuation checkpoint — 19 November 2026, 01:03 IST

### Post-merge site verification
- Main run [#251](https://github.com/piyushimself/files/actions/runs/44380872713) for PR #17 merge commit `1903c3787156523193380affa23b13ed4c6d2e11` completed successfully, with both build and Pages deploy jobs green.
- Its browser artifact `reading-room-browser-qa` (ID `14463562848`) was downloaded and inspected. It reports 34 collections, 32 apps, 34 wrappers, 34 desktop pages, 68 mobile pages, 96 iframe loads, 204 mobile reader controls, 34 reader navigation menus, 7 direct mature-app gate tests and zero issues.
- GitHub Pages deployment job success is confirmed. An independent live HTTP fetch could not be completed from this environment because the site was inaccessible to the browser fetcher and outbound DNS/network resolution was unavailable; do not claim a separate live-browser verification beyond the GitHub deployment result.

### Toddler-guide PDF layout corrections
- The initial corrected-PDF review identified a two-line “10” badge in each toddler guide and two missing-glyph squares after “Happy reading.” in `Three_Year_Old_Reading_Guide (1).pdf`.
- The correction script now centers “10” on one line in both badges, removes the unsupported footer glyphs cleanly, and fixes the two whitespace-normalization expressions in its 647-PDF idempotence checks.
- Workflow [44381955172](https://github.com/piyushimself/files/actions/runs/44381955172) completed successfully, committed only the two reviewed PDF corrections to the PR branch, and uploaded artifact `toddler-guide-pdf-layout-fixes` (ID 14464436487). Both fresh page-15 renders were inspected at full size and pass the visual checks.
- PR [#18](https://github.com/piyushimself/files/pull/18) remains open pending removal of the temporary one-off workflow, a fresh PR regression run, and merge/deployment verification.

### Remaining work
- PR #16 still needs branch refresh against current main, mergeability/check revalidation and merge if clean. Its run #245 passed the full Chromium suite with zero issues and the static Pine invariants passed; TradingView compilation/backtesting and exchange-specific cost calibration remain external.
- PR #18 still contains only a high-confidence correction pass for ten PDFs; full-page editorial/factual review, remaining count/scope issues, cultural classification, URL verification, table/layout review and rating provenance remain incomplete.
- Rights/ownership evidence is still absent for the source files. Keep them withheld from Pages. The GitHub repository is public, so the root-level source files remain accessible there; changing visibility or rewriting history requires explicit informed authorization.
- The final completion report is not ready. Do not notify completion.


## Branch refresh and PDF validation checkpoint — 19 November 2026, 01:08 IST

- The source-correction branch was merged forward with current main commit `1903c3787156523193380affa23b13ed4c6d2e11` using a two-parent merge commit `f1c30eed140c053f7042d45218d715cfaf90536d`. It is now 18 commits ahead and zero behind main; the PR branch includes the mature-gate QA fix.
- The temporary one-off PDF correction workflow has been removed from the PR branch. The reproducible correction script remains.
- The latest corrected toddler-guide PDF screenshots from workflow run [44381955172](https://github.com/piyushimself/files/actions/runs/44381955172) were inspected at full size. Both page-15 “10” badges now display on one line; the Three-Year-Old guide's footer has no unsupported glyphs or visible cover-up patch.
- Main deployment after PR #17 is confirmed by run [44380872713](https://github.com/piyushimself/files/actions/runs/44380872713): build and deploy succeeded. The post-merge browser artifact (ID 14463562848) reports zero issues across 34 desktop pages, 68 mobile pages, 96 iframe loads, 204 reader controls and 34 reader navigation menus. Independent live HTTP verification remains unavailable in this environment due outbound DNS/network restrictions.
- PR [#18](https://github.com/piyushimself/files/pull/18) still needs a fresh full PR workflow after the branch refresh and final report updates, then merge and post-merge deployment verification.
- The repository remains far from full remediation: the source-document review still lists unresolved count/scope and metadata issues, unverified resource links, remaining layout/editorial checks, missing rating provenance, and absent rights evidence. Pine TradingView validation remains external. Do not notify completion.
