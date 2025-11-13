
# ACQUIRE DATA

import pandas as pd
import requests
import os

import hashlib
from pathlib import Path


#dataset 1: me data from City of Chicago, download as CSV
df_me = pd.read_csv("data/raw/Medical_Examiner_Case_Archive_20251104.csv", low_memory=False)


#dataset 2: census acs5 data for cook county

os.makedirs("data/raw", exist_ok=True)

# ACS 5-Year 2023 (data collected 2019–2023)
url = "https://api.census.gov/data/2023/acs/acs5"

variables = [
    # Population + race
    "B01003_001E",  # total population
    "B03002_003E",  # white (non-Hispanic)
    "B03002_004E",  # black
    "B03002_006E",  # asian
    "B03002_012E",  # hispanic

    # Income & poverty
    "B19013_001E",  # median income
    "B17001_002E",  # below poverty

    # Education
    "B15003_022E",  # bachelor's degree or higher

    # Age structure (male + female counts)
    "B01001_003E", "B01001_027E",  # under 18
    "B01001_007E", "B01001_031E",  # 18–34
    "B01001_010E", "B01001_034E",  # 35–64
    "B01001_020E", "B01001_044E",  # 65+

    # New: Unemployment, Health Insurance, Rent
    "B23025_002E",  # labor force
    "B23025_005E",  # unemployed
    "B27010_017E",  # no health insurance (all people)
    "B25064_001E"   # median gross rent
]

params = {
    "get": ",".join(["NAME"] + variables),
    "for": "tract:*",
    "in": "county:031 state:17"  # Cook County, IL
}

r = requests.get(url, params=params)
r.raise_for_status()

data = r.json()
cols = data[0]
rows = data[1:]
df_census = pd.DataFrame(rows, columns=cols)

# Rename columns for clarity
df_census = df_census.rename(columns={
    "B01003_001E": "TotalPop",
    "B03002_003E": "White_NonHisp",
    "B03002_004E": "Black",
    "B03002_006E": "Asian",
    "B03002_012E": "Hispanic",
    "B19013_001E": "MedianIncome",
    "B17001_002E": "BelowPoverty",
    "B15003_022E": "BachelorsOrHigher",
    "B01001_003E": "Male_Under18",
    "B01001_027E": "Female_Under18",
    "B01001_007E": "Male_18_34",
    "B01001_031E": "Female_18_34",
    "B01001_010E": "Male_35_64",
    "B01001_034E": "Female_35_64",
    "B01001_020E": "Male_65plus",
    "B01001_044E": "Female_65plus",
    "B23025_002E": "LaborForce",
    "B23025_005E": "Unemployed",
    "B27010_017E": "NoHealthInsurance",
    "B25064_001E": "MedianRent",
    "state": "STATE",
    "county": "COUNTY",
    "tract": "TRACT"
})


# Unique tract ID for merging
df_census["TRACT_FIPS"] = df_census["STATE"] + df_census["COUNTY"] + df_census["TRACT"].str.zfill(6)

df_census.to_csv("data/raw/census_tract_data.csv", index=False)
print(f"Saved enriched Census data for {len(df_census)} tracts.")


# ---- checksum 
me_path = Path("data/raw/Medical_Examiner_Case_Archive_20251104.csv")
census_path = Path("data/raw/census_tract_data.csv")

def compute_sha256(file_path):
    """Compute SHA-256 checksum for a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

raw_files = [me_path, census_path]

for file in raw_files:
    checksum = compute_sha256(file)
    checksum_file = file.with_suffix(".sha256")
    checksum_file.write_text(checksum)
    print(f"🔐 SHA-256 for {file.name}: {checksum[:12]}... (saved to {checksum_file})")

print("✔️ Data acquisition and integrity verification complete.")