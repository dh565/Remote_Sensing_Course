# Replace the class (see from previous print) with the height in meters
h = [np.nan,1.5,0.3,1.0,np.nan,0,np.nan,0,8,8,8,8,5,5,5,5,np.nan]

# This will create the new array (it might take long if your AOI is big
# because the spatial resolution is 100 m...)
def switch_val(x):
    return h[list_land_use.index(x)] if x in list_land_use else x
vc       = np.vectorize(switch_val)
h_raster = vc(land_use_raster)
print("end")
