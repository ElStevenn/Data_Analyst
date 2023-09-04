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


#

myFile = pd.read_json("deviation.json")
# print(myFile)
np_array = np.array([])

name = myFile['name'].to_numpy()
gt_corners = myFile['gt_corners'].to_numpy()
rb_corners = myFile['rb_corners'].to_numpy()
mean = myFile['mean'].to_numpy()
max = myFile['max'].to_numpy()
min = myFile['min'].to_numpy()
floor_mean = myFile['floor_mean'].to_numpy()


Enumarated_names = np.hstack((np.arange(0, len(name)), name)).reshape(len(name),2, order="f")

rb_corners_extacted = np.hstack((np.arange(0, len(floor_mean)), floor_mean)).reshape(len(floor_mean), 2, order="f")

order_array = np.argsort(rb_corners_extacted[:,1])

sorted_gt_corners = rb_corners_extacted[order_array]

print(Enumarated_names)
print(sorted_gt_corners)




##################
"""
TheArray = np.array([[0,2],[1,5],[2,7],[3,1],[4,2]]) # The result would be: [[3,1],[0,2],[4,2],[1,5],[2,7]]

ordered_array = np.argsort(TheArray[:,1])

Final_Result = TheArray[ordered_array]
print(Final_Result)
# Final_Result = np.hstack((ordered_array, np.sort(TheArray[:,1]))).reshape(TheArray.shape, order="f")
"""