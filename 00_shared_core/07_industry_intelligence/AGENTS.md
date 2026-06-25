# Industry Intelligence Instructions

This folder contains raw and processed industry research for Overclocked CourseOS.

Raw reports and data files are source material, not student-facing course content.

Do not move or rename raw files unless explicitly instructed.

Use metadata-first classification:
1. NAICS classification
2. Course-facing industry cluster
3. Overclocked framework/capability tags
4. Course module/session mapping
5. Access and rights status

Preserve the original filename in source_manifest.csv.

When filenames begin with NAICS codes:
- Parse the leading NAICS code.
- Store NAICS codes as text.
- Use the NAICS code as the source classification.
- Use course_cluster as the teaching classification.
- Allow one primary course cluster and multiple secondary clusters.

Default access status for IBIS, analyst, proprietary, and licensed reports:
- student_facing_allowed: false
- access_status: licensed
- permitted_use: instructor_only_summary

Create processed assets only after manifest classification is reviewed.

Do not quote long passages from licensed sources.

Flag uncertain classifications in review_needed.md.