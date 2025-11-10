#!/usr/bin/env python3

import pandas as pd
from pathlib import Path
import os

# Ensure output directory exists
os.makedirs("data/processed", exist_ok=True)

# load data 
df_me = pd.read_csv("data/processed/me_cleaned.csv", dtype={"Incident Zip Code": str})
df_zip = pd.read_excel("data/raw/ZIP_TRACT_062025.xlsx", dtype={"ZIP": str, "TRACT": str})
df_census = pd.read_csv("data/processed/census_data_cleaned.csv", dtype={"TRACT_FIPS": str})

# ---- Filter Crosswalk to Cook County (FIPS 17031xxxxx) ----
df_zip_cook = df_zip[df_zip["TRACT"].str.startswith("17031")].copy()

# ---- Select dominant tract per ZIP based on residential address share ----
df_zip_primary = (
    df_zip_cook
    .sort_values(["ZIP", "RES_RATIO"], ascending=[True, False])
    .drop_duplicates("ZIP")
    .reset_index(drop=True)
)

# ---- Merge ME Records with ZIP→TRACT primary mapping ----
df_merge = df_me.merge(
    df_zip_primary,
    how="left",
    left_on="Incident Zip Code",
    right_on="ZIP"
)

# ---- Merge with Census tract-level attributes ----
df_merge = df_merge.merge(
    df_census,
    how="left",
    left_on="TRACT",
    right_on="TRACT_FIPS"
)

# ---- Clean Columns ----
# Standardize tract column name
df_merge["TRACT"] = df_merge["TRACT_x"]

# Drop duplicate/unneeded columns
df_merge = df_merge.drop(columns=[
    "TRACT_x", "TRACT_y", "TRACT_FIPS",
    "USPS_ZIP_PREF_CITY", "USPS_ZIP_PREF_STATE",
    "BUS_RATIO", "OTH_RATIO", "TOT_RATIO"
], errors="ignore")

# ---- Save Final File ----
output_path = "data/processed/me_census_data_merged.csv"
df_merge.to_csv(output_path, index=False)
