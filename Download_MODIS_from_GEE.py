# Go to GEE and download data (image/s) for your AOI (data file/s will be downloaded to your Google Drive account)
product_name = 'MODIS/006/MOD13A2'
band         = 'NDVI'
name_to_save = 'NDVI_22_03_2017'
scale_res    = 1000 

# ============================================================================= #
# Don't change anything below this line
# ============================================================================= #
#var temps2013 = ee.ImageCollection('MODIS/006/MCD15A3H').filterDate('2015-12-25', '2018-12-25')
img          = ee.Image(product_name + '/2017_03_22').select(band);
fc           = ee.FeatureCollection('users/davidhelman1/Spain_AOI_for_TVDI'); # HERE change it to your GEE address of your shp file 
  
task = ee.batch.Export.image.toDrive(image=img,     # an ee.Image object.
                                     region         = fc.geometry().bounds(), # an ee.Geometry object.
                                     description    = name_to_save,
                                     folder         = 'gdrive_folder',
                                     fileNamePrefix = name_to_save,
                                     scale          = scale_res,
                                     crs='EPSG:4326')
task.start()
