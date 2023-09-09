import numpy as np
import time

A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,8]
], dtype=np.int8)

B = np.array([
    [6,5],
    [4,3],
    [2,1]
])


print(np.hstack((A,np.zeros((A.shape[0],1)))))
print(np.arange(1,10, anext=1))