import numpy as np
import matplotlib.pyplot as plt


"""Create an array with a sequence of elements:"""

zeros = np.zeros(2)
ones = np.ones(5)

range_elements = np.arange(10) # we can create an array with a rage of elements

range_elements_with_step_size = np.arange(3,10, 2) # Even we can create an array with step size

lineary_values = np.linspace(0, 20, 5) # To create an array with values that are spaced linearly in a specified interval.
                               # The first two numbers is the range, and the third number is 
                               # how much values between these values we want



"""Adding, remobing, and sorting elements"""

array_example = np.array([2, 1, 5, 3, 7, 4, 6, 8])


sort_array = np.sort(array_example) # Sort an array quickly 

"""
In addition to sort, which returns a sorted copy of an array, you can use:

    - argsort, which is an indirect sort along a specified axis,

    - lexsort, which is an indirect stable sort on multiple keys,

    - searchsorted, which will find elements in a sorted array, and

    - partition, which is a partial sort.
"""

arA = np.array([1, 2, 3, 4])
arB = np.array([5, 6, 7, 8])
# This way we can concatenate both arrays using np.conctatenate()
array_contcat = np.concatenate((arA, arB))
# Or even if we have these arays (2-D array will keep):
arA = np.array([[1, 2], [3, 4]])
arB = np.array([[5, 6]])
array_contcat = np.concatenate((arA, arB), axis=0)
# print(array_contcat)

"""This way i can create a numbered array without use a loop inside an array"""
x2 = np.arange(15, dtype=np.int64).reshape(3, 5) 
# With reshape I can divide the array with 3 (in this case) or whatever I want. -> I might have an error if i don't use well the method


"""Perform element-wise addition, subtraction, multiplication, and division"""

y1 = np.array([1, 2, 3, 4, 5])
y2 = np.array([6, 7, 8, 9, 10])


result = y1 + y2
result1 = y1 * y2
result2 = y1 / y2
result3 = y1 - y2

sum = np.sum(y1) # Sum all values

mean = np.mean(y1) # Get a mean of all values

min = np.min(y1) # Get smallest number

max = np.max(y1) # Get biggest number


"""Matrix operations"""
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])



"""Revising these things about reshape and Transpose"""

# Reshape
a1 = np.array([
    [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]],
    [[13, 14, 15, 16],[17, 18, 19, 20],[21, 22, 23, 24]]
])



a2 = np.array([3, 7, 3, 8, 12, 2, 5, 9, 3, 10, 6, 9])

a2_ = a2.reshape(len(a1[1]), 4)
a2_ * a1



# Transpose() | Transpose literally switches the axis

a1.shape # Output -> (2, 3, 4)
a1.transpose().shape # Output -> (4, 3, 2)1

# We can do this in a larger array as well:
b1 = np.array([
    [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]],
    [[13, 14, 15, 16],[17, 18, 19, 20],[21, 22, 23, 24]]
])


print(b1.shape)
print(b1.T.shape)


