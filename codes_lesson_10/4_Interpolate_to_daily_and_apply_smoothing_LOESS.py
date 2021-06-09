# 4_Interpolate_to_daily_and_apply_smoothing_LOESS

idx              = pd.date_range('01-01-2017', '03-01-2021') # First is month then day
df_ndvi['index'] = df_ndvi.index
df_ndvi          = df_ndvi.reindex(idx)
df_int           = df_ndvi.reindex(idx)
df_loess         = df_ndvi.reindex(idx)

# We want to expand the vector from having data every 16 days to having daily data
n = len(df_ndvi)
x = list(range(0,n))

original_y  = df_ndvi['NDVI'].tolist()
original_x  = df_ndvi['index'].tolist()

# We will use linear interpolation for that..
df_int['NDVI'] =  df_int['NDVI'].interpolate('linear')
y = df_int['NDVI'].tolist()
x = df_int['index'].tolist()
x = list(range(0,n))

# Now, let's apply the LOESS smoothing technique to get rid of noisy data
lowess = sm.nonparametric.lowess(y, x, frac=.12)
lowess_x = list(zip(*lowess))[0]
lowess_y = list(zip(*lowess))[1]
df_loess['NDVI'] = lowess_y

# Display both, original and smoothed ts:
plt.figure(figsize=(10, 6))    
plt.plot(x, original_y, 'o',label="Original NDVI")#
plt.plot(x, lowess_y, '-k',label="Smoothed NDVI")#
plt.legend(loc="upper left")
plt.figure()

# Display smoothed NDVI with real dates
df_ndvi['NDVI_after_smoothing'] = lowess_y
df_ndvi['NDVI_after_smoothing'].plot(ylabel='NDVI',xlabel='DATE',title='NDVI after smoothing in US-Bi2 site')
