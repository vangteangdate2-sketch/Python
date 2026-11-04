import numpy as np

# 1. Load the single connected file
loaded_data = np.load('connected_data.npz')

# 2. Extract both arrays using the keys we defined in File 1
matrix = loaded_data['array1']
vector = loaded_data['array2']

# 3. Print the results
print("--- Loaded Array 1 (Matrix) ---")
print(matrix)

print("\n--- Loaded Array 2 (Vector) ---")
print(vector)
