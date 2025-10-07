#  Mapping and Modeling Drug-Related Deaths in Cook County

## Team Members
- **Aaliyah Ali**  and **Rithikka Souresh**

---

## Project Goal
To analyze drug-related deaths in Cook County to uncover spatial, demographic, and temporal trends, focusing on how the distribution of different drug types (opioids, fentanyl, cocaine, heroin, etc.) varies across time and location.  

This project will use data modeling and visualization to highlight emerging overdose patterns* and public health implications.

---

##  Research Questions
1. How have drug-related deaths changed over time in Cook County?  
2. Which drug categories (fentanyl, heroin, cocaine, etc.) are most associated with fatal overdoses?  
3. What demographic patterns (age, race, gender) exist across drug types?  
4. Are there geographic hotspots for specific drug categories?  

---

## Data Sources
- **Cook County Medical Examiner’s Office (Public Dataset)**  (https://datacatalog.cookcountyil.gov/Health-Human-Services/Medical-Examiner-Case-Archive/cjeq-bs86/about_data)
  - Variables: primary cause, secondary cause, date of death, race, gender, age, latitude/longitude, etc. 
- **U.S. Census Bureau / Chicago Data Portal**  (https://hub-cookcountyil.opendata.arcgis.com/pages/boundary-open-data)
  - Provides a geographic context for spatial analysis, which includes spatial boundaries for Cook County.  

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


##  Tools
- **Python:** pandas, geopandas, matplotlib, seaborn  
- **Jupyter Notebook:** reproducible analysis pipeline  

---

## Expected Outputs
- A cleaned, reproducible dataset for drug-related death analysis  
- Visual dashboards showing spatial and demographic patterns  
- Statistical summary of associations between drug types and outcomes  
- Policy implications and recommendations for local health departments  
