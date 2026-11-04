import numpy as np

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['N','O','P'],['Q','R','S']],
                  [['T','u','v'],['W','X','Y'],['Z',' ',' ']]])

word = array[0,0,0] + array[1,2,2] + array[1,2,2]

print(word)
print(array.shape)
print(array.ndim)
