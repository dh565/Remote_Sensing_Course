# Exclude values that are greater than 3 std from the LST data 
std  = np.nanstd(TS)  # calculate std
mean = np.nanmean(TS) # calculate mean

lower_limit = mean - (std*3)
upper_limit = mean + (std*3)

np.where(TS, TS < lower_limit, np.nan)
np.where(TS, TS > upper_limit, np.nan)

print("Minimum limit:", np.nanmin(TS), "°K")
print("Maximum limit:", np.nanmax(TS), "°K")
