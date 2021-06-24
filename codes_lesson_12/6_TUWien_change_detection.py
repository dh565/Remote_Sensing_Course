#6 TU Wien Change Detection Approach and plot Histogram 

################################################################################################################
# IMPORTANT NOTE:
# Here you should calculate the moisture index as shown in class using the TU Wein change detection index.
# The index is calculated as an 2-D array.
# Name your index as follows: moisture_index 
# You'll use the index array 'moisture_index' in following lines to display an histogram of the index.
################################################################################################################

SAR_C = rasterio.open('/content/sentinel 1_data.tif')
SAR_C = SAR_C.read(1) # read the data from the TIF file

plt.hist(moisture_index.ravel(), bins=256, range=(moisture_index.min(), moisture_index.max()),  ec='royalblue')
plt.show()
