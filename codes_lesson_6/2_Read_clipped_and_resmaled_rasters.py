# Use rasterio to read your clipped and resampled rasters
# Use rasterio to read your clipped and resampled rasters
resm_WRF1030 = rasterio.open('/content/drive/MyDrive/gdrive_folder/WRF1030_resampled_to_1km.tif')
resm_WRF1330 = rasterio.open('/content/drive/MyDrive/gdrive_folder/WRF1330_resampled_to_1km.tif')
MOD1030_clip = rasterio.open('/content/drive/MyDrive/gdrive_folder/Clipped_new_MOD11A1_03022019_1030.tif')
MYD1330_clip = rasterio.open('/content/drive/MyDrive/gdrive_folder/Clipped_new_MYD11A1_03022019_1330.tif')
