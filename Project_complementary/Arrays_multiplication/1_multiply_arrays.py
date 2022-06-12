# This is an example of how to multiply two 2-D arrays, such that x1 is multiplied by x1
# and y1 by y1 of each array, avoiding algebraic matrix multiplication
import numpy as np
in_arr1 = np.matrix([[2, -7, 5], [-6, 2, 0]])
in_arr2 = np.matrix([[0, -7, 8], [5, -2, 9]])
	
print ("1st Input array : ", in_arr1)
print ("2nd Input array : ", in_arr2)

out_arr = np.array(in_arr1) * np.array(in_arr2)
print ("Resultant output array: ", out_arr)

# Now you can use it with arrays created from the TIFFs
# {Note: another way to do this is by using loops, but 
# this is much more computaionally costly and would take
# much more time}
