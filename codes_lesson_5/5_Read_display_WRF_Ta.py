# 5_Read the WRF tif file and display

raster_wrf = rasterio.open('/content/wrf_file.tif')
show((raster_wrf, 1))

# Let's get the coordinates of the tile
raster_wrf.bounds
