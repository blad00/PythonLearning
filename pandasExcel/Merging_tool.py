import pandas as pd

# 2020
watermelon2020 = pd.read_excel("/mnt/WORKSPACE/dcr_workspace/Projects/QC_reseq/Irene/Nov2022Q/WM_5K_seqSNP_2020_Py.xlsx")

watermelon2020.dropna(how="all", axis=1, inplace=True)

watermelon2020.shape

# 2021
watermelon2021 = pd.read_excel("/mnt/WORKSPACE/dcr_workspace/Projects/QC_reseq/Irene/Nov2022Q/WM_5K_seqSNP_2021_Py.xlsx")

watermelon2020.dropna(how="all", axis=1, inplace=True)

watermelon2021.shape

merged_total = pd.merge(
    watermelon2020, watermelon2021, how="outer", on=["Marker_ID"]
)

merged_total.shape

# merged_total.to_excel('WMSeqSNP_merged_toy.xlsx', index=False)

merged_total2 = merged_total

# find repeated samples
for col in merged_total2.columns:
    if "_x" in col:
        just_name = col.split("_x")[0]
        merged_total2[just_name] = merged_total2[col] + "_" + merged_total2[just_name+"_y"]
        merged_total2.drop([col, just_name+"_y"], axis=1, inplace=True)

merged_total2.to_excel('WMSeqSNP_merged_toy2.xlsx', index=False)

merged_total2.replace(['A_A'], 'A', inplace=True)
merged_total2.replace(['B_B'], 'B', inplace=True)
merged_total2.replace(['H_H'], 'H', inplace=True)
merged_total2.replace(['U_U'], 'U', inplace=True)
merged_total2.replace(['AHB_U'], 'SEG', inplace=True)
merged_total2.replace(['AHB_AHB'], 'SEG', inplace=True)
merged_total2.replace(['B_A'], '?', inplace=True)
merged_total2.replace(['A_B'], '?', inplace=True)
merged_total2.replace(['A_H'], 'SEG', inplace=True)
merged_total2.replace(['B_H'], 'SEG', inplace=True)
merged_total2.replace(['H_A'], 'SEG', inplace=True)
merged_total2.replace(['H_B'], 'SEG', inplace=True)
merged_total2.replace(['U_H'], 'H', inplace=True)
merged_total2.replace(['H_U'], 'H', inplace=True)
merged_total2.replace(['U_A'], 'A', inplace=True)
merged_total2.replace(['A_U'], 'A', inplace=True)
merged_total2.replace(['U_B'], 'B', inplace=True)
merged_total2.replace(['B_U'], 'B', inplace=True)
merged_total2.replace(['A_AHB'], 'SEG', inplace=True)
merged_total2.replace(['B_AHB'], 'SEG', inplace=True)
merged_total2.replace(['H_AHB'], 'SEG', inplace=True)
merged_total2.replace(['U_AHB'], 'SEG', inplace=True)

merged_total2.to_excel('WMSeqSNP_merged_final.xlsx', index=False)