import numpy as np

anArray = None  # Initialize with None

value_1 = np.array([1, 2, 3, 4, 5])
value_2 = np.array([6, 7, 8, 9, 10])

# If `anArray` is still None, assign it `value_1`; otherwise, stack `value_1` below `anArray`
anArray = value_1 if anArray is None else np.vstack((anArray, value_1))

anArray = value_1 if anArray is None else np.vstack((anArray, value_2))

print(anArray)