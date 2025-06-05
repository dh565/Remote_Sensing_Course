# ============================================================================== #
# 9a_Save the TVDI map as a TIF file.
# ============================================================================== #

# Save the TVDI array as a TIF file (using metadata from the LST TIF file)
with rasterio.open('/content/drive/MyDrive/gdrive_folder/LST_15_03_2017.tif') as src:
    raster = src.read(1)   

kwargs = src.meta

# Update kwargs (change in data type)
kwargs.update( dtype=rasterio.float64, count = 1)

with rasterio.open('TVDI.tif', 'w', **kwargs) as dst:
          dst.write_band(1, TVDI.astype(rasterio.float64))
