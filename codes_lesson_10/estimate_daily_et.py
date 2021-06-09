# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:59:07 2020

@author: slauniai

Estimate daily ET from meteorological station data in absense of radiation data:
    1) estimate net radiation balance in absense of direct measurements
    2) compute daily reference ETo
    3) compute actual evaporation as ETa = Kc x ETo

    The crop coefficient Kc should be determined against ET measurements from
    similar ecosystem; it is function of LAI, plant water use traits, albedo, soil moisture etc.

Step 1) can be omitted or modified if met. station provides radiation data or records sunshine hours

Tested part 1) with FAO -reference Example 16

"""

import evapotranspiration_fao as et

# vapour pressure from relative humidity:
# es, _ =  et.saturation_vapor_pressure(Tave)
# ea = (1 - RH / 100.0) * es

air_pressure = et.pressure_from_altitude(elev)

# 1) net radiation balance [MJ m-2 d-1]

# daily solar radiation and daily clear-sky solar radiation estimated from met. station data
Rs, Rso = et.fao_shortwave_radiation(latitude, jday, Tmin, Tmax, krs=0.19)

# daily net longwave radiation
Rnl = et.fao_net_longwave_radiation(Tmin, Tmax, ea, Rs, Rso)

# daily net radiation of reference crop
Rn = (1. - albedo) * Rs - Rnl

# 2) daily reference ETo [mm d-1]
ETo = et.fao_reference_et(Rn, Tave, U, ea, P=air_pressure)

# 3) actual ET [mm d-1]
ETa = et.actual_evapotranspiration(ETo, Kc)

print('*** ETa = %.2f mm d-1, ETo = %.2f mm d-1 ***' %(ETa, ETo))
print('*** Rn = %.2f MJ m-2 d-1, Rs = %.2f MJ m-2 d-1, Rnl = %.2f MJ m-2 d-1 ***' %(Rn, Rs, Rnl))
