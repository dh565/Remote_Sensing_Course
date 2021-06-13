from rasterstats import zonal_stats
import pandas as pd

# Open shapefile
gdf  = gpd.read_file('/content/drive/MyDrive/gdrive_folder_NPP/MtCarmel_wildfire_area.shp') # YOU NEED to upload the data first, of course!

with rasterio.open('/content/drive/MyDrive/gdrive_folder_NPP/NPP_avg_2001_2009') as src:
    affine = src.transform
    array  = src.read(1)
    df_zonal_stats = pd.DataFrame(zonal_stats(gdf, array, affine=affine))
    
# adding statistics back to original GeoDataFrame
gdf       = pd.concat([gdf, df_zonal_stats], axis=1) 

# Now all you need is to inquire gdf to get the number of pixels in the polygon and the mean value of all pixels in the polygon... 
