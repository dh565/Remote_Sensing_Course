# Plot the Trapez and a density scatterplot
bins = [316, 316] # number of bins

#for density plot-
x1 = NDVI.flatten()
y1 = TS.flatten()

# take only existing values of both, NDVI and LST
mask = ~np.isnan(x1) & ~np.isnan(y1) 

x = x1[mask]
y = y1[mask]

# Histogram the data
hh, locx, locy = np.histogram2d(x, y, bins=bins)

# Sort the points by density, so that the densest points are plotted last
z = np.array([hh[np.argmax(a<=locx[1:]),np.argmax(b<=locy[1:])] for a,b in zip(x,y)])
idx = z.argsort()
x2, y2, z2 = x[idx], y[idx], z[idx]

# Plot data
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), tight_layout=True)

ax1.plot(NDVI.ravel(), TS.ravel(), "+", color='dimgray', markersize=4)
ax1.plot(NDVI_vector[21:], MiniList[21:], '+', color='b')
ax1.plot(NDVI_vector[21:], MaxList[21:], '+', color='r')
ax1.plot([0, 1], linhamax, color='r', markersize=8,\
                 label=f"Tsmax = {'%.1f'% b1} - {'%.1f' % abs(a1)} * NDVI")
ax1.plot([0, 1], linhamin, color='b', markersize=8,\
                 label=f"Tsmin = {'%.1f' % b2} + {'%.1f' % abs(a2)} * NDVI")
ax1.legend(loc='upper right', fontsize=12)
ax1.set_ylim(top=324)
ax1.set_xlabel("NDVI")
ax1.set_ylabel("TS (K)")
ax1.set_title("NDVI vs TS Scatterplot")

ax2.scatter(x2, y2, c=z2, cmap='jet', marker='.')
ax2.set_xlabel("NDVI")
ax2.set_ylim(top=324)
ax2.set_xlim(right=1.)
ax2.set_title("NDVI vs  LST")
