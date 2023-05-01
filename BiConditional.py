w=0
x=1
y=2
z=3

def fun(a):
    return (x^2+1<=4)

#This is the implication truth table for P(2)<->P(1)
if fun(x)==True and fun(y)==True:
    print("True")
elif fun(x)==True and fun(y)== False:
    print("False")
elif fun(x)==False and fun(y)==True:
    print("False")
elif fun(x)==False and fun(y)==False:
    print("True")

#This is the implication truth table for P(3)<->P(0)
if fun(z)==True and fun(w)==True:
    print("True")
elif fun(z)==True and fun(w)== False:
    print("False")
elif fun(z)==False and fun(w)==True:
    print("False")
elif fun(z)==False and fun(w)==False:
    print("True")