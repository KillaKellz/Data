x={6,5,2,9,3}
y={6,8,7,10,12,5,1}
z=[]

for i in x:
    if z.__contains__(i):
        print("Already added")
    else:
        z.append(i)

for i in y:
    if z.__contains__(i):
        print("Already added")
    else:
        z.append(i)

z.sort
print("The union set of x and y is:", z)
