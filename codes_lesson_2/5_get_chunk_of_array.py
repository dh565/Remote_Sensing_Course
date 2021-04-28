sub_data = data[:,0:1000:, 2000:3000] # get a chunk of the total area
# create new array with name "band":
band=sub_data[10]
# display small array:
plt.imshow(band, interpolation='none')
plt.show()
