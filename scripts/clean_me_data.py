# imports

import pandas as pd
import requests
import hashlib
import os

from pathlib import Path


RAW_ME_PATH = Path("data/raw/Medical_Examiner_Case_Archive_20251104.csv")
df = pd.read_csv(RAW_ME_PATH, low_memory=False)

# Standardize ZIP code (keep 5 digits)
df["Incident Zip Code"] = df["Incident Zip Code"].astype(str).str.extract(r"(\d{5})")
df["Incident Zip Code"] = df["Incident Zip Code"].str.zfill(5)

#missing demos
df["Race"] = df["race"].fillna("Unknown")
df["Gender"] = df["gender"].fillna("Unknown")

# create columns for deaths related to drugs 
fent_names = "FENTANYL| 4-ANILINO-N-PHENETHYLPIPERIDINE | 4-ANPP | Acetyl-alphamethyl-fentanyl | Alfentanil | Alpha-methylfentanyl | 4ANPP | 4FIBF | Alpha-methylthiofentanyl | Beta-hydroxyfentanyl | Beta-hydroxy-3 methylfentanyl | 3-methylfentanyl | 3-methylthio-fentanyl | Para-fluoro-fentanyl | Remifentanil | Sufentanil | Thiofentanyl | Carfentanil | 2-furanoylfentanyl | Furanylfentanyl | 4-anilino-N-phenethylpiperidine | 4-Fluorofentanyl | ACETYLFENTANYL | ACRYLFENTANYL | Butyrfentanyl | Lofentanil | Valerylfentanyl | Isobutyrylfentanyl"
df['contanins_fentanyl'] = df['Primary Cause'].str.contains(fent_names, case=False, na=False)

df['contains_cocaine'] = df['Primary Cause'].str.contains("cocaine|Benzoylmethylecgonine", case=False, na=False)
df["contains_heroin"] =df['Primary Cause'].str.contains('HEROIN', case=False, na=False)

# ---- Drop records missing location (cannot map later) ----
df = df.dropna(subset=["Incident Zip Code"])

# ---- Save cleaned ME dataset ----
OUTPUT_PATH = Path("data/processed/me_cleaned.csv")
df.to_csv(OUTPUT_PATH, index=False)

