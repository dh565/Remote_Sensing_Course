import scipy
from matplotlib import ticker
import cartopy.crs as ccrs
import sklearn.metrics as metrics

Y_test = soil_mostire_list
Y_pred = TVDI_list

mae  = metrics.mean_absolute_error(Y_test, Y_pred)
mse  = metrics.mean_squared_error(Y_test, Y_pred)
rmse = np.sqrt(mse) 
r2   = metrics.r2_score(Y_test, Y_pred)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(Y_test, Y_pred)

print("Statistics:")
print("MAE.       : {:.2f}".format(mae),"\N{DEGREE SIGN}C")
print("RMSE.      : {:.2f}".format(rmse),"\N{DEGREE SIGN}C")
print("Pearson's-R: {:.2f}".format(r_value))
print("P-value.   : {:.3f}".format(p_value))
print('')

plt.figure(1,figsize=(5,4)).clf()
plt.scatter(Y_test,Y_pred)
plt.xlabel('Soil water content (cm$^{3}$ cm$^{-3}$)')
plt.ylabel('TVDI')
plt.plot(np.unique(Y_test), np.poly1d(np.polyfit(Y_test, Y_pred, 1))(np.unique(Y_test)))
pearson_coef = np.round(pearson_coef, 2)
plt.title('TVDI vs. soil water content')
plt.xlim([0, 0.25])
plt.ylim([0.5, 1.0])
plt.show()
