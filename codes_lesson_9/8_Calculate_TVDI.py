# Use the linear regressions' coefficients to derive TVDI 
a1, b1 = MaxPfit
a2, b2 = MinPfit

Ts_max = b1 + (a1 * NDVI)
Ts_min = b2 + (a2 * NDVI)

TVDI = (TS - Ts_min) / (Ts_max - Ts_min)
print(np.nanmin(TVDI))
print(np.nanmax(TVDI))
