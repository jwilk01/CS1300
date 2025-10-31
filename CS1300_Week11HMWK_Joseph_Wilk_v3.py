# Joseph Wilk
# CS1300
# Week 11 Homework
# Oct 31 2025

problem_2_break_loop = False

print("#" * 12, "$" * 4)
print("PROBLEM 1:\n")
user_grid_size = 0

while (user_grid_size < 1) or (user_grid_size > 12):
	user_grid_size = int(input("Please ENTER a grid size for multiplication table (from 1 to 12):  "))
	if user_grid_size < 1 or user_grid_size > 12:
		print("You did not enter a valid grid size (1 to 12)!  ")
		continue

print("    |     ", end="")
for i in range(1, user_grid_size + 1):
# The format:2 number, then FOUR spaces:
	print(f"{i:>2}    ", end="")
print()
print(" - -+ - - ", end="")
print("- - - " * user_grid_size)
for col in range(1, user_grid_size + 1):
	print(f" {col:>2} | ", end="")
	for row in range(1, user_grid_size + 1):
		row_col = row * col
		print(f"{row_col:>6}", end="")
	print()
input("\nPress \"enter\" to continue:  ")
print("\n\n\n")



print("PROBLEM 2:\n\n")

print("=== Pattern Analysis ===\n")

numbers = [23, 8, 45, 12, 78, 34, 67, 91, 15, 52, 41, 3]
problem_2_even_nums = []
# Four variables for 0-25, 26-50, 51-75, 76-100.  Find the length of the lists.
quarterly_1 = []
quarterly_2 = []
quarterly_3 = []
quarterly_4 = []
divisible_three = []
sum_divisible_three = 0
bool_sentinel = True
user_sentinel = 0


print(f"Original numbers:  {numbers}\n")


# FIND THE FIRST NUMBER GREATER THAN 75:
for i in range(len(numbers)):
	if numbers[i] > 75:
		print(f"First number > 75:  {numbers[i]} (at position {i})")
		problem_2_break_loop = True
		break
# THIS IS HERE AS THE BREAK ABOVE DOES NOTHING
	if problem_2_break_loop == True:
		break
else:
	print("There is no number greater than 75 here.")
#DEBUG:  print("Loop completed")


# FIND ALL EVEN NUMBERS:
for i in range(len(numbers)):
	if numbers[i] % 2 == 0:
		problem_2_even_nums.append(numbers[i])
print("\nFILTER PATTERN: EVEN NUMBERS")
print(f"{problem_2_even_nums}\n")


# FIND NUMBERS 0-25, 26-50, 51-75, 76-100
for i in range(len(numbers)):
	if numbers[i] < 0:
		print("Number is less than 0.  Exit program.")
		exit(0)
	elif numbers[i] > 100:
		print("Number is greater than 100.  Exit program.")
		exit(0)
	elif numbers[i] <= 25:
		quarterly_1.append(numbers[i])
	elif numbers[i] <= 50:
		quarterly_2.append(numbers[i])
	elif numbers[i] <= 75:
		quarterly_3.append(numbers[i])
	else:
		quarterly_4.append(numbers[i])
print("\nCOUNTER PATTERN -------")
print(f"Numbers from 0-25:    {len(quarterly_1)}")
print(f"Numbers from 25-50:   {len(quarterly_2)}")
print(f"Numbers from 50-75:   {len(quarterly_3)}")
print(f"Numbers from 75-100:  {len(quarterly_4)}")


# FIND NUMBERS DIVISIBLE BY 3:
for i in range(len(numbers)):
	if numbers[i] % 3 == 0:
		divisible_three.append(numbers[i])
for i in range(len(divisible_three)):
	sum_divisible_three += divisible_three[i]
print("\nACCUMULATOR PATTERN:")
print(divisible_three)
print(f"Sum of these numbers:  {sum_divisible_three}")


# SENTINEL PATTERN: ADD MORE NUMBERS UNTIL -1 IS ENTERED.
print("\nSENTINEL PATTERN:")
print("Enter more numbers from 0 to 100 (or \"-1\" to quit):  ", end="")

while True:
	user_sentinel = int(input())
	if 0 <= user_sentinel <= 100:
		numbers.append(user_sentinel)
		continue
	break
		
	
print(f"Updated numbers list:  {numbers}")
print(f"New count:   {len(numbers)} numbers")
print("\nPress \"enter\" to continue to bonus problem:")
print("\n\n\n\n")








# BONUS PROBLEM


# I DID NOT USE DICTIONARIES OR TUPLES!


grades = [
[92, 88, 95, 87, 90], # Alice
[78, 82, 73, 85, 80], # Bob
[95, 91, 98, 92, 94], # Carol
[65, 70, 68, 72, 75], # David
[88, 85, 82, 90, 87] # Emma
]

#alice_list = [92, 88, 95, 87, 90]
#bob_list = [78, 82, 73, 85, 80]
#carrol_list = [95, 91, 98, 92, 94]
#david_list = [65, 70, 68, 72, 75]
#emma_list = [88, 85, 82, 90, 87]

#array_grades = [alice_list, bob_list, carrol_list, david_list, emma_list]
#DEBUG
#print(f"\n\narray_grades = {array_grades}\n\n")
#print(f"\nCarrol's fourth letter grade: {array_grades[2, 3]}\n\n")
student_names = ["Alice", "Bob", "Carrol", "David", "Emma"]

#Some variables are defined as the program executes
alice_grades = grades[0]
bob_grades = grades[1]
carrol_grades = grades[2]
david_grades = grades[3]
emma_grades = grades[4]
#

alice_avg = 0
bob_avg = 0
carrol_avg = 0
david_avg = 0
emma_avg = 0
#
student_avg = []
letter_grade = ["F"] * len(grades)
count_honor = 0
count_warning = 0
#
class_avg = 0
#
alice_highest = alice_grades[-1]
bob_highest = bob_grades[-1]
carrol_highest = carrol_grades[-1]
david_highest = david_grades[-1]
emma_highest = emma_grades[-1]
alice_lowest = alice_grades[-1]
bob_lowest = bob_grades[-1]
carrol_lowest = carrol_grades[-1]
david_lowest = david_grades[-1]
emma_lowest = emma_grades[-1]
# Variables for the highest and lowest scores for each student
student_highest = [0] * len(grades)
student_lowest = [0] * len(grades)
# These get redefined later
highest_grade = 0
lowest_grade = 0
#
HW1_list = []
HW2_list = []
Quiz1_list = []
Exam1_list = []
Quiz2_list = []
#
HW1_avg = 0
HW2_avg = 0
Quiz1_avg = 0
Exam1_avg = 0
Quiz2_avg = 0
# highest and lowest scores defined as global here for outside loops
HW1_highest = grades[-1][0]
HW2_highest = grades[-1][1]
Quiz1_highest = grades[-1][2]
Exam1_highest = grades[-1][3]
Quiz2_highest = grades[-1][4]
#
HW1_lowest = grades[-1][0]
HW2_lowest = grades[-1][1]
Quiz1_lowest = grades[-1][2]
Exam1_lowest = grades[-1][3]
Quiz2_lowest = grades[-1][4]




#FINDING STUDENT AVERAGES
# ".append" only works for one argument at a time

for i in range(len(alice_grades)):
	alice_avg += alice_grades[i]
alice_avg = alice_avg / len(alice_grades)
student_avg.append(alice_avg)

for i in range(len(bob_grades)):
	bob_avg += bob_grades[i]
bob_avg = bob_avg / len(bob_grades)
student_avg.append(bob_avg)

for i in range(len(carrol_grades)):
	carrol_avg += carrol_grades[i]
carrol_avg = carrol_avg / len(carrol_grades)
student_avg.append(carrol_avg)

for i in range(len(david_grades)):
	david_avg += david_grades[i]
david_avg = david_avg / len(david_grades)
student_avg.append(david_avg)

for i in range(len(emma_grades)):
	emma_avg += emma_grades[i]
emma_avg = emma_avg / len(emma_grades)
student_avg.append(emma_avg)

# FETCH THE LETTER GRADE OF EACH STUDENT AVERAGE
# Multiple "if" statements if more students need added.  I did not use a dictionary or tuple here!
for i in range(len(grades)):
	if i == 0:
		if alice_avg < 60:
			continue
		elif alice_avg < 70:
			letter_grade[i] = "D"
		elif alice_avg < 80:
			letter_grade[i] = "C"
		elif alice_avg < 90:
			letter_grade[i] = "B"
		elif alice_avg <= 100:
			letter_grade[i] = "A"
		else:
			print("Your code has an error (score above 100")
			exit(0)
	elif i == 1:
		if bob_avg < 60:
			continue
		elif bob_avg < 70:
			letter_grade[i] = "D"
		elif bob_avg < 80:
			letter_grade[i] = "C"
		elif bob_avg < 90:
			letter_grade[i] = "B"
		elif bob_avg <= 100:
			letter_grade[i] = "A"
		else:
			print("Your code has an error (score above 100")
			exit(0)
	elif i == 2:
		if carrol_avg < 60:
			continue
		elif carrol_avg < 70:
			letter_grade[i] = "D"
		elif carrol_avg < 80:
			letter_grade[i] = "C"
		elif carrol_avg < 90:
			letter_grade[i] = "B"
		elif carrol_avg <= 100:
			letter_grade[i] = "A"
		else:
			print("Your code has an error (score above 100")
			exit(0)
	elif i == 3:
		if david_avg < 60:
			continue
		elif david_avg < 70:
			letter_grade[i] = "D"
		elif david_avg < 80:
			letter_grade[i] = "C"
		elif david_avg < 90:
			letter_grade[i] = "B"
		elif david_avg <= 100:
			letter_grade[i] ="A"
		else:
			print("Your code has an error (score above 100")
			exit(0)
	elif i == 4:
		if emma_avg < 60:
			continue
		elif emma_avg < 70:
			letter_grade[i] = "D"
		elif emma_avg < 80:
			letter_grade[i] = "C"
		elif emma_avg < 90:
			letter_grade[i] = "B"
		elif emma_avg <= 100:
			letter_grade[i] = "A"
		else:
			print("Your code has an error (score above 100")
			exit(0)
# DEBUG print(letter_grade)

# CHECK FOR HONORS OR ACADEMIC WARNINGS ON STUDENT AVERAGE.  I DID NOT USE DICTIONARIES OR TUPLES!
for i in range(len(grades)):
	if letter_grade[i] == "A":
		count_honor += 1
	elif letter_grade[i] == "D" or letter_grade[i] == "F":
		count_warning += 1


#print(david_avg, bob_avg, carrol_avg, david_avg, emma_avg)


#CLASS AVERAGE
# DEBUG print(f"student_avg=  {student_avg}")
class_avg = round(sum(student_avg) / 5, 1)



#FINDING HIGHEST SCORES FOR EACH STUDENT

for i in range(len(alice_grades)):
	if alice_grades[i] >= alice_highest:
		alice_highest = alice_grades[i]
#DEBUG print(f"Highet grade by Alice =  {alice_highest}\n\n\n")	

for i in range(len(bob_grades)):
	if bob_grades[i] >= bob_highest:
		bob_highest = bob_grades[i]

for i in range(len(carrol_grades)):
	if carrol_grades[i] >= carrol_highest:
		carrol_highest = carrol_grades[i]

for i in range(len(david_grades)):
	if david_grades[i] >= david_highest:
		david_highest = david_grades[i]

for i in range(len(emma_grades)):
	if emma_grades[i] >= emma_highest:
		emma_highest = emma_grades[i]

#FINDING LOWEST SCORES FOR EACH STUDENT

for i in range(len(alice_grades)):
	if alice_grades[i] < alice_lowest:
		alice_lowest = alice_grades[i]

for i in range(len(bob_grades)):
	if bob_grades[i] < bob_lowest:
		bob_lowest = bob_grades[i]

for i in range(len(carrol_grades)):
	if carrol_grades[i] < carrol_lowest:
		carrol_lowest = carrol_grades[i]

for i in range(len(david_grades)):
	if david_grades[i] < david_lowest:
		david_lowest = david_grades[i]

for i in range(len(emma_grades)):
	if emma_grades[i] < emma_lowest:
		emma_lowest = emma_grades[i]

#For final display
student_highest = [alice_highest, bob_highest, carrol_highest, david_highest, emma_highest]
student_lowest = [alice_lowest, bob_lowest, carrol_lowest, david_lowest, emma_lowest]



#Highest/Lowest total grades:

highest_grade = student_avg[-1]
lowest_grade = student_avg[-1]

for i in range(len(grades)):
	if student_avg[i] >= highest_grade:
		highest_grade = student_avg[i]
for i in range(len(grades)):
	if student_avg[i] < lowest_grade:
		lowest_grade = student_avg[i]




#print(f"length of grades:  {len(grades)}") # result: 5
#FINDING AVERAGE FOR EACH COLUMN

for i in range(len(grades)):
	HW1_list.append(grades[i][0])
HW1_avg = (sum(HW1_list) / len(grades))
# DEBUG print(f"HW1_avg = {HW1_avg}")		

for i in range(len(grades)):
	HW2_list.append(grades[i][1])
HW2_avg = (sum(HW2_list) / len(grades))

for i in range(len(grades)):
	Quiz1_list.append(grades[i][2])
Quiz1_avg = (sum(Quiz1_list) / len(grades))

for i in range(len(grades)):
	Exam1_list.append(grades[i][2])
Exam1_avg = (sum(Exam1_list) / len(grades))

for i in range(len(grades)):
	Quiz2_list.append(grades[i][4])
Quiz2_avg = (sum(Quiz2_list) / len(grades))



#FINDING HIGHEST SCORE IN EACH COLUMN

for i in range(len(grades)):
	if grades[i][0] >= HW1_highest:
		HW1_highest = grades[i][0]
#DEBUG print(f"Highest HW1 score =  {HW1_highest}")

for i in range(len(grades)):
	if grades[i][1] >= HW2_highest:
		HW2_highest = grades[i][1]

for i in range(len(grades)):
	if grades[i][2] >= Quiz1_highest:
		Quiz1_highest = grades[i][2]

for i in range(len(grades)):
	if grades[i][3] >= Exam1_highest:
		Exam1_highest = grades[i][3]

for i in range(len(grades)):
	if grades[i][4] >= Quiz2_highest:
		Quiz2_highest = grades[i][4]



#FINDING LOWEST SCORE IN EACH COLUMN

for i in range(len(grades)):
	if grades[i][0] < HW1_lowest:
		HW1_lowest = grades[i][0]
		# DEBUG:  print(f"HW1_lowest =  {HW1_lowest}")

for i in range(len(grades)):
	if grades[i][1] < HW2_lowest:
		HW2_lowest = grades[i][1]

for i in range(len(grades)):
	if grades[i][2] < Quiz1_lowest:
		Quiz1_lowest = grades[i][2]

for i in range(len(grades)):
	if grades[i][3] < Exam1_lowest:
		Exam1_lowest = grades[i][3]

for i in range(len(grades)):
	if grades[i][4] < Quiz2_lowest:
		Quiz2_lowest = grades[i][4]






"""		
		HW1_avg = round((grades[0][0] + grades[1][0] + grades[2][0] + grades[3][0] + grades[4][0] ) / 5, 1)
		#DEBUG print(HW1_avg)
		HW2_avg = round((grades[0][1] + grades[1][1] + grades[2][1] + grades[3][1] + grades[4][1] ) / 5, 1)
"""


print("\n\n\n")








print("BONUS PROBLEM\n\n")
print("=== GRADE REPORT SYSTEM ===\n")
print("Grade Table:")
# FORMAT:  names= 10 spaces.   HW1= 3 spaces.   HW2= 7 spaces.   "Quiz1 "= 9 spaces.   "Exam1 "= 6 spaces.   
print(" " * 10, "HW1", "    HW2", "    Quiz1 ", " Exam1 ", " Quiz2   ", "AVG    ", "Grade     ", sep="")
print("- " * 30)

# All students have same number of graded items.
for i in range(len(grades)):
	print(f"{student_names[i]:<6}", end="")
	for j in range(len(grades[i])):
		print(f"{grades[i][j]:>7}", end="")
	print(f"     {student_avg[i]}", end="   ")
	print(f"{letter_grade[i]}")
print("# ## ##" * 3)
print(" # ## #" * 3)
print("\n\nGrade Analysis:")
print(f"\nNumber of students on Honor Roll (90%+):          {count_honor}")
print(f"Number of students on Academic Warning (<70%):    {count_warning}\n")

print(f"Class average:      {class_avg}%\n")

print(f"Highest Grade:      {highest_grade}%")
print(f"Lowest Grade:       {lowest_grade}%")

print("\nHighest/Lowest score:")
for i in range(len(grades)):
	print(f"Student {i+1}:")
	print(f"\tAverage grade:  {student_avg[i]}%")
	print(f"\tHighest grade:  {student_highest[i]}%")
	print(f"\tLowest grade:   {student_lowest[i]}%")

print("\nHW1 Analysis:")
print(f"\tAverage score:   {HW1_avg}%")
print(f"\tHighest score:   {HW1_highest}%")
print(f"\tLowest score:    {HW1_lowest}%")

print("\nHW2 Analysis:")
print(f"\tAverage score:   {HW2_avg}%")
print(f"\tHighest score:   {HW2_highest}%")
print(f"\tLowest score:    {HW2_lowest}%")

print("\nQuiz1 Analysis:")
print(f"\tAverage score:   {Quiz1_avg}%")
print(f"\tHighest score:   {Quiz1_highest}%")
print(f"\tLowest score:    {Quiz1_lowest}%")

print("\nExam1 Analysis:")
print(f"\tAverage score:   {Exam1_avg}%")
print(f"\tHighest score:   {Exam1_highest}%")
print(f"\tLowest score:    {Exam1_lowest}%")

print("\nQuiz2 Analysis:")
print(f"\tAverage score:   {Quiz2_avg}%")
print(f"\tHighest score:   {Quiz2_highest}%")
print(f"\tLowest score:    {Quiz2_lowest}%\n\n")
















