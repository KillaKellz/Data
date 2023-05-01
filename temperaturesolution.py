#Define the temperature check variable.
def temp_check(scale, int):
    #Check if the scale is valid.
    if (scale == "Celcius" or scale == "celcius"):
        #Convert the degrees over.
        fahrenheit = (int * 9/5) + 32
        #Let the user know the coversion.
        print("The conversion from celcius is:", fahrenheit, "degrees Fahrenheit.")
        
    elif(scale == "Fahrenheit" or scale == "fahrenheit"):
        #Convert the degrees over.
        celcius = ((int - 32) * 5/9)
        #Let the user know the coversion.
        print("The conversion from fahrenheit to celcius is:", celcius, "degrees Celcius.")
        
    #Self check to make sure you are using a proper scale.
    else:
        print("The scale you have entered does not match with the avalible temperature scales: Celcius or Fahrenheit")
        
#Call temp_check in main.
def main():
    #Ask user for inputs.
    scale = input("Enter the temperature scale: ")
    degrees = int(input("Enter the degrees: "))
    
    #Let user know verbose output.
    print("The program will now calculate the degrees in the opposite scale...")
    
    #Call temp_check function.
    temp_check(scale, degrees)
    
main()