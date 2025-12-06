# Reproducing the Analysis

This document describes how to reproduce the complete analysis workflow from scratch.

## Prerequisites

- Python 3.10+  
- Git  

## Step 1: Clone the Repository

```bash
git clone <YOUR_REPO_URL>.git
cd IS477-FinalProject
```

## Step 2: Set Up Environment

Follow documentation/environment_setup.md:


```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Step 3: Download or Place Input Data

You have two options:
1. Use Box-hosted data (reccomended)
- Download the contents of the shared Box folder (link provided in README.md).
- Place raw files into data/raw/ and processed files into data/processed/ as described in documentation/filesystem_structure.md.

2. Re-acquire from original sources
- Run the acquisition script to programmatically retrieve Census data: python scripts/acquire_data.py
- Download the Medical Examiner CSV and HUD ZIP–tract file from their portals and place them in data/raw/ using the filenames expected by the scripts.

## Step 4: Run the Full Workflow

```bash
python scripts/run_all.py
```

This will:
- Acquire Census data (acquire_data.py)
- Clean Medical Examiner data (clean_me_data.py)
- Clean Census data (clean_census_data.py)
- Merge ME and Census datasets (merge_data.py)
- Generate all plots and maps (visualize_analyze_data.py)

## Step 5: View Outputs

Final merged dataset:
data/processed/me_census_data_merged.csv

Static figures and analysis plots:
visualizations/*.png

Interactive map:
visualizations/chicago_drug_deaths_map.html
visualizations/fentanyl_hotspots.html

These outputs are referenced and interpreted in README.md under the Findings section.


