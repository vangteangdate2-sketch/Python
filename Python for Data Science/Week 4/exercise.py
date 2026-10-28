import math

numlist = list(range(1,11))

# a) reverse the list
numlist.reverse()
print(numlist)

# b) remove all even number
filter = list(filter(lambda x: x % 2 !=0, numlist))
print(filter)

# c) square all the remaining number
numlist = [x ** 2 for x in numlist]
print(numlist)

# e) find the sum of the squared number
total = sum(numlist)
print(total)





