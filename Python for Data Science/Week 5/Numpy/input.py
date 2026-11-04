import numpy as np

# 1. Define all your arrays in one place
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]]) # From your second snippet

arr2 = np.array([7, 8, 9])    # From your first snippet

# 2. Save them ALL into one single file using descriptive keys
np.savez('connected_data.npz', array1=arr1, array2=arr2)

print("All arrays successfully saved to connected_data.npz!")
