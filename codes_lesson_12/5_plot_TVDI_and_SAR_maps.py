#4 plot the  TVDI image and the SAR data 
TVDI_clip = rasterio.open('/content/Clipped_new_MOD11A1_03022019.tif')


# set font size for title:
plt.rcParams.update({'font.size': 15}) 

# set panel for plots
fig, (ax1, ax2)= plt.subplots(ncols=1, nrows=2,figsize=(10,10))


array1                  = SAR.read(1) 
array1                  = array1 
img1                    = ax1.imshow(array1,cmap='jet')

array2                  = TVDI_clip = TVDI_clip.read(1)
array2                  = array2 
array2                  = array2
img2                    = ax2.imshow(array2,cmap='jet')

# set colorbar, axes, and title for WRF
cbar1 = fig.colorbar(img1, ax=ax1)
cbar1.ax.set_ylabel('need to chnge')

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title(r'$\overline{\gamma^o}$ [dB]')
ax1.set_aspect('auto')

# set colorbar, axes, and title for MODIS
cbar2 = fig.colorbar(img2, ax=ax2)

cbar2.ax.set_ylabel('wet')

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title("TVDI")
ax2.set_aspect('auto')

plt.tight_layout(h_pad=1)
