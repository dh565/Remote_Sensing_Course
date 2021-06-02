# Get the SM data from the shapefile
soil_mostire_list = []
TVDI_list = []

# Open point shapefile
pointData  = gpd.read_file('/content/data_sm.shp') # YOU NEED to upload the data first, of course!

# Get TVDI raster
tvdiRaster = rasterio.open('/content/TVDI.tif')

print(tvdiRaster.crs)
print(tvdiRaster.count)

# Show point and raster on a matplotlib plot
fig, ax = plt.subplots(figsize=(12,12))
pointData.plot(ax=ax, color='orangered')
show(tvdiRaster, ax=ax)

for point in pointData['geometry']:
    print(point.xy[0][0],point.xy[1][0])
    
index = -1   
for point in pointData['geometry']:
    x = point.xy[0][0]
    y = point.xy[1][0]
  
    index += 1

    soil_mostire =pointData["SM"][index]
    row, col = tvdiRaster.index(x,y)
    TVDI=tvdiRaster.read(1)[row,col]
    TVDI_list.append(TVDI)
    soil_mostire_list.append(soil_mostire)
