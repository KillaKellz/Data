mid_arr = []

# get input from the user and fill up the array
for i in range(6):
    num = int(input("Enter an integer: "))
    mid_arr.append(num)

# calculate the summation of the integers
summation = sum(mid_arr)
print("The summation of the integers is:", summation)

# find the largest number in the array
largest = max(mid_arr)
print("The largest number in the array is:", largest)

# find the smallest number in the array
smallest = min(mid_arr)
print("The smallest number in the array is:", smallest)

# calculate the average of the integers
average = summation / len(mid_arr)
print("The average of the integers is:", average)
