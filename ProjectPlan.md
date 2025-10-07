#  IS 477 Final Project: Mapping and Modeling Drug-Related Deaths in Cook County

## Team Members
- **Aaliyah Ali**  and **Rithikka Souresh**

---

## Project Goal

This project aims to analyze drug-related deaths in Cook County to uncover spatial and demographic trends over time using open-source public health data. Specifically, we seek to understand how the distribution of key drug categories (e.g., fentanyl, heroin, cocaine, prescription opioids) varies across time, demographic groups, and geographic areas.

Through data modeling, visualization, and integration of census tract–level demographics, our analysis will provide insight into socioeconomic-level factors associated with overdose risk and highlight emerging public health disparities across Cook County.

This work is particularly important given the rising prevalence of synthetic opioids and polysubstance use in the region. By connecting the Cook County Medical Examiner’s data to demographic and socioeconomic indicators, we aim to build a picture of which communities face the highest burden and what social and/or structural factors may be driving these trends.

Our goal is to produce interpretable, visually compelling results that could inform policymakers, public health officials, or community-based organizations seeking to develop more targeted overdose prevention strategies.

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
-  Use: Identify and categorize drug-related deaths; analyze demographic and temporal trends

- **U.S. Census Bureau**  (https://data.census.gov/all?q=cook+county)
  -  Provides demographic and socioeconomic characteristics of Cook County census tracts, including race/ethnicity composition, income levels, education attainment, and population density. Additionally, the spatial boundaries of Cook County – which is necessary for mapping and visualizations – will also be provided through this data source. 
- Use: Merge with Medical Examiner data to identify patterns between overdose rates and community-level characteristics

---


## Planned Methods


| Step | Description | Course Module Alignment | Lead |
|------|--------------|-------------------------|------|
| **1. Data Collection & Ethics Review** | Obtain and merge datasets from the **Cook County Medical Examiner’s Office** and **U.S. Census Bureau** (tract-level demographics). Document data licenses and ethical considerations. | **Modules 1–3: Data Lifecycle, Ethical Data Handling, and Data Collection** – Understanding open data ethics, API access, and multi-source acquisition. | Both |
| **2. Data Storage & Organization** | Organize raw and cleaned datasets into a reproducible folder structure (raw, processed, analysis). Ensure consistent file naming and metadata documentation. | **Modules 4–5: Data Storage & Organization** – File system structure, relational schema design, and naming conventions. | Aaliyah |
| **3. Data Cleaning & Integration** | Standardize drug names, correct typos, handle missing values, and merge with demographic and geographic data using census tract codes. | **Modules 7 & 10: Data Integration and Cleaning** – Schema alignment, missing data handling, and text normalization. | Aaliyah |
| **4. Feature Creation & Enrichment** | Create new columns for drug type indicators (fentanyl, heroin, cocaine, etc.), opioid involvement, and demographic categories (age bins, race groups). Add census features like income or education. | **Modules 6 & 8: Extraction and Enrichment, Feature Engineering** – Deriving new analytical variables. | Aaliyah |
| **5. Exploratory Data & Spatial Analysis (EDA)** | Visualize distributions of drug-related deaths across demographics and census tracts using plots and spatial maps. Identify trends and potential hotspots. | **Modules 4 & 9: Exploratory Analysis and Data Quality** – Visual and statistical pattern exploration and data reliability checks. | Rithikka |
| **6. Statistical Modeling & Pattern Analysis** | Perform logistic regression and association rule analysis to identify relationships between substances, demographics, and locations. | **Module 5: Modeling & Machine Learning** – Applying and interpreting regression or association models. | Both |
| **7. Workflow Automation & Provenance** | Develop a reproducible Jupyter/Quarto workflow from raw data import to final visualization. | **Modules 11–12: Workflow Automation & Provenance** – Ensuring process traceability and automation. | Both |
| **8. Visualization & Communication** | Create geographic heatmaps, demographic visualizations, and summary dashboards to communicate findings. | **Modules 7 & 13: Visualization and Reproducibility** – Transparent presentation and replicable visual analysis. | Rithikka |
| **9. Ethical Reflection & Documentation** | Reflect on ethical implications such as privacy, representation, and potential bias. Document metadata, methods, and reproducibility details. | **Modules 2, 13 & 15: Ethics, Reproducibility, and Metadata** – Contextual and transparent reporting. | Both |
| **10. Final Report & Presentation** | Compile findings, visualizations, and interpretations into a professional report and presentation. | **Module 9 & 15: Professional Communication & Documentation** – Presenting results effectively for technical and nontechnical audiences. | Both |

---

## Timeline

| Week | Task | Module Connection |
|------|------|-------------------|
| **Week 1** | Collect datasets (Cook County + Census), review ethical guidelines, and document licenses. | Modules 1–3 |
| **Week 2** | Organize data directories, perform initial cleaning, and integrate datasets via census tract. | Modules 4–7 & 10 |
| **Week 3** | Engineer features (drug categories, demographics), enrich data with census variables, and begin EDA. | Modules 6–8 |
| **Week 4** | Conduct regression and association analyses to uncover spatial and demographic patterns. | Module 5 |
| **Week 5** | Build spatial visualizations, automate workflow, and validate findings for reproducibility. | Modules 9, 11–12, 13 |
| **Week 6** | Write ethical reflection, document metadata, and compile a notebook with reproducible analysis. | Modules 2, 13, 15 |



---
## Constraints and Gaps

In terms of constraints, with the current shutdown of the Federal government, there may be delays in the updates to federally maintained data sources (such as the US Census data). As a result, certain datasets could have reduced accuracy or limited generalizability during this period. Also, integrating the location data with the Medical Examiner’s (ME) data may be challenging – or may have certain constraints – depending on what location data the ME’s data lists (zip codes, lat/long) is the most available. From a preliminary look at the ME’s data,some records may lack demographic or location data, which constrains the completeness of the analysis. Also, some toxicology results may not explicitly list all the detected substances – or may report compound analogs inconsistently – which can make it more challenging to distinguish between prescription, illicit, and synthetic variants of similar drugs.

In terms of gaps, our team has limited prior experience with spatial modeling. We anticipate needing additional guidance in developing and interpreting geographic visualizations within Python to ensure that our mapping outputs are both accurate and meaningful.

---


##  Tools
- **Python:** pandas, geopandas, matplotlib, seaborn, plotly (interactive dashboard)  
- **Jupyter Notebook:** reproducible analysis pipeline  
- **GitHub:** for version control and collaborative development

