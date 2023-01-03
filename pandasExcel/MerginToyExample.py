import pandas as pd

# 2020
squash2020 = pd.read_excel("/mnt/WORKSPACE/dcr_workspace/Projects/QC_reseq/Irene/2020_small.xlsx")

squash2020.dropna(how="all", axis=1, inplace=True)

squash2020.shape

# 2021

squash2021 = pd.read_excel("/mnt/WORKSPACE/dcr_workspace/Projects/QC_reseq/Irene/2021_small.xlsx")

squash2021.dropna(how="all", axis=1, inplace=True)

squash2021.shape


merged_total = pd.merge(
    squash2020, squash2021, how="outer", on=["Reference", "Position"]
)

merged_total.shape

# Correct columns
merged_total_2 = merged_total.drop(["ID_y", "Reference allele_y", "Alternate allele(s)_y", "Filter(s)_y"], axis=1)

merged_total_3 = merged_total_2

merged_total_4 = merged_total_3.rename(columns={'ID_x':'ID', 'Reference allele_x':'Reference allele', 'Alternate allele(s)_x':'Alternate allele(s)',
                                  "Filter(s)_x":"Filter(s)"})

# storage result
merged_total_5 = merged_total_4

# find repeated samples
for col in merged_total_4.columns:
    if "_x" in col:
        just_name = col.split("_")[0]
        merged_total_5[just_name] = merged_total_5[col] + "_" + merged_total_5[just_name+"_y"]
        merged_total_5.drop([col, just_name+"_y"], axis=1, inplace=True)

merged_total_5.replace(['A_A'], 'A', inplace=True)
merged_total_5.replace(['B_B'], 'B', inplace=True)
merged_total_5.replace(['H_H'], 'H', inplace=True)
merged_total_5.replace(['U_U'], 'U', inplace=True)

merged_total_5.to_excel('SeqSNP_merged_toy.xlsx', index=False)




# to prune excel

# squash2020 = pd.read_excel("/mnt/WORKSPACE/dcr_workspace/Projects/QC_reseq/Irene/Squash XX_NGS2221_ABH_2020.xlsx",
#                           header=None, skiprows=2, usecols=list(range(0, 7))