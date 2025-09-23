 # Joseph Wilk
 # CS1300
 # FALL 2025
 
 # Code chain can be as long as necessary.
 #a == b == c == d == e == f == g
 # That can help you with mathematical concepts.
 
 #0 <= scores and scores <= 100
 
 #1a
 # TODO: Complete this program
temp = float(input("Enter temperature (F): "))
 # Use chained comparison to check if comfortable
 # Comfortable range: 68-76 degrees
if 68 <= temp <= 76:
 	print(temp)


#1b
# TODO: Complete this program
age = int(input("Enter age: "))
	 # Use chained comparisons for each group:
	 # Baby: 0-2
	 # Child: 3-12
	 # Teen: 13-19
	 # Young Adult: 20-35
	 # Adult: 36-65
	 # Senior: 66+
if age <= 2:
	print("Baby age")
elif age <= 12:
	print("Child age")
elif age <= 19:
	print("Teenager")
elif age <= 35:
	print("Young Adult")
elif age <= 65:
	print("Adult age")
else:
	print("Senior age")
	

#2a
# TODO: Complete this program
day = input("Enter day of week: ").lower()
	# Use conditional expression to set day_type
	# Monday-Friday = "weekday"
	# Saturday-Sunday = "weekend"
#day_type = # Your code here
if day == "sunday" or day == "saturday":
	day_type = "weekend"
else:
	day_type = "weekday"
print(f"It's a {day_type}")


#2b
# TODO: Complete this program
order_amount = float(input("Enter order amount: $"))
# Use conditional expressions for:
# 1. Shipping: Free if order >= $50, else $5.99
# 2. Express available: Yes if order >= $25, else No
# 3. Discount: 10% if order >= $100, else 0%

shipping = 0 if order_amount >= 50 else 5.99
express = True if order_amount >= 25 else False
discount = 0.1 if order_amount >= 100 else 0
print(shipping,express,discount)






"""
De Morgan's Laws
not (A and B) = (not A) or (not B)
not (A or B) = (not A) and (not B)
"""




#3a
# TODO: Complete this program
is_member = input("Are you a member? (yes/no): ").lower() == "yes"
has_invitation = input("Do you have an invitation? (yes/no): ").lower() == "yes"
# Create truth table output showing:
# - Can attend with AND (need both)
# - Can attend with OR (need either)
# - Is excluded (has neither)
print("\n--- Truth Table Results ---")
print(f"Has Ticket: {is_member}")
print(f"Has ID: {has_invitation}")
print("-" * 30)

can_enter_and = is_member and has_invitation
print(f"Can enter (need BOTH): {is_member}")
print(f"Logic: {has_invitation} AND {is_member} = {can_enter_and}")





"""
#3b
# TODO: Complete this program
gpa_good = float(input("Enter GPA: ")) >= 3.5
attendance_good = float(input("Enter attendance %: ")) >= 90
volunteer = input("Did volunteer work? (yes/no): ").lower() == "yes"
# Determine:
# 1. Full scholarship (all three true)
# 2. Partial scholarship (any two true)
# 3. No scholarship (one or none true)
# Show the logic used for each decision
#  
#CODE BELOW IS NOT COMPLETE:
#
"""
"""
print("\n--- Truth Table Results ---")
print(f"GPA Good: {gpa_good}")
print(f"Attendance Good: {attendance_good})
print(f"Volunteer: {volunteer})
#CALCULATION
scholarship = "Full scholarship" if (gpa_good == True and attendance_good == True and volunteer == True) elif  
print(f"Logic -->  GPA Good: {gpa_good} AND Attendance Good: {attendance_good} AND Volunteer: {volunteer}  =  {scholarship}")
"""





#4a
# TODO: Complete this program
phone = input("Enter phone (10 digits, no dashes): ")
# Validate:
# 1. Contains only digits
# 2. Exactly 10 digits long
# 3. Doesn't start with 0 or 1
# Provide specific error messages
if not phone.isdigit():
	print("Your phone number can only contain 0-9 digits")
elif not len(phone) == 10:
	print("Your phone number needs to be exactly 10 digits.")
	



# TODO: Complete this program
password = input("Create password: ")
confirm = input("Confirm password: ")
	# Validate:
	# 1. At least 8 characters
	# 2. Not all lowercase
	# 3. Not all uppercase
	# 4. Doesn't contain spaces
	# 5. Matches confirmation
	# Count how many requirements are met




# TODO: Fix the bugs in this code
username = input("Username: ")
password = input("Password: ")
	# This code has bugs - fix them!
if username == "admin": # Bug 1
	if password == "secret":
		print("Welcome admin!") # Bug 2
elif username == "guest" or username == "visitor": # Bug 3
	print("Welcome guest!")
else:
	print("Unknown user") # Bug 4










