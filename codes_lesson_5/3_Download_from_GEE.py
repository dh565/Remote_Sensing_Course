# Go to GEE and download data (image/s) for your AOI (data file/s will be downloaded to your Google Drive account)

img = ee.Image('MODIS/006/MOD11A1/2019_02_03').select('LST_Day_1km');
fc= ee.FeatureCollection('users/davidhelman1/AOI_Israel');

task = ee.batch.Export.image.toDrive(image=img,     # an ee.Image object.
                                     region         = fc.geometry().bounds(), # an ee.Geometry object.
                                     description    = 'LST_MOD11A1_03022019_1000',
                                     folder         = 'gdrive_folder',
                                     fileNamePrefix = 'LST_MOD11A1_03022019_1000',
                                     scale          = 1000,
                                     crs='EPSG:4326')
task.start()
