from matplotlib import ticker
import cartopy.crs as ccrs

array_input = dT1330 # Change here the map that u want to display

plt.figure(figsize=(9,6))

ax1 = plt.axes(projection=ccrs.Robinson())
ax1.coastlines()
ax1.add_feature(cartopy.feature.OCEAN)
ax1.add_feature(cartopy.feature.LAKES, alpha=1.0)
ax1.add_feature(cartopy.feature.RIVERS)

#gl = ax.gridlines(draw_labels=False)     # uncomment this if u want a grid on your map
p1 = array_input.plot(ax=ax1,
             levels=17, vmin=-15, vmax=15,
             cmap='RdBu_r',               # This is the name of the color pallete 
             transform=ccrs.PlateCarree(),
             add_colorbar=False)

plt.title('Lapse rate at 13:30') # This is the title of the map (change here if u want...)

ax_cb = plt.axes([0.325, 0.08, 0.40, 0.02])
tick_locator = ticker.MaxNLocator(nbins=7)
cb = plt.colorbar(p1, cax=ax_cb, orientation='horizontal')
cb.locator = tick_locator
cb.update_ticks()
cb.ax.set_xlabel('$\Delta$T (°C)'); # This is the colorbar title
