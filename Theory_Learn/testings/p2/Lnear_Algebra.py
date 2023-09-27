from scipy import misc
import matplotlib.pyplot as plt
import numpy as np



img = misc.face()

img_array = img / 255

red_arry = img_array[:,:,0]
green_array = img_array[:,:,1]
blue_array = img_array[:,:,2]

print(green_array.max(),green_array.min())


"""
plt.imshow(img)
plt.show()
"""
