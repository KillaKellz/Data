x= 2
y= 1
#print(x and y)

def fun(a):
    return (2*a+2>=6)

#This is the implication truth table 
if fun(x)==True and fun(y)==False:
    print("False")
elif fun(x)==False and fun(y)== True:
    print("True")
elif fun(x)==False and fun(y)==False:
    print("True")
else:
    print("True")