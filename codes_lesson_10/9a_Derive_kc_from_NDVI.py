# 9a_Derive_kc_from_NDVI

# We need to relate our flux data to the NDVI data in terms of dates
filtered_NDVI = df_loess.loc[start_date:end_date]
filtered_df   = df.loc[start_date:end_date]

data          = pd.merge(filtered_NDVI, filtered_df, left_index=True, right_index=True, how='outer')

# Delete the unnecessary rows from NDVI data:
data.drop('mean' , inplace=True, axis=1)  
data.drop('index', inplace=True, axis=1)

#function FOR  FVC
NDVImin = 0.05
NDVImax = 0.95
def FVC(NDVI):
     FVC_V = (NDVI - NDVImin) / (NDVImax - NDVImin)
     if FVC_V > 1:
       FVC_V = 1.0
     if FVC_V < 0.0:
       FVC_V = 0.0
     return FVC_V

data['fvc'] = data['NDVI'].apply(FVC)  

# We'll use the maximum value of kc for maize from a lookup table to constrain 
# our kc:
Kc_max = 1.2
data['kc'] = data['fvc'] * Kc_max

# Let's display kc:
data['kc'].plot(ylabel='kc (unitless)', xlabel='DATE',title='Crop coefficient for Maize site US-Bi2')
