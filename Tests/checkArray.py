import numpy as np
import pandas as pd

"""
# First we create our array 
Given_Array = np.array([
    [[4,2,5,6,9],[9,7,1,0,3],[2,9,4,2,8]],
    [[2,9,6,3,0],[3,0,7,8,2],[8,1,2,5,6]],
    [[8,2,5,0,7],[5,2,4,1,3],[7,2,4,9,0]],
    [[7,2,0,6,5],[2,0,8,4,1],[0,4,9,1,2]]
    ])

Result = np.hstack((np.arange(0,10),np.zeros(10))).reshape(10,2, order="F")


print("Given array:")
print(Given_Array)

print("Count array:")
for i in range(0,10):
    count = np.sum(Given_Array == i)
    Result[i][1] = count

print(Result)
"""
##########################################################################################################################



myFile = pd.read_json("deviation.json")
print(myFile)
np_array = np.array([])

name = myFile['name'].to_numpy()
gt_corners = myFile['gt_corners'].to_numpy()
rb_corners = myFile['rb_corners'].to_numpy()
mean = myFile['mean'].to_numpy()
max = myFile['max'].to_numpy()
min = myFile['min'].to_numpy()
floor_mean = myFile['floor_mean'].to_numpy()


Enumarated_names = np.hstack((np.arange(0, len(name)), name)).reshape(len(name),2, order="f")

# Create a numpy array with indices and floor_mean values
floor_mean_with_indices = np.hstack((np.arange(0,len(floor_mean)), floor_mean)).reshape(len(floor_mean), 2, order="F")

np.set_printoptions(precision=4, suppress=True) 
order_array_indx = np.argsort(floor_mean_with_indices[:,1])
Result = floor_mean_with_indices[order_array_indx]

print(Result[:100])
print(Enumarated_names[:100])
##################




"""
# Order values with this way ->
ArrayNumeric = np.array([[3,1],[0,2],[4,2],[1,5],[2,7]])
ArrayWithTheirNames = np.array([[0,'Pompeye'],[1,'Sugar'],[2,'Mugar'],[3,'Colombus'],[4,'Marisius']])

# Extracting indices from ArrayNumeric
indices = ArrayNumeric[:, 0].astype(int)

# Using advanced indexing to get names corresponding to the indices
names = ArrayWithTheirNames[indices, 1]

# Combining indices, names, and the second column of ArrayNumeric
Result = np.column_stack((np.arange(len(names)),indices, names, ArrayNumeric[:, 1]))


print(Result)
"""

"""
# Order values in a simple example
TheArray = np.hstack((np.arange(0,len(floor_mean)), floor_mean)).reshape(len(floor_mean), 2, order="F") # The result would be: [[3,1],[0,2],[4,2],[1,5],[2,7]]

ordered_array = np.argsort(TheArray[:,1])
np.set_printoptions(precision=4, suppress=True) 
Final_Result = TheArray[ordered_array]
print(Final_Result)# The result is: [[3,1],[0,2],[4,2],[1,5],[2,7]] | As you see i've ordered the array from the second value
"""