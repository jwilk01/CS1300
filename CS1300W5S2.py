# Joseph Wilk
# CS1300


# elif = else + if in one statement
"""
if pattern:
	statement
elif patten:
	statement
elif pattern:
	statement
else:
	statement
	



"""
#1a
# TODO: Complete this program
	# Ask for age and print the appropriate category
	# Child: 0-12
	# Teen: 13-17
	# Adult: 18-64
	# Senior: 65+
age = int(input("Enter your age: "))
	# Write your code here
	# sys.exit(0) -- to test your code, uncomment this and exit
	# -- to see the prompt
	
	# YOU ONLY NEED ONE AGE TO CHECK AGAINST IN EACH CONDITION CHECK AS IT IS   IMPLICIT   THAT MULTIPLE RANGES ARE BEING CHECKED.
	
if age < 13:
	print("You are twelve years old or less as a child.")
elif age <= 17:
	print("You are a teenager.")
elif age <= 64:
	print("You are between eighteen years old and sixty-four years old as an adult.")
else:
	print("You are a senior citizen!")
		

#1b
# TODO: Complete this program
		# Ask for temperature in Fahrenheit
		# Give appropriate clothing advice
temp = float(input("What's the temperature (F)? "))
		# Write your code here
		# Below 32: "Wear a heavy coat!"
		# 32-50: "Wear a jacket"
		# 51-70: "Wear a light sweater"
		# 71-85: "Wear a t-shirt"
		# Above 85: "Wear shorts and stay cool!"
		# sys.exit(0)
if temp < 32:
	print("Wear a heavy coat!")
elif temp <= 50:
	print("Wear a jacket.")
elif temp <= 70:
	print("Wear a light sweater.")
elif temp <= 85:
	print("Wear a T-shirt.")
else:
	print("Wear shorts and stay cool!")
	
	

# multiple if and elif statements cannot overlap and skip one another, they can only be nested in order within each other.
# if you are in software engineering, then you do not want to have more than two layers as that alone will likely be half a page already.  It is not good practice to
# have A LOT of nested layers of if and elif and else statements.



#2a
# TODO: Complete this program
# Regular price: $12
# Child (under 12): $8
# Senior (65+): $8
# Tuesday discount: All tickets $6
age = int(input("Enter your age: "))
day = input("What day is it? ").lower()
# Write nested if statements here
price = 0
if age <= 12 or age >= 65:
	price = 8
	if day == "Tuesday":
		price = 6
else:
	price = 12
	if day == "Tuesday":
		price = 6
print("Your ticket price:  ", price)
# sys.exit(0)



#2b
# TODO: Complete this program
# Must be enrolled (yes/no)
# If enrolled, check if full-time or part-time
# Full-time with GPA >= 3.5: 20% discount
# Full-time with GPA < 3.5: 10% discount
# Part-time: 5% discount
# Not enrolled: No discount
enrolled = input("Are you enrolled? (yes/no): ").lower()
# Write your nested logic here
# sys.exit(0)
if enrolled == True:
	print("Boolean test.")

gpa = input("Please enter your GPA:  ")




# IN PYTHON AND ALSO C, YOU CAN DO THIS:   if 18 >= age <= 65:
score = int(input("Please ENTER a score between 0 and 100:  "))
attendance = int(input("Please ENTER the number of people in attendance:  "))
volunteer_hours = int(input("Please ENTER number of hours you volunteered:  "))
if (score >= 80) and (attendance >= 90) and (volunteer_hours) >= 50:
	print("CONDITION MET.")
else:
	print("CONDITION NOT MET.")

#3a
# TODO: Complete this program
# Correct username: "student"
# Correct password: "learn123"
# Both must be correct to login
username = input("Username: ")
password = input("Password: ")
# Use 'and' to check both conditions
# sys.exit(0)
if username == "student" and password == "Password":
	print("ACCESS GRANTED.  username and password matches an account.")
	if username != "student":
		print("ACCESS DENIED.")
		# sys.exit(0)
	if password != "Password":
		print("ACCESS DENIED.")
		# sys.exit(0)



#3b
# TODO: Complete this program
		# To pass, student needs:
		# - Midterm score >= 60
		# - Final score >= 60
		# - Average of both >= 70
midterm = float(input("Midterm score: "))
final = float(input("Final score: "))
average = (midterm + final) / 2
		# Write your logic using 'and'
if midterm >= 60 and final >= 60 and average >=70:
	print("You have passed your course!")
else:
	print("Unfortunately, you did not meet all course achievements.")
	

#3c
# TODO: Complete this program
	# Requirements for approval:
	# - Age >= 18 and Age <= 75
	# - Income >= 25000
	# - Credit score >= 650
	# Show specific reasons for denial
age = int(input("Age: "))
income = float(input("Annual income: "))
credit_score = int(input("Credit score: "))
if 18 <= age <= 75:
	if income >= 25000:
		if credit_score >= 650:
			print("You have been successfully approved for our loan program!")
		else:
			print("Unfortunately, your credit score is not high enough.")
	else:
		print("Unfortunately, your income is not high enough.")
else:
	print("Unfortunately, you do not meet our age requirements.")


#5a
# TODO: Complete this program
	# Check if input is not empty AND starts with 'A'
	# Use short-circuit to prevent error on empty string
user_input = input("Enter a word: ")
	# Check safely using short-circuit
	# Hint: Check if not empty first, then check first letter
	# sys.exit(0)
if user_input != "" and user_input[0] == "A":
	print("Your input is not blank AND it starts with \"A\"")
else:
	print("Your two conditions are not met.")
	


#5b
# TODO: Complete this program
# Menu options: 1, 2, 3, or 'q' to quit
# Check if input is digit before converting to int
# Use short-circuit for efficiency
choice = input("Enter choice (1-3 or 'q'): ")
# Validate efficiently
# If 'q', quit immediately
# If digit, check if in valid range
# sys.exit(0)
if choice != "q":
	choice = int(choice)
	if 1 <= choice <= 3:
		print("Your choice is VALID.")
	else:
		print("Your choice is not valid.")
else:
	print("You QUIT program.")
	sys.exit(0)
	
	






	
