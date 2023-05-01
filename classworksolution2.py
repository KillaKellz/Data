#While loop and counter to keep program going and to keep track of no. of tries.
guesscount = 0
while guesscount < 3:
    #Ensure that you tell the user how many tries they have left.
    if guesscount == 0:
        print("You have 3 total tries.")
    elif guesscount == 1:
        print("You have 2 more tries left...")
    elif guesscount == 2:
        print("You have 1 more try left...")
        
    #Grab user input    
    guess = eval(input("Enter a # to guess: "))
    
    #Evaluate user's guess.
    if guess == 6:
        print("Congratulations, you've hit the correct number!")
        break
    elif guess < 0 or guess > 10:
        print("Your guess is out of range! Please restart the program.")
        break
    elif guess >= 7 and guess < 10:
        print("Your guess is too large.")
        guesscount += 1
    elif guess <= 5:
        print("Your guess is too small.")
        guesscount += 1

#Display losing message.
if guesscount == 3:
        print("You've lost, please try again.")
    