import numpy as np

array = np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])

#print(array.ndim)

# array[start:end:step]
# print(array[::-1])
# array(0,0,0)
print(array[:, 0::-2])

