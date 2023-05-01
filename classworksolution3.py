def Grading(x): 
    valid = True
    while valid == True:        
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
    
def main():
    x = eval(input("Enter your grade to be graded: "))
    Grading(x)

main()