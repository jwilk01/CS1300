"""
CS1300 - Homework 4: Decision Structures I
Name: Joseph Wilk
Date: Sep 29, 2025
Description: Programs using conditional statements for decision-making
"""




print("=== Temperature Converter & Weather Advisor ===")
# Get temperature from user
temp = float(input("Enter temperature: "))
# Get the scale (C or F)
scale = input("Is this Celsius or Fahrenheit? (C/F): ").upper()
# YOUR CODE HERE
# 1. Check which scale was entered
# 2. Convert to the other scale
# 3. Display both temperatures
# 4. Give weather advice based on Fahrenheit

if scale == "F":
	temp_conversion = round(((temp - 32) / 1.8), 2)
elif scale == "C":
	temp_conversion = round(((temp * 1.8) + 32), 2)
else:
	print("You did not enter \"C\" or \"F\".  Exit program.")
	SystemExit(0)

print(f"Your chosen temperature:  {temp}°{scale}")

#Flip the F or C value here.
if scale == "F":
	new_scale = "C"
else:
	new_scale = "F"

print(f"Converted temperature:  {temp_conversion}°{new_scale}")

if scale == "C":
	temp = temp_conversion
if temp <= 15:
	print("It\'s very cold outside.  Wear a heavy jacket!")
elif temp <= 38:
	print("It\'s cold outside.  Wear a winter jacket!")
elif temp <= 59:
	print("It\'s chilly outside.  Wear a hoodie or sweatshirt!")
elif temp <= 79:
	print("The air is about room temperature.  Wear whatever you want!")
elif temp <= 89:
	print("It\'s warm outside.  Wear a T-shirt and shorts.")
else:
	print("It\'s hot outside!  Wear sunscreen and cool clothing!  Stay hydrated!")
input("Press ENTER to continue:")
print(("#" * 30) + ("\n" * 6))


print("=== Movie Theater Ticket System ===")
# Get customer information
age = int(input("Enter customer age: "))
day = input("Enter day of week: ").lower()
# YOUR CODE HERE
# Remember:
# - Check for Tuesday special first
# - If not Tuesday, ask for show time
# - Apply age-based pricing
# - Apply matinee discount if applicable
ticket_price = 15

#This is for special output of ticket pricing display
child = ""
senior = ""
matinee = ""

if day == "tuesday":
	ticket_price = 7
	print("Tuesday special: All tickets $7!")
else:
	ticket_price = 15
	if age <= 12:
		ticket_price = 8
		child = "Child"
	elif age >= 65:
		ticket_price = 10
		senior = "senior"
	time = int(input("Please ENTER the hour of the matinee (0-23):  "))
	if time < 17:
		ticket_price = ticket_price - 3
		matinee = "matinee"
		
# This is for display output with dynamic spacing	
	print(f"Your ticket price:  ${ticket_price}   ", end=" ")
	if child != "" or senior != "" or matinee != "":
		print(f"( {child}{senior}", end="")
		if child != "" or senior != "":
			print(" ", end="")
		print(f"{matinee}", end="")
		if matinee != "":
			print(" ", end="")
		print(")", end="")
	print("")
print("---------")
input("\nPress ENTER to continue:  ")
print(("#" * 30) + ("\n" * 6))





# Get three test scores
test1 = float(input("Enter Test 1 score (0-100): "))
test2 = float(input("Enter Test 2 score (0-100): "))
test3 = float(input("Enter Test 3 score (0-100): "))
#This variable is for the conditional >=60 score
sixty = False

# YOUR CODE HERE
# 1. Validate all scores are between 0 and 100
# 2. If invalid, print error and stop
# 3. Calculate average
# 4. Determine letter grade using elif
# 5. Check passing criteria (D or better AND at least one test >= 60)
# 6. Display results

if test1 < 0 or test1 > 100:
	print("You did not enter a valid test score (0-100)!")
	SystemExit(0)
if test2 < 0 or test2 > 100:
	print("You did not enter a valid test score (0-100)!")
	SystemExit(0)
if test3 < 0 or test3 > 100:
	print("You did not enter a valid test score (0-100)!")
	SystemExit(0)

avg = round(((test1 + test2 + test3) / 3), 2)

if not (test1 < 60 and test2 < 60 and test3 < 60):
	sixty = True
	#Display and grade the average score
	print(f"AVERAGE SCORE:  {avg:.2f}%")
	if avg < 60:
		print(f"You did NOT pass this course (your grade: {avg:.2f}%).")
	elif avg < 70:
		print(f"You passed this course with a grade \"D\" at {avg:.2f}%.")
	elif avg < 80:
		print(f"You passed this course with a grade \"C\" at {avg:.2f}%.")
	elif avg <90:
		print(f"You passed this course with a grade \"B\" at {avg:.2f}%.")
	else:
		print(f"Congradulations!  You passed this course with a grade \"A\" at {avg:.2f}%!")
else:
	print("\tYou did NOT pass this course (at least one test must be at least 60%)!")

input("\nPress ENTER to continue:  ")
print(("#" * 30 ) + ("\n" * 6))







print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")
# Initialize criteria counters
criteria_met = 5
feedback = []
# YOUR CODE HERE
# 1. Check each criterion
# 2. For each criterion met, increment criteria_met
# 3. For each criterion not met, add feedback message
# 4. Determine strength level
# 5. Display results and feedback
# Hint for checking digits:

#create list of weak passwords to check for
common_passwords = ["password", "12345678", "qwerty"]

if len(password) < 8 or len(password) > 24:
	print("You have NOT entered a valid password length (8-24 characters).  ")
	criteria_met -= 1
has_upper = any(char.isupper() for char in password)
if has_upper == False:
	print("You have NOT entered a valid password (needs at least one upper-case letter).  ")
	criteria_met -= 1
has_lower = any(char.islower() for char in password)
if has_lower == False:
	print("You have NOT entered a valid password (needs at least one lower-case letter).  ")
	criteria_met -= 1
has_digit = any(char.isdigit() for char in password)
if has_digit == False:
	print("You have NOT entered a valid password (needs at least one number).  ")
	criteria_met -= 1
if password in common_passwords:
	print("Your password is common and considered weak.")
	criteria_met = 0

#Display password strength
if criteria_met == 5:
	print("PASSWORD STRENGTH:  PERFECT")
elif criteria_met == 4:
	print("PASSWORD STRENGTH:  MEDIUM")
elif criteria_met == 3:
	print("PASSWORD STRENGTH:  POOR")
else:
	print("PASSWORD STRENGTH:  FAILURE")



print(f"Criteria met:  {criteria_met}/5")

input("\nPress ENTER to continue:  ")
print(("#" * 30 ) + ("\n" * 6))





print("=== Restaurant Bill Calculator ===")
# Get initial information
food_total = float(input("Enter food total: $"))
is_holiday = input("Is today a holiday? (yes/no): ").lower()
party_size = int(input("How many people in your party? "))
membership = input("Do you have a membership? (yes/no):  ").lower()
day = input("What day of the week is it?:  ").lower()
automatic_gratuity = 1.18
tax = 1.085
# YOUR CODE HERE
# Follow the requirements and calculation order
# Remember to ask additional questions based on conditions
# Display a detailed breakdown of the bill
"""
1. Input the food total
2. Ask if it's a holiday (15% surcharge on holidays)
3. Ask for party size
4. Ask if they have a membership (10% discount for members)
5. Ask for day of week (10% senior discount on Wednesdays for parties with seniors)
6. Calculate automatic gratuity for parties of 6 or more (18%)
7. Calculate tax (8.5%)
8. Display itemized bill
Order of calculations:
1. Apply holiday surcharge to food total (if applicable)
2. Apply membership discount (if applicable)
3. Apply senior discount (if Wednesday and has seniors)
4. Add tax on the discounted amount
5. Add automatic gratuity on pre-tax amount (if applicable)
"""

#For the display of the Thursday discount
if day == "thursday":
	thursday_discount = "yes"
else:
	thursday_discount = "no"

# Calculations and Display
print("--------- BILL BREAKDOWN")
print(f"Holiday surcharge = {is_holiday}")
if is_holiday == "yes":
	food_total = round(food_total * 1.15, 2)
	print(f"              ${food_total:.2f}")
print(f"Member discount:  {membership}")
if membership == "yes":
	food_total = round(food_total * 0.90, 2)
	print(f"              ${food_total:.2f}")
print(f"Thursday discount:  {thursday_discount}")
if day == "thursday":
	food_total = round(food_total * 0.90, 2)
	print(f"              ${food_total:.2f}")
if party_size >= 6:
	food_total = food_total * automatic_gratuity
	print("Party size is at least six.  Automatic gratuity applied.")
	print(f"              ${food_total:.2f}")
else:
	print("Gratuity is NOT added to this party")

food_total = food_total * tax
print(f"FINAL TOTAL (INCLUDING TAX):  {food_total:.2f}")
input("\nPress ENTER to end Homework #4:  ")





	





