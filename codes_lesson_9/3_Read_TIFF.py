# Notice that you need to download the TIF files from GEE (using the procedure that we already used before)
# and save the files in your folder or Google Drive, if you use the Google Colab...

# Read the TIF files using rasterio
NDVI = rasterio.open('/content/NDVI_22_03_2017.tif') # This is the name of your LST saved file
NDVI = NDVI.read(1) # read the data from the TIF file
NDVI = NDVI*0.0001  # data need to be scaled for this product
NDVI[NDVI <= 0.0] = np.nan # replace invalid, negative values with nan

LST = rasterio.open('/content/LST_15_03_2017.tif') # This is the name of your NDVI saved file
LST = LST.read(1)   # read the data from the TIF file
LST = LST*0.02      # data need to be scaled for this product

# Replace all zeros with nan
LST[LST == 0.0] = np.nan

# Round values to 2 places after the decimal point (not sure that this is necessary)
TS   = np.round(LST, 2)
NDVI = np.round(NDVI, 2)