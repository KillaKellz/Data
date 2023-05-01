valid = True
while valid == True:        
    x = eval(input("Insert a value: "))
    if x > 100 or x < 0:
        print("Invalid input! You have insterted the incorrect grade.")
        valid = True
    elif x >= 90:
        print("You recived an A! Great Job!")
        valid = False
    elif x >= 80:
        print("You recived a B! Good Job!")
        valid = False
    elif x >= 70:
        print("You recived a C! An 'okay' Job!")
        valid = False
    elif x >= 60:
        print("You recived a D, Try better next time...")
        valid = False
    elif x <= 50:
        print("You recived an F...")
        valid = False
