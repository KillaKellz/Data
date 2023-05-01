import random

# Create the 3x3 multi-dimensional array
grades = [[0 for column in range(3)] for row in range(3)]

# Get random function to fill out the grades
for i in range(3):
    for j in range(3):
        grades[i][j] = int(random.randrange(0,100))

# Make sure to print out the array
print("Grades:")
for i in range(3):
    for j in range(3):
        print(grades[i][j], end=" ")
    print()

# Store all passed and failed grades in two separate arrays
pass_grade = []
fail_grade = []
for i in range(3):
    for j in range(3):
        if grades[i][j] >= 50:
            pass_grade.append(grades[i][j])
        else:
            fail_grade.append(grades[i][j])

# Print out pass_grade & fail_grade arrays
print("All Passing Grades:", pass_grade)
print("All Failing Grades:", fail_grade)