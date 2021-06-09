# 5_Read_meteo_data

# NOTE: You need to upload these two python codes into your working dir first: 
# 'estimate_daily_et.py' and 'evapotranspiration_fao.py'
import evapotranspiration_fao as et

# Let's set the timeframe of our analysis:
start_date = '2017-01-01' # first is month and then day
end_date   = '2021-03-01' 

# Upload your meteo data (from Fluxnet site...)
df_full = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/AMF_US-Bi2_BASE_HH_10-5.csv',parse_dates=['DATE'], dayfirst=True)
df_full = df_full.set_index('DATE')
df_full.head()

df = df_full.loc[start_date:end_date]

# Let's see if it read our data...
df
