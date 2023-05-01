# open the file for writing
file = open("My_File.txt", "w")

# write the first line to the file as per the instructions
file.write("This is the midterm exam for CS 236")

# write the second line to the file as per the instructions
file.write("\nToday's date is March 9, 2023")

# close the file
file.close()

# open the file for reading
file = open("My_File.txt", "r")

# read and print the contents of the file for the user to read.
print(file.read())

# close the file
file.close()
