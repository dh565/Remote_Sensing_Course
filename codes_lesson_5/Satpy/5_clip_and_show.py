# Crop to a region via lat/lon values (lon_min, lat_min, lon_max, lat_max)
scn_cropped = scn.crop(ll_bbox=(30, 30, 36, 50))
scn_cropped.show("natural_color")
