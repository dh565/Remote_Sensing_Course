# =============================================================================== #
# 9d_Evaluate our TVDI with true SWC data.
#  ============================================================================== #

import scipy
from matplotlib import ticker
import cartopy.crs as ccrs
import sklearn.metrics as metrics

# We're getting the lists from previous code sections:
Y_test = soil_mostire_list
Y_pred = TVDI_list

# Let's do some statistics...
mean_TVDI = np.mean(Y_pred)
#mae   = metrics.mean_absolute_error(Y_test, Y_pred)
#mse   = metrics.mean_squared_error(Y_test, Y_pred)
#rmse  = np.sqrt(mse) 
#rrmse = 100 * (rmse / mean_TVDI)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(Y_test, Y_pred)
r_square     = r_value**2

print("Statistics:")
#print("MAE.       : {:.2f}".format(mae),"unitless")
#print("RMSE.      : {:.2f}".format(rmse),"cm\u00b3 cm\u207b3")
#print("rRMSE.     : {:.2f}".format (rrmse), "%")
print("Pearson's-R: {:.2f}".format(r_value))
print("R\u00b2         : {:.2f}".format(r_square))
print("P-value    : {:.3f}".format(p_value))

plt.figure(1,figsize=(5,4)).clf()
plt.scatter(Y_test,Y_pred)
plt.xlabel('Soil water content (cm$^{3}$ cm$^{-3}$)')
plt.ylabel('TVDI')
plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)))
plt.title('TVDI vs. soil water content')
plt.xlim([0, 0.27])
plt.ylim([0.65, 0.9])
plt.show()
