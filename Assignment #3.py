#-----------
#Question 1 (Markell Winters-Edwards)
#-----------

def P(x):
      return x**2 - 3 <= (2*x/3)

# 1) P(2) ^ ¬ P(4)
value_1 = P(2) and not P(4)

# 2) ¬P(0) ⊕ P(2)
value_2 = (not P(0)) != P(2)

print("\nTruth value for operation 2:", value_1)
print("\nTruth value for operation 2:", value_2)

#-----------
#Question 2
#-----------

def intersection(X, Y):
    Z = []
    for x in X:
        if x in Y:
            Z.append(x)
    return Z

X = {1, 2, 3, 4, 5}
Y = {3, 4, 9, 6, 8}
Z = intersection(X, Y)
print("\nThe intersection between the two sets is:", Z)

#-----------
# Question 3
#-----------

A = [3, 6, 7, 10, 12, 9, 5]
B = [6, 15, 8, 9, 3, 4, 7]

# 1) A - B
difference_1 = set(A) - set(B)

# 2) B - A
difference_2 = set(B) - set(A)

print("\nThe new set for operation A-B is:", difference_1)
print("\nThe new set for operation B-A is:", difference_2)