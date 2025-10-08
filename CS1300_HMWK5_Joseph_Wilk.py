"""
CS1300 - Homework #5: Advanced Control Structures
Name: Joseph Wilk
Date: 2025-10-08
Description: Advanced conditional logic and validation
"""

# Remember that it is more "Pythonic" to have a chained comparison like   18 <= age <= 65   than have this:  ''' age >= 18 and age <=65  '''




"""
1. Get current temperature, desired temperature, time of day (0-23), and season
2. Use chained comparisons to check temperature ranges
3. Apply these rules:
Comfortable range: 68-76°F
Night hours: 22-6 (reduce by 3 degrees for energy saving)
Summer: Never below 72°F
Winter: Never above 70°F
4. Calculate adjustment needed and estimated time to reach target (2 degrees per hour)
5. Show energy efficiency rating
"""
print("=== SMART THERMOSTAT SYSTEM ===")
# Get inputs
current_temp = float(input("Current temperature (F): "))
desired_temp = float(input("Desired temperature (F): "))
hour = int(input("Current hour (0-23): "))
season = input("Season (summer/winter/spring/fall): ").lower()
comfortable_min = 68
comfortable_max = 76
hours_needed = 0
energy_rating = "Poor"
# YOUR CODE HERE
# 1. Check if current temp is in comfortable range using chained comparison
# 2. Determine if it's night time (22-6)
# 3. Apply seasonal restrictions
# 4. Calculate actual target temperature after adjustments
# 5. Calculate time to reach target
# 6. Determine energy efficiency (Excellent/Good/Fair/Poor)
# Hint: Use chained comparisons like: 68 <= current_temp <= 76
# Hint: Night check needs: hour >= 22 or hour <= 6


if season == "summer":
	comfortable_min = 72
	print("\nSummer temperature restriction applied (cannot be below 72°).\n")
elif season == "winter":
	comfortable_max = 70
	print("\nWinter temperature restriction applied (cannot be above 70°).\n")
if not 6 < hour < 22:
	comfortable_min -= 3
	comfortable_max -= 3
	print("\nNighttime hours applied to temperature calculations.\n")
#Calculate time to get to comfortable range within n-hours
if not comfortable_min <= current_temp <= comfortable_max:
	if comfortable_min >= current_temp:
		hours_needed = round(((comfortable_min - current_temp) // 2) + 1, 1)
	else:
		hours_needed = round(((current_temp - comfortable_max) // 2) + 1, 1)
#Energy rating calculation.  Poor rating is default value.
	if hours_needed <= 8:
		if hours_needed <= 2:
			energy_rating = "Excellent"
		elif hours_needed <= 4:
			energy_rating = "Good"
		elif hours_needed <= 6:
			energy_rating = "Fair"
	print(f"\nCURRENT TIME:  {hour}:00")
	print(f"CURRENT TEMPERATURE (°F):  {current_temp}")
	print(f"DESIRED TEMPERATURE (°F):  {desired_temp}")
	print(f"TARGET MINIMUM TEMP (°F):  {comfortable_min}")
	print(f"TARGET MAXIMUM TEMP (°F):  {comfortable_max}")
	print(f"\nTime needed to reach desired range:  {hours_needed} hours.")
	print(f"Energy Efficiency Rating:  {energy_rating}")
else:
	print("***\n***\n***\nYour current temperature is in a desirable range.\n***")
	print(f"\nCURRENT TIME:  {hour}:00")
	print(f"CURRENT TEMPERATURE (°F):  {current_temp}")
	print(f"DESIRED TEMPERATURE (°F):  {desired_temp}")
	print(f"TARGET MINIMUM TEMP (°F):  {comfortable_min}")
	print(f"TARGET MAXIMUM TEMP (°F):  {comfortable_max}")
input("Press ENTER to continue to Part 2 of Homework:  ")
print("\n\n\n\n\n")



print("=== PASSWORD SECURITY ANALYZER ===")
password = input("Enter password to analyze: ")
# Initialize score
password_tally = 0
length_points = 0
upper_points = 0
lower_points = 0
digit_points = 0
special_points = 0
has_special = not password.isalnum()
password_strength = ""
# YOUR CODE HERE
# Use conditional expressions for each check
# Example: length_points = 30 if len(password) >= 16 else 20 if len(password) >=
#	12 else 10 if len(password) >= 8 else 0
# Check length (use conditional expression)
# Check for common patterns
common_patterns = ["123", "abc", "qwerty", "password", "111"]
has_pattern = any(pattern in password.lower() for pattern in common_patterns)
if has_pattern == True:
	print("Your password is considered insecure (reason: common pattern found)!")
	exit()

length_password = len(password)
if length_password < 8:
	print("You did not enter a valid password (min char length: 8).  ")
	exit()
elif length_password <= 12:
	length_points = 1
elif length_password <= 16:
	length_points = 3
elif length_password <= 24:
	length_points = 5
else:
	print("You did not enter a valid password (max char length: 24).  ")
	exit()

# Check for uppercase (use conditional expression)
has_upper = password != password.lower()
if has_upper == False:
	print("Password red flag: password does not have an uppercase letter.")
else:
	upper_points = 2
	
# Check for lowercase
has_lower = password != password.upper()
if has_lower == False:
	print("Password red flag: password does not have a lowercase letter.")
else:
	lower_points = 2
	
# Check for numbers
has_digit = any(c.isdigit() for c in password)
if has_digit == False:
	print("Password red flag: password does not have a digit.")
else:
	digit_points = 2

if has_special == False:
	print("Password red flag: password does not have a special character.")
else:
	special_points = 2


#pattern_points = # Your code here
# Calculate total score and determine strength level
# Display detailed analysis
password_tally = upper_points + lower_points + digit_points + special_points
#Password strength: Excellent (13 or 11), Fair (9 or 7), or Failure 
if password_tally < 6:
	print("You did not enter a secure password (too many red flags).")
	exit()
password_tally = password_tally + length_points
if password_tally <= 9:
	password_strength = "Fair"
else:
	password_strength = "Excellent"

print(f"Password strength:  {password_strength}")
print("Password conditions have been met.")
input("Press ENTER to continue to part 3 of homework:  ")




print("\n\n\n\n\n=== GRADE VALIDATION SYSTEM ===")
# Get four test scores
test1 = float(input("Test 1 score: "))
test2 = float(input("Test 2 score: "))
test3 = float(input("Test 3 score: "))
test4 = float(input("Test 4 score: "))
# YOUR CODE HERE
# 1. Validate each score is 0-100 using chained comparisons
# 2. Check for suspicious patterns
# 3. Use truth table logic:
# valid_range AND not_suspicious AND not_identical
# 4. If valid, calculate average, highest, lowest, improvement
# 5. Provide appropriate feedback
# Example validation:
all_valid_range = (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100) and (0 <= test4 <= 100)

# Check if all identical
all_identical = (test1 == test2 == test3 == test4)

# Check for huge jumps
huge_jump = ((abs(test1 - test2) > 40) or (abs(test2 - test3) > 40) or (abs(test3 - test4) > 40))

# Combine validations using truth table logic

# Look for suspicious patterns first
if (all_valid_range == False) or (all_identical == True) or (huge_jump == True):
	if all_valid_range == False:
		print("\nYou have not entered a valid range of test scores (0-100)!\n\n")
	else:
		print("\nA suspicious pattern is in your inputed test scores.\n\n")
	exit()

# Begin score feedback
else:
#Calculate average
	score_average = (round((test1 + test2 + test3 + test4) // 4, 2))
	
	
#Calculate highest score
	if (test1 > test2) and (test1 > test3) and (test1 > test4):
		highest_score = "test1"
	if (test2 > test1) and (test2 > test3) and (test2 > test4):
		highest_score = "test2"
	if (test3 > test1) and (test3 > test2) and (test3 > test4):
		highest_score = "test3"
#This is for error-checking
	if (test4 > test1) and (test4 > test2) and (test4 > test3):
		highest_score = "test4"

# calculate lowest score
	if (test1 < test2) and (test1 < test3) and (test1 < test4):
		lowest_score = "test1"
	if (test2 < test1) and (test2 < test3) and (test2 < test4):
		lowest_score = "test2"
	if (test3 < test1) and (test3 < test2) and (test3 < test4):
		lowest_score = "test3"
# Error checking
	if (test4 < test1) and (test4 < test2) and (test4 < test3):
		lowest_score = "test4"
	
	
#Calculate improvement
#Slight(5), low(15), moderate(25), large(40)
	raw_improvement = test4 - test1
	if raw_improvement > 0:
		feedback_improvement = "improvement"
	else:
		feedback_improvement = "decrease"
	# in your score from test1 to test4.
	if abs(raw_improvement) <= 5:
		improvement_rating = "slight"
	elif abs(raw_improvement) <= 15:
		improvement_rating = "low"
	elif abs(raw_improvement) <= 25:
		improvement_rating = "moderate"
	else:
		improvement_rating = "large"
	
	print(f"AVERAGE SCORE:  {score_average}")
	print(f"HIGHEST SCORE:  {highest_score}")
	print(f"LOWEST SCORE:   {lowest_score}")
	print(f"\nFEEDBACK:  Your test scores have seen a {improvement_rating} {feedback_improvement} from Test1 to Test4.")
	print(" #" * 20)

"""
	# Find highest score
	if test1 > test2:
		if test1 > test3:
			if test1 > test4:
				highest_score = "test1"
	elif test2 > test1:
		# print("this should print (1)")
		if test2 > test3:
			# print("this should print (2)")
			if test2 > test4:
				# print("this should print (3)")
				highest_score = "test2"
	elif test3 > test1:
		if test3 > test2:
			if test3 > test4:
				highest_score = "test3"
	else:
		highest_score = "test4"
	lowest_score = "Undefined"
	if test1 < test2:
		print("TEST1 is lower than TEST2")
		if test1 < test3:
			if test1 < test4:
				lowest_score = "test1"
	elif test2 < test1:
		print("this should print (1)")
		if test2 < test3:
			print("this should print (2)")
			if test2 < test4:
				print("this should print (3)")
				lowest_score = "test2"
	elif test3 < test1:
		print("this should print (2.1)")
		if test3 < test2:
			print("this should print (2.1)")
			if test3 < test4:
				lowest_score = "test3"
	else:
		print("TEST 4 SHOULD BE LOWEST")
		lowest_score = "test4"
"""