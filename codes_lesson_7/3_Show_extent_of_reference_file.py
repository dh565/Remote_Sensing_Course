# 3_Show reference file
raster_wrf = rasterio.open(path + 'WRF_u10.tif')
show((raster_wrf, 1))
