import scipy

x1 = array2.flatten()
y1 = array3.flatten()

mask = ~np.isnan(x1) & ~np.isnan(y1)

x = x1[mask]
y = y1[mask]

mae  = metrics.mean_absolute_error(x, y)
mse  = metrics.mean_squared_error(x, y)
rmse = np.sqrt(mse) 
r2   = metrics.r2_score(x,y)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)

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

# Sort the points by density, so that the densest points are plotted last
z = np.array([hh[np.argmax(a<=locx[1:]),np.argmax(b<=locy[1:])] for a,b in zip(x,y)])
idx = z.argsort()
x2, y2, z2 = x[idx], y[idx], z[idx]

plt.figure(1,figsize=(4,4)).clf()
s = plt.scatter(x2, y2, c=z2, cmap='jet', marker='.') 
plt.xlabel('MODIS LST [\N{DEGREE SIGN}C]')
plt.ylabel('WRF Ta [\N{DEGREE SIGN}C]')
plt.title("WRF vs. MODIS") 
