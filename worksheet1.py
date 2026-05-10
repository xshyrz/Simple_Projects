# Worksheet 1: THE BASICS OF PYTHON

# Problem 1: Hello, Your Name
name = input("What is your name? ") 
print(f"Hello, {name}! Welcome to our DSA class.") 

#------------------------------------------------------------------------------------------

# Problem 2: A Simple Calculator
n1 = input("Enter the first number: ") # the 'input()' always returns a string, even if you type a number.
n2 = input("Enter the second number: ") 

sum = n1 + n2 # this will perform a string concatenation, not addition.
              
# using the 'int()' we convert the inputs to numbers
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

sum = n1 + n2 # finally, we will be able to add correctly the two numbers

print(f"The sum of {n1} and {n2} is {sum}.") # printing the sum of the two added numbers

#------------------------------------------------------------------------------------------

# Problem 3: Student Information
stdnt_id = 8374765
full_name = "Gianna De Santis"
gpa = 2.45
is_enrolled = True

print(f"Student ID: {stdnt_id}, Type:", type(stdnt_id))
print(f"Name: {full_name}, Type:", type(full_name))
print(f"GPA: {gpa}, Type:", type(gpa))
print(f"Is enrolled: {is_enrolled}, Type:", type(is_enrolled))

#------------------------------------------------------------------------------------------

# Problem 4: String Manipulation
full_name = "dela cruz, juan"

print(full_name.upper())
print(full_name.title())

comma = full_name.find(",") # finding the comma to split the name into parts

last = full_name[:comma].strip() # slices the full name up to the comma-'dela cruz'
first = full_name[comma + 1:].strip() # slices the full name after the comma-'juan'

flipped_name = f"{first} {last}" 
print(flipped_name.upper()) # prints with the format of first name then last name 
