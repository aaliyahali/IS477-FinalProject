#!/usr/bin/env python3

"""
Run the full end-to-end workflow for the project.

Assumes you are running from the project root:

    python scripts/run_all.py
"""

import subprocess
import sys

STEPS = [
    ["python", "scripts/acquire_data.py"],
    ["python", "scripts/clean_me_data.py"],
    ["python", "scripts/clean_census_data.py"],
    ["python", "scripts/merge_data.py"],
    ["python", "scripts/visualize_analyze_data.py"],
]

def main():
    for cmd in STEPS:
        print("\n" + "=" * 80)
        print("Running:", " ".join(cmd))
        print("=" * 80)
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f" Step failed: {' '.join(cmd)}")
            sys.exit(result.returncode)

    print("\n Full workflow completed successfully.")

if __name__ == "__main__":
    main()
