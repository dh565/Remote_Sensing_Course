from matplotlib import ticker
import cartopy.crs as ccrs

file_new    = '/content/drive/MyDrive/gdrive_folder/new_Clipped_Resampled_1km_LSASAF_MSG_DSSF.tif'
LSASAF_DSSF = xr.open_rasterio(file_new)

array_input = LSASAF_DSSF

plt.figure(figsize=(9,6))

ax1 = plt.axes(projection=ccrs.Robinson())
ax1.coastlines()
ax1.add_feature(cartopy.feature.OCEAN)
ax1.add_feature(cartopy.feature.LAKES, alpha=1.0)
ax1.add_feature(cartopy.feature.RIVERS)

#gl = ax.gridlines(draw_labels=False)
p1 = array_input.plot(ax=ax1,
             levels=15, vmin=50, vmax=80,
             cmap='viridis',
             transform=ccrs.PlateCarree(),
             add_colorbar=False)

plt.title('DSSF from LSA-SAF at 10:00')

ax_cb = plt.axes([0.325, 0.08, 0.40, 0.02])
tick_locator = ticker.MaxNLocator(nbins=8)
cb = plt.colorbar(p1, cax=ax_cb, orientation='horizontal')
cb.locator = tick_locator
cb.update_ticks()
cb.ax.set_xlabel('Downward Surface Shortwave Flux (W m$^{-2}$)');
