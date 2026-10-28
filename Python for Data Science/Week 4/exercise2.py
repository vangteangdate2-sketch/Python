import statistics

students = {"John": 75, 'Mary': 90, 'Many': 100}

# a) Calculate average grade for each student 
averages = statistics.mean(students.values())
print("a) Averages:", averages)

# b) Find the student with the highest average 
highest_student = ""
highest_avg = -1

for name, avg in students.items():
    if avg > highest_avg:
        highest_avg = avg
        highest_student = name

print("b) Highest average: ", highest_student,"with ", highest_avg)

# c) Add a new student with grades
students["Mary"] = 89
print("c) Added Mary:", students)

# d) Remove a student
del students["John"]
print("d) Removed John:", students)