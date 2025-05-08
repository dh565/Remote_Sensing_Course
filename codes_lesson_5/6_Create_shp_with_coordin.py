# 6_Create a shapefile with the coordinates of the smaller tile (WRF)
minx, miny = ????????, ???????? # copy the coordinates to HERE...
maxx, maxy = ????????, ????????
bbox = box(minx, miny, maxx, maxy)
print(bbox)

import geopandas as gpd
from fiona.crs import from_epsg

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

from rasterio.mask import mask

# Now we are ready to clip the raster with the polygon using the coords 
# variable that we just created. Clipping the raster can be done easily with 
# the mask function that we imported from rasterio, and specifying clip=True.
out_img, out_transform = mask(raster_MOD, shapes=coords, crop=True)

# Next, we need to modify the metadata. 
# Let’s start by copying the metadata from the original data file.
out_meta = raster_MOD.meta.copy()
print(out_meta)

# Next we need to parse the EPSG value from the CRS so that we can create a 
# Proj4 string using PyCRS library (to ensure that the projection information 
# is saved correctly).
epsg_code = 4326
print(epsg_code)

# Now we need to update the metadata with new dimensions, transform (affine) 
# and CRS (as Proj4 text)
import pycrs
out_meta.update({"driver": "GTiff","height": out_img.shape[1],
                 "width": out_img.shape[2],
                 "transform": out_transform,
                 "crs": pycrs.parse.from_epsg_code(epsg_code).to_proj4()})

# Finally, we can save the clipped raster to disk with following command
out_tif = '/content/Clipped_new_MOD11A1_03022019.tif'
with rasterio.open(out_tif, "w", **out_meta) as dest:
  dest.write(out_img)
  
# Let’s check that the result is correct by plotting our new clipped raster
clipped_MOD = rasterio.open(out_tif)
show((clipped_MOD, 1), cmap='terrain')
