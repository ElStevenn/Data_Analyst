import numpy as np
import matplotlib.pyplot as plt


"""Basic operations"""
# copyto() || Copies values from one array to another, broadcasting as necessary.
A = np.array([4, 5, 6])
B = [1, 2, 3]
np.copyto(A, B)

# shape() || Return the shape
array1 = np.array([9,8,7,6,5,4,3,2,1])
array_shape = array1.shape

"""Changing array shape"""
# reshape() || Gives a new shape to an array without changing its data
array2 = np.array([1,2,3,4,5,6,7,8])
new_shape = np.reshape(array2,(2,4)) # The new shape should be compatible with the original shape

# Output -> 
# [[1 2 3 4]
#  [5 6 7 8]]

# Ravel() || Return a contiguous flattened array
array3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
flattened_array = np.ravel(array3)

# Output ->
# [ 1  2  3  4  5  6  7  8  9 10]

# Even if whe can specify the array order

array3.reshape(-1)
flattened_array_otder_F = np.ravel(array3, order='F')

# Output -> 
# [ 1  6  2  7  3  8  4  9  5 10]

# ndarray.flat || A 1-D iterator over the array. For example, if we have 2-D array, we can iterate like it was a 1-D array
array4 = np.array([[1,2,3,4],[5,6,7,8]])
array4.flat[3]

# Output ->
# 4

# flatten() || Return a copy of the array collapsed into one dimension
array5 = np.arange(1,16).reshape(3,5)
array5.flatten()

# Output ->
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]

"""Transpose-like operations"""

# rollaxis() || Roll the specified axis backward until it lies in given position

array7 = np.arange(1,16).reshape(3,5)
array7.shape

result = np.rollaxis(array7, 1, )
result.shape

# Output ->
# [[ 1  6 11]
# [ 2  7 12]
# [ 3  8 13]
# [ 4  9 14]
# [ 5 10 15]


# moveaxis() || Change possittion of an axes in multidimentional array but provides imore ntuitive and flexible syntax than rollaxis()
array6 = np.arange(1,16).reshape(3,5)
result = np.moveaxis(array6, source=1, destination=-1)

# Output ->
# result.shape -> (3, 5, 4)

# swapaxes() || Swap two axes in a multidimentional array
array8 = np.arange(1,21).reshape(5,4) # We need multidimentional array

print(array8)
print(np.swapaxes(array8, 0, 1))

# Output->
#



