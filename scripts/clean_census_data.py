# scripts/clean_census.py

import pandas as pd
import os



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


df.to_csv("data/processed/census_tract_cleaned.csv", index=False)
print("Saved cleaned and enriched census dataset → data/processed/census_tract_cleaned.csv")


