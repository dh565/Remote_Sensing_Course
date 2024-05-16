sub_data = data[:,0:1000:, 2000:3000] # get a chunk of the total area
# Create a new array with the name "band":
band=sub_data[10]
# Display a small chunk of this array:
plt.imshow(band, interpolation='none')
plt.show()
