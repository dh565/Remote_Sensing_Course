# Show resampled LSASAF 
file_new  = '/content/drive/MyDrive/gdrive_folder/Clipped_Resampled_1km_LSASAF_MSG_DSSF.tif'
trim_name = file_new[55:-4]
print (trim_name)
MSG = rasterio.open(file_new)

array_LSASAF2 = MSG.read(1) * 10.0 # Note here that there's a factor of 10.0 required for the DSSF product.
print(np.nanmin(array_LSASAF))

array_LSASAF2[array_LSASAF2 < 10] = 'nan'
plt.imshow(array_LSASAF2, interpolation='none')
plt.show()

# This function saves your new (delts) array into a TIF file with geographical attributes
# from your previously saved 'Clipped_new_MOD11A1_03022019_1030.tif' file
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

array_input     = array_LSASAF2             
saved_file_name = 'new2_' + file_new[37:]  ### This is the name of your newly save TIF file - (change the name here) ###

# DON'T TOUCH ENEYTHING FROM HERE -----------------------------------------------------------------------------

with rasterio.open('/content/drive/MyDrive/gdrive_folder/Clipped_new_MOD11A1_03022019_1030.tif') as src:
    raster = src.read(1)   

kwargs = src.meta

# Update kwargs (change in data type)
kwargs.update( dtype=rasterio.float64, count = 1)

with rasterio.open("/content/drive/MyDrive/gdrive_folder/" + saved_file_name, 'w', **kwargs) as dst:
          dst.write_band(1, array_input.astype(rasterio.float64))
