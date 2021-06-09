# 3_Get_NDVI_ts_from_GEE_for_lat_lon

ee.Initialize()
# donwload NDVI for our site https://ameriflux.lbl.gov/sites/siteinfo/US-Bi2#overview 
# This is the lat/lon of the Fluxnet site (US-Bi2)
poi  = ee.Geometry.Point(-121.5351, 38.1091)

# We will get NDVI time series for this site from 1/1/2017 to 1/5/2021
NDVI = ee.ImageCollection("MODIS/006/MOD13Q1").filterDate('2017-01-01','2021-05-01')

# This is how we get it from an image collection using GEE API:
def poi_mean(img):
    mean = img.reduceRegion(reducer=ee.Reducer.mean(), geometry=poi, scale=250).get('NDVI')
    return img.set('date', img.date().format()).set('mean',mean)
poi_reduced_imgs = NDVI.map(poi_mean)
nested_list = poi_reduced_imgs.reduceColumns(ee.Reducer.toList(2), ['date','mean']).values().get(0)
df_ndvi     = pd.DataFrame(nested_list.getInfo(), columns=['date','mean'])

df_ndvi["NDVI"] = df_ndvi["mean"] * 0.0001 # !!Remember: there's a scale factor to apply!!
df_ndvi['date'] = pd.to_datetime(df_ndvi['date'])
df_ndvi.set_index('date', inplace=True)

# Display the NDVI time series for this site (notice: it's a 16-day ts and we
# need daily data...)
df_ndvi["NDVI"].plot(ylabel='NDVI',title='NDVI in US-Bi2 site')
NDVI_=df_ndvi["NDVI"].tolist()
