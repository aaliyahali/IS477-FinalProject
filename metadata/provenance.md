# Provenance and Data Lineage

This document describes how the final analysis dataset `me_census_data_merged.csv` was created from the original source data.

## Source Datasets

1. **Cook County Medical Examiner Case Archive**
   - Source: Cook County Open Data Portal  
   - Format: CSV  
   - Local path: `data/raw/Medical_Examiner_Case_Archive_20251104.csv`  
   - Description: Individual-level death records including demographics, location, and free-text causes of death.

2. **U.S. Census Bureau – ACS 5-Year Estimates (2019–2023, 2023 release)**
   - Source: U.S. Census API (`acs/acs5`)  
   - Format: JSON → CSV  
   - Local path: `data/raw/census_tract_data.csv`  
   - Description: Tract-level demographic and socioeconomic indicators for Cook County, IL.

3. **HUD USPS ZIP–Tract Crosswalk**
   - Source: HUD User dataset  
   - Format: Excel originally (e.g., `ZIP_TRACT_062025.xlsx`), then filtered and joined in Python.  
   - Used to map incident ZIP codes to Census tracts.

## Transformation Steps

### 1. Acquisition (`scripts/acquire_data.py`)
- Loads the raw Medical Examiner CSV from `data/raw/`.
- Requests ACS 5-year data for Cook County tracts via the Census API.
- Saves the resulting tract-level Census table to `data/raw/census_tract_data.csv`.
- Generates SHA-256 checksums for raw files and stores them in `data/checksums/`.

### 2. Medical Examiner Cleaning (`scripts/clean_me_data.py`)
- Verifies integrity of the raw ME file using the checksum in `data/checksums/`.
- Parses and standardizes date columns; creates `Updated_Date_of_Death` and `Year_of_Death`.
- Cleans ZIP codes and basic demographic fields.
- Normalizes cause-of-death text and creates drug involvement flags:
  - `contanins_fentanyl` (fentanyl involvement; typo preserved in column name)
  - `contains_cocaine`
  - `contains_heroin`
- Outputs cleaned data to `data/processed/me_cleaned.csv`.

### 3. Census Cleaning (`scripts/clean_census_data.py`)
- Loads `data/raw/census_tract_data.csv`.
- Converts numeric columns from strings to appropriate numeric types.
- Aggregates age group counts into:
  - `Age_Under18`, `Age_18_34`, `Age_35_64`, `Age_65plus`
- Computes tract-level percentages:
  - `Pct_Black`, `Pct_Hispanic`, `Pct_Asian`, `Pct_WhiteNonHisp`
  - `Pct_BelowPoverty`, `Pct_BachelorsPlus`
  - `Pct_Unemployed`, `Pct_Uninsured`
- Saves cleaned census data to `data/processed/census_data_cleaned.csv`.

### 4. ZIP–Tract Linking and Merge (`scripts/merge_data.py`)
- Loads:
  - `data/processed/me_cleaned.csv`
  - `data/processed/census_data_cleaned.csv`
  - HUD ZIP–Tract mapping (filtered from `ZIP_TRACT_062025.xlsx`).
- Standardizes ZIP codes and derives a `TRACT` identifier compatible with Census data.
- Joins Medical Examiner records to Census tracts via the HUD crosswalk using incident ZIP codes.
- Merges tract-level socioeconomic indicators onto each death record.
- Writes final merged dataset to:  
  `data/processed/me_census_data_merged.csv`.

### 5. Analysis and Visualization (`scripts/visualize_analyze_data.py`)
- Reads `me_census_data_merged.csv`.
- Produces:
  - Descriptive plots (gender, race, age, year of death).
  - Drug involvement trends over time.
  - Race-by-drug involvement breakdowns.
  - Tract-level fentanyl involvement distribution.
  - Correlation heatmap between socioeconomic factors and fentanyl involvement.
  - Spatial scatterplots and an interactive Folium map.
- All outputs are stored in `visualizations/`.

## Integrity and Reproducibility

- Integrity of critical raw files is enforced via SHA-256 checksums stored in `data/checksums/`.
- The **entire workflow** can be reproduced by running:

```bash
python scripts/run_all.py


