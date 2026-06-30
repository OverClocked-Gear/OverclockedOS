# Canonical Relationship Vocabulary

## Purpose

Relationships connect observations, hypotheses, concepts, frameworks, capabilities, Kinetic Stack objects, applications, and outputs without duplicating content.

## Canonical Verbs

### supports

Indicates that one object provides evidence or reasoning in favor of another.

Example: `evidence:psychological_safety_paper supports hypothesis:psychological_safety_reduces_adaptation_tax`

### contradicts

Indicates that one object challenges or conflicts with another.

Example: `case:failed_transformation contradicts hypothesis:agility_always_increases_velocity`

### extends

Indicates that one object adds scope, detail, or new application to another.

Example: `concept:learning_velocity extends concept:organizational_learning`

### depends_on

Indicates that one object requires another to function, hold, or be understood.

Example: `capability:decision_velocity depends_on concept:distributed_decision_making`

### enables

Indicates that one object makes another possible or easier.

Example: `technology:cloud enables operating_model:platform_team`

### strengthens

Indicates that one object increases the effectiveness, validity, or durability of another.

Example: `concept:trust strengthens concept:psychological_safety`

### weakens

Indicates that one object reduces the effectiveness, validity, or durability of another.

Example: `concept:cognitive_load weakens capability:learning_velocity`

### measures

Indicates that one object quantifies or assesses another.

Example: `kpi:decision_cycle_time measures capability:decision_velocity`

### instantiates

Indicates that one object is a concrete instance of another.

Example: `company:example_platform instantiates business_model:marketplace`

### belongs_to

Indicates membership in a category, layer, domain, or parent object.

Example: `concept:identity belongs_to layer:human`

### influences

Indicates that one object affects another without requiring direct causality.

Example: `concept:status influences concept:fear`

### orchestrates

Indicates that one object coordinates multiple actors, resources, or components.

Example: `operating_model:ecosystem_orchestration orchestrates business_model:platform`

### transforms

Indicates that one object changes the form, state, or operating logic of another.

Example: `technology:agentic_ai transforms operating_model:customer_service`

### validates

Indicates that one object provides sufficient evidence or review to advance another's research status.

Example: `research_review:meta_analysis validates hypothesis:trust_increases_learning_velocity`

### challenges

Indicates that one object raises a critique, limitation, or unresolved issue.

Example: `review:devils_advocate challenges hypothesis:adaptability_always_improves_performance`

### requires_research

Indicates that one object has unresolved uncertainty requiring additional investigation.

Example: `hypothesis:human_adaptation_tax requires_research research_gap:cognitive_load_thresholds`

### derived_from

Indicates that one object was generated from another source, observation, or validated object.

Example: `hypothesis:learning_velocity derived_from observation:learning_pattern_cluster`

### applied_in

Indicates that one object is used in an application or context.

Example: `concept:adaptability applied_in application:mba_digital_strategy`

### taught_in

Indicates that one object is taught in a course, module, lecture, or workshop.

Example: `framework:dynamic_capabilities taught_in course:mba_digital_strategy`

### used_by

Indicates that one object is used by an application, company, capability, or workflow.

Example: `capability:customer_intelligence used_by application:web_strategy_course`

## Governance Rules

- Use canonical verbs whenever possible.
- Do not invent new relationship verbs without review.
- Prefer relationships over duplicated content.
- Relationships should be directional.
- Relationships should include confidence where possible.
- Contradictory relationships are valuable and should not be suppressed.
- Record evidence basis when a relationship affects hypothesis validation or canonical promotion.
- Use `challenges`, `contradicts`, and `weakens` to preserve adversarial findings rather than deleting them.
