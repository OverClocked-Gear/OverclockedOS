# Adversarial Review Workflow

## Purpose

Define the canonical handoff sequence for hypothesis development, adversarial review, research acquisition, and theory promotion.

The CODEX should prefer constructive disagreement over premature certainty.

## Workflow Overview

```text
Observer
  -> Synthesizer
  -> Hypothesis Builder
  -> Devil's Advocate
  -> Skeptic
  -> Historian
  -> Research Director
  -> Research Radar
  -> Theory Builder
  -> Publisher
```

## Agent Roles

### Observer

Input:
- Evidence files
- Observation records
- Metadata
- Research inventory

Work performed:
- Captures what evidence directly says.
- Records provenance, metadata, and direct observations.
- Flags missing or ambiguous evidence.

Output:
- Observation notes
- Evidence metadata
- Direct claim summaries
- Review flags

Exit criteria:
- Observations are traceable, non-interpretive, and ready for synthesis.

### Synthesizer

Input:
- Observation notes
- Classified evidence
- Direct claim summaries
- Review flags

Work performed:
- Identifies recurring patterns, themes, anomalies, and signals across evidence.
- Preserves uncertainty and contradictions.
- Prepares patterns for hypothesis development.

Output:
- Pattern summaries
- Signal clusters
- Anomaly notes
- Hypothesis prompts

Exit criteria:
- Patterns are evidence-linked and ready for provisional hypothesis generation.

### Hypothesis Builder

Input:
- Pattern summaries
- Signal clusters
- Anomaly notes
- Hypothesis prompts

Work performed:
- Creates plausible, testable hypotheses.
- Links hypotheses to observations and patterns.
- Identifies supporting evidence, contradictory evidence, and research needed.

Output:
- Hypothesis object
- Provisional confidence
- Research-needed notes
- Exploratory application notes when useful

Exit criteria:
- Hypothesis is provisional, testable, evidence-linked, and ready for Devil's Advocate review.

### Devil's Advocate

Input:
- Hypothesis object
- Supporting observations
- Contradictory observations
- Research-needed notes

Work performed:
- Challenges hypothesis logic and evidence.
- Identifies contradictory evidence, alternative explanations, confounders, weak methodology, boundary conditions, and counterexamples.
- Recommends revisions or additional research.

Output:
- Devil's Advocate review
- Contradiction map
- Alternative explanation notes
- Revision recommendations

Exit criteria:
- Hypothesis has been adversarially challenged and overclaiming risks are explicit.

### Skeptic

Input:
- Hypothesis object
- Devil's Advocate review
- Existing concepts
- Existing frameworks
- Canonical objects

Work performed:
- Evaluates novelty.
- Checks whether the hypothesis restates existing theory.
- Identifies duplicate risk, naming variants, and overlap with canonical knowledge.

Output:
- Skeptic review
- Novelty assessment
- Duplicate-risk notes
- Revision or merge recommendations

Exit criteria:
- Novelty and duplicate risk are explicit before concept formation is considered.

### Historian

Input:
- Hypothesis object
- Skeptic review
- Existing frameworks
- Literature notes
- Canonical records

Work performed:
- Traces intellectual lineage, prior frameworks, first principles, and related research traditions.
- Identifies citation needs and historical context.

Output:
- Historian lineage note
- Prior-framework map
- Research tradition summary
- Citation-needed flags

Exit criteria:
- Hypothesis has sufficient lineage context to guide validation and avoid false novelty.

### Research Director

Input:
- Hypothesis object
- Devil's Advocate review
- Skeptic review
- Historian lineage note
- Research gaps

Work performed:
- Converts unresolved uncertainty into a research agenda.
- Defines validation criteria and appropriate methodologies.
- Prioritizes evidence gaps.

Output:
- Research agenda
- Research gap records
- Validation criteria
- Research priorities

Exit criteria:
- Research needed to validate, reject, or refine the hypothesis is explicit and prioritized.

### Research Radar

Input:
- Research agenda
- Research gap records
- Validation criteria
- Research priorities

Work performed:
- Identifies external sources, search terms, journals, reports, datasets, interviews, and monitoring targets.
- Converts research needs into acquisition plans.

Output:
- Research acquisition plan
- Search-term list
- Monitoring targets
- Source priority notes

Exit criteria:
- Evidence acquisition targets are actionable and tied to validation needs.

### Theory Builder

Input:
- Hypothesis object
- Devil's Advocate review
- Skeptic review
- Historian lineage note
- Research agenda
- Evidence strength assessment
- Relationship map

Work performed:
- Determines whether a validated hypothesis should become a concept, framework, relationship, or enrichment to an existing canonical object.
- Checks duplicate risk and ontology fit.
- Strengthens canonical relationships where justified.

Output:
- Theory Builder recommendation
- Concept recommendation
- Framework recommendation
- Canonical enrichment proposal
- Relationship map

Exit criteria:
- Promotion path is evidence-backed, relationship-aware, and does not duplicate canonical knowledge.

### Publisher

Input:
- Canonical knowledge
- Theory Builder recommendation
- Relationship map
- Application constraints

Work performed:
- Transforms validated canonical knowledge into books, courses, simulations, articles, lectures, and other outputs.
- Preserves provenance and uncertainty.
- Creates outputs that can re-enter the lifecycle as new observations.

Output:
- Publication-ready outputs
- Application drafts
- Output dependency notes
- New observation triggers

Exit criteria:
- Output is grounded in validated canonical knowledge and does not redefine canonical objects.

## Required Gates

- No hypothesis proceeds to validation without Devil's Advocate review.
- No hypothesis proceeds to concept formation without Skeptic novelty review.
- No concept becomes canonical without evidence strength and relationship mapping.
- No application generation occurs from unvalidated hypotheses unless clearly labeled exploratory.

## Required Artifacts

- Hypothesis object
- Devil's Advocate review
- Skeptic review
- Historian lineage note
- Research agenda
- Research acquisition plan
- Relationship map
- Theory Builder recommendation

## Status Progression

```text
Observation -> Hypothesis -> Emerging -> Validated -> Canonical -> Rejected
```

## Governance Principle

Constructive disagreement is part of the research system. Contradictions, alternative explanations, weak evidence, duplicate risk, and failed hypotheses should be preserved because they improve the quality of canonical knowledge.
