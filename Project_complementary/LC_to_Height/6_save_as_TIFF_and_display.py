# save the new file using the attributes of the original TIFF:
with rasterio.open('/content/LAN_COVER_100m.tif') as src:
    raster = src.read(1)   

kwargs = src.meta

# Update kwargs (change in data type)
kwargs.update( dtype=rasterio.float64, count = 1)

with rasterio.open('/content/height_from_LC_100.tif', 'w', **kwargs) as dst:
          dst.write_band(1, h_raster.astype(rasterio.float64))
 

# Display only if the TIFF was already saved in your dir
raster_height = rasterio.open('/content/height_from_LC_100.tif')
show((raster_height, 1))
