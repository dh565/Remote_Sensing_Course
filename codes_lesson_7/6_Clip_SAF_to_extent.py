# 6_Clip LSA-SAF files to the extent of the reference file (WRF)

# Now we are ready to clip the raster with the polygon using the coords 
# variable that we just created. Clipping the raster can be done easily with 
# the mask function that we imported from rasterio, and specifying clip=True.
out_img, out_transform = mask(raster_LSASAF, shapes=coords, crop=True)
out_img[out_img<0] = 0
# Next, we need to modify the metadata. 
# Let’s start by copying the metadata from the original data file.
out_meta = raster_LSASAF.meta.copy()
print(out_meta)

# Next we need to parse the EPSG value from the CRS so that we can create a 
# Proj4 string using PyCRS library (to ensure that the projection information 
# is saved correctly).
epsg_code = 4326
#epsg_code = int(raster_LSASAF.crs.data['init'][5:]) # This was for an older version
print(epsg_code)

# Now we need to update the metadata with new dimensions, transform (affine) 
# and CRS (as Proj4 text)
import pycrs
out_meta.update({"driver": "GTiff","height": out_img.shape[1],
                 "width": out_img.shape[2],
                 'dtype': 'float64',
                 "transform": out_transform,
                 "crs": pycrs.parse.from_epsg_code(epsg_code).to_proj4()})

# Finally, we can save the clipped raster to disk with following command
out_tif = path + 'Clipped_' + SAF_name + '.tif'
with rasterio.open(out_tif, "w", **out_meta) as dest:
  dest.write(out_img* 0.01)#NEED TO SCALE
  
# Let’s check that the result is correct by plotting our new clipped raster
clipped_LSASAF = rasterio.open(out_tif)
array = clipped_LSASAF.read(1)
show((clipped_LSASAF, 1), cmap='terrain')
