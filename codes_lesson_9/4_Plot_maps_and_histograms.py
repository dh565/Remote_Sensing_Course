# ============================================================================== #
# 4_Plot the maps of NDVI and LST and their histograms
# ============================================================================== #

# Prepare for plotting
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
plt.subplots_adjust(left=0.125, right = 0.9, wspace=0.3)

# Subplot LST
img1 = ax1.imshow(TS, cmap='magma', vmin=280, vmax=305)
ax1.set_title("TS - daily\n15/Mar/2017")
divider = make_axes_locatable(ax1)
cax1 = divider.append_axes("right", size="5%", pad=0.2)
cbar = fig.colorbar(img1, cax=cax1)
cbar.set_label("Land surface temperature (°Kelvin)")

# Subplot NDVI
img2 = ax2.imshow(NDVI, cmap='RdYlGn', vmin=0.1, vmax=0.8)
ax2.set_title("NDVI - 16 days\n15/Mar/2017 - 22/Mar/2017")
divider = make_axes_locatable(ax2)
cax2 = divider.append_axes("right", size="5%", pad=0.2)
cbar = fig.colorbar(img2, cax=cax2)
cbar.set_label("NDVI")

# Subplot Histogram LST
img3 = ax3.hist(TS.ravel(), bins=256, range=(280, 310), lw=4, ec='royalblue')
ax3.set_aspect(1./ax3.get_data_ratio())
ax3.set_title("Histogram LST")
ax3.set_xlabel('LST')
ax3.set_ylabel('Number of pixels')

# Subplot Histogram NDVI
img4 = ax4.hist(NDVI.ravel(), bins=256, range=(0.1, 0.9), lw=4, ec='royalblue')
ax4.set_aspect(1./ax4.get_data_ratio())
ax4.set_title("Histogram NDVI")
ax4.set_xlabel('NDVI')
ax4.set_ylabel('number of pixels')
