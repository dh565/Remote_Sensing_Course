# Show resampled LSASAF 
# ------------------------------------------------------------------------------------------------------------------------- #
file_new  = '/content/drive/MyDrive/gdrive_folder/Clipped_Resampled_1km_LSASAF_MSG_DSSF.tif'
trim_name = file_new[55:-4]
print (trim_name)
MSG = rasterio.open(file_new)

array_LSASAF = MSG.read(1) * 10.0 # Note here that there's a factor of 10.0 required for the DSSF product.
print(np.nanmax(array_LSASAF))    # Print maximum value for this image

array_LSASAF[array_LSASAF < 10] = 'nan'
plt.imshow(array_LSASAF, interpolation='none')
plt.show()
# ------------------------------------------------------------------------------------------------------------------------- #
# This function saves your new (delts) array into a TIF file with geographical attributes
# from your previously saved 'Clipped_new_MOD11A1_03022019_1030.tif' file
# ------------------------------------------------------------------------------------------------------------------------- #
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

array_input     = array_LSASAF    
# ------------------------------------------------------------------------------------------------------------------------- #
saved_file_name = 'new_' + file_new[37:]  ### This is the name of your newly saved file - (change name here if you want)  ###
# ------------------------------------------------------------------------------------------------------------------------- #
# @@@@@@@@      DON'T CHANGE ANYTHING BELOW THIS LINE   @@@@@@@@@
# ------------------------------------------------------------------------------------------------------------------------- #
with rasterio.open('/content/drive/MyDrive/gdrive_folder/Clipped_new_MOD11A1_03022019_1030.tif') as src:
    raster = src.read(1)   

kwargs = src.meta

# Update kwargs (change in data type)
kwargs.update( dtype=rasterio.float64, count = 1)

with rasterio.open("/content/drive/MyDrive/gdrive_folder/" + saved_file_name, 'w', **kwargs) as dst:
          dst.write_band(1, array_input.astype(rasterio.float64))
# ------------------------------------------------------------------------------------------------------------------------- #
