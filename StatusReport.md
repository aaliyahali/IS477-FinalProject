#  IS 477 Final Project: Status Report 

## Team Members
- **Aaliyah Ali**  and **Rithikka Souresh**

---

## Project Updates

An update on each of the tasks described on your project plan including references to specific artifacts in your repository (such as datasets, scripts, workflows, workflow diagrams, etc).

In terms of *project updates*: 

### Storage and Organization.

All project data and scripts follow a standardized and reproducible directory structure. Raw source files are stored under data/raw/ and are kept immutable to preserve provenance. Derived datasets produced during cleaning and transformation are stored separately in data/processed/ to maintain clear separation between original inputs and generated outputs. To support data integrity and reproducibility, each raw dataset has an associated SHA-256 checksum file stored in data/checksums/ using a consistent naming convention (<filename>.sha256). This ensures that the project can automatically verify that no raw data have been corrupted or altered over time.

The project uses consistent file-naming conventions across all components:

- Lowercase, snake_case naming for files and folders (medical_examiner_data.csv, clean_me.py)
- semantic directory roles (raw, processed, checkpoints, scripts)
- Mirrored names between files and their checksums (e.g., census_tract_data.csv ↔ census_tract_data.sha256)

This organization supports the FAIR principles—particularly Findability (logical structure, predictable names), Accessibility (clear paths), and Reusability (versioning and integrity verification). The structure is also compatible with automated workflows (e.g., Snakemake), enabling future users or graders to reproduce results from raw data in a clean, transparent pipeline.

### Workflow Automation Progress 

To ensure full reproducibility and minimize manual intervention, the project will use Snakemake to automate the entire data pipeline—from acquisition to cleaning to analysis. Each major stage of the workflow is implemented as a separate Python script stored in the scripts/ directory (e.g., acquire_data.py, clean_me.py, merge_census.py, analyze.py). Snakemake rules will orchestrate these scripts by specifying their inputs, outputs, and execution commands. For example, raw datasets in data/raw/ will trigger the acquisition rule, which generates checksum files in data/checksums/; these validated inputs will then trigger the cleaning rule to produce standardized outputs in data/processed/. This workflow is still in progress and will be adapted as our project progresses, as mentioned in the timeline. 



1. Data Acquisition

- Successfully obtained two datasets from distinct and trustworthy sources:
  - Cook County Medical Examiner Case Archive (downloaded CSV) — contains all deaths investigated by the ME’s Office, including cause, demographics, and coordinates.
  - U.S. Census Bureau (ACS 5-Year, 2023) — accessed programmatically via the Census API (scripts/acquire_data.py) to retrieve demographic, socioeconomic, and housing data at the tract level.

- Implemented a standardized acquisition workflow with automated directory creation (data/raw) and integrity checks.
  - Added variables relevant to overdose vulnerability, including income, poverty, race ethnicity, age structure, education, unemployment, uninsured rate, and median rent.

Artifacts:
- scripts/acquire_data.py
- data/raw/Medical_Examiner_Case_Archive_20251104.csv
- data/raw/census_tract_data.csv


2. Data Cleaning & Standardization

- Implemented cleaning scripts for both datasets to ensure consistency and readiness for merging, which includes standardized column names and formats. We also converted date/time and numeric fields and normalized ZIP codes and cause-of-death fields. Additionally, we added binary indicators for drug categories (fentanyl, heroin, cocaine, opioids). Also, we Created aggregated age group fields and percentage-based socioeconomic indicators for ease of analysis and even derived additional metrics (e.g., poverty %, unemployment %, uninsured %) for each census tract.

- Artifacts:
  - scripts/clean_me.py
  - scripts/clean_census.py
  - data/processed/me_clean.csv
  - data/processed/census_clean.csv


3. Data Integration

- Downloaded and processed the HUD USPS ZIP → Census Tract Crosswalk to bridge ZIP codes (in ME data) and tracts (in Census data). In ther merging process, we merged the ME and Census datasets using the crosswalk. This prroduced a unified dataset for analysis (data/processed/merged_me_census.csv). We then preserved unmatched ZIPs and flagged missing Census linkage. Finally, we confirmedthat we  ~95% ZIP coverage within Cook County and aligned Census tracts for spatial analysis.

Artifacts:
  - data/raw/zip_to_tract_crosswalk.csv
  - scripts/merge_datasets.py
  - data/processed/merged_me_census.csv

- 


4. Exploratory Data Analysis (In Progress)

Currently, we have conducted preliminary EDA in EDA.ipynb, which includes generating summary statistics for age, race, and drug type frequency, geographic distribution of overdose cases, missing value inspection and data completeness. We have also buily tract-level heatmaps with GeoPandas and done a correlation analysis between overdose frequency and Census-derived socioeconomic factors. Moving forward, we hope to provide temporal context to these spatial statistics by looking at these factors from 2018–2025.

Artifacts:
- EDA.ipynb
- visualizations folder 


- 

## Updated Timeline

| Task                                    | Original Target | Current Status | Expected Completion |
| --------------------------------------- | --------------- | -------------- | ------------------- |
| Data Collection & Ethics Review         | Week 1          | Completed    | Week 1              |
| Data Storage & Organization             | Week 2          | Completed    | Week 2              |
| Data Cleaning & Integration             | Week 2          | Completed    | Week 3              |
| Feature Creation & Enrichment           | Week 3          | Comepleted | Week 4              |
| Exploratory Data & Spatial Analysis     | Week 3–4        | STARTED     | Week 5              |
| Statistical Modeling & Pattern Analysis | Week 4–5        | Pending      | Week 6              |
| Workflow Automation & Provenance        | Week 5          | Planned      | Week 6              |
| Visualization & Communication           | Week 5–6        | Pending      | Week 6              |
| Ethical Reflection & Documentation      | Week 6          | Pending      | Week 6              |
- 

## Project Plan Changes + Next Steps 


Project Plan Changes:

  - Adjusted timeline: added one additional week for feature engineering due to complexity of drug-type categorization and spatial joins.
  - Expanded Census variable scope to include unemployment, health insurance, and median rent to strengthen socioeconomic context.
  - Introduced modular Python scripts for acquisition, cleaning, and merging to improve reproducibility and allow pipeline re-execution.
  - Implemented relative pathing and organized directories to meet reproducibility requirements outlined in course guidelines.
  - No significant scope changes to core research questions or analytical goals.

  Next Steps:

  - Complete Census-tract–level feature aggregation and drug-type rate calculations.
  - Perform initial spatial analysis (choropleth maps, tract clustering).
  - Begin model development for association or regression analysis on overdose rates.
  - Document all pipeline steps for reproducibility and metadata submission.

- 


## Contribution Summaries

### Aaliyah Ali
During this milestone, I led the **data acquisition, cleaning pipeline development, and initial integration steps** for the project. My contributions included:

#### **Data Acquisition**

* Obtained the **Cook County Medical Examiner’s dataset** from the Cook County Public Data Portal and added it to the project’s `data/raw/` directory.
* Implemented `scripts/acquire_data.py` to access the  **American Community Survey (ACS 2023 5-Year)** demographic using their API and the downloading the data for **Cook County Census Tracts**  from the US Census portal as and adding it to the project’s `data/raw/` directory.
* Selected and included variables in the US Census data relevant to overdose vulnerability, including:

  * **Income**, **poverty**, **education**
  * **Age structure**
  * **Race/ethnicity**
  * **Unemployment**
  * **Uninsured rate**
  * **Housing cost burden**

---

#### **Data Cleaning & Standardization**

* Created `scripts/clean_census.py` to:

  * Convert Census fields to numeric values
  * Derive age group totals
  * Calculate percentage-based socioeconomic indicators
* Authored `scripts/clean_me.py` to clean and standardize Medical Examiner data, including:

  * Normalizing column names and formats
  * Converting dates and numeric fields
  * Standardizing ZIP code formatting for geographic joins
  * Lowercasing and normalizing cause-of-death text fields
  * Creating **drug involvement indicator variables** (fentanyl, heroin, cocaine)

---

#### **Data Integration Progress**

* Downloaded and processed the **HUD USPS ZIP → Census Tract crosswalk**, saved as `data/raw/raw/ZIP_TRACT_062025.xlsx.csv`.
* Developed `scripts/merge_data.py` to merge the ME data and Census tract data through the ZIP → TRACT link, producing `data/processed/me_census_data_merged.csv`.
* Ensured that unmatched rows were retained and added a `has_census_data` flag to support spatial completeness evaluation.

---

#### **Reproducibility & Project Organization**

* Established a standardized directory structure:

  ```
  data/raw/
  data/processed/
  scripts/
  ```
* Verified **relative path handling** to ensure that all scripts can be executed reproducibly on any environment or after cloning from GitHub.





## Rithikka Souresh 

During this milestone, I led the **exploratory data analysis (EDA), spatial visualization, and pattern identification** for the project. My contributions included:

#### **Data Quality Assessment & Validation**

* Conducted comprehensive data quality checks on the merged dataset (`me_census_data_merged.csv`), including:
  * Shape and structure validation (dimensions, data types)
  * Missing value analysis with visual ranking of top 15 columns
  * Duplicate row detection
  * Mixed data type identification across columns
* Corrected data quality issues, including fixing the `contanins_fentanyl` typo to `contains_fentanyl`
* Generated descriptive statistics for all variables to establish baseline distributions

---

#### **Demographic & Temporal Analysis**

* Analyzed **victim demographics** through visualizations:
  * Gender distribution of drug-related deaths
  * Racial breakdown of overdose victims
  * Age distribution at time of death using histogram with KDE overlay
* Created **temporal trend analysis** showing:
  * Year-over-year changes in drug-related deaths (2019-2023)
  * Time-series evolution of drug involvement rates for fentanyl, cocaine, and heroin
  * Drug-specific prevalence trends over the five-year period

---

#### **Drug Involvement Pattern Analysis**

* Calculated prevalence rates for each drug type (fentanyl, cocaine, heroin) across the full dataset
* Developed **race-stratified drug involvement analysis**:
  * Generated cross-tabulations of drug presence by racial group
  * Created horizontal bar charts showing percentage of deaths involving each drug type by race
  * Identified disparities in drug involvement patterns across demographic groups
* Computed **tract-level fentanyl rates** and visualized their distribution to identify geographic hotspots

---

#### **Socioeconomic Correlation Analysis**

* Selected seven key socioeconomic indicators for analysis:
  * Median income, poverty rate, unemployment rate
  * Educational attainment (bachelor's degree or higher)
  * Racial composition (% Black, % Hispanic)
  * Health insurance coverage (% uninsured)
* Generated **correlation heatmap** between socioeconomic factors and fentanyl involvement
* Identified potential vulnerability indicators for overdose risk

---

#### **Spatial Visualization & Mapping**

* Created **point-based scatter plot** of all drug death locations in Cook County with:
  * Color-coding by fentanyl involvement status
  * Geographic coordinate filtering to ensure data quality
* Developed **comparative spatial analysis** showing side-by-side distributions of:
  * Fentanyl-involved deaths
  * Cocaine-involved deaths
  * Heroin-involved deaths
* Built **interactive web map** (`chicago_drug_deaths_map.html`) using Folium featuring:
  * Multi-layer heatmaps with distinct color gradients for each drug type
  * Layer toggle controls for selective visualization
 

