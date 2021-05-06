import satpy
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Read MSG's NetCDF file
scn  = satpy.Scene(reader='seviri_l1b_nc', filenames=['W_XX-EUMETSAT-Darmstadt,VIS+IR+HRV+IMAGERY,MSG1+SEVIRI_C_EUMG_20060402120009.nc'])

# Get info on attributes
scn.attrs

# Get info on channels
scn.all_dataset_names()

# Load specific channels:
scn.load(["VIS006",'VIS008','IR_016','WV_073','WV_062',"IR_097"])

scn.keys()# the VIS006 and VIS008 have IR_016 are been calibration  to reflectance automatically satpy 
