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


## Latest automation continuation — 19 November 2026, 00:23 IST

### New source/Pine progress

- PR [#15](https://github.com/piyushimself/files/pull/15) was squash-merged as `dd07e4eeb75a06460136ca7aa18fd711fd370b56`.
- It replaces the old ATH indicator with `ATH_Weekly_Confirmed_Strategy.pine`, requires a weekly chart, uses only the previous confirmed monthly candle, evaluates weekly exits on confirmed weekly bars, and places actual Strategy Tester stop/limit orders.
- PR #15's Chromium/build workflow [44373157611](https://github.com/piyushimself/files/actions/runs/44373157611) passed the site QA (34 collections, 32 apps, 96 iframe loads, 204 mobile reader controls and zero automated issues). The deploy job was skipped because this was a PR run. A main-branch deployment still needs confirmation.
- Static Pine source invariants passed. **TradingView compilation, symbol-specific Strategy Tester backtests, Bar Magnifier fill review and broker-cost calibration remain unperformed external validation.** Do not use the new strategy live or claim performance until those checks are done.
- Visual PDF corrections have been generated and visually sampled for 10 high-confidence documents on branch `source-pdf-corrections`; its latest correction workflow [44373234367](https://github.com/piyushimself/files/actions/runs/44373234367) passed and produced artifact `reading-room-corrected-source-pdfs`. The branch is 20 commits ahead and 4 behind main, so it still needs a clean PR/rebase and complete PDF page verification before merge.
- The corrected 647 ratings PDF now distinguishes 647 ranked category entries from 629 unique films. The 18 duplicate groups were independently re-parsed from all 647 ranked rows; unique-film statistics recalculate to average IMDb 7.58, average RT 88%, 26 films at IMDb 8.5+, 184 at 8.0+, and 53 films at 100% RT. The complete per-row CSV manifest and executable parser are still needed to make this independently reproducible from the repository.

### New Crypto Trend Rider hardening in progress

- Branch `crypto-spread-cost-model` was created from main commit `dd07e4eeb75a06460136ca7aa18fd711fd370b56`.
- This branch adds a configurable spread-cost estimate per side to the existing fee/slippage/funding model and caps partial-target percentage at 99% so a nominally partial exit cannot leave a zero-quantity leg counted as open.
- Static validation has been extended to assert both controls. A PR and CI run are still pending.
