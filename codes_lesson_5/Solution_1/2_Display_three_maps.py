# Now let's display both images together and see typical values:

# set font size for title:
plt.rcParams.update({'font.size': 12}) 

# set panel for plots
fig, (ax1, ax2, ax3)= plt.subplots(ncols=3, nrows=1, figsize=(10.5,4.5), constrained_layout=True)

# Read WRF tile, replace no values with nan and convert to degrees C
array3                  = resm_WRF.read(1) 
array3                  = array3 * 1.0
array3                  = array3 - 273.15
array3[array3 < -270]   = np.nan
img1                    = ax1.imshow(array3,cmap='jet', vmin=0, vmax=32)

# Read MODIS clipped tile, replace no values with nan and convert to degrees C
# (notice that there's a factor required to get true values for MOD11A1 product)
array2                  = clipped_MOD.read(1)
array2                  = array2 * 1.0
array2[array2 == 0]     = np.nan
array2                  = array2 * 0.02 - 273.15
img2                    = ax2.imshow(array2,cmap='jet', vmin=0, vmax=32)

# Read Delta T tile
img3                    = ax3.imshow(delta_T,cmap='coolwarm', vmin=-20, vmax=20)

# set colorbar, axes, and title for WRF
cax1  = make_colorbar_with_padding(ax1) # add a colorbar within its own axis the same size as the image plot
cbar1 = fig.colorbar(img1, ax=ax1, cax=cax1)
cbar1.ax.set_ylabel('Ta [\N{DEGREE SIGN}C]')

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title("WRF")
ax1.set_aspect('auto')

# set colorbar, axes, and title for MODIS
cax2  = make_colorbar_with_padding(ax2)
cbar2 = fig.colorbar(img2, ax=ax2, cax=cax2)
cbar2.ax.set_ylabel('Ts [\N{DEGREE SIGN}C]')

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title("MODIS")
ax2.set_aspect('auto')

# set colorbar, axes, and title for Delta T
cax3  = make_colorbar_with_padding(ax3)
cbar3 = fig.colorbar(img3, ax=ax3, cax=cax3)
cbar3.ax.set_ylabel('$\Delta$Temp [\N{DEGREE SIGN}C]')

ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_title("$\Delta$Temp")
ax3.set_aspect('auto')

plt.tight_layout(h_pad=1)
