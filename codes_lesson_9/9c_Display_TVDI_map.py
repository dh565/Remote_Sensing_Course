# Let's plot the TVDI image nicely...
from matplotlib import ticker
import cartopy.crs as ccrs

TVDI = xr.open_rasterio(tvdiRaster)
array_input = TVDI

plt.figure(figsize=(9,6))

ax1 = plt.axes(projection=ccrs.Robinson())
ax1.coastlines()
ax1.add_feature(cartopy.feature.OCEAN)
ax1.gridlines(draw_labels=True)

p1 = array_input.plot(ax=ax1,
             vmin=0, vmax=1,
             cmap='RdBu_r',
             transform=ccrs.PlateCarree(),
             add_colorbar=False)

plt.title('TVDI for 15/Mar/2017 (Spain)')

ax_cb = plt.axes([0.25, 0.05, 0.525, 0.02])
tick_locator = ticker.MaxNLocator(nbins=10)
cb = plt.colorbar(p1, cax=ax_cb, orientation='horizontal')
cb.locator = tick_locator
cb.update_ticks()
cb.ax.set_xlabel('Wet                                              TVDI                                              Dry');
