#CS1300 Week 5 LAB 1


current_temp = 72
# Check if it's freezing (32 degrees or below)
is_freezing = current_temp <= 32
print(f"Is it freezing? {is_freezing}")
# Check if it's exactly room temperature (72 degrees)
is_room_temp = current_temp == 72
print(f"Is it room temperature? {is_room_temp}")
# Check if it's not 100 degrees
not_boiling = current_temp != 100
print(f"Is it not 100 degrees? {not_boiling}")



score = 85
# Check if the grade is an A (90 or above)
is_A = score >= 90 # Write your expression here
print(f"Score: {score}")
print(f"Is it an A (>=90)? {is_A}")
# Check if the grade is failing (below 60)
is_failing = score < 60 # Write your expression here
print(f"Is it failing (<60)? {is_failing}")
# Check if the grade is between 80 and 89 (B grade)
# Hint: You'll need two comparisons here!
is_B = score >= 80 and score <= 89
print(f"Is it a B (80-89)? {is_B}")
# Check if the grade is NOT a perfect score (not 100)
not_perfect = score != 100 # Write your expression here
print(f"Is it not perfect (!= 100)? {not_perfect}")


"""
# Shopping cart data
num_items = 3
cart_total = 45.50
coupon_code = "SAVE10"
is_member = True
# TODO: Create these Boolean expressions
# 1. Check if cart qualifies for free shipping (total >= $50)
free_shipping = cart_total 
# 2. Check if cart is empty (0 items)
cart_empty = ___
# 3. Check if customer entered the correct coupon code
valid_coupon = ___
# 4. Check if customer gets member discount (is a member AND cart > $25)
member_discount = ___
# 5. Check if this is a small order (less than 5 items AND total under $30)
small_order = ___
# Display results
print("Shopping Cart Analysis:")
print(f"Items in cart: {num_items}")
print(f"Cart total: ${cart_total}")
print(f"Free shipping eligible: {free_shipping}")
print(f"Cart is empty: {cart_empty}")
print(f"Valid coupon: {valid_coupon}")
print(f"Member discount applies: {member_discount}")
print(f"Small order: {small_order}")
"""


temperature = 10 # Try changing this value!
print(f"Current temperature: {temperature}°F")
print("Weather advice:")
if temperature > 90:
	print("It's very hot! Stay hydrated!")
if temperature < 32:
	print("It's freezing!  Bundle up!")
if temperature == 72:
	print("Perfect weather!")
	


"""
purchase_amount = 125.00
is_student = True
is_senior = False
is_veteran = False
print("=== Discount Calculator ===")
print(f"Original amount: ${purchase_amount:.2f}")
discount = 0
if 
	# TODO: Add if statements for each discount
	# If purchase > $100, add 10% discount
if ___:
discount = discount + (purchase_amount * 0.10)
	print(" 10% discount for purchases over $100")✓
	# If customer is a student, add $5 discount
if ___:
	___
	print(" $5 student discount applied")✓
	# If customer is a senior (over 65), add 15% discount
if ___:
	___
	print(" 15% senior discount applied")✓
	# If customer is a veteran, add $10 discount
if ___:
	___
print(" $10 veteran discount applied")✓
	# Calculate and display final amount
final_amount = purchase_amount - discount
print(f"\nTotal discount: ${discount:.2f}")
print(f"Final amount: ${final_amount:.2f}")
"""


# 3a
# Complete the if-else statements
# Decision 1: Weekend or Weekday?
day = "Saturday" # Try "Monday" too!
print(f"Today is {day}")
if day == "Saturday" or day == "Sunday":
	print("It's the weekend!")
# Add a print statement for weekend activity
	print("Time to relax")
else:
	print("It's a weekday!")
# Add a print statement for weekday activity
	print("Time to go to school")
# Decision 2: Hot or Cold Beverage?
temperature = 45 # Try different values!
print(f"\nTemperature: {temperature}°F")
# Complete this if-else statement
if temperature > 70:
	print("It is above 70 degrees, time to wear shorts!")
else:
	print("It is below or equal to 70 degrees, time to wear jeans!")
# Decision 3: Light or Dark Mode?
current_hour = 20 # 8 PM in 24-hour format
print(f"\nCurrent hour: {current_hour}:00")
# Write an if-else to choose display mode
# make dark mode a variable
# Use dark mode after 6 PM (18:00) or before 6 AM
if current_hour < 20:
	print("DISPLAY: Light-mode")
else:
	print("DISPLAY: Dark-mode")
	

age = 15 # Try different ages!
day = "Wednesday" # Try different days!
print("=== Movie Ticket Pricing ===")
print(f"Customer age: {age}")
print(f"Day: {day}")
# Base ticket price
base_price = 12.00
final_price = base_price
# TODO: Implement pricing rules with if-else
# Rule 1: Children (12 and under) get 50% off, others pay full price
if age < 13:
	final_price = base_price * 0.5
	print(" Child discount applied (50% off)")
else:
	print("Standard pricing")
# Rule 2: Seniors (65+) get 30% off, others no discount
if age > 64:
	final_price = final_price * 0.7
	print(" Senior discount applied (30% off)")
else:
	# No additional discount
	pass
# Rule 3: Wednesday is discount day - everyone gets $2 off
if day == "Wednesday":
	final_price = base_price - 2
	print(" Wednesday special ($2 off)")
else:
	print("Today is not Wednesday, nobody gets $2 discount")
print(f"\nFinal ticket price: ${final_price:.2f}")
	# Add a message based on savings
savings = base_price - final_price
if savings > 0:
	print(f"You saved: ${savings:.2f}!")
else:
	print("No discounts applied today.")
	
	
print("\n\nExercise 4a")
# Practice: Fix all indentation errors
	# Each line should be properly indented
score = 85
	# Fix this code:
print("Checking your grade...")
if score >= 90:
	print("You got an A!") # FIX: Add indentation
	print("Excellent work!") # FIX: Add indentation
else:
	print("Not an A") # FIX: Should be 4 spaces, not 2
	if score >= 80: # FIX: Too much indentation
		print("You got a B!")
		print("Good job!")
# Fix this code:
age = 15
if age >= 16:
	print("You can drive")
	if age >= 18:
		print("You can vote") # FIX: Add indentation
else:
	print("Too young to drive") # FIX: Too much indentation
	
	
print("\n\nExercise 4b")
# Practice: Create a grade and attendance checker
# Use proper indentation for nested conditions
grade = 75
attendance = 85
extra_credit = True
print("=== Student Evaluation ===")
print(f"Grade: {grade}")
print(f"Attendance: {attendance}%")
print(f"Extra credit: {extra_credit}")
# TODO: Create this structure with proper indentation:
# 1. If grade >= 60 (passing)
if grade >= 60:
	print("Passing Grade")
# - Print "Passing grade"
# - If attendance >= 80
# * Print "Good attendance"
	if attendance >= 80:
		print("Good attendance")
# * If extra_credit is True
# > Add 5 to grade
		if extra_credit == True:
			grade = grade + 5
			print(f"Grade is: {grade}")
# > Print new grade
# - Else (attendance < 80)
# * Print "Attendance needs improvement"
	else:
		print("Attendance needs improvement")
# 2. Else (grade < 60)
else:
	print("Failing grade.")
	print("Must retake this course.")
# - Print "Failing grade"
# - Print "Must retake course"
# Start your code here:
# Add your code with proper indentation
	print("\n=== End of Evaluation ===")




# Practice: Range validation system
# Use chained comparisons to validate different ranges
# Test values
test_score = 78
body_temp = 98.6
ph_level = 7.2	
humidity = 45
print("=== Range Validator ===")
# TODO: Check if values are in valid ranges using chained comparisons
# Test score should be between 0 and 100
valid_score = ___
if valid_score:
	print(f" Test score {test_score} is valid")
# Check grade range using chained comparisons
if 90 >= test_score <= 100: # 90-100
	print(" Grade: A")
elif 80 >= test_score < 90: # 80-89
	print(" Grade: B")
elif 70 >= test_score < 80:: # 70-79
	print(" Grade: C")
elif 60 >= test_score < 70: # 60-69
	print(" Grade: D")
	else:
	print(" Grade: F")
else:
	print(f" Invalid test score: {test_score}")
# Body temperature: normal is 97.0 - 99.0
normal_temp = ___
if normal_temp:
print(f" Temperature {body_temp}°F is normal")
else:
if body_temp < 97.0:
print(f" Low temperature: {body_temp}°F")
else:
print(f" Fever detected: {body_temp}°F")
# pH level: neutral is 6.5 - 7.5
neutral_ph = ___
if neutral_ph:
print(f" pH {ph_level} is neutral")
else:
if ___:
print(f"Acidic: pH {ph_level}")
else:
print(f"Basic: pH {ph_level}")
# Humidity: comfortable is 30-50%
comfortable_humidity = ___
print(f"Humidity {humidity}% is comfortable: {comfortable_humidity}")




