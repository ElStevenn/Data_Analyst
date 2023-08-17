import numpy as np


# np.Where is oen os the most important method
array = np.random.randint(1,100,(10,10))

print("Complted array: ")
print(array)


array2 = np.where(array <= 90, 0, 1)

print("With where: ")
print(array2)


print("**********************")






