# 2_Read_LSA_SAF files
SAF_file = 'NETCDF4_LSASAF_MSG_MDSSFTD_MSG-Disk_201902031030.nc'

SAF_name = SAF_file[0:-25]
print(SAF_name)

rds       = xr.open_dataset(path + SAF_file) # Read SAF NetCDF file {whean rioxarray as rio}

# dset_w84 = rds.rio.reproject("EPSG:4326")# reproject to WG84
rds["DSSF_TOT"].rio.to_raster('SAF.tif') # select LST band
raster_LSASAF = rasterio.open('SAF.tif')
array = raster_LSASAF.read(1)
show((raster_LSASAF, 1))
