rds = rio.open_rasterio('saf_netcdf.nc') # Read SAF NetCDF file

dset_w84 = rds.rio.reproject("EPSG:4326")# reproject to WG84
dset_w84["LST"].rio.to_raster('SAF.tif') # select LST band
raster_MSG_LST = rasterio.open('SAF.tif')
array = raster_MSG_LST.read(1)
show((raster_MSG_LST, 1))
