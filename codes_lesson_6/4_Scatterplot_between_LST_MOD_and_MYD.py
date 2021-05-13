import scipy

# Remember that MOD11A1 is an LST product at 10:30 and MYD11A1 is LST at 13:30
x1 = array_MYD.flatten()
y1 = array_MOD.flatten()

# Use only pixels in both arrays that are not nan
mask = ~np.isnan(x1) & ~np.isnan(y1)

# mask nan in both arrays
x = x1[mask]
y = y1[mask]

# calculate statistics
mae  = metrics.mean_absolute_error(x, y)
mse  = metrics.mean_squared_error(x, y)
rmse = np.sqrt(mse) 
r2   = metrics.r2_score(x,y)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

# Print statistics
print("Statistics:")
print("MAE: {:.2f}".format(mae),"\N{DEGREE SIGN}C")
print("MSE: {:.2f}".format(mse),"\N{DEGREE SIGN}C")
print("RMSE: {:.2f}".format(rmse),"\N{DEGREE SIGN}C")
print("R-Squared: {:.2f}".format(r_value**2))
print("P-value: {:.4f}".format(p_value))

#histogram definition
bins = [316, 316] # number of bins

# histogram the data
hh, locx, locy = np.histogram2d(x, y, bins=bins)

# Sort the points by density, so that the density points are plotted last
z = np.array([hh[np.argmax(a<=locx[1:]),np.argmax(b<=locy[1:])] for a,b in zip(x,y)])
idx = z.argsort()
x2, y2, z2 = x[idx], y[idx], z[idx]
# some plotting elements (play with these and see what can u change)
plt.figure(1,figsize=(4,4)).clf()
s = plt.scatter(x2, y2, c=z2, cmap='jet', marker='.') 
plt.xlabel('LST 13:30 [\N{DEGREE SIGN}C]')
plt.ylabel('LST 10:30 [\N{DEGREE SIGN}C]')
plt.title("MODIS LST Terra vs. Aqua") 
plt.xlim([-5, 40])
plt.ylim([-5, 40])

# draw a 1:1 line:
plt.plot([-5, 40], [-5, 40], 'k--', linewidth=0.9)
