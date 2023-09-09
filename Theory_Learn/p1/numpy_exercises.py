import numpy as np
import matplotlib.pyplot as plt
"""
Exercixes:

- Exercise 1: Bubble Sort
Implement the Bubble Sort algorithm using NumPy. Sort an array of integers in ascending order.

- Exercise 2: Binary Search
Implement the Binary Search algorithm using NumPy. Search for a specific element in a sorted array.

- Exercise 3: Matrix Transposition
Implement a function that takes a matrix as input and returns its transpose using NumPy.

- Exercise 4: Fibonacci Sequence
Write a function that generates the Fibonacci sequence up to a given number using NumPy.

- Exercise 5: Prime Number Check
Implement a function that checks whether a given number is prime or not using NumPy.

"""

# Exercise 1:
Array1 = np.array([8,3,10,2,5,4,6,9,11,1])

# I just have to use np.sort() to sort the array
result1 = np.sort(Array1)


# Exercise 2:
Array2 = np.array([1,2,3,4,5,6,7,8,9,10])

def Binary_Search(arr, target):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
            
    return -1 # Target element not found


# print(Binary_Search(Array2, 2))

# Exercise 3, Matrix array:
Array3 = np.array([[3,6,12,5], [11,1,7,13], [7,1,10,12]])

# I just have to use this function to transpose the array
# Transponse = np.transpose(Array3, 3)

# Exercise 4, Fibonacci Sequence
def Fibonacci_sequence(num, max = 10):
    result = np.array([])
    for i in range(num,num+max+1):
        if len(result) == 0:
            result = np.append(i, result)
        elif len(result) == 1:
            result = np.append(i-1, result)
        else:
            last_values = np.array(result[:2:])

            result = np.append((last_values[0] + last_values[1]), result)

    return np.flip(result)



# Exercise 5
def check_if_is_prime(number):
    if number < 2:
        return False

    # Generate an array of numbers from 2 to the square root of 'number'
    potential_divisors = np.arange(2, int(np.sqrt(number)) +1)
    print(potential_divisors)
    # Check for divisibility using NumPy's broadcasting
    is_divisible = (number % potential_divisors) == 0
    print(is_divisible)

    # If any element is True, the number is not prime
    if np.any(is_divisible):
        print(np.any(is_divisible))
        return False
    else:
        return True

  


# Extra exercise -> I have a longer array e.g: [10, 11, 15, 12, 16, 9, 8, 7, 7, 6, 6, 3, 2, 3, 4, 5, 7, 9, 12, 13, 20, 25, 26, 24, 22, 23, 22, 24, 30, 33]
"""I have to calculate the mide of the last 5 registers. """
def calc_middle(array, num=5):
    finally_array = np.zeros(len(array))
    for i in range(len(array)):
        if i >= num - 1:
            finally_array[i] = np.mean(array[i - num + 1: i + 1])
        else:
            finally_array[i] = np.mean(array[0: i + 1])
    
    np.set_printoptions(precision=2)  # Set a max of decimal numbers to show in console
    return finally_array


MyArray = np.array([10, 11, 15, 12, 16, 9, 8, 7, 7, 6, 6, 3, 2, 3, 4, 5, 7, 9, 12, 13, 20, 25, 26, 24, 22, 23, 22, 24, 30, 33])
#print(calc_middle(MyArray))


"""
MORE EXECISES (PART B)

1- Matrix Transposition: Given a matrix of size (m x n), swap its rows with its columns using numpy.swapaxes or numpy.transpose.

2- Reshaping a 3D Tensor: Given a 3D tensor of shape (a, b, c), use numpy.moveaxis to change its shape to (b, c, a).

3- Calculating Mean along Specific Axes: Given a 3D array of shape (m, n, p), use numpy.mean along with numpy.swapaxes to calculate the mean along different axes.

4- Calculating Covariance Matrix: Given two data matrices of shape (n, m), use numpy.cov to calculate the covariance matrix, and then use numpy.moveaxis 
to change the resulting shape.

5- Working with Images: Load an RGB image into a NumPy 3D array (height x width x channels) and use numpy.swapaxes or numpy.moveaxis to change 
the order of channels, e.g., from RGB to BGR or vice versa.

6- Data Visualization in a Chart: Given three 1D arrays with time, temperature, and humidity data, use numpy.vstack to combine them into a 2D array, 
and then use numpy.moveaxis to swap rows and columns before plotting.

7- Time Series Analysis: Given a 2D array of shape (days, variables), use numpy.rollaxis to organize the data into a 3D array of shape (variables, days, 1), 
and then apply time series analysis techniques.

"""
# PART B -->

# Exercise 1: 
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [9,10,11]])

Transposed_matrix = matrix.swapaxes(0,1) # As you see, the rows are columns and the columns are rows. 

# Exercise 2:

Array4 = np.array([
    [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24]],
    [[25,26,27,28,29,30],[31,32,33,34,35,36],[37,38,39,40,41,42],[43,44,45,46,47,48]]
])
print(Array4.shape)
result = np.moveaxis(Array4, 0, 2)
print(result.shape)

# Exercise 3:

