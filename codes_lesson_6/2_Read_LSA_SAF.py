rds = rio.open_rasterio('saf_netcdf.nc')# i dount like to read the original name of the file mybe to longe

dset_w84 = rds.rio.reproject("EPSG:4326")# reproject to wg84
dset_w84["LST"].rio.to_raster('SAF.tif')
raster_MSG_LST = rasterio.open('SAF.tif')
array = raster_MSG_LST.read(1)
show((raster_MSG_LST, 1))
