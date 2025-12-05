# Filesystem Structure

This document describes the project folder layout and naming conventions.

```text
IS477-FinalProject/
├── data/
│   ├── raw/
│   │   ├── Medical_Examiner_Case_Archive_20251104.csv
│   │   ├── census_tract_data.csv
│   │   └── ZIP_TRACT_062025.xlsx
│   ├── processed/
│   │   ├── me_cleaned.csv
│   │   ├── census_data_cleaned.csv
│   │   └── me_census_data_merged.csv
│   ├── checksums/
│   │   ├── Medical_Examiner_Case_Archive_20251104.sha256
│   │   └── census_tract_data.sha256
│   └── box/                # (optional) large or restricted data from Box
│
├── notebooks/
│   ├── EDA.ipynb
│   └── midpoint_acq_clean_merge.ipynb
│
├── scripts/
│   ├── acquire_data.py
│   ├── clean_me_data.py
│   ├── clean_census_data.py
│   ├── merge_data.py
│   ├── visualize_analyze_data.py
│   └── run_all.py
│
├── visualizations/
│   ├── *.png
│   └── *.html
│
├── metadata/
│   ├── data_dictionary.md
│   ├── provenance.md
│   └── dataset_metadata.json
│
├── documentation/
│   ├── filesystem_structure.md
│   ├── environment_setup.md
│   ├── reproduction_steps.md
│   └── licenses.md
│
├── requirements.txt
├── README.md
└── .gitignore
