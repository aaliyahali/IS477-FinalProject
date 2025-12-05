#!/usr/bin/env python3

import os
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

# Always run from project root: python scripts/visualization_analysis.py
DATA_PATH = Path("data/processed/me_census_data_merged.csv")
OUT_DIR = Path("visualizations")
OUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

# -----------------------------------------------------------------------------
# Load data
# -----------------------------------------------------------------------------

if not DATA_PATH.exists():
    raise FileNotFoundError(f"Cannot find merged data at: {DATA_PATH}")

df = pd.read_csv(DATA_PATH, low_memory=False)

# Fix typo in column name if present
if "contanins_fentanyl" in df.columns and "contains_fentanyl" not in df.columns:
    df.rename(columns={"contanins_fentanyl": "contains_fentanyl"}, inplace=True)

# Identify drug indicator columns (contains_*)
drug_cols = [col for col in df.columns if "contain" in col.lower()]

# -----------------------------------------------------------------------------
# Helper: save and close figures
# -----------------------------------------------------------------------------

def save_current_fig(filename):
    out_path = OUT_DIR / filename
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"📈 Saved figure: {out_path}")


# -----------------------------------------------------------------------------
# 1. Distribution of deaths by gender and race
# -----------------------------------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

if "Gender" in df.columns:
    sns.countplot(data=df, x="Gender", ax=axes[0], palette="Set2")
    axes[0].set_title("Distribution of Drug-Related Deaths by Gender")
    axes[0].set_xlabel("Gender")
    axes[0].set_ylabel("Count")
else:
    axes[0].text(0.5, 0.5, "Gender column missing", ha="center", va="center")
    axes[0].set_axis_off()

if "Race" in df.columns:
    sns.countplot(
        data=df,
        x="Race",
        ax=axes[1],
        order=df["Race"].value_counts().index,
        palette="Set3"
    )
    axes[1].set_title("Distribution of Drug-Related Deaths by Race")
    axes[1].set_xlabel("Race")
    axes[1].set_ylabel("Count")
    plt.setp(axes[1].xaxis.get_majorticklabels(), rotation=45, ha="right")
else:
    axes[1].text(0.5, 0.5, "Race column missing", ha="center", va="center")
    axes[1].set_axis_off()

save_current_fig("distribution_gender_race.png")


# -----------------------------------------------------------------------------
# 2. Age distribution
# -----------------------------------------------------------------------------

if "Age" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Age"].dropna(), bins=30, kde=True)
    plt.title("Distribution of Age at Death")
    plt.xlabel("Age")
    plt.ylabel("Count")
    save_current_fig("age_distribution.png")
else:
    print("⚠️ No 'Age' column found — skipping age distribution plot.")


# -----------------------------------------------------------------------------
# 3. Deaths by year
# -----------------------------------------------------------------------------

if "Year_of_Death" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="Year_of_Death", palette="magma")
    plt.title("Drug-Related Deaths by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Deaths")
    save_current_fig("deaths_by_year.png")
else:
    print("⚠️ No 'Year_of_Death' column found — skipping yearly deaths plot.")


# -----------------------------------------------------------------------------
# 4. Share of deaths involving each drug over time
# -----------------------------------------------------------------------------

if "Year_of_Death" in df.columns and len(drug_cols) > 0:
    plt.figure(figsize=(10, 6))
    for drug in drug_cols:
        yearly = df.groupby("Year_of_Death")[drug].mean() * 100
        plt.plot(yearly.index, yearly.values, marker="o", label=drug.replace("contains_", "").capitalize())

    plt.legend()
    plt.title("Share of Deaths Involving Each Drug Type Over Time (%)")
    plt.xlabel("Year")
    plt.ylabel("% of Deaths")
    save_current_fig("share_deaths_involving_each_drug_over_time.png")
else:
    print("⚠️ Missing 'Year_of_Death' or drug columns — skipping time series share plot.")


# -----------------------------------------------------------------------------
# 5. % of deaths involving each drug by race
# -----------------------------------------------------------------------------

if "Race" in df.columns and len(drug_cols) > 0:
    for drug in drug_cols:
        ctab = pd.crosstab(df["Race"], df[drug], normalize="index") * 100
        if True in ctab.columns:
            plt.figure(figsize=(8, 4))
            ctab[True].sort_values().plot(kind="barh")
            plt.title(f"% of Deaths Involving {drug.replace('contains_', '').capitalize()} by Race")
            plt.xlabel("% of Deaths")
            plt.ylabel("Race")
            filename = f"pct_deaths_{drug.replace('contains_', '')}_by_race.png"
            save_current_fig(filename)
        else:
            print(f"⚠️ No True values for {drug} — skipping race breakdown plot.")
else:
    print("⚠️ Missing 'Race' or drug columns — skipping race x drug plots.")


# -----------------------------------------------------------------------------
# 6. Distribution of fentanyl-involved death rates by tract
# -----------------------------------------------------------------------------

if "TRACT" in df.columns and "contains_fentanyl" in df.columns:
    tract_stats = (
        df.groupby("TRACT")["contains_fentanyl"]
        .mean()
        .reset_index()
        .rename(columns={"contains_fentanyl": "fentanyl_rate"})
    )

    plt.figure(figsize=(8, 5))
    sns.histplot(tract_stats["fentanyl_rate"], bins=20)
    plt.title("Distribution of Fentanyl-Involved Death Rates by Census Tract")
    plt.xlabel("Fentanyl Involvement Rate")
    plt.ylabel("Number of Tracts")
    save_current_fig("fentanyl_rate_distribution_by_tract.png")
else:
    print("⚠️ Missing 'TRACT' or 'contains_fentanyl' — skipping tract fentanyl distribution.")


# -----------------------------------------------------------------------------
# 7. Correlation heatmap: socioeconomic factors vs fentanyl involvement
# -----------------------------------------------------------------------------

required_cols = [
    "MedianIncome", "Pct_BelowPoverty", "Pct_Black",
    "Pct_Hispanic", "Pct_Unemployed", "Pct_Uninsured", "Pct_BachelorsPlus",
    "contains_fentanyl"
]

if all(col in df.columns for col in required_cols):
    corr = df[required_cols].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
    plt.title("Correlation Between Socioeconomic Factors and Fentanyl Involvement")
    save_current_fig("corr_socioeconomic_fentanyl.png")
else:
    print("⚠️ One or more socioeconomic columns missing — skipping correlation heatmap.")


# -----------------------------------------------------------------------------
# 8. Spatial scatter: all deaths and fentanyl vs non-fentanyl
# -----------------------------------------------------------------------------

if {"latitude", "longitude"} <= set(df.columns):
    df_mapped = df.dropna(subset=["latitude", "longitude"])

    # All deaths with fentanyl colored
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(
        df_mapped["longitude"],
        df_mapped["latitude"],
        c=df_mapped["contains_fentanyl"] if "contains_fentanyl" in df_mapped.columns else 0,
        cmap="RdYlGn_r",
        alpha=0.4,
        s=5
    )
    cbar = plt.colorbar(scatter)
    cbar.set_label("Fentanyl Involved (1=Yes, 0=No)")
    plt.title("Drug Death Locations in Cook County")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    save_current_fig("spatial_all_deaths_fentanyl_overlay.png")

    # Separate panels for fentanyl, cocaine, heroin
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    drugs = ["contains_fentanyl", "contains_cocaine", "contains_heroin"]
    titles = ["Fentanyl Deaths", "Cocaine Deaths", "Heroin Deaths"]

    for ax, drug, title in zip(axes, drugs, titles):
        if drug not in df_mapped.columns:
            ax.text(0.5, 0.5, f"{drug} missing", ha="center", va="center")
            ax.set_axis_off()
            continue

        drug_deaths = df_mapped[df_mapped[drug] == True]

        ax.scatter(df_mapped["longitude"], df_mapped["latitude"],
                   c="lightgray", s=1, alpha=0.2, label="All deaths")
        ax.scatter(drug_deaths["longitude"], drug_deaths["latitude"],
                   c="red", s=3, alpha=0.6, label=title)
        ax.set_title(title, fontsize=14)
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.legend()

    plt.suptitle("Spatial Distribution of Different Drug Types", fontsize=16)
    save_current_fig("spatial_by_drug_type.png")

else:
    print("⚠️ Missing 'latitude' or 'longitude' — skipping spatial scatter plots.")


# -----------------------------------------------------------------------------
# 9. Interactive heatmap with Folium (saved as HTML)
# -----------------------------------------------------------------------------

if {"latitude", "longitude"} <= set(df.columns):
    df_mapped = df.dropna(subset=["latitude", "longitude"])

    # Center map on approximate Chicago coordinates
    m = folium.Map(location=[41.8781, -87.6298], zoom_start=11, tiles="OpenStreetMap")

    # Fentanyl heatmap
    if "contains_fentanyl" in df_mapped.columns:
        fentanyl_data = df_mapped[df_mapped["contains_fentanyl"] == True][["latitude", "longitude"]].values.tolist()
        HeatMap(fentanyl_data, radius=10, blur=15, max_zoom=13, name="Fentanyl Deaths").add_to(m)

    # Cocaine heatmap
    if "contains_cocaine" in df_mapped.columns:
        cocaine_data = df_mapped[df_mapped["contains_cocaine"] == True][["latitude", "longitude"]].values.tolist()
        HeatMap(
            cocaine_data,
            radius=10,
            blur=15,
            max_zoom=13,
            gradient={0.4: "blue", 0.6: "cyan", 1: "lime"},
            name="Cocaine Deaths"
        ).add_to(m)

    # Heroin heatmap
    if "contains_heroin" in df_mapped.columns:
        heroin_data = df_mapped[df_mapped["contains_heroin"] == True][["latitude", "longitude"]].values.tolist()
        HeatMap(
            heroin_data,
            radius=10,
            blur=15,
            max_zoom=13,
            gradient={0.4: "purple", 0.6: "magenta", 1: "pink"},
            name="Heroin Deaths"
        ).add_to(m)

    folium.LayerControl().add_to(m)

    html_out = OUT_DIR / "chicago_drug_deaths_map.html"
    m.save(str(html_out))
    print(f"🗺️ Saved interactive map: {html_out}")
else:
    print("⚠️ Missing 'latitude' or 'longitude' — skipping Folium map.")
