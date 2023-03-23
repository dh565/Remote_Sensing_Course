#x   = x.values

# chose channels {these are the real attribute names of the MSG NetCDF layers}
chl =["channel_1","channel_2","channel_3","channel_4","channel_5","channel_6","channel_7","channel_8","channel_9","channel_10","channel_11"]
# create an empty array
array = []
# loop over channels and get them into the array
for i in chl:
  array.append(np.flipud(ds[i]))
data = np.stack((array),axis=0)
# print shape of the array
print(data.shape)

plt.imshow(data[0], interpolation='none')
plt.show()
