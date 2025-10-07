#  IS 477 Final Project: Mapping and Modeling Drug-Related Deaths in Cook County

## Team Members
- **Aaliyah Ali**  and **Rithikka Souresh**

---

## Project Goal
To analyze drug-related deaths in Cook County to uncover spatial, demographic, and temporal trends. Specifically, our goal is to analyze how the distribution of different drug types (opioids, fentanyl, cocaine, heroin, etc.) varies across time and location.  

This project will use data modeling and visualization to highlight emerging overdose patterns and public health implications.

---

##  Research Questions
1. What spatial and demographic patterns emerge when comparing overdose rates across Cook County census tracts, and which demographic characteristics are most associated with higher fatality rates?
2. How have drug-related deaths changed over time in Cook County?  
3. Which drug categories (fentanyl, heroin, cocaine, etc.) are most associated with fatal overdoses?  
4. What demographic patterns (age, race, gender) exist across drug types?  
5. Are there geographic hotspots for specific drug categories? 

---

## Data Sources
- **Cook County Medical Examiner’s Office (Public Dataset)**  (https://datacatalog.cookcountyil.gov/Health-Human-Services/Medical-Examiner-Case-Archive/cjeq-bs86/about_data)
  -  Contains detailed information on deaths investigated by the Cook County Medical Examiner’s Office, including variables such as primary cause, secondary cause, date of death, age, race, gender, and geographic location (ZIP code, latitude/longitude).

- **U.S. Census Bureau**  (https://data.census.gov/all?q=cook+county)
  -   - Provides demographic and socioeconomic characteristics of Cook County census tracts, including race/ethnicity composition, income levels, education attainment, and population density. Additionally, the spatial boundaries of Cook County – which is necessary for mapping and visualizations – will also be provided through this data source. 


---


##  Planned Methods (as per class modules)

| Step | Description | Course Module Alignment | Lead |
|------|--------------|-------------------------|------|
| 1. Data Collection | Obtain and merge Cook County Medical Examiner and Census datasets. | **Module 1: Data Acquisition & Ethics** – Handling open data responsibly and documenting sources. | Both |
| 2. Data Cleaning | Standardize drug names, correct typos, handle missing values, and format date/time variables. | **Module 2: Data Preprocessing & Wrangling** – Cleaning, transformation, and feature engineering. | Aaliyah |
| 3. Feature Creation | Create binary indicators for drug types (fentanyl, heroin, cocaine, etc.) and demographic groups. | **Module 3: Feature Engineering** – Encoding, categorization, and creating interpretable variables. | Aaliyah |
| 4. Exploratory Data Analysis (EDA) | Explore relationships between drug type, demographics, and location using plots and descriptive stats. | **Module 4: Exploratory Analysis** – Visualizing distributions and identifying trends/patterns. | Rithikka |
| 5. Statistical & Predictive Modeling | Conduct logistic regression and association rule analysis to identify key predictors of opioid involvement. | **Module 5: Modeling & Machine Learning** – Applying appropriate statistical or ML models. | Both |
| 6. Model Evaluation | Evaluate model accuracy and interpret coefficients to assess the reliability of findings. | **Module 6: Model Evaluation** – Using metrics like accuracy, AUC, and confusion matrices for validation. | Both |
| 7. Visualization & Communication | Develop spatial heatmaps, demographic bar plots, and an interactive dashboard summarizing insights. | **Module 7: Data Visualization & Communication** – Turning results into visual stories. | Rithikka |
| 8. Ethical Reflection | Reflect on the social and ethical implications of drug-related data use and misclassification risk. | **Module 8: Ethics & Interpretation** – Responsible reporting and contextual understanding. | Both |
| 9. Final Presentation | Present findings, visualizations, and conclusions in a polished final report. | **Module 9: Professional Communication** – Presenting insights effectively to technical and nontechnical audiences. | Both |

---

##  Timeline (6 Weeks)

| Week | Task | Module Connection |
|------|------|-------------------|
| **1** | Collect and document datasets; review ethical data use. | Module 1 |
| **2** | Clean data, standardize drug names, and handle missing values. | Module 2 |
| **3** | Engineer features (drug type indicators, demographic bins); begin exploratory analysis. | Module 3–4 |
| **4** | Perform regression and association analyses; interpret key predictors. | Module 5 |
| **5** | Evaluate models, visualize results with maps and dashboards. | Module 6–7 |
| **6** | Write up ethical reflection, finalize a report, and present findings. | Module 8–9 |

---
## Constraints and Gaps

In terms of constraints, with the current shutdown of the Federal government, there may be delays in the updates to federally maintained data sources (such as the US Census data). As a result, certain datasets could have reduced accuracy or limited generalizability during this period. Also, integrating the location data with the Medical Examiner’s data may be challenging – or may have certain constraints – depending on what location data the Medical Examiner’s data lists (zip codes, lat/long) is the most available. 

In terms of gaps, our team has limited prior experience with spatial modeling. We anticipate needing additional guidance in developing and interpreting geographic visualizations within Python to ensure that our mapping outputs are both accurate and meaningful.

---


##  Tools
- **Python:** pandas, geopandas, matplotlib, seaborn  
- **Jupyter Notebook:** reproducible analysis pipeline  

---

## Expected Outputs
- A cleaned, reproducible dataset for drug-related death analysis  
- Visual dashboards showing spatial and demographic patterns  
- Statistical summary of associations between drug types and outcomes  
- Policy implications and recommendations for local health departments  
