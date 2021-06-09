# 9b_Calculate_FAO56_ET_and_display

# Calculate actual ET [mm d-1] using FAO56 with NDVI:
data['ET_model'] = data[['kc','fao_reference_et']].apply(
    lambda row: et.actual_evapotranspiration(row['kc'], row['fao_reference_et']) , axis=1)

# Display modeled and observed ET
data[['ET_model', 'ET']].plot(figsize=(15,4),ylabel='ET mm d-1',xlabel='DATE',title='Observed and modeled ET in maize (US-Bi2 site)')
