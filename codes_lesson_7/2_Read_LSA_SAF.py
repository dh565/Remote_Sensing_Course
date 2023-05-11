# 2_Read_LSA_SAF files
SAF_file = 'LSASAF_MSG_DSSF_MSG-Disk_201902021000.nc'
SAF_name = SAF_file[0:-25]
print(SAF_name)

rds      = rio.open_rasterio(path + SAF_file) # Read SAF NetCDF file {whean rioxarray as rio}

dset_w84 = rds.rio.reproject("EPSG:4326")# reproject to WG84
dset_w84["DSSF"].rio.to_raster('SAF.tif') # select LST band
raster_LSASAF = rasterio.open('SAF.tif')
array = raster_LSASAF.read(1)
show((raster_LSASAF, 1))
