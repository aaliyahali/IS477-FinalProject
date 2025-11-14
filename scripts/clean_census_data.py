# scripts/clean_census.py

import pandas as pd
import os
from acquire_data import compute_sha256
from pathlib import Path

import pandas as pd
from pathlib import Path
import hashlib


checksum_dir = Path("data/checksums")

def compute_sha256(file_path):
    """Compute SHA-256 checksum for a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def verify_checksum(file_path):
    """Compare current file hash against stored checksum in data/checksums/."""
    file_path = Path(file_path)

    # checksum is stored in data/checksums/<stem>.sha256
    checksum_file = checksum_dir / f"{file_path.stem}.sha256"

    if not checksum_file.exists():
        raise FileNotFoundError(f"❌ No checksum file found: {checksum_file}")

    expected = checksum_file.read_text().strip()
    actual = compute_sha256(file_path)

    if actual != expected:
        raise ValueError(
            f"❌ Checksum mismatch for {file_path.name}\n"
            f"Expected: {expected}\nActual:   {actual}"
        )

    print(f"✅ Checksum verified for {file_path.name}")

verify_checksum("data/raw/census_tract_data.csv")

# def compute_sha256(file_path):
#     """Compute SHA-256 checksum for a file."""
#     sha256_hash = hashlib.sha256()
#     with open(file_path, "rb") as f:
#         for byte_block in iter(lambda: f.read(4096), b""):
#             sha256_hash.update(byte_block)
#     return sha256_hash.hexdigest()

# def verify_checksum(file_path):
#     """Compare current file hash against stored checksum."""
#     expected = Path(file_path).with_suffix(".sha256").read_text().strip()
#     actual = compute_sha256(file_path)
#     if actual != expected:
#         raise ValueError(f"❌ Checksum mismatch for {file_path}")
#     print(f"✅ Verified checksum for {file_path}")

# # Verify integrity before loading raw census data



# CLEAN CENSUS DATA

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/census_tract_data.csv", low_memory=False)

# Convert to numeric (are strings right now)
num_cols = [c for c in df.columns if c not in ["NAME", "STATE", "COUNTY", "TRACT", "TRACT_FIPS"]]
df[num_cols] = df[num_cols].apply(pd.to_numeric, errors="coerce")

# ----- Compute age group totals -----
df["Age_Under18"] = df["Male_Under18"] + df["Female_Under18"]
df["Age_18_34"] = df["Male_18_34"] + df["Female_18_34"]
df["Age_35_64"] = df["Male_35_64"] + df["Female_35_64"]
df["Age_65plus"] = df["Male_65plus"] + df["Female_65plus"]

# ----- Compute demographic proportions -----
df["Pct_Black"] = df["Black"] / df["TotalPop"] * 100
df["Pct_Hispanic"] = df["Hispanic"] / df["TotalPop"] * 100
df["Pct_Asian"] = df["Asian"] / df["TotalPop"] * 100
df["Pct_WhiteNonHisp"] = df["White_NonHisp"] / df["TotalPop"] * 100

# ----- SES & Education percentages -----
df["Pct_BelowPoverty"] = df["BelowPoverty"] / df["TotalPop"] * 100
df["Pct_BachelorsPlus"] = df["BachelorsOrHigher"] / df["TotalPop"] * 100

# ----- Unemployment & Insurance -----
df["Pct_Unemployed"] = (df["Unemployed"] / df["LaborForce"]) * 100
df["Pct_Uninsured"] = (df["NoHealthInsurance"] / df["TotalPop"]) * 100


df.to_csv("data/processed/census_data_cleaned.csv", index=False)
print("Saved cleaned and enriched census dataset → data/processed/census_tract_cleaned.csv")


