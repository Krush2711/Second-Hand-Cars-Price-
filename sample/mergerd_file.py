import pandas as pd
import glob
import os

# Folder containing the CSV files
path = "sample"

# List all CSV files
all_csv = glob.glob(os.path.join(path, "*.csv"))

# Read + concat
df = pd.concat((pd.read_csv(f) for f in all_csv), ignore_index=True)

# Save final merged CSV
df.to_csv("merged.csv", index=False)

print("Done! Merged", len(all_csv), "files.")
    