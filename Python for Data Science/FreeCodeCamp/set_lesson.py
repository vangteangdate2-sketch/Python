my_set = {1, 2, 3, 4, 5} 

set() # Set
{}    # Dictionary

my_set.add(6)
my_set.add(5)
my_set.remove(4)
my_set.discard(4)

my_set.clear()

my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

print(my_set.isdisjoint(your_set)) # False

my_set | your_set # {1, 2, 3, 4, 5, 6}
my_set & your_set # {2, 3, 4}
my_set - your_set # {1, 5}
my_set ^ your_set # {1, 5, 6}