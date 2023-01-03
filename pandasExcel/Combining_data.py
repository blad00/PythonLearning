import pandas as pd
climate_temp = pd.read_csv("climate_temp.csv")
climate_precip = pd.read_csv("climate_precip.csv")

climate_temp.head()

climate_precip.head()

climate_temp.shape

climate_precip.shape

precip_one_station = climate_precip.query("STATION == 'GHCND:USC00045721'")
precip_one_station.head()

precip_one_station.shape

# Merge
inner_merged = pd.merge(precip_one_station, climate_temp)
inner_merged.head()

inner_merged.shape

inner_merged_total = pd.merge(
    climate_temp, climate_precip, on=["STATION", "DATE"]
)
inner_merged_total.shape

outer_merged = pd.merge(
    precip_one_station, climate_temp, how="outer", on=["STATION", "DATE"]
)
outer_merged.shape

left_merged = pd.merge(
    climate_temp, precip_one_station, how="left", on=["STATION", "DATE"]
)
left_merged.shape

left_merged_reversed = pd.merge(
    precip_one_station, climate_temp, how="left", on=["STATION", "DATE"]
)
left_merged_reversed.shape

right_merged = pd.merge(
    precip_one_station, climate_temp, how="right", on=["STATION", "DATE"]
)
right_merged.shape

# join

precip_one_station.join(
    climate_temp, lsuffix="_left", rsuffix="_right"
).shape

climate_temp.join(
    precip_one_station, lsuffix="_left", rsuffix="_right"
).shape

inner_merged_total = pd.merge(
    climate_temp, climate_precip, on=["STATION", "DATE"]
)
inner_merged_total.shape

inner_joined_total = climate_temp.join(
    climate_precip.set_index(["STATION", "DATE"]),
    on=["STATION", "DATE"],
    how="inner",
    lsuffix="_x",
    rsuffix="_y",
)
inner_joined_total.shape

climate_temp.join(climate_precip, lsuffix="_left").shape

# concat
double_precip = pd.concat([precip_one_station, precip_one_station])
double_precip.shape

reindexed = pd.concat(
    [precip_one_station, precip_one_station], ignore_index=True
)
reindexed.index

outer_joined = pd.concat([climate_precip, climate_temp])
outer_joined.shape

inner_joined = pd.concat([climate_temp, climate_precip], join="inner")
inner_joined.shape

inner_joined_cols = pd.concat(
    [climate_temp, climate_precip], axis="columns", join="inner"
)
inner_joined_cols.shape

hierarchical_keys = pd.concat(
    [climate_temp, climate_precip], keys=["temp", "precip"]
)
hierarchical_keys.index



# concat 1 on top the other axis=rows or 1 next to the other axis = columns

# use Keys in case you have duplicate col or rows IDs

# use ignore_ index to reset IDs rows or in columns replace by serie of numbers
# use join param inner to ignore things that dont match in the DF

# pd.merge(fruits, veggies)

# only the same rows are output

#  left_on, left_index


