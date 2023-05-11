# 4_Get the coordinates of the reference file (WRF, in our case)
minx, miny = raster_wrf.bounds[0], raster_wrf.bounds[1] # copy the coordinates to HERE...
maxx, maxy = raster_wrf.bounds[2], raster_wrf.bounds[3]
bbox = box(minx, miny, maxx, maxy)
print(bbox)
