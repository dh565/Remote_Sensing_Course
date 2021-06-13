# Read shapefile
shp_fname      = r'/content/drive/MyDrive/gdrive_folder_NPP/MtCarmel_wildfire_area.shp'
shape_feature = ShapelyFeature(Reader(shp_fname).geometries(),
                               ccrs.PlateCarree(), facecolor="none",
                               edgecolor='black', lw=0.5)

# To add your shapefile over a raster you need to use the same procedure used to upload
# and present the coastline or oceans in cartopy - i.e. ax1.add_feature(shape_feature)...
