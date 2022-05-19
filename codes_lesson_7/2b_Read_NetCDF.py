SAF_file = 'LSASAF_MSG_DSSF_MSG-Disk_201902021000.nc'
SAF_name = SAF_file[0:-25]
print(SAF_name)

rds      = xr.open_dataset(path + SAF_file) # Read NetCDF file (the LSASAF product in ncdf format)

rds["DSSF"].plot()
