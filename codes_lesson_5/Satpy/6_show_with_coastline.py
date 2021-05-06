from pyresample import geometry
area_id = "Griechenland"
description = "Griechenland und Umgebung in Mercator-Projektion"
proj_id = "Griechenland"
proj_dict = {"proj": "merc", "lat_ts": 38, 'lon_0': 25}

width = 800    # width of the result domain in pixels
height = 800   # height of the result domain in pixels

llx = -10E5   # projection x coordinate of lower left corner of lower left pixel
lly =  27E5   # projection y coordinate of lower left corner of lower left pixel
urx =  10E5   # projection x coordinate of upper right corner of upper right pixel
ury =  47E5   # projection y coordinate of upper right corner of upper right pixel

area_extent = (llx,lly,urx,ury)
area_def_greece = geometry.AreaDefinition(area_id, proj_id, description, proj_dict, width, height, area_extent)

local_scn = scn.resample(area_def_greece)

# First, we have to transpose the natural color composite values to a shape that can be interpreted 
# by the imshow method: (M,N,3)
image = np.asarray(local_scn["natural_color"]).transpose(1,2,0)

# Then we scale the values to the range between 0 and 1, clipping the lower and upper percentiles
# so that a potential contrast decrease caused by outliers is eliminated.
image = np.interp(image, (np.percentile(image,1), np.percentile(image,99)), (0, 1))

# Now we "copy" the coordinate reference system of our composite data set...
crs = local_scn["natural_color"].attrs["area"].to_cartopy_crs()

# ... and use it to generate an axes in our figure with the same CRS
fig = plt.subplots(figsize=(10,10))
ax = plt.axes(projection=crs)

# Now we can add some coastlines...
ax.coastlines(resolution="10m", color="white")

# ... and a lat/lon grid:
ax.gridlines(xlocs=range(10,45,5),ylocs=range(25,55,5))

# In the end, we can plot our image data...
ax.imshow(image, transform=crs, extent=crs.bounds, origin="upper")

# and add a title to our plot
plt.title("Natural color composite of Greece and surroundings, recorded by MSG at " + local_scn.attrs["start_time"].strftime("%Y-%m-%d %H:%M"))

# Finally, we can show the plot to the user:
plt.show()
