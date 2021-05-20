# We need to resample one of the images to the spatial resolution of the
# other. Let's resample LSASAF 4-km to the 1-km resolution of MODIS

from osgeo import gdal, gdalconst

# The tile needed to be resampled to teh new resolution
inputfile  = out_tif
input      = gdal.Open(inputfile, gdalconst.GA_ReadOnly)
inputProj  = input.GetProjection()
inputTrans = input.GetGeoTransform()

# The reference file for resampling
# ======================================================================================= #
# This is the MODIS raster clipped to the extent of WRF 
# (our reference extent) that we'll use as a reference of our new spatial resolution
# ======================================================================================= #
referencefile = path + 'Clipped_new_MYD11A1_03022019_1330.tif' 
# ======================================================================================= #

reference = gdal.Open(referencefile, gdalconst.GA_ReadOnly)
referenceProj = reference.GetProjection()
referenceTrans = reference.GetGeoTransform()
bandreference = reference.GetRasterBand(1)    
x = reference.RasterXSize 
y = reference.RasterYSize

# The output resampled file (WRF to 1 km)
# ======================================================================================= #
# This is the name we're giving to our new resampled SAF raster file:
# ======================================================================================= #
outputfile = path + 'Clipped_Resampled_1km_' + SAF_name + '.tif'
# ======================================================================================= #
driver= gdal.GetDriverByName('GTiff')
output = driver.Create(outputfile,x,y,1,bandreference.DataType)
output.SetGeoTransform(referenceTrans)
output.SetProjection(referenceProj)

gdal.ReprojectImage(input,output,inputProj,referenceProj,gdalconst.GRA_Bilinear)

del output
