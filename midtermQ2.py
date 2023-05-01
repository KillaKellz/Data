Arr_grades = [66, 99, 87, 25, 105, 78, -20, 55, 0, 18, 808, 64, 35, 91, 85, 79, 85, -3, 75]

# a function to find the number of A grades
def grd_a(arr):
    return len([x for x in arr if 90 <= x <= 100])

# a function to find the number of F grades
def grd_f(arr):
    return len([x for x in arr if 0 <= x < 50])

# a function to find the number of B grades
def grd_b(arr):
    return len([x for x in arr if 80 <= x <= 89])

# a function to find the number of invalid grades
def grd_inv(arr):
    return len([x for x in arr if x < 0 or x > 100])

# remove invalid grades from the array
Arr_valid = [x for x in Arr_grades if 0 <= x <= 100]
print("Valid grades:", Arr_valid)

# sort the valid grades in ascending order
Arr_valid.sort()
print("Sorted grades:", Arr_valid)