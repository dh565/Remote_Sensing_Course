from osgeo import gdal
referenceFile = '/content/Clipped_new_MOD11A1_03022019.tif'
reference = gdal.Open(referenceFile, 0)  # this opens the file in only reading mode
referenceTrans = reference.GetGeoTransform()
x_res = referenceTrans[1]
y_res = referenceTrans[2]

inDs = gdal.Open( '/content/ESA_LAND_USE_2019_SMOLL2.tif')
outDs = gdal.Warp( 'new.tif', inDs,
                  format = 'GTiff',
                  xRes = x_res, yRes =y_res,
                  resampleAlg = gdal.GRA_Mode)# mode: GRA_Mode resampling, selects the value which appears most often of all the sampled points.see- https://gdal.org/programs/gdalwarp.html

inDs = None
outDs = None
