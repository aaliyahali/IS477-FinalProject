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

Each of the datasets wer used had distinct data quality challenges.To ensure analytical validity, we implemented a comprehensive data quality assessment framework addressing integrity verification, missing data, format standardization, and validation checks throughout the pipeline.

#### Integrity Verification and Provenance

The data integrity was etablished though SHA-256 check-sums that were computed immediately after the data aqusiition and verified after each step. All of the raw data files were stored with their corresponding SHA-256 files to make sure any modifications of corruptions were detected before the processing. This step was critical to confirm no data loss has occured during the download process.

#### Medical Examiner Data Quality Issues

The medical Examiner dataset had a couple signifigant dta quality challenges we had to adress. First we filtered the data set to 2019-2023 so that it would align with the Census ACS 5-year time period.Date fields were converted from strings ('MM/DD/YYYY HH:MM:SS AM/PM') to datetime objects, with year extracted for filtering and temporal analysis. The location data was problamatic because the "Incident Zip Code' fiedl had inconsistent formattin. To combat this we standardized all the zipcodes with 5-digit strings using a regex extraction and zero-padding. We ended up dropping any records with missing zip-codes as they could not be mapped to the cencus tracts. This introduces a trade-off between the completeness and the spatial validity. The last data quality challenge we adressed within the medical examiner data involved the toxicology coding. The "Primary Cause" feild was not stuctured and required extensive keyword matching to indetify the drug that was involved. Instead we created binary inducators for Fentanyl, Cocaine and Heroin by usign regular expression that could capture multiple names and synonyms. This meant that our analysis captured the presence/absence fo the drug instead of the specific variant of the substance.

#### Census Data Quality Issues

The Census ACCS data used strin-formatted numeric-values to this required some type conversion along with error handling. This process revealed that some values were intentionally hidden/supressed and showed up as werid numbers. During the conversion process these showed up as missing values and we kept them as this rather than imputing the values. This decision focused on prioritizing accuracy over the completeness of the data.

#### Crosswalk and Spatial Join Quality

The zip codes and the census tracts did not match cleanly beause one zipcode could have multiple tracts, and one tract could overlap with multiple zipcodes. To deal with this we picked a single tract that could best represent the zipcode. This was done by choosing the tract that had the highes RES-RATIO. This essentially picks the tract that had the largest share of residentuals adressed in that particular zipcode. When we joined the death record with the census data some records didn't have matching tracts. We decided to still keep these record and just record the tract-level data as missing.

#### Validation and Quality Check

After merging all of the data ran a couple checks including, (1) verifying that the number of ME records matched between input and output (no records lost during joins), (2) checking the distribution of missing values in key variables to identify systematic gaps, and (3) spot-checking a random sample of records to ensure geographic coordinates, census variables, and drug indicators aligned as expected. We foudn that 15-20% of the ME records couldn't be matched to a census tract but we were still left over 70,000 deaths with a valid tract with was a large and reliable dataset for analysis.


## Findings

Cook County experienced a signifigant rise in the drug-related death over the 5-year period we analyzed(2019-2023). The mortality jumped from 6,223 deaths in 2019 to 15,773 in 2020. This shows a 153% increase which coincides with the start of the COVID-19 pandemic. Deaths did decline to 12,102 in 2021, 10,114 in 2022, and 7,579 in 2023, but mortality in 2023 was till 22% higher than in 2019.

A key finding was the rise of fentanyl as the key substance in the fatal overdoses. During the study period fentanyl was detected in 7,571 deaths (14.6%), compared to 4,370 cocaine-involved deaths (8.4%) and 2,750 heroin-involved deaths (5.3%). Through the time-series patterns we can see major shifts in the fentanyl patterns in which fentanyl appeared in ~15% of drug deaths in 2019, dipped unexpectedly to ~10% in 2020, then increased steadily to 14% in 2021, 18% in 2022, and 21% in 2023—a 40% relative increase from 2019. While the heroin involvement fell sharply from 11% in 2019 to 4% in 2023 (a 64% decline). And lastly Cocaine involvement decreased from 9% in 2019 to 5% in 2020, then rose steadily to 14% by 2023. These patterns are likely due to fentanyl replacing heroin in the illicit markets as well as the growing fentanyl contamination of cocaine.

The demographic profiles show some interesting diparities.Males accounted for 68.8% of deaths (35,545), compared to 31.1% among females (16,114), with a male-to-female ratio of 2.2:1. Racial disparities were also severe: White individuals accounted for 53.6% of deaths (27,736), Black individuals for 41.5% (21,475), and Asian individuals for 2.7% (1,387). Substance-specific patterns varied across groups: American Indian/Alaska Native decedents had the highest fentanyl involvement (~22%), Black and White decedents showed rates of ~20% and ~15%, respectively, while Asian decedents had the lowest (~5%). Cocaine involvement was highest among Black individuals (~12%), while heroin involvement was highest among American Indian/Alaska Native (~8%) and Black decedents (~7%). These patterns coincide with structural inequalities like segregation, and unequal access to care which causes vulnerability to overdose.The disproportionate impact on Black and American Indian/Alaska Native communities demands urgent attention to health equity and targeted interventions addressing root causes of disparities.

By linking the deaths to census tract data analyzed the socioeconomic conditions that are correlated with the risk of overdose. Median income and educational attainment showed weak negative correlations with fentanyl involvement (r ≈ –0.07), while poverty, unemployment, and lack of health insurance showed positive associations. These patterns underscore how neighborhood disadvantage contributes to overdose vulnerability.

Finally, the analysis of the fentanyl involvement rates by census tracts showed signifigant heterogeneity. Most tracts (approximately 23 tracts) show fentanyl involvement rates near zero, while approximately 25 tracts show peak involvement around 0.04-0.08 (4-8%), with several tracts showing rates exceeding 0.1 (10%). The distribution is skewed to the right and has a long tail which tells us that a small number of tracts have diproportionate overdose burdens. This can be used to create more targeted interventions that are place-based on some of these high-risk neighborhoods to create a more substantial impact.

## Future Work

#### Lessons Learned


This project taught us a lot of important real-world lessons about data-science and specifically public health. A key lesson was integrating data across multiple administrative systems, in this case which was the medical examiner records and the census tract data. This data set introduced us to spatial uncertainty that we combatted with the Zip-to-tract crosswalk to link the data sets. Though this method worked for our analysis purposed it was imperfect and could definitely be made more precise. It would be beneficial to future analysis if we used precise geocoding like exact coordinates or even stree-level addresses.


Another lesson we learned was through the complexity of the free-text medical data. The medical examiner toxicology notes contained very detailed descriptions of the substances that were involved in the deaths, but concerting these to text fields into more structured indicators required a lot of manual keyword curation and more medical expertise in the field. In the future applying NLP techniques like named entity recognition models trained on medical examiner text, could automate and improve the accuracy of substance detection.


This project has also taught us about the value of strong reproducibility practices. Through the use of check-sums, cleaning code, and unified pipeline we were able to increase the transparency and allow the workflow to be replicated.


#### Future Opportunities and Expansion


Though we conducted a lot of exploratory data analysis and modeling, other approaches could strengthen our work and provide more insight. Modeling techniques such as spatial regressions or machine learning approaches could help us better isolate the neighborhood-level risk factors and focus more on the non-linear relationships. A time-series analysis could also be helpful to dive deeper into the monthly and quarterly patterns. We could also use this to look at seasonal changes regarding overdose patters and focus on any relevant policy changes and their impacts. For our purposes we uses a binary indicator for the type of substance that cause the overdose, but more advanced methods can be used to learn about polysubstance use. This can be helpful to learn about the most common substance combinations and the patterns we see in the drug supply.


Our dataset could also be enriched by linking additional datasets like treatment center locations, EMS and police overdose responses, and broader social determinant metrics (evictions, transit access, crime rates). this could help contextualize mortality patterns and identify any gaps in the harm-reduction practices. the integration of clinical data like the emergency department visits would be valuable but these may be harder to obtain due to privacy concerns and access constraints. 


Future work could focus on taking these finding and translating them to meaningful actions for public health measures. Resources like presentation in communities that are considered hotspots and cost-effectiveness analysis for interventions such as mobile clinics, or supervised consumptions sites. Through this more advanced approach to the analysis of overdoses we can ensure resources are distributed more proportionately considering the geographic and demographic disparities.

Overall, this project has established a strong reproducible foundation for the understanding of overdose patterns in Cook County. With recommendation mentioned above we can gain more insight into this and create a community-centered public health impact.

## Reproducing

The steps for reproducing can be found under the documentation folder in the reproduction_steps.md file.

## References

### Cook County Medical Examiner Case Archive

- Citation: Cook County Medical Examiner's Office. (2024). Medical Examiner Case Archive 
     [Dataset]. Cook County Open Data Portal. Downloaded as CSV November 4, 2024, 
     from https://datacatalog.cookcountyil.gov/d/cjeq-bs86
- Source: Cook County Open Data Portal  
- License/Terms: Governed by Cook County’s open data terms of use.  

### U.S. Census Bureau – ACS 5-Year Data

- Citation: U.S. Census Bureau. (2023). American Community Survey 5-year estimates 
     (2019-2023) [Dataset]. Retrieved via API from 
     https://api.census.gov/data/2023/acs/acs5
- Source: U.S. Census Bureau  
- License: Public domain as a U.S. Government work  

### HUD USPS ZIP–Tract Crosswalk

- Citation: U.S. Department of Housing and Urban Development. (2025). USPS ZIP code to 
     census tract crosswalk files: Second quarter 2025 [Dataset]. HUD User. 
     https://www.huduser.gov/portal/datasets/usps_crosswalk.html
- Source: U.S. Department of Housing and Urban Development (HUD User)  
- Used only for ZIP–to–tract linkage.  
