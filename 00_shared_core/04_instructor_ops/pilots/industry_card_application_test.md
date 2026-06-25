# Industry Card Application Test

## Test Objective

Determine whether the processed industry intelligence cards are sufficient to generate useful, differentiated Web Strategy and Digital Strategy course materials without reopening raw industry reports or data files.

## Raw-Source Constraint

No files inside `00_shared_core/07_industry_intelligence/raw_sources/` were opened or used. The test used syllabi, Overclocked materials, and processed industry intelligence cards only.

## Outputs Created

- `00_shared_core/02_Web_Strategy/working_drafts/module_04_capital_one_brand_pod_pilot.md`
- `00_shared_core/01_Digital_Strategy/working_drafts/capital_one_infrastructure_live_lab_pilot.md`

## 1. Cards And Source Materials Used

| Filename | Type | Why selected | Output supported |
|---|---|---|---|
| `RPT-011_52-finance-insurance.md` | Source card | Provides the banking/finance source anchor, NAICS 52 classification, access posture, and course-use notes around trust, risk, data, regulation, onboarding, account flows, and digital operating models. | Web Strategy draft; Digital Strategy draft |
| `IND-banking_finance_insurance.md` | Industry profile | Defines the cluster as regulated digital services shaped by trust, risk, data, compliance, service reliability, and customer experience. | Web Strategy draft; Digital Strategy draft |
| `SIG-banking-trust-friction.md` | Signal card | Supplies the core customer-facing insight: regulated services must balance confidence, compliance, and completion. | Web Strategy Team A; Digital Strategy risk/debrief |
| `SIG-banking-data-governance.md` | Signal card | Supplies the governance insight: segmentation, personalization, and automation create value only with consent, security, and explainability. | Web Strategy Team B; Digital Strategy launch conditions |
| `Web Strategy - Iowa Online Course Syllabus - Spring 2026.docx` | Course syllabus | Identified Module 4, Enabling Infrastructure, and its objectives around digital infrastructure and infrastructure decisions. | Web Strategy draft |
| `Digital Strategy - Syllabus - Fall 2025.docx` | Course syllabus | Identified Week/Module 2, Digital Evolution & Infrastructure, as the best fit for infrastructure readiness and digital growth. | Digital Strategy draft |
| `OVERCLOCKED_CHAPTER OVERVIEW.docx` | Overclocked chapter overview | Confirmed Chapter 4 as Digital Infrastructure and linked infrastructure to Chapter 6 insights and broader Overclocked sequence. | Both drafts |
| `OVERCLOCKED_STUDENT_TEXT.docx` | Overclocked manuscript | Supplied Chapter 4 concepts, Capital One as an infrastructure case context, TOE, five-layer stack, infrastructure maturity, and the infrastructure-as-competitive-capability framing. | Both drafts |
| `OVERCLOCKED_ APPENDIX B - The Overclocked Framework Library.docx` | Framework library | Supplied Five-Layer Technology Stack, Kinetic Strategy, and Insight Value Chain framework definitions. | Digital Strategy draft; audit |
| `OVERCLOCKED_ APPENDIX G - Enterprise AI Reference Guide.docx` | Framework/reference guide | Supplied AI operating model, AI governance questions, and AI readiness dimensions. | Digital Strategy draft |

## 2. Traceability Audit

### Claims From Overclocked

- Infrastructure is a competitive capability rather than background plumbing.
- Chapter 4 aligns with digital infrastructure, TOE, integrated technology stack, infrastructure maturity, and Capital One as a case context.
- TOE evaluates technology, organization, and environment together.
- The Five-Layer Technology Stack can be used for infrastructure and AI readiness analysis.
- The Insight Value Chain converts data into action through capture, integration, analysis, synthesis, planning, execution, and measurement.
- Kinetic Strategy evaluates velocity and adaptability.
- Digital Horizon Planning separates optimization, extension, and transformation.
- AI readiness requires leadership, usable data, infrastructure, workforce, governance, and culture.
- AI governance should address transparency, accountability, privacy, security, compliance, and ethics.

### Claims From Processed Industry Cards

- Banking/finance is a regulated digital-services context where trust, risk, data, compliance, and service reliability shape customer experience.
- Finance and insurance uses trust systems, risk management, data advantage, and regulation as relevant Overclocked connections.
- Web Strategy use can focus on trust cues, onboarding, disclosure design, account flows, lead quality, and secure service journeys.
- Digital Strategy use can focus on risk, governance, data products, and digital operating models.
- Trust friction requires balancing confidence, compliance, and completion.
- Data advantage requires consent, security, explainability, and governance.

### Claims That Remain Assumptions

- Capital One is appropriate as the common brand/app inspection object for students because Overclocked uses it as a Chapter 4 infrastructure case. This is supported by Overclocked, but any current public surface details must be observed by students.
- A hypothetical AI-enabled financial guidance capability is pedagogically plausible for a banking context. It is a scenario design choice, not a claim that Capital One currently offers or is building that capability.
- Suggested metrics such as authentication success, completion rate, safe-escalation rate, complaint rate, and compliance exception rate are teaching metrics, not sourced Capital One metrics.

### Content Requiring External Or Current Verification Before Student Use

- Any statement about current Capital One website/app features, product flows, AI tools, account-management paths, or support capabilities.
- Any claim about Capital One's current regulatory posture, AI roadmap, data architecture, cloud architecture, or internal systems.
- Any current performance benchmark, market claim, adoption statistic, customer metric, or compliance event.

## 3. Raw-Source Independence Test

- Were raw reports needed? No.
- Did the processed cards provide sufficient context? Yes, for a lightweight undergraduate application and a graduate executive workshop draft.
- What was missing from the cards? The cards did not include confirmed publisher/year, source-specific evidence, dated industry trends, subsegment specificity, current course module/session mappings, or examples of permitted student-facing claims.
- Effect on output quality: The drafts were useful but intentionally conservative. They rely on framework application and public student observation rather than industry-specific factual claims.

## 4. Course Differentiation Test

| Dimension | Web Strategy output | Digital Strategy output |
|---|---|---|
| Cognitive level | Apply and analyze a public website/app surface. | Evaluate and create a 90-day executive recommendation. |
| Delivery mode | Undergraduate asynchronous discussion extension. | Graduate synchronous live workshop. |
| Decision complexity | Identify friction, infrastructure layers, improvement, and metric. | Decide preconditions, pilot scope, exclusions, risk, and scale-up KPI. |
| Student workload | Under 30 incremental minutes. | 20-25 minutes prep plus 35-45 minutes live workshop; optional memo. |
| Expected evidence | Public observation, course concepts, and concise reasoning. | Framework-based executive judgment, scenario tradeoffs, and risk-balanced KPI. |
| Instructor involvement | Light; prompt can sit inside existing discussion. | High; requires facilitation, timing, role assignment, and debrief. |

## 5. Card-Schema Improvement Recommendations

### Source Cards

- Add `student_safe_claims` for claims that can be used without reopening raw sources.
- Add `current_verification_required` for claims that must be checked externally before use.
- Add `course_module_candidates` and `course_session_candidates` after crosswalk review.
- Add `recommended_activity_types`, such as discussion, live lab, case warmup, memo, or operator audit.
- Add `known_limitations` to separate broad-sector weakness from source uncertainty.

### Data Cards

- Add `data_period`, `publisher_confirmed`, and `metric_fields_available` when verified.
- Add `allowed_aggregation_level` to clarify what can be summarized.
- Add `category_to_course_lens` for non-NAICS market/category files.
- Add `chart_or_table_safe_for_students` with yes/no/review-needed.

### Industry Profiles

- Add `best_course_fit` with undergraduate, graduate, or both.
- Add `operator_surfaces_to_inspect`, such as homepage, app listing, onboarding, support, account flow, or product page.
- Add `decision_scenarios` for graduate workshops.
- Add `thin_coverage_warning` with recommended source additions.

### Signal Cards

- Add `student_prompt_ready` flag.
- Add `executive_decision_ready` flag.
- Add `sample_metric_options`.
- Add `risk_level` for low, medium, or high-stakes use.
- Add `needs_current_brand_verification` flag.

## 6. Overall Result

Rating: Pass with revisions.

The card system passed the core test: it supported differentiated, course-appropriate drafts for Web Strategy and Digital Strategy without reopening raw industry reports or data files. The undergraduate output stayed light, asynchronous, and website/app-operator oriented. The graduate output shifted to an executive launch-readiness decision with governance, infrastructure, data, AI, compliance, and risk tradeoffs.

The needed revisions are mostly schema improvements. The cards are strong enough for instructor planning, but future cards should make student-safe claims, verification requirements, course mapping, activity fit, and metric options more explicit. That would reduce the amount of interpretation needed when turning cards into course materials.

Recommendation:

- Revise the card templates before large-scale processing.
- Run one more application pilot in a different cluster, preferably retail_cpg_commerce or technology_saas_platforms.
- After the second pilot, scale processing to the remaining industry sources in small reviewed batches.
