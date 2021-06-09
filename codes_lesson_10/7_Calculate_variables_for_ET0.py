# 7_Calculate_variables_for_ET0

# Calculate saturation vapor pressure from Tavg and RH:
df['es'] = df['TA'].apply(et.Saturation_vapor_pressure)

# Now, let's use es to calculate the actual vapour pressure (ea)
df['ea'] = ( (1 - (df['RH']) / 100) ) * df['es']

# Display the actual vapor pressure:
df['ea'].plot(ylabel='ea (kPa)',xlabel='DATE',title='Actual vapor pressure (US-Bi2 site)')
