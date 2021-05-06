# Now let's display both images together and see typical values:

# set font size for title:
plt.rcParams.update({'font.size': 12}) 

# set panel for plots
fig, (ax1, ax2)= plt.subplots(ncols=2, nrows=1)

# Read WRF tile, replace no values with nan and convert to degrees C
array1                  = raster_wrf.read(1) 
array1[array1 == 32768] = 'nan'
array1                  = array1 - 273.15
img1                    = ax1.imshow(array1,cmap='jet')

# Read MODIS clipped tile, replace no values with nan and convert to degrees C
# (notice that there's a factor required to get true values for MOD11A1 product)
array2                  = clipped_MOD.read(1)
array2                  = array2 * 1.0
array2[array2 == 0]     = np.nan
array2                  = array2 * 0.02 - 273.15
img2                    = ax2.imshow(array2,cmap='jet')

# set colorbar, axes, and title for WRF
cbar1 = fig.colorbar(img1, ax=ax1)
cbar1.ax.set_ylabel('Temp [\N{DEGREE SIGN}C]')

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title("WRF")
ax1.set_aspect('auto')

# set colorbar, axes, and title for MODIS
cbar2 = fig.colorbar(img2, ax=ax2)
cbar2.ax.set_ylabel('Temp [\N{DEGREE SIGN}C]')

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title("MODIS")
ax2.set_aspect('auto')

plt.tight_layout(h_pad=1)
