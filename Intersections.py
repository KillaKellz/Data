x={6,5,2,9,3}
y={6,8,7,10,12,5,1}
z=[]

for i in x:
    if y.__contains__(i):
        z.append(i)

print(z)
    