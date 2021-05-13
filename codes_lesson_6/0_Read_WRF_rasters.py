# Read the WRF tif file and display

raster_wrf_1030 = rasterio.open('/content/drive/MyDrive/gdrive_folder/wrf_Ta_2019-02-03-10-30-WG84.tif')
raster_wrf_1330 = rasterio.open('/content/drive/MyDrive/gdrive_folder/wrf_Ta_2019-02-03-13-30-WG84.tif')
show((raster_wrf_1030, 1))
show((raster_wrf_1330, 1))
