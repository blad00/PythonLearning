# Imports
import pandas as pd

# Read in data
data1_loc = "/mnt/WORKSPACE/dcr_workspace/Projects/QC_reseq/Irene/2020_small.xlsx"
data2_loc = "/mnt/WORKSPACE/dcr_workspace/Projects/QC_reseq/Irene/2021_small.xlsx"

df1 = pd.read_excel(data1_loc)
df2 = pd.read_excel(data2_loc)
print(df1)
print(df2)

# Main
# Define columns that stay the same e.g names
all_df = [df1, df2]
same_cols = pd.concat(all_df, axis=0, join="inner").columns.to_list()

# Cat the columns
df_cat = pd.concat(all_df, join="inner", axis=0)
# Merge overlappring columns based on sets (a set is ONLY unique values so that would be perfect here!)
df_fuse = df_cat.groupby(["Reference", "Position"], sort=False, as_index=False).agg(lambda x: "_".join(set(x)))

# Add unique columns back to the dataframe
for df in all_df:
    df_fuse = df_fuse.merge(df, how="left")

df_fuse

# take care of caps