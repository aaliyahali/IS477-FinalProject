#  IS 477 Final Project: Status Report 

## Team Members
- **Aaliyah Ali**  and **Rithikka Souresh**

---

## Project Updates

An update on each of the tasks described on your project plan including references to specific artifacts in your repository (such as datasets, scripts, workflows, workflow diagrams, etc).
- 

An updated timeline indicating the status of each task and when they will be completed.
- 

A description of any changes to your project plan itself, in particular about your progress so far. Also include changes you made to your plan based on feedback you may have received for Milestone 2.
- 


## Contribution Summaries

# Aaliyah Ali
During this milestone, I led the **data acquisition, cleaning pipeline development, and initial integration steps** for the project. My contributions included:

#### **Data Acquisition**

* Obtained the **Cook County Medical Examiner’s dataset** from the Cook County Public Data Portal and added it to the project’s `data/raw/` directory.
* Implemented `scripts/acquire_data.py` to programmatically download **American Community Survey (ACS 2023 5-Year)** demographic and socioeconomic data for **Cook County Census Tracts** using the **U.S. Census API**.
* Selected and included variables relevant to overdose vulnerability, including:

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
  * Creating **drug involvement indicator variables** (fentanyl, heroin, cocaine, opioids)

---

#### **Data Integration Progress**

* Downloaded and processed the **HUD USPS ZIP → Census Tract crosswalk**, saved as `data/raw/zip_to_tract_crosswalk.csv`.
* Developed `scripts/merge_datasets.py` to merge the ME data and Census tract data through the ZIP → TRACT link, producing `data/processed/merged_me_census.csv`.
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





# Rithikka Souresh 


