# Mapping and Modeling Drug-Related Deaths in Cook County 

## Contributors
- Aaliyah Ali 
- Rithikka Souresh 

## Summary 

Drug overdoses have emerged as one of the most pressing public health crises in the United States, with synthetic opioids such as fentanyl contributing to a historic rise in mortality. Cook County, Illinois — home to nearly 5.1 million residents and encompassing Chicago as well as diverse suburban and industrial regions — has witnessed particularly severe impacts. The purpose of this project is to map, quantify, and contextualize drug-related deaths across Cook County by linking individual-level mortality records from the Cook County Medical Examiner's Office (ME) with demographic and socioeconomic characteristics of local census tracts.

The project seeks to answer several interconnected research questions:
- How do drug-related deaths vary spatially across Cook County neighborhoods and census tracts?
- Which demographic or socioeconomic characteristics are most associated with higher overdose fatalities?
- Which substances — fentanyl, heroin, cocaine, or others — most frequently appear in fatal overdoses, and how has their involvement changed over time?
- Are there clear geographic hotspots for fentanyl or other substances?
- How do race, ethnicity, gender, and age shape the distribution of drug-related mortality?

To address these questions, we integrate two primary data sources:

(1) the Cook County Medical Examiner’s Case Archive, which provides individual-level death records including age, race, gender, cause of death, location coordinates, and free-text toxicology fields; and
(2) the U.S. Census Bureau ACS 5-Year (2023) dataset, which provides tract-level socioeconomic statistics such as income, poverty, race composition, education, insurance coverage, and housing costs. Because the ME data uses ZIP codes, we incorporate a third dataset from the HUD USPS ZIP–Tract Crosswalk to map incident ZIP codes into census tracts.

This project followed the end-to-end data lifecycle from acquisition, cleaning, integration, quality assessment, analysis, visualization, provenance, and reproducibility. All processing steps were scripted in Python, all data transformations are logged, and the entire workflow can be re-run with a single command (python scripts/run_all.py).

*Key Findings*

1. Fentanyl is overwhelmingly the dominant substance involved in drug-related deaths.
Across the merged dataset, fentanyl appeared in a substantial majority of fatal overdoses, often alongside other substances (polysubstance use). Cocaine and heroin appear frequently but significantly less often.

2. Overdose deaths are not uniformly distributed across Cook County.
Spatial scatterplots and hotspot analyses show concentrated clusters in specific Chicago community areas, particularly on the West Side and near certain South Side neighborhoods. Suburban areas show lower but non-negligible patterns.

3. Race and socioeconomic inequalities appear prominently.
Tracts with higher poverty rates, lower median income, higher unemployment, and larger Black populations show significantly higher fentanyl-involved death rates.
Correlation heatmaps reveal strong positive associations between fentanyl involvement and socioeconomic distress indicators.

4. Overdose deaths increased sharply over time.
The annual trend plot shows increasing deaths each year, with notable spikes in 2020–2022, consistent with national patterns associated with the COVID-19 pandemic and fentanyl market shifts.

5. Age distribution reveals overdoses are concentrated among adults 25–54.
Younger minors and older adults show comparatively low representation.

These findings together point toward a complex interplay of substance availability (e.g., fentanyl replacing heroin), structural inequalities, and neighborhood-level vulnerability. By linking health outcomes with demographic context, this project provides a foundation for more targeted public health interventions and resource allocation.

All data, workflow scripts, figures, and metadata are included in this repository, and all analyses are fully reproducible. The merged dataset is available through Box due to storage constraints and redistribution rules, and instructions are provided below for reproducing the data pipeline end-to-end.

## Data Profile 

This project uses three carefully curated datasets, each representing a different stage of the data lifecycle. All datasets are described below, including their origin, structure, access method, licensing constraints, and transformation steps.

1. Cook County Medical Examiner Case Archive (Individual-Level Mortality Data)

Source: Cook County Open Data Portal
Access Method: Direct CSV download (manual, due to portal restrictions) -- available in Box link 
File: data/raw/Medical_Examiner_Case_Archive_20251104.csv
License: Cook County Open Data Terms; redistribution permitted but we store via Box to limit repository size.

The dataset contains ~92,000 death investigation records with fields including case number, dates, age, gender, race, toxicology, cause of death, and location. These records include both natural and unnatural deaths, but our analysis focuses on drug-related fatalities. Important considerations include:
- Many “Primary Cause” and “Secondary Cause” fields are free text, requiring cleaning and drug keyword detection.
- ZIP codes are inconsistently formatted; some appear missing or malformed.
- A subset of deaths occurs outside Cook County; these are preserved but may not match Census tracts.

Ethical considerations include respecting privacy: even though this is public data, it contains sensitive mortality information. We do not redistribute raw files publicly in GitHub; instead, they are provided through Box for grading purposes.


2. U.S. Census Bureau ACS 5-Year (2019–2023, 2023 Release)

Source: U.S. Census API
Access Method: Programmatic API request
File: data/raw/census_tract_data.csv
License: U.S. Government public domain data

Variables collected include:
- Race/Ethnicity: White (non-Hispanic), Black, Asian, Hispanic
- Socioeconomic indicators: Median income, poverty count, unemployment, education, uninsured rate, rent burden
- Population age distribution: Under 18, 18–34, 35–64, 65+

Census ACS data is essential for contextualizing overdose patterns in relation to neighborhood conditions. Since ACS is a rolling estimate sampled over multiple years, small sample noise is expected but generally does not bias large-tract analysis.

3. HUD USPS ZIP–Tract Crosswalk

Source: HUD User USPS Crosswalk Files
Access Method: Manual Excel download (public dataset)
File: data/raw/ZIP_TRACT_062025.xlsx
License: HUD open-use policies

This dataset maps ZIP codes to Census tracts, along with a residential ratio (RES_RATIO). The ME data only provides ZIP codes, so this crosswalk is essential for joining individual-level death records to tract-level Census data. Without it, spatial demographic analysis would not be possible.

4. Merged Dataset (Final Analysis Dataset)

File: data/processed/me_census_data_merged.csv
Columns: Fully documented in metadata/data_dictionary.md

This dataset contains each ME record enriched with:
- Drug involvement indicators (fentanyl, heroin, cocaine)
- Cleaned ZIP codes and derived tract codes
- Socioeconomic and demographic tract-level Census variables
- Percentage-based indicators (Pct_Black, Pct_Poverty, etc.)
- Age group totals

This is the dataset used for all EDA, spatial modeling, and correlation analyses.

## Data Quality 

