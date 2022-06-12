dataset = rasterio.open('/content/LAND_US100ME.tif')

land_use_raster        = dataset.read(1)
land_use_raster_unique = np.unique(land_use_raster)
list_land_use          = list(land_use_raster_unique)
