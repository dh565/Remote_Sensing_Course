# ============================================================================== #
# 3_Read TIFF from your folder (IMPORTANT - read next comments)
# ============================================================================== #

# Notice that you need to download the TIF files from GEE (using the procedure 
# that we already used before) and save the files saved on your PC or Google 
# Drive folder if you use the Google Colab...

# Read the NDVI TIF file using rasterio
NDVI = rasterio.open('/content/drive/MyDrive/gdrive_folder/NDVI_22_03_2017.tif')
NDVI = NDVI.read(1) # read the data from the TIF file
NDVI = NDVI*0.0001  # data need to be scaled for this product
NDVI[NDVI <= 0.0] = np.nan # replace invalid, negative values with nan (nan = not a number)

# Read the LST TIF file using rasterio
LST = rasterio.open('/content/drive/MyDrive/gdrive_folder/LST_15_03_2017.tif')
LST = LST.read(1)   # read the data from the TIF file
LST = LST*0.02      # data need to be scaled for this product
LST[LST == 0.0] = np.nan # Replace all zeros with nan

# Round values to 2 places after the decimal point (not sure if this is really necessary...)
TS   = np.round(LST, 2)
NDVI = np.round(NDVI, 2)
