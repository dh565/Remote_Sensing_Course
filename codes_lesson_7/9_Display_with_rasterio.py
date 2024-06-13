# 9_Display nicely your result...(using rasterio and geographic elements)

# Import necessary libraries
from matplotlib import ticker
import cartopy.crs as ccrs

# Define the file path for the dataset
file_new    = '/content/drive/MyDrive/gdrive_folder/new_Clipped_Resampled_1km_LSASAF_MSG_DSSF.tif'

# Open the dataset using xarray with rasterio engine
LSASAF_DSSF = xr.open_dataset(file_new, engine='rasterio')

# Set the input array for plotting
array_input = LSASAF_DSSF

# Create a new figure for the plot
plt.figure(figsize=(9,6))

# Set up the map projection using a Robinson projection
ax1 = plt.axes(projection=ccrs.Robinson())

# Add coastlines, ocean, lakes, and rivers to the map
ax1.coastlines()
ax1.add_feature(cartopy.feature.OCEAN)
ax1.add_feature(cartopy.feature.LAKES, alpha=1.0)
ax1.add_feature(cartopy.feature.RIVERS)

# Plot the data on the map, specifying levels, min and max values, colormap, and projection
p1 = array_input['band_data'].plot(ax=ax1, 
                                   levels=15, vmin=400, vmax=800, 
                                   cmap='viridis', 
                                   transform=ccrs.PlateCarree(), 
                                   add_colorbar=False)
#gl = ax.gridlines(draw_labels=False)

# Set the title for the plot
plt.title('DSSF from LSA-SAF at 10:00')

# Create a colorbar
ax_cb = plt.axes([0.325, 0.08, 0.40, 0.02])
tick_locator = ticker.MaxNLocator(nbins=8)
cb = plt.colorbar(p1, cax=ax_cb, orientation='horizontal')
cb.locator = tick_locator
cb.update_ticks()
cb.ax.set_xlabel('Downward Surface Shortwave Flux (W m$^{-2}$)');
