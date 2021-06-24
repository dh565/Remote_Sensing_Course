#7 save the moisture_index of SAR

with rasterio.open('/content/sentinel 1_data.tif') as src:
    raster = src.read(1)   
kwargs = src.meta
kwargs.update( dtype=rasterio.float64, count = 1)

with rasterio.open('SAR_sm.tif', 'w', **kwargs) as dst:
          dst.write_band(1, moisture_index.astype(rasterio.float64))
