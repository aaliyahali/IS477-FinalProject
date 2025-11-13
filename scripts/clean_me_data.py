# imports

import pandas as pd
import requests
import hashlib
import os
from pathlib import Path

import pandas as pd
from pathlib import Path
import hashlib

# --- Verify data integrity before cleaning ---
def compute_sha256(file_path):
    """Compute SHA-256 checksum for a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def verify_checksum(file_path):
    """Compare current file hash against stored checksum."""
    expected = Path(file_path).with_suffix(".sha256").read_text().strip()
    actual = compute_sha256(file_path)
    if actual != expected:
        raise ValueError(f"❌ Checksum mismatch for {file_path}")
    print(f"✅ Verified checksum for {file_path}")

# Verify integrity before loading raw ME data
file_path = "data/raw/Medical_Examiner_Case_Archive_20251104.csv"
verify_checksum(file_path)

# ---- 



RAW_ME_PATH = Path("data/raw/Medical_Examiner_Case_Archive_20251104.csv")
df = pd.read_csv(RAW_ME_PATH, low_memory=False)

df["Updated_Date_of_Death"] = pd.to_datetime(df['Date of Death'], format='%m/%d/%Y %I:%M:%S %p')
df["Year_of_Death"] = df["Updated_Date_of_Death"].dt.year
df = df[(df["Year_of_Death"] >= 2019) & (df["Year_of_Death"] <= 2023)]


# Standardize ZIP code (keep 5 digits)
df["Incident Zip Code"] = df["Incident Zip Code"].astype(str).str.extract(r"(\d{5})")
df["Incident Zip Code"] = df["Incident Zip Code"].str.zfill(5)

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

