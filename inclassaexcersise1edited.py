arr=[]
   
def arr_fill():
    usrinput = ""
    while usrinput != "stop":
        usrinput = input("Enter user grades or type stop to end input: ")
        if usrinput == "stop":
            break
        elif usrinput != "stop":
            arr.append(eval(usrinput))
        if eval(usrinput) > 100 or eval(usrinput) < 0:
            print("Invalid input! You have insterted the incorrect grade. (Out of Range)")
            break
        elif eval(usrinput) >= 90:
            print("You recived an A! Great Job!")
        elif eval(usrinput) >= 80:
            print("You recived a B! Good Job!")
        elif eval(usrinput) >= 70:
            print("You recived a C! An 'okay' Job!")
        elif eval(usrinput) >= 0:
            print("You recived an F...")
    
def average(numbers):
    return sum(numbers) / len(numbers)

def find_min_max(arr):
    min_num = min(arr)
    max_num = max(arr)
    return min_num, max_num

def main():
    arr_fill()
    print("The avreage of all your grades is: ", average(arr))
    min_num, max_num = find_min_max(arr)
    print("Minimum number in the list:", min_num)
    print("Maximum number in the list:", max_num)
    
main()