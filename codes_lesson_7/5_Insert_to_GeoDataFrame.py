# Insert the bbox into a GeoDataFrame
geo = gpd.GeoDataFrame({'geometry': bbox}, index=[0], crs=from_epsg(4326))

# Re-project into the same coordinate system as the raster data
geo = geo.to_crs(crs=raster_wrf.crs.data)

# Next we need to get the coordinates of the geometry in such a format that rasterio wants them. 
# This can be conducted easily with following function.
def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]
  
# Get the geometry coordinates by using the function
coords = getFeatures(geo)
print(coords)
