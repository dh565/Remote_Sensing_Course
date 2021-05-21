# Go to GEE and download data (image/s) for your AOI (data file/s will be downloaded to your Google Drive account)
product_name = 'MODIS/006/MCD15A3H'
band         = 'Lai'
name_to_save = 'LAI_MCD15_03022019'
scale_res    = 500 

# ============================================================================= #
# Don't change anything below this line
# ============================================================================= #
#var temps2013 = ee.ImageCollection('MODIS/006/MCD15A3H').filterDate('2015-12-25', '2018-12-25')
img          = ee.Image(product_name + '/2019_02_02').select(band);
fc           = ee.FeatureCollection('users/davidhelman1/AOI_Israel');
  
task = ee.batch.Export.image.toDrive(image=img,     # an ee.Image object.
                                     region         = fc.geometry().bounds(), # an ee.Geometry object.
                                     description    = name_to_save,
                                     folder         = 'gdrive_folder',
                                     fileNamePrefix = name_to_save,
                                     scale          = scale_res,
                                     crs='EPSG:4326')
task.start()
