arr_multi= [10, 15, 3, 8], [20, 26, -14, 3], [0, 6, 50, -3], [33, 61, 17, 5]

#Find and print the number of odd and even numbers
odd_numbers = 0
even_numbers = 0
for row in arr_multi:
    for number in row:
        if number % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
print("Number of odd numbers:", odd_numbers)
print("Number of even numbers:", even_numbers)

#calculate the summation of all the numbers.
sum_of_numbers = 0
for row in arr_multi:
    for number in row:
        sum_of_numbers += number
print("Sum of all numbers:", sum_of_numbers)

#Find the average of all the numbers in the array.

total_numbers = len(arr_multi) * len(arr_multi[0])
average_of_numbers = sum_of_numbers / total_numbers
print("Average of all the numbers:", average_of_numbers)

#Replace all of the negative numbers with zeros.
for i in range(len(arr_multi)):
    for j in range(len(arr_multi[i])):
        if arr_multi[i][j] < 0:
            arr_multi[i][j] = 0
print("Array after replacing negative numbers with zeros:", arr_multi)

#Multiply all the numbers in the array with 2.
for i in range(len(arr_multi)):
    for j in range(len(arr_multi[i])):
        arr_multi[i][j] *= 2
print("Array after multiplying all numbers by 2:", arr_multi)

#Print out and display the full array.
for row in arr_multi:
    print(row)
