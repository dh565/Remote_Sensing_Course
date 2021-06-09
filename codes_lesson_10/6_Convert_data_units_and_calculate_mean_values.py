# 6_Convert_data_units_and_calculate_mean_values

# We need only some of the variables: LE, net radiation, average temperature, wind speed
# atmospheric pressure, and relative humidity

#https://ameriflux.lbl.gov/sites/siteinfo/US-Bi2#overview
list_of_column = ['LE','NETRAD','TA','WS','PA','RH']
df             = df[['LE','NETRAD','TA','WS','PA','RH']]

# Let's drop dates with nan (-9999 in the csv file):
for column in list_of_column:
    print (column)
    index_names = df[ df[column] == -9999 ].index
    df.drop(index_names, inplace = True)

# We need to convert Rn from W m-2 to MJ m-2 day-1
df['NETRAD_daily'] = df['NETRAD'] * 3600 * 24 / 1000000 

# We need to get max and min Temp. (all other variables are mean values)
d_TA_MIN        = df['TA'].resample('D').min()
d_TA_MAX        = df['TA'].resample('D').max()

# Calculate daily mean values for all variables
df = df.resample('D').mean() 

# Save the new data
#df['NETRAD_daily'] = df_NETRAD_daily.tolist()
df['TA_MIN']       = d_TA_MIN.tolist()
df['TA_MAX']       = d_TA_MAX.tolist()

# We also need to convert LE to ET from W m-2 to mm day-1
# the conversion factor is: 1 W m-2 = 28.94 mm day-1 (dependes on Tavg)
df['ET']           = df['LE'] / 28.94 

# Display daily ET:
df['ET'].plot(ylabel = 'ET (mm day$^{-1}$)',xlabel='DATE',title='ET for US-Bi2 site')
