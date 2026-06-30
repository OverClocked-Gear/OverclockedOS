# Review Needed

## Ambiguous NAICS Codes

- C2531-GL Global Automobile  Light-Duty Motor Vehicle Manufacturing Industry Report.docx: filename prefix appears to be a source or publisher report code, not NAICS. Needs instructor/source confirmation before NAICS mapping.
- 42449 Soft Drink Baked Goods  Other Grocery Wholesaling in the US Industry Report.docx: five-digit code parsed from filename. Confirm exact NAICS title and whether a more specific six-digit mapping is required.

## Missing Or Uncertain Report Years

- All 14 DOCX reports need year verification. No year is visible in the filenames.
- All 7 XLSX data files need year or data-period verification. No year is visible in the filenames.

## Unclear Publisher Or Source

- All 14 DOCX reports have publisher marked unknown in the first-pass manifest because publisher is not visible from filename.
- All 7 XLSX files have publisher marked unknown in the first-pass manifest because publisher is not visible from filename.
- Treat all raw DOCX and XLSX files as licensed, instructor-only sources until rights are confirmed.

## Duplicate Or Near-Duplicate Files

- No exact duplicate filenames were found in the current raw source folders.
- Potential overlap to review: 42 Wholesale Trade in the US Industry Report.docx and 42449 Soft Drink Baked Goods  Other Grocery Wholesaling in the US Industry Report.docx. These appear hierarchical rather than duplicate, but downstream processing should preserve the distinction.
- Potential overlap to review: 31-33 Manufacturing in the US Industry Report.docx and C2531-GL Global Automobile  Light-Duty Motor Vehicle Manufacturing Industry Report.docx. These appear broad-sector and industry-specific rather than duplicate.
- Potential overlap to review: 44-45 Retail Trade in the US Industry Report.docx and ecommerce_ecommerce_worldwide_USD_en.xlsx. These are different source types but may support related commerce modules.

## Files With Multi-Cluster Value

- 31-33 Manufacturing in the US Industry Report.docx: manufacturing_industrial; automotive_mobility; retail_cpg_commerce; logistics_supply_chain.
- 42 Wholesale Trade in the US Industry Report.docx: logistics_supply_chain; retail_cpg_commerce; manufacturing_industrial.
- 42449 Soft Drink Baked Goods  Other Grocery Wholesaling in the US Industry Report.docx: retail_cpg_commerce; agriculture_food_beverage; logistics_supply_chain.
- 44-45 Retail Trade in the US Industry Report.docx: retail_cpg_commerce; advertising_media_marketing; logistics_supply_chain; technology_saas_platforms; ecommerce operator lens.
- 48-49 Transportation  Warehousing in the US Industry Report.docx: logistics_supply_chain; retail_cpg_commerce; manufacturing_industrial; automotive_mobility.
- 51 Information in the US Industry Report.docx: technology_saas_platforms; media_entertainment_sports_gaming; advertising_media_marketing.
- 52 Finance  Insurance in the US Industry Report.docx: banking_finance_insurance; technology_saas_platforms; professional_services.
- 53 Real Estate  Rental  Leasing in the US Industry Report.docx: real_estate_construction_built_environment; hospitality_travel_qsr; professional_services.
- 54 Professional Scientific and Technical Services in the US Industry Report.docx: professional_services; technology_saas_platforms; advertising_media_marketing.
- C2531-GL Global Automobile  Light-Duty Motor Vehicle Manufacturing Industry Report.docx: automotive_mobility; manufacturing_industrial; logistics_supply_chain; technology_saas_platforms.
- consumer_consumer-electronics_worldwide_USD_en.xlsx: retail_cpg_commerce; technology_saas_platforms; manufacturing_industrial; ecommerce operator lens.
- ecommerce_ecommerce_worldwide_USD_en.xlsx: retail_cpg_commerce; technology_saas_platforms; advertising_media_marketing; logistics_supply_chain.

## XLSX Data Files Without NAICS Codes

- advertising-media_advertising_worldwide_USD_en.xlsx: map by advertising/media category, geography Worldwide, currency USD.
- consumer_alcoholic-drinks_worldwide_USD_en.xlsx: map by beverage/consumer category, geography Worldwide, currency USD.
- consumer_apparel_worldwide_USD_en.xlsx: map by apparel/consumer category, geography Worldwide, currency USD.
- consumer_consumer-electronics_worldwide_USD_en.xlsx: map by consumer electronics category, geography Worldwide, currency USD.
- consumer_food_worldwide_USD_en.xlsx: map by food/consumer category, geography Worldwide, currency USD.
- consumer_pet-animal-supplies_worldwide_USD_en.xlsx: map by pet and animal supplies category, geography Worldwide, currency USD.
- ecommerce_ecommerce_worldwide_USD_en.xlsx: map by ecommerce category, geography Worldwide, currency USD.

## Instructor Decisions Before Processing

- Confirm source publisher and license terms for all DOCX and XLSX files.
- Confirm report years and data periods.
- Confirm whether any raw source can be summarized for students, or whether all outputs must remain instructor-only summaries.
- Confirm course-facing clusters for broad sectors that span many business models, especially 31-33, 44-45, 48-49, and 51.
- Confirm authoritative Web Strategy module and Digital Strategy session mappings once syllabi and course_crosswalk files are available.
- Confirm whether to create an explicit ecommerce course cluster or keep ecommerce as a cross-cluster operator lens.

## Processed Asset Pilot Review

### Uncertain Source Metadata

- RPT-005, RPT-008, RPT-010, RPT-011, and RPT-014 still have unknown publisher and unknown report year.
- DATA-001 and DATA-007 still have unknown publisher and unknown data period.
- RPT-014 uses C2531-GL as a source/report code, not NAICS. Any NAICS assignment needs instructor or authoritative source confirmation.
- RPT-010 uses broad NAICS 51. Subsegment focus is still unresolved.
- RPT-005 uses broad NAICS sector range 31-33. Narrower manufacturing subsegments are unresolved.

### Rights And Access Concerns

- All pilot source cards, data cards, industry profiles, and signal cards are instructor-facing only.
- No pilot asset should be copied into student-facing content until rights and permitted-use decisions are confirmed.
- Do not quote long passages from the raw reports or data files.
- The current pilot uses metadata-first synthesis only; it does not validate source contents inside the raw DOCX or XLSX files.

### Weak Or Thin Source Coverage

- banking_finance_insurance is supported by one broad sector report only; fintech, payments, banking, insurance, and wealth subsegments need more specific sources.
- retail_cpg_commerce has strong pilot relevance from retail and ecommerce sources, but category-specific depth is thin.
- technology_saas_platforms relies on broad information-sector coverage and ecommerce-adjacent data; dedicated SaaS, software, cloud, cybersecurity, and AI platform sources would improve coverage.
- manufacturing_industrial is supported by a broad sector report and automotive-adjacent source; industrial automation, robotics, and B2B industrial software are thin.
- automotive_mobility is supported by a global automotive manufacturing report; dealer retail, EV charging, auto finance, aftersales, and mobility services are thin.
- advertising_media_marketing is supported by advertising market data and adjacent information/retail sources; adtech, agency services, creator media, and channel-specific benchmarks are thin.

### Recommended New Industry Reports To Add Later

- Banking, payments, fintech, insurance, and wealth management reports.
- Software publishing, SaaS, cloud infrastructure, cybersecurity, AI platforms, and data services reports.
- Ecommerce platforms, online marketplaces, digital retail, and category-specific retail reports.
- Advertising agencies, digital advertising, adtech, creator economy, streaming/media, and social platform reports.
- EV manufacturing, auto retail/dealers, charging infrastructure, auto finance, aftermarket, and connected vehicle services reports.
- Industrial automation, robotics, industrial software, electronics manufacturing, and durable goods manufacturing reports.

### Course Mapping Uncertainty

- Web Strategy modules and Digital Strategy sessions remain marked TBD because authoritative syllabi and course_crosswalk files were not present in the inspected manifest context.
- Ecommerce is treated as an operator lens in this pilot, not as a formal course-facing cluster.
- Signal cards are suitable as instructor planning aids only; they are not assessment-ready and do not include quiz or exam material.
