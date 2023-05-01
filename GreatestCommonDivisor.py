
# def GCD(a, b):
#     if b==0:
#         return a
#     else:
#         return GCD(b, a % b)


# def main():
#     num1 = eval(input("Enter your first number: "))
#     num2 = eval(input("Enter your second number: "))
    
#     print("The GCD of", num1, "and", num2, "is:", GCD(num1, num2))

# main()

x = int(input("Please insert the first number: "))
count1=1
x_div=[]
while count1<x:
    if x%count1==0:
        x_div.append(count1)
    count1+=1

y=int(input("Please insert the second number: "))
count2=1
y_div=[]
while count2<y:
    if y %count2==0:
        y_div.append(count2)

z=[]
for i in x_div:
    if i in y_div:
        z.append(i)
    
print("The GCD of", x, "and", y, "is:", z)
        