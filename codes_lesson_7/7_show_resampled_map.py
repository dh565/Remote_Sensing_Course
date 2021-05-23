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
