# This example shows various array manipulation operations
import numpy as np

# numpy.reshape(array_to_reshape, tuple_of_new_shape) gives new shape (dimension) to our array
myArray = np.arange(0, 30, 2)
print(myArray)              # [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28]

myArrayReshaped = myArray.reshape(5, 3)
print(myArrayReshaped)

print(myArray.flat[1])      # 10

# numpy.ndarray.flatten() restores the reshaped array into a 1-D array
print(myArrayReshaped.flatten())

# numpy.tranpose() this helps to find the tranpose of the given array
print(myArrayReshaped.transpose())

# numpy.swapaxes(array, axis1, axis2) interchanges the two axes of an array
originalArray = np.arange(8).reshape(2,2,2)
print(originalArray)


print(originalArray.ndim)             # 2


print(np.swapaxes(originalArray, 2, 0))


print(np.rollaxis(originalArray, 2))
