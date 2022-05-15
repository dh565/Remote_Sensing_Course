# We need to resample one of the images to the spatial resolution of the
# other. Let's resample WRF 2-km to the 1-km resolution of MODIS

from osgeo import gdal, gdalconst

# The tile needed to be resampled to the new resolution
inputfile  = "/content/wrf_file.tif"
input      = gdal.Open(inputfile, gdalconst.GA_ReadOnly)
inputProj  = input.GetProjection()
inputTrans = input.GetGeoTransform()

# The refernce file for resampling
referencefile = "/content/Clipped_new_MOD11A1_03022019.tif"
reference = gdal.Open(referencefile, gdalconst.GA_ReadOnly)
referenceProj = reference.GetProjection()
referenceTrans = reference.GetGeoTransform()
bandreference = reference.GetRasterBand(1)    
x = reference.RasterXSize 
y = reference.RasterYSize

# The output resampled file (WRF to 1 km)
outputfile = "/content/WRF_resampled_to_1km.tif"
driver= gdal.GetDriverByName('GTiff')
output = driver.Create(outputfile,x,y,1,bandreference.DataType)
output.SetGeoTransform(referenceTrans)
output.SetProjection(referenceProj)

gdal.ReprojectImage(input,output,inputProj,referenceProj,gdalconst.GRA_Bilinear)

del output

resm_WRF = rasterio.open(outputfile)
