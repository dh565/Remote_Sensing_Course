# =================================================================================================== #
# Uses Planck to calculate brightness temperature for each MSG channel (use wavenumber formula):
# =================================================================================================== #

b     = len(chl)
print(b)
wl    = [0.6,0.8,1.6,3.9,6.2,7.3,8.7,9.7,10.8,12.0,13.5]
T_rad = sub_data * 0.0

for i in range(0,b):
    wn    = 1e4/wl[i]
    print(wn)
    BT    = sub_data[i,:,:]
    T_rad[i] = (C2*wn)/(np.log((((C1*(wn)**3)/BT)+1))) - 273.15
# =================================================================================================== #
# That's all the loop stuff problem...
# =================================================================================================== #