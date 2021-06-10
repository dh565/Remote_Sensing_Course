# 9c_Scatterplot_of_obs_vs_mod

import scipy
import sklearn.metrics as metrics
# Remember that MOD11A1 is an LST product at 10:30 and MYD11A1 is LST at 13:30
x1 = data["ET_model"].values
y1 = data["ET"].values

# Use only pixels in both arrays that are not nan
mask = ~np.isnan(x1) & ~np.isnan(y1)

# mask nan in both arrays
x = x1[mask]
y = y1[mask]

# calculate statistics
mae  = metrics.mean_absolute_error(x, y)
mse  = metrics.mean_squared_error(x, y)
rmse = np.sqrt(mse)

delta_et = x-y
bias = delta_et.sum()/len(delta_et)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

# Print statistics
print("Statistics:")
print("MAE:  {:.2f}".format(mae),'mm day-1')
print("RMSE: {:.2f}".format(rmse),'mm day-1')
print("Bias: {:.2f}".format(bias),'mm day-1')
print("R-Squared: {:.2f}".format(r_value**2))
print("P-value: {:.4f}".format(p_value))
print('')
print('')

plt.figure(1,figsize=(4,4)).clf()
s = plt.scatter(x, y, marker='.', color='blue') 
plt.xlabel('Modeled ET (mm day$^{-1}$)')
plt.ylabel('Observed ET (mm day$^{-1}$)')
plt.title('Comparison between eddy-covariance (observed) and FAO56 (modeled)') 
plt.xlim([-1, 8])
plt.ylim([-1, 8])

# draw a 1:1 line:
plt.plot([-10, 40], [-10, 40], 'k--', linewidth=0.9)
