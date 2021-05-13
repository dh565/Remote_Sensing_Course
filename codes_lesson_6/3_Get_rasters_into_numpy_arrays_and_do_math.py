# Read WRF tile, replace no values with nan and convert to degrees C
array_wrf1030                       = resm_WRF1030.read(1) 
array_wrf1030                       = array_wrf1030 * 1.0
array_wrf1030                       = array_wrf1030 - 273.15
array_wrf1030[array_wrf1030 < -270] = np.nan

# Read WRF tile, replace no values with nan and convert to degrees C
array_wrf1330                       = resm_WRF1330.read(1) 
array_wrf1330                       = array_wrf1330 * 1.0
array_wrf1330                       = array_wrf1330 - 273.15
array_wrf1330[array_wrf1330 < -270] = np.nan

# Read MODIS clipped tile, replace no values with nan and convert to degrees C
# (notice that there's a factor required to get true values for MOD11A1 product)
array_MOD                  = MOD1030_clip.read(1)
array_MOD                  = array_MOD * 1.0
array_MOD[array_MOD == 0]  = np.nan
array_MOD                  = array_MOD * 0.02 - 273.15

# Read MODIS clipped tile, replace no values with nan and convert to degrees C
# (notice that there's a factor required to get true values for MOD11A1 product)
array_MYD                  = MYD1330_clip.read(1)
array_MYD                  = array_MYD * 1.0
array_MYD[array_MYD == 0]  = np.nan
array_MYD                  = array_MYD * 0.02 - 273.15
