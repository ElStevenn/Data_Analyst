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
Transponse = np.transpose(Array3, 2)
print(Transponse)
