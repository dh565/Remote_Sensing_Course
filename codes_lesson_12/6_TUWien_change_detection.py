#6 TU Wien Change Detection Approach and plot Histogram 
SAR_C = rasterio.open('/content/sentinel 1_data.tif')
SAR_C = SAR_C.read(1) # read the data from the TIF file

plt.hist(moisture_index.ravel(), bins=256, range=(moisture_index.min(), moisture_index.max()),  ec='royalblue')
plt.show()
