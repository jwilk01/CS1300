# Joseph Wilk
# CS1300
# 2025-10-30
# Week 10 Homework

import random


print("\n\n*****\nProblem 1:  \n")

temperatures = [72, 68, 75, 71, 69, 77, 74, 70, 73, 76]
sum = 0
avg_temp = 0
highest_temp = temperatures[-1]
lowest_temp = temperatures[-1]
days_above_72 = 0
#loop_high_temperature = 0

#From previous HMWK
#temp_conversion = round(((temp - 32) / 1.8), 2)
#temp_conversion = round(((temp * 1.8) + 32), 2)

#AVERAGE TEMP LOOP
for i in range(len(temperatures)):
	sum += temperatures[i]
else:
	avg_temp = sum / len(temperatures)
	#print(avg_temp)

#HIGHEST TEMP LOOP (DEBUG)
"""
for i in range(len(temperatures)):
	highest_temp = temperatures[i]
	for j in range(len(temperatures)):
		if temperatures[j-1] <= highest_temp:
			continue
		else:
			highest_temp_j = temperatures[j-1]
		
else:
	print(f"highest temp: {highest_temp}.  Highest temp j:  {highest_temp_j}")
"""
#HIGHEST TEMP LOOP:
for i in range(len(temperatures)):
	if temperatures[i] >= highest_temp:
		highest_temp = temperatures[i]	
#else:
#	print(f"Highest temperature: {highest_temp}")


#LOWEST TEMP LOOP:
for i in range(len(temperatures)):
	if temperatures[i] < lowest_temp:
		lowest_temp = temperatures[i]
#print(f"Lowest temp: {lowest_temp}")


#DAYS ABOVE 72°
for i in range(len(temperatures)):
	if temperatures[i] > 72:
		days_above_72 += 1
#print(f"days above 72:  {days_above_72}")


#DISPLAY
for i in range(len(temperatures)):
	#temp_celsius is not needed as a list, can be replaced for the display.
	temp_celsius = round(((temperatures[i] - 32) / 1.8), 2)
	#DEBUG: print(temp_celsius)
	print(f"Day {i+1}:  {temperatures[i]}°F, {temp_celsius}°C")
print("\nSTATISTICS")
print(f"Highest temperature:  {highest_temp}°F")
print(f"Lowest temperature:   {lowest_temp}°F")
print(f"Average temperature:  {avg_temp}°F")
print(f"Days above 72°F --- {days_above_72}")
input("\nPress ENTER to continue:  ")
print("\n\n\n")






print("Problem 2:\n")

random_number = random.randrange(1, 21)
guesses = 0
guess_list = []
#print(random_number)
print("You have 5 chances to guess a number between 1 and 20.")
for i in range(1, 6):
	user_guess = int(input(f"Guess #{i}:  "))
	guess_list.append(user_guess)
	guesses += 1
	if user_guess == random_number:
		if guesses == 1:
			print("Amazing! You're a mind reader!")
			print(f"Your guesses:  {guess_list}")
		elif guesses == 2 or guesses == 3:
			print("Good job!")
			print(f"Your guesses:  {guess_list}")
		else:
			print("Good work!")
			print(f"Your guesses:  {guess_list}")
		break
	if user_guess > random_number:
		print("Your guess is too HIGH.  Try again.")
		continue
	if user_guess < random_number:
		print("Your guess is too LOW.  Try again.")
		continue
else:
	print(f"Unfortunately, you did not guess the correct number \"{random_number}\".")
	print(f"Your guesses:  {guess_list}")
	print("Better luck next time!")
input("\nPress ENTER to continue:  ")
print("\n\n\n")






print("Problem 3:\n\n")

grades = [85, -10, 92, 150, 78, 0, 95, 88, -5, 100, 73, 200]
valid_grades = []
letter_grade = "F"
invalid_count = 0
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0
grades_sum = 0
avg_grade = 0

print("PROCESSING GRADES..\n")
for i in range(len(grades)):
	if grades[i] < 0 or grades[i] > 100:
		print(f"SKIPPING INVALID GRADE \"{grades[i]}\"")
		invalid_count += 1
		continue
	if grades[i] >= 90:
		letter_grade = "A"
		a_count += 1
	elif grades[i] >= 80:
		letter_grade = "B"
		b_count += 1
	elif grades[i] >= 70:
		letter_grade = "C"
		c_count += 1
	elif grades[i] >= 60:
		letter_grade = "D"
		d_count += 1
	else:
		letter_grade = "F"
		f_count += 1
	print(f"Grade {i+1}:  {grades[i]} ({letter_grade})")
	valid_grades.append(grades[i])

print("\nSUMMARY REPORT:\n============")
print(f"Total grades processed:  {len(grades)}")
print(f"Total grades skipped:    {invalid_count}\n")
print("Grade Distribution:")
if a_count != 1:
	print(f"A:  {a_count} students.")
else:
	print(f"A:  {a_count} student.")
if b_count != 1:
	print(f"B:  {b_count} students.")
else:
	print(f"B:  {b_count} student.")
if c_count != 1:
	print(f"C:  {c_count} students.")
else:
	print(f"C:  {c_count} student.")
if d_count != 1:
	print(f"D:  {d_count} students.")
else:
	print(f"D:  {d_count} student.")
if f_count != 1:
	print(f"F:  {f_count} students.")
else:
	print(f"F:  {f_count} student.")

for i in range(len(valid_grades)):
	grades_sum += valid_grades[i]
avg_grade = round(grades_sum / len(valid_grades), 2)


print(f"\nClass Average:  {avg_grade}")




