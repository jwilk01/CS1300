# Joseph Wilk
# CS1300
# Function Hmwk1
# Nov 14, 2025

from decimal import Decimal, ROUND_HALF_UP
from decimal import *
getcontext().prec = 9
# SOURCE = docs.python.org

# PROBLEM 1


def celsius_to_fahrenheit(celsius):
#Convert Celsius to Fahrenheit
# Formula: F = C * 9/5 + 32
# Your code here
	F = celsius * 9/5 + 32
	return F


def fahrenheit_to_celsius(fahrenheit):
#Convert Fahrenheit to Celsius
# Formula: C = (F - 32) * 5/9
# Your code here
	C = round((fahrenheit - 32) * (5/9), 1)
	return C


def temperature_report(orig_temp, new_temp, scale="C"):
	"""
	Print temperature in both scales.
	Parameters:
	temp: temperature value
	scale: "C" for Celsius or "F" for Fahrenheit (default "C")
	
	# Your code here
	# If scale is "C", show temp in C and converted to F
	# If scale is "F", show temp in F and converted to C
	"""
	print(f"Your original temperature:  {orig_temp}°{scale}")
	if scale.upper() == "F":
		scale = "C"
	else:
		scale = "F"
	print(f"Converted temperature:  {new_temp}°{scale}")



print("\nWelcome to HW9!\n\n")
print("PROBLEM 1: Temperature conversion\n")

# THIS LOOP IS FOR CORRECTLY ENTERING TEMPERATURE SCALE:
while True:
	user_scale = input("ENTER either Fahrenheit (F) or Celsius (C):  ")
	if user_scale[0].upper() == "C" or user_scale[0].upper() == "F":
		if len(user_scale) == 1:
			# print("Debug: correct scale entered.")
			break
		else:
			if user_scale.upper() == "FAHRENHEIT" or user_scale.upper() == "CELSIUS":
				# print("Debug: correct scale entered.")
				break
	else:
		print("You did not enter a valid temperature scale (F or C).")
		print(f"You entered:  {user_scale}\n\n")
		continue

# print("DEBUG Outside Problem 1 loop.")


# USER TEMPERATURE
# If user enters a decimal number, it is converted to INT
user_temperature = round(float(input("ENTER a temperature (integer):  ")), 0)


# CONVERSIONS

if user_scale[0].upper() == "F":
# CHANGING VARIABLE NAMES FOR READABILITY
	original_temperature = user_temperature
	converted_temperature = fahrenheit_to_celsius(user_temperature)
else:
	original_temperature = user_temperature
	converted_temperature = celsius_to_fahrenheit(user_temperature)

# DEBUG print(converted_temperature)

if len(user_scale) > 1:
	user_scale = user_scale[0].upper()



# RUN THE TEMPERATURE REPORT:
temperature_report(original_temperature, converted_temperature, user_scale)


# TEST CASES
"""
F 0
F 100
C 32
C 68
"""
print("\nTEST CASES:\n")
user_scale = "F"
original_temperature = 32
converted_temperature = fahrenheit_to_celsius(original_temperature)
temperature_report(original_temperature, converted_temperature, user_scale)

original_temperature = 68
converted_temperature = fahrenheit_to_celsius(original_temperature)
temperature_report(original_temperature, converted_temperature, user_scale)

user_scale = "C"
original_temperature = 0
converted_temperature = celsius_to_fahrenheit(original_temperature)
temperature_report(original_temperature, converted_temperature, user_scale)

original_temperature = 100
converted_temperature = celsius_to_fahrenheit(original_temperature)
temperature_report(original_temperature, converted_temperature, user_scale)

user_scale = ""
original_temperature = 25
converted_temperature = celsius_to_fahrenheit(original_temperature)
temperature_report(original_temperature, converted_temperature)

user_scale = "F"
original_temperature = 77
converted_temperature = fahrenheit_to_celsius(original_temperature)
temperature_report(original_temperature, converted_temperature, user_scale)


input("\n\nPress ENTER to continue to Problem 2:  ")









print("\n\n\n\n\nPROBLEM 2\n\n")
bool_percentage = True # THIS IS TO DEFINE THE VARIABLE AS A GLOBAL
grade1 = 0
user_hw = 0
user_mid = 0
user_final_e = 0
hw_num = 0
mid_num = 0
final_e_num = 0



student_name = input("Please ENTER student name:  ")


def percentage_check(perc):
	global bool_percentage
	if perc < 0 or perc > 100:
		print("You did not enter a valid percentage integer (0 to 100)\n\n")
		bool_percentage = False

# THIS IS WHEN THE % WEIGHTS ARE ENTERED
def weight_check(perc):
	global bool_percentage
	if perc < 0 or perc > 1:
		print("You did not enter a valid % weight.\n\n")
		bool_percentage = False

# ABBREVIATED "WEIGHT" VARIABLES FOR FUNCTION USE:
# TWO GROUPS OF THREE IS THE WAY TO MEMORIZE A LONG LIST OF SIX VARIABLES:
def calculate_weighted_grade(hw, mid, final, hw_w=0.3, mid_w=0.3, final_w=0.4):
	global user_hw, user_mid, user_final_e, hw_num, mid_num, final_e_num
	user_hw = float(round(hw, 7))
	hw_num = user_hw
	user_mid = float(round(mid, 7))
	mid_num = user_mid
	user_final_e = float(round(final, 7))
	final_e_num = user_final_e
	hw_w = float(round(hw_w, 7))
	mid_w = float(round(mid_w, 7))
	final_w = float(round(final_w, 7))
	print("\n\n")
	print("#__##__#" * 3)
	print(f"Homework grade =  {user_hw:.0f}%")
	print(f"Midterm grade =   {user_mid:.0f}%")
	print(f"Final Exam  =     {user_final_e:.0f}%")
# FIND AVERAGE UNWEIGHTED GRADE
	unweighted_avg = round((hw + mid + final)/3, 7) # LOCAL VARIABLE
	print(f"Unweighted average  =    {unweighted_avg:.2f}%")
	print(f"\nWeight of Homework =  {hw_w:.2f}")
	print(f"Weight of Midterm  =    {mid_w:.2f}")
	print(f"Weight of Final Exam =  {final_w:.2f}")
# ROUND TO 7 DECIMAL PLACES BEFORE FINAL PERCENTAGE IS ROUNDED TO 2 DECIMAL PLACES
	user_hw = round(user_hw * hw_w, 7)
	print(f"{user_hw:.7f}")
	user_mid = round(user_mid * mid_w, 7)
	print(f"{user_mid:.7f}")
	user_final_e = round(user_final_e * final_w, 7)
	print(f"{user_final_e:.7f}")
	print(f"\tWeighted Homework  ~   {user_hw:.2f}")
	print(f"\tWeighted Midterm   ~   {user_mid:.2f}")
	print(f"\tWeighted Final Exam ~  {user_final_e:.2f}")
	weighted_avg  = user_hw + user_mid + user_final_e
	print(f"\n\tFinal Grade (%) =  {weighted_avg:.3f}")
	return weighted_avg

def get_letter_grade(score):
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"

def print_grade_report(grade, letter):
	global hw_num, mid_num, final_e_num, student_name, grade1, letter_grade
	print("\n\n  STUDENT REPORT  -----")
	print(f"\nName:  {student_name}")
	print(f"Homework grade =  {hw_num}%")
	print(f"Midterm grade =   {mid_num}%")
	print(f"Final Exam  =     {final_e_num}%")
	print("")
	print(f"FINAL WEIGHTED =  {grade1:.3f}% \"{letter_grade}\"")
	
 
# LOOP FOR CHECKING A VALID PERCENTAGE USING A FUNCTION
while True:
# I save redundancy of putting bool_percentage = True when it is already true, but two additional lines of code are added.
	print("User will input Homework, Midterm, and Final Exam grades as INTEGERS.")
	user_hw = int(float(input("ENTER Homework %  --> ")))
	percentage_check(user_hw)
	if bool_percentage == False:
		bool_percentage = True
		continue
	user_mid = int(float(input("ENTER Midterm %  --> ")))
	percentage_check(user_mid)
	if bool_percentage == False:
		bool_percentage = True
		continue
	user_final_e = int(float(input("ENTER Final Exam %  --> ")))
	percentage_check(user_final_e)
	if bool_percentage == False:
		bool_percentage = True
		continue
	break



# LOOP FOR USER WEIGHT DISTRIBUTION
while True:
	user_prompt_weight = input("\nDo you want to change the weight distribution of the grade %'s (y or n):  ")
	if user_prompt_weight[0].lower() == "y" or user_prompt_weight[0].lower() == "n":
		if len(user_prompt_weight) == 1:
			user_prompt_weight = user_prompt_weight.lower()
			break
		elif user_prompt_weight.lower() == "yes" or user_prompt_weight.lower() == "no":
			user_prompt_weight = user_prompt_weight.lower()
			user_prompt_weight = user_prompt_weight[0]
			break
	print("\nYou did not enter \"y\" or \"n\"\n\n")
	continue

# DEBUG print("end of program")


# I save redundancy of putting bool_percentage = True when it is already true, but two additional lines of code are added.
if user_prompt_weight == "y":
	while True:
		print("HW, Midterm, and Final are weighted at 1.00 cumulatively.  ")
		hw_weight = round(float(input("ENTER the weight of Homework (0.00 to 1.00):  ")), 2)
		weight_check(hw_weight)
		if bool_percentage == False:
			bool_percentage = True
			continue
		mid_weight = round(float(input("ENTER the weight of Midterm (0.00 to 1.00):  ")), 2)
		weight_check(mid_weight)
		if bool_percentage == False:
			bool_percentage = True
			continue
		final_weight = round(float(input("ENTER the weight of Final Exam (0.00 to 1.00):  ")), 2)
		weight_check(final_weight)
		if bool_percentage == False:
			bool_percentage = True
			continue
		if round(hw_weight + mid_weight + final_weight, 2) != 1.00:
			print("Your total weights do not equal to 1.00!\n")
			continue
		break

if user_prompt_weight == "n":
	grade1 = calculate_weighted_grade(user_hw, user_mid, user_final_e)
else:
	grade1 = calculate_weighted_grade(user_hw, user_mid, user_final_e, hw_weight, mid_weight, final_weight)

letter_grade = get_letter_grade(grade1)

print_grade_report(grade1, letter_grade)

print("\n\n\nCASE REPORT (85, 78, 92):")
grade1 = calculate_weighted_grade(85, 78, 92)
letter_grade = get_letter_grade(grade1)
print_grade_report(grade1, letter_grade)

print("\nCASE REPORT (90, 85, 80, 0.4, 0.2, 0.4")
grade1 = calculate_weighted_grade(90, 85, 80, 0.4, 0.2, 0.4)
letter_grade = get_letter_grade(grade1)
print_grade_report(grade1, letter_grade)

#print("end of program")

input("\n\nPress ENTER to continue to Problem 3:  ")











print("\n\n\n\nPROBLEM 3   #######\n\n")

print("NO GLOBAL KEYWORD HERE!\n\n")

bonus_multiplier = 1.1
#These three variables are in the reset_game function
n = 10
game_score = 0
bool_reset = False

def add_score(total, score):
	total += score
	return total

def add_bonus(total, bonus):
	total *= bonus
	return total

def reset_game(n, total, bool):
	while True:
		user_reset = input("\nDo you want to reset the game (y or n):  ").lower()
		if user_reset == 'y' or user_reset == 'n' or user_reset == 'yes' or user_reset == 'no':
			if user_reset == 'n' or user_reset == 'no':
				bool = False
			else:
				bool = True
				n = 10
				total = 0
			return n, total, bool
		print("You did not enter 'y' or 'n'\n")

print(f"Add up to ten different point totals that will factor a bonus multiplier ({bonus_multiplier}x)!")
while True:
	user_points_list = []
	user_points = 0
	while n > 0:
		user_points = float(input("ENTER any number (Enter a negative number to leave loop):  "))
		if user_points < 0:
			if len(user_points_list) == 0:
				print("Please append a positive number to your list.")
				continue
			break
		user_points_list.append(user_points)
		n -= 1
	print(user_points_list)
	
	for i in range(len(user_points_list)):
		game_score = add_score(game_score, user_points_list[i])
		print(game_score)
	else:
		game_score = add_bonus(game_score, bonus_multiplier)
	
	print(f"FINAL TOTAL SCORE WITH BONUS MULTIPLIER({bonus_multiplier}x) =  {game_score:.3f}")
	
	n, game_score, bool_reset = reset_game(n, game_score, bool_reset)
	# DEBUG print(n, game_score, bool_reset)
	if bool_reset == False:
		break

print("TEST CASE WORKS WITH 50 THEN 100 FOLLOWED BY NEGATIVE NUMBER.  CORRECTLY ADDS UP TO 165 WITH BONUS MULTIPLIER(1.1X).")
print("End Program")
#END PROGRAM