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
