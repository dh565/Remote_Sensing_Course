# 4_Read the downloaded MODIS tif file from GEE and display

raster_MOD = rasterio.open('/content/drive/MyDrive/gdrive_folder/LST_MOD11A1_03022019_1030.tif')
show((raster_MOD, 1))

# Let's get the coordinates of the tile
raster_MOD.bounds
