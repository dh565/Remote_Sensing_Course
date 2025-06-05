# ============================================================================== #
# 8_Calculate TVDI (general formula) and apply to numpy NDVI and LST arrays
# ============================================================================== #

# Use the linear regression's coefficients to derive TVDI 
a1, b1 = MaxPfit
a2, b2 = MinPfit

Ts_max = b1 + (a1 * NDVI)
Ts_min = b2 + (a2 * NDVI)

TVDI = (TS - Ts_min) / (Ts_max - Ts_min)

# Print the range in this map
print(np.nanmin(TVDI))
print(np.nanmax(TVDI))
