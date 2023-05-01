import random
arr=[[1,2,3],[4,5,6],[7,8,9]]

sum = 0
count = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = random.randint(0,100)
        print(arr[i][j], end=" ")
        sum += arr[i][j]
        count+=1
    print()
# print(random.randint(1,10))

A_Grades= 0
B_Grades= 0
C_Grades= 0
D_Grades= 0
F_Grades= 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] >= 90:
            A_Grades+=1
            print("The location of this A grade is:", i, j)            
        elif arr[i][j] >= 80 and arr[i][j]<90:
            B_Grades+=1
            print("The location of this B grade is:", i, j)         
        elif arr[i][j] >=70 and arr[i][j]<80:
            C_Grades+=1
            print("The location of this C grade is:", i, j)         
        elif arr[i][j] >= 60 and arr[i][j]<70:
            D_Grades+=1
            print("The location of this D grade is:", i, j)         
        else:
            F_Grades+=1
            print("The location of this F grade is:", i, j)         
            


print("Grades A:", A_Grades)
print("Grades B:", B_Grades)
print("Grades C:", C_Grades)
print("Grades D:", D_Grades)
print("Grades Failed:", F_Grades)

avg = sum//count
print("The sum of all the grades is: ", sum)
print("The average of all the grades is:", avg)

