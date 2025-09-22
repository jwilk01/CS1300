# CS 1300 - Homework 2
# Name: Joseph Wilk
# Date: Sep 22 2025
# Description: Variables, Input/Output, and Type Conversions

import math

# YOU CANNOT   CLEAR   THE SCREEN LIKE YOU CAN IN BASH WITH ONE WORD COMMAND





print("\n\n\n\n\n\n")
print("=" * 30)
print("PERSONAL FINANCE CALCULATOR".center(30, "-"))
print("=" * 30)

income = input("\n\n\nPlease ENTER your monthly INCOME in dollars:  ")
rent = input("Please ENTER your monthly cost of RENT in dollars:  ")
food = input("Please ENTER your monthly FOOD bill:  ")
transportation = input("Please ENTER your monthly TRANSPORTATION cost:  ")
other = input("If applicable, please enter OTHER total montly expense total in dollars (enter  0  if N/A):  ")

# NEXT THREE SUBSECTIONS ARE FOR CALCULATIONS, THEN THE PRINTING:

income = float(income)
rent = float(rent)
food = float(food)
transportation = float(transportation)
other = float(other)

income = round(income, 2)
rent = round(rent, 2)
food = round(food, 2)
transportation = round(transportation, 2)
other = round(other, 2)

# I HAD TO USE   ROUND   TO PREVENT DISCREPANT PYTHON FLOAT DECIMAL VALUES

total_expenses = round(rent + food + transportation + other, 2)
remaining = round(income - total_expenses, 2)
savings_rate = round(remaining / income, 2)

print("\n\n")
print("=" * 30)
print("MONTHLY BUDGET REPORT".center(30, "-"))
print("=" * 30)
print("\n INCOME:         ", income)
print("\n")
print("-" * 25)
print("\n EXPENSES:")
print("\tRENT:            ", rent)
print("\tFOOD:            ", food)
print("\tTRANSPORTATION:  ", transportation)
print("\tOTHER:           ", other)
print("\n")
print("-" * 21)
print("\n")
print("TOTAL EXPENSES:        ", total_expenses)
print("REMAINING BALANCE:     ", remaining)
print("SAVINGS RATE:          ", savings_rate)
print("=" * 30)
print("DEGUG TESTING:")
print(type(income))
print(income, rent, food, transportation, other)
print(f"{total_expenses:.2f}")
print(savings_rate)
input("Press ENTER to continue to part 2/4:  ")
print("\n\n\n\n\n\n\n\n")



# END SECTION 1
# END SECTION 1
# END SECTION 1






print("*" * 35)
print("GRADE STATISTICS CALCULATOR".ljust(35, "_"))
print("*" * 35)
test_score_1 = input("\nPlease ENTER test score #1 (out of 100):  ")
test_score_2 = input("Please ENTER test score #2 (out of 100):  ")
test_score_3 = input("Please ENTER test score #3 (out of 100):  ")
test_score_4 = input("Please ENTER test score #4 (out of 100):  ")
test_score_5 = input("Please ENTER test score #5 (out of 100):  ")
# DEBUG print(avg_score)


# CALCULATIONS
test_score_1 = float(test_score_1)
test_score_2 = float(test_score_2)
test_score_3 = float(test_score_3)
test_score_4 = float(test_score_4)
test_score_5 = float(test_score_5)
test_score_1 = round(test_score_1, 1)
test_score_2 = round(test_score_2, 1)
test_score_3 = round(test_score_3, 1)
test_score_4 = round(test_score_4, 1)
test_score_5 = round(test_score_5, 1)
score_total = test_score_1 + test_score_2 + test_score_3 + test_score_4 + test_score_5
avg_score = round((test_score_1 + test_score_2 + test_score_3 + test_score_4 + test_score_5) / 5, 1)
needed_90 = 0

# DISPLAY OUTPUT
print("\n       GRADE REPORT")
print("*" * 25)
print("\n   TEST SCORES ENTERED:")
print(" TEST 1:  ", test_score_1,"/100")
print(" TEST 2:  ", test_score_2,"/100")
print(" TEST 3:  ", test_score_3,"/100")
print(" TEST 4:  ", test_score_4,"/100")
print(" TEST 5:  ", test_score_5,"/100")
print("")
print("*" * 25)
print("\nSTATISTICS:")
print(" TOTAL SCORE:   ", score_total,"/500")
print(" AVERAGE SCORE: ", avg_score,"/100")
print(" OVERALL GRADE: ", avg_score,"%", sep="")
if score_total < 450:
	#DO THE CALCULATION ONLY IF THE IF-STATEMENT IS FULFILLED
	needed_90 = 450 - score_total
	print("\nPOINTS NEEDED FOR A 90%:  ", needed_90)
else:
	print("YOUR SCORE IS AT LEAST 90%.  GOOD JOB!")
print("")
print("*" * 35)
print("*" * 35)
print("*" * 35)
input("\n\nPress ENTER to continue to part 3/4:  ")
print("\n\n\n\n\n\n\n\n")



# END SECTION 2
# END SECTION 2
# END SECTION 2



print("\n" + "=" * 40)
print("Problem 3: Time Zone Converter")
print("=" * 40 + "\n")

user_hour_24 = input("Please ENTER the current HOUR in EST (24-hour format):  ")
user_minute = input("Please ENTER the MINUTE (two digits):  ")


user_hour_24 = int(user_hour_24)
#  LEAVE MINUTE AS A STRING FOR "00" option.  user_minute = int(user_minute)
calculation_24 = user_hour_24
am_pm = "A.M."
hour_12 = 0

# CONVERSION FROM 24 TO 12 HOUR FORMAT
if user_hour_24 == 0:
	hour_12 = 12
	am_pm = "A.M."
elif user_hour_24 == 12:
	hour_12 = 12
	am_pm = "P.M."
elif 12 < user_hour_24 <= 23:
	hour_12 = user_hour_24 - 12
	am_pm = "P.M."
	# DEBUG print("am_pm should be P.M. --> ", am_pm)
else:
	hour_12 = user_hour_24
	am_pm = "A.M."
	
calculation_12 = hour_12

# START AT 14:00 and 2:00 

# This modulus calculation was borrowed from another Indiana Tech course.
calculation_24 = ((calculation_24 + 24) + 24 ) % 24
calculation_12 = ((calculation_12 + 12) + 12 ) % 12
if calculation_12 == 0:
	calculation_12 = 12
# any variable in a print-f command is automatically converted into a string.
print(f"  EST  |  {calculation_24}:{user_minute}  |  {calculation_12}:{user_minute}{am_pm}  ||||")

calculation_24 = (((calculation_24 - 1) + 24) + 24 ) % 24
calculation_12 = (((calculation_12 - 1) + 12) + 12 ) % 12
if calculation_12 == 0:
	calculation_12 = 12
if calculation_12 == 11:
	if am_pm == "A.M.":
		am_pm = "P.M."
	else:
		am_pm = "A.M."
print(f"  CST  |  {calculation_24}:{user_minute}  |  {calculation_12}:{user_minute}{am_pm}  ||||")


calculation_24 = (((calculation_24 - 1) + 24) + 24 ) % 24
calculation_12 = (((calculation_12 - 1) + 12) + 12 ) % 12
if calculation_12 == 0:
	calculation_12 = 12
if calculation_12 == 11:
	if am_pm == "A.M.":
		am_pm = "P.M."
	else:
		am_pm = "A.M."
print(f"  MST  |  {calculation_24}:{user_minute}  |  {calculation_12}:{user_minute}{am_pm}  ||||")


calculation_24 = (((calculation_24 - 1) + 24) + 24 ) % 24
calculation_12 = (((calculation_12 - 1) + 12) + 12 ) % 12
if calculation_12 == 0:
	calculation_12 = 12
if calculation_12 == 11:
	if am_pm == "A.M.":
		am_pm = "P.M."
	else:
		am_pm = "A.M."
print(f"  PST  |  {calculation_24}:{user_minute}  |  {calculation_12}:{user_minute}{am_pm}  ||||")
print("+--------------------------------------+")
input("Press ENTER to continue to part 4/4:  ")
print("\n\n\n\n\n\n\n\n")


#END SECTION
#END SECTION
#END SECTION



print("\n" + "=" * 40)
print("Problem 4: Recipe Scaler")
print("=" * 40)

original_serving = int(input("\nEnter original serving size (integer):  "))
desired_serving = int(input("Enter desired serving size (integer):  "))

print("\nEnter FIVE ingredients and portions below -->\n")

ingredient_1 = input("ENTER ingredient #1:  ")
portion_1 = float(input("ENTER portion SIZE of #1 (float):  "))
unit_1 = input("ENTER portion unit of measurement of #1 (cups,tbsp,tsp,whole,half,quarter):  ")

ingredient_2 = input("\nENTER ingredient #2:  ")
portion_2 = float(input("ENTER portion SIZE of #2 (float):  "))
unit_2 = input("ENTER portion unit of measurement of #2 (cups,tbsp,tsp,whole,half,quarter):  ")

ingredient_3 = input("\nENTER ingredient #3:  ")
portion_3 = float(input("ENTER portion SIZE of #3 (float):  "))
unit_3 = input("ENTER portion unit of measurement of #3 (cups,tbsp,tsp,whole,half,quarter):  ")

ingredient_4 = input("\nENTER ingredient #4:  ")
portion_4 = float(input("ENTER portion SIZE of #4 (float):  "))
unit_4 = input("ENTER portion unit of measurement of #4 (cups,tbsp,tsp,whole,half,quarter):  ")

ingredient_5 = input("\nENTER ingredient #5:  ")
portion_5 = float(input("ENTER portion SIZE of #5 (float):  "))
unit_5 = input("ENTER portion unit of measurement of #5 (cups,tbsp,tsp,whole,half,quarter):  ")


#CALCULATIONS

ratio = round(float(desired_serving / original_serving),2)
new_portion_1 = round(ratio * portion_1,2)
new_portion_2 = round(ratio * portion_2,2)
new_portion_3 = round(ratio * portion_3,2)
new_portion_4 = round(ratio * portion_4,2)
new_portion_5 = round(ratio * portion_5,2)


#PRINTING

print("\n\n" + "#" * 35)
print("     RECIPE SCALING RESULTS")
print("#" * 35 + "\n")

print(f"Scaling factor: {ratio}x ({original_serving} to {desired_serving} servings).")
print("-" * 20 + "\n")

print(f"Original recipe ({original_serving} servings).  Desired recipe ({desired_serving} servings).")
print("-" * 15 + "|" + "-" * 15)

print(f"{ingredient_1}:  {portion_1} {unit_1} |  {ingredient_1}:  {new_portion_1} {unit_1} ")
print(f"{ingredient_2}:  {portion_2} {unit_2} |  {ingredient_2}:  {new_portion_2} {unit_2} ")
print(f"{ingredient_3}:  {portion_3} {unit_3} |  {ingredient_3}:  {new_portion_3} {unit_3} ")
print(f"{ingredient_4}:  {portion_4} {unit_4} |  {ingredient_4}:  {new_portion_4} {unit_4} ")
print(f"{ingredient_5}:  {portion_5} {unit_5} |  {ingredient_5}:  {new_portion_5} {unit_5} ")

print("#" * 40)
input("\n\n\nEND OF HOMEWORK 2 CS1300 FALL 2025")

