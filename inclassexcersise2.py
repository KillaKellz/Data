print("This is the start of the array.")
Arr = [55,23,-12,96,14,74,48,20,36,96,-50,102,150,66,15,19,30] 
print(Arr)

#Store all the even numbers in a new array
print("\nThis is all the even numbers from the array.")
arr_even = [num for num in Arr if num % 2 == 0]
print(arr_even)

#Store all the odd numbers in a new array
print("\nThis is all the odd numbers from the array.")
arr_odd = [num for num in Arr if num % 2 != 0]
print(arr_odd)

#Remove negative numbers from the array
print("\nRemoved all negative numbers from the array.")
Arr = [num for num in Arr if num >= 0]

#Sort the array in ascending order
print("\nSorted all the numnbers in the array.")
arr_asc = sorted(Arr)
print(arr_asc)

#Sort the array in descending order
print("\nReverse sorted all the numnbers in the array.")
arr_des = sorted(Arr, reverse=True)
print(arr_des)

#Add new elements to the array
print("\nAdded 4 new elements to the array.")
Arr.append([67, 20, -9, 33])

# Task 7: Print the array
print("\nThis is the array now:")
print(Arr)
