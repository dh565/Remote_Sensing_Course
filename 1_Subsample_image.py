sub_data = data[:,600:1000:, 2600:3000] # get a chunk of the total area

band=sub_data[10]
plt.imshow(band, interpolation='none')
plt.show()
