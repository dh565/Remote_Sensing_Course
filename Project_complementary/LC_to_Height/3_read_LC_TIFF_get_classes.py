# You'll need first to download the LC TIFF of the 100m
# CGLS-LC100 Collection 3 (Copernicus product) and save it
# as 'LAND_COVER_100m.tif
dataset = rasterio.open('/content/LAND_COVER_100m.tif')

land_use_raster        = dataset.read(1)
land_use_raster_unique = np.unique(land_use_raster)
list_land_use          = list(land_use_raster_unique)
