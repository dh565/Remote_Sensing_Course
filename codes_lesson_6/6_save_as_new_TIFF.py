# This function saves your new (delts) array into a TIF file with geographical attributes
# from your previously saved 'Clipped_new_MOD11A1_03022019_1030.tif' file
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

array_input = DT_1030             ### DT_1030 - this is the array u want to save (change here the array)    ###
saved_file_name = "DT_1030.tif"   ### This is the name of your newly save TIF file - (change the name here) ###

# DON'T TOUCH ENEYTHING FROM HERE -----------------------------------------------------------------------------

with rasterio.open('/content/drive/MyDrive/gdrive_folder/Clipped_new_MOD11A1_03022019_1030.tif') as src:
    raster = src.read(1)   

kwargs = src.meta

# Update kwargs (change in data type)
kwargs.update( dtype=rasterio.float64, count = 1)

with rasterio.open(saved_file_name, 'w', **kwargs) as dst:
          dst.write_band(1, array_input.astype(rasterio.float64))
