# Worksheet 2: LOGIC AND CONTROL FLOW

# Problem 1: Grading System
grade = int(input("Enter your grade: ")) 

if 90 <= grade <= 100: 
    print("Excellent! You are a top student.") 
elif 80 <= grade <= 89: 
    print("Good job! You passed with flying colors.") 
elif 75 <= grade <= 79: 
    print("You passed, but there's room for improvement.") 
else: 
    print("You failed. Please review the materials.") 
    
#------------------------------------------------------------------------------------------

# Problem 2: Simple Login Check
og_username = "shyneigh"
og_password = "shy123"

username = input("Enter username: ")
password = input("Enter password: ")

message = "Login Successful." if username == og_username and password == og_password else "Invalid username or password"
print(message)
    
#------------------------------------------------------------------------------------------
    
# Problem 3: Guess the Number
secNum = 7 

while True: 
    guess = int(input("Guess the number: ")) 
    
    if guess == secNum: 
        print("Correct! You win!") 
        break 
    else: 
        print("Try again!") # this will be print everytime the user does not guess the number

#------------------------------------------------------------------------------------------

# Problem 4: Calculating the Total and Average Score
scores = [18, 20, 19, 21, 23, 20]

total_score = 0
for iskor in scores:
    total_score += iskor
    
avgScore = total_score / len(scores)
print(f"Total score: {total_score}")
print(f"The average score: {avgScore}")