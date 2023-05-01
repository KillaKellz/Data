avn = [3, 6, 20, 32, 6]
sum = 0

for i in range(0, len(avn)):
    sum += avn[i]

average = (sum / len(avn))

# middle = int(len(avn) / 2)
# print("The median of the array is:", middle)
print("The average of the array is:", average)

def median(arr):
    n = len(arr)
    arr.sort()
    if n % 2 == 0:
        median1 = arr[n//2]
        median2 = arr[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = arr[n//2]
    return median

print("The median of the array is:", median(avn)) # Output: (3, 3.0)