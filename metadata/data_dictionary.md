# Data Dictionary – `me_census_data_merged.csv`

This table describes the final merged analysis dataset located at  
`data/processed/me_census_data_merged.csv`. This is the dataset from which all of our analysis has been conducted.

| Column Name               | Type      | Description |
|---------------------------|-----------|-------------|
| `Case Number`             | string    | Unique identifier assigned by the Cook County Medical Examiner for each case. |
| `Date of Incident`        | string    | Date and time when the incident leading to death occurred (raw text from ME data). |
| `Date of Death`           | string    | Date and time of death as recorded by the Medical Examiner (raw text). |
| `Age`                     | float     | Age of the decedent in years at time of death. |
| `Gender`                  | string    | Gender of the decedent (as recorded by ME office). |
| `Race`                    | string    | Race of the decedent (as recorded by ME office). |
| `Latino`                  | bool      | Indicator for whether the decedent was recorded as Latino/Hispanic. |
| `Manner of Death`         | string    | Manner of death classification (e.g., Accident, Suicide, Homicide, Natural). |
| `Primary Cause`           | string    | Free-text primary cause of death as entered in the ME system. |
| `Primary Cause Line A`    | string    | Additional structured line for primary cause of death (if present). |
| `Primary Cause Line B`    | string    | Additional structured line for primary cause of death (if present). |
| `Primary Cause Line C`    | string    | Additional structured line for primary cause of death (if present). |
| `Secondary Cause`         | string    | Free-text secondary cause(s) of death if recorded. |
| `Gun Related`             | string    | Indicator from ME data for whether the death involved a firearm. |
| `Opioid Related`          | string    | Original ME flag indicating opioid involvement (not used directly for classification). |
| `Cold Related`            | bool      | Indicator for deaths related to cold exposure. |
| `Heat Related`            | bool      | Indicator for deaths related to heat exposure. |
| `Commissioner District`   | float     | Cook County Commissioner district for the incident, if available. |
| `Incident Address`        | string    | Street address where the incident occurred (if available). |
| `Incident City`           | string    | City where the incident occurred. |
| `Incident Zip Code`       | string    | ZIP code of the incident location (raw, used for ZIP→tract linkage). |
| `longitude`               | float     | Longitude of the incident or death location. |
| `latitude`                | float     | Latitude of the incident or death location. |
| `location`                | string    | Text representation of coordinate pair from the ME dataset. |
| `Residence City`          | string    | City of residence of the decedent (if recorded). |
| `Residence Zip`           | string    | ZIP code of residence (may be missing or non-Cook County). |
| `OBJECTID`                | int       | Internal object ID used by the source system. |
| `Chicago Ward`            | float     | Chicago ward number (if applicable for city deaths). |
| `Chicago Community Area`  | string    | Chicago community area name (if applicable). |
| `COVID Related`           | string    | Original ME indicator for whether the death was COVID-related. |
| `Updated_Date_of_Death`   | datetime  | Cleaned and parsed date of death used for analysis. |
| `Year_of_Death`           | int       | Extracted calendar year of death (from `Updated_Date_of_Death`). |
| `contanins_fentanyl`      | bool      | **Typo column name** carried through from earlier processing; indicates whether the primary/secondary cause text suggests fentanyl involvement. Treated as equivalent to `contains_fentanyl` in analysis. |
| `contains_cocaine`        | bool      | Indicator for whether the cause-of-death text indicates cocaine involvement. |
| `contains_heroin`         | bool      | Indicator for whether the cause-of-death text indicates heroin involvement. |
| `ZIP`                     | string    | Incident ZIP code standardized for joining with the ZIP→tract crosswalk. |
| `RES_RATIO`               | float     | Proportion of residential addresses in the ZIP/tract crosswalk (from HUD ZIP–tract data). |
| `NAME`                    | string    | Census tract name (e.g., "Census Tract 101; Cook County; Illinois"). |
| `TotalPop`                | int       | Total population of the Census tract (ACS 5-year estimates). |
| `White_NonHisp`           | int       | Count of non-Hispanic white residents in the tract. |
| `Black`                   | int       | Count of Black residents in the tract. |
| `Asian`                   | int       | Count of Asian residents in the tract. |
| `Hispanic`                | int       | Count of Hispanic/Latino residents (any race) in the tract. |
| `MedianIncome`            | float     | Median household income in the tract (inflation-adjusted dollars, ACS). |
| `BelowPoverty`            | int       | Count of individuals below the federal poverty line in the tract. |
| `BachelorsOrHigher`       | int       | Count of individuals with a bachelor’s degree or higher. |
| `Male_Under18`            | int       | Count of male residents under age 18. |
| `Female_Under18`          | int       | Count of female residents under age 18. |
| `Male_18_34`              | int       | Count of male residents ages 18–34. |
| `Female_18_34`            | int       | Count of female residents ages 18–34. |
| `Male_35_64`              | int       | Count of male residents ages 35–64. |
| `Female_35_64`            | int       | Count of female residents ages 35–64. |
| `Male_65plus`             | int       | Count of male residents ages 65 and older. |
| `Female_65plus`           | int       | Count of female residents ages 65 and older. |
| `LaborForce`              | int       | Number of individuals in the labor force in the tract. |
| `Unemployed`              | int       | Number of unemployed individuals in the tract. |
| `NoHealthInsurance`       | int       | Count of individuals without health insurance. |
| `MedianRent`              | float     | Median gross rent in the tract (ACS). |
| `STATE`                   | string    | State FIPS code (Illinois = "17"). |
| `COUNTY`                  | string    | County FIPS code (Cook County = "031"). |
| `Age_Under18`             | int       | Total population under age 18 (male + female). |
| `Age_18_34`               | int       | Total population age 18–34 (male + female). |
| `Age_35_64`               | int       | Total population age 35–64 (male + female). |
| `Age_65plus`              | int       | Total population age 65 and above (male + female). |
| `Pct_Black`               | float     | Percent of tract population that is Black. |
| `Pct_Hispanic`            | float     | Percent of tract population that is Hispanic/Latino. |
| `Pct_Asian`               | float     | Percent of tract population that is Asian. |
| `Pct_WhiteNonHisp`        | float     | Percent of tract population that is non-Hispanic white. |
| `Pct_BelowPoverty`        | float     | Percent of tract population below the poverty line. |
| `Pct_BachelorsPlus`       | float     | Percent of tract population with a bachelor’s degree or higher. |
| `Pct_Unemployed`          | float     | Percent of the labor force that is unemployed. |
| `Pct_Uninsured`           | float     | Percent of tract population without health insurance. |
| `TRACT`                   | string    | Census tract identifier (11-digit FIPS code used for joining with spatial boundaries). |
