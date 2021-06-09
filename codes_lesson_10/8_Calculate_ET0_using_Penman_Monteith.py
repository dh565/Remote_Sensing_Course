# 8_Calculate_ET0_using_Penman_Monteith

df['fao_reference_et'] = df[['NETRAD_daily','TA','WS','ea','PA']].apply(
    lambda row: et.fao_reference_et(row['NETRAD_daily'],
                                    row['TA'],row['WS'],
                                    row['ea'],row['PA']) , axis=1)

# Display both, ET0 and actual ET
df['fao_reference_et'].plot(figsize=(15,4), 
                            ylabel='ET fluxes (mm day$^{-1}$)',xlabel='DATE',
                            title='Water vapor fluxes (US-Bi2 site)', 
                            label="$ET_{0}$  (P-M)")
df['ET'].plot(ylabel = 'ET (mm day$^{-1}$)', label="$ET_{A}$")
plt.legend(loc="upper right")
