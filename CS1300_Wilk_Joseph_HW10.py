# Joseph Wilk
# CS 1300
# HW 10
# Dec 4, 2025




list_numbers = []
stat_min = 0
stat_max = 0
stat_avg = 0
stat_range = 0

def get_numbers():

	numbers = []
# Your code here
# Use input(), float() conversion
# Handle 'done' to stop
	while True:
		numbers.append(input("ENTER a number (or 'done'):  "))
		if numbers[-1].lower() == "done":
			break
			numbers[-1].float()
	del numbers[-1]
	print(f"Your numbers list:  {numbers}")
	return numbers


def calculate_stats(numbers):
	user_min = min(numbers)
	user_max = max(numbers)
	user_avg = int((sum(numbers))/len(numbers))
	user_range = user_max - user_min
	return user_min, user_max, user_avg, user_range
	
	
#def format_stats(minimum, maximum, average, range_val):

# Use round() for 2 decimal places
# Create formatted output string

def main():
	while True:
		print("=== Statistics Calculator ===\n\nMENU\n---------------\n")
# Call functions in order:
# 1. Get numbers
# 2. Calculate stats
# 3. Format output
# 4. Display result
		print("1:  Get numbers")
		print("2:  Calculate stats")
		print("3:  Format output")
		print("4:  Display result")
		user_menu = int(input("ENTER a number 1-4:  "))
		if user_menu < 1 or user_menu > 5:
			continue
		if user_menu == 1:
			list_numbers = get_numbers()
			continue
		if user_menu == 2:
			stat_min, stat_max, stat_avg, stat_range = calculate_stats(list_numbers)
			continue
		if user_menu == 3:
			continue
			


list_numbers = get_numbers()
print(list_numbers)







user_student_list = []
user_student_count = 0
student_scores = []
student_letters = []

def validate_score(score):
	valid = True
# The code already converts user input to INT, but this would be error-checking
	if isinstance(score, int) != True:
		print("You did not enter a valid data type (int only)!")
		valid = False
	if score < 0 or score > 100:
		print("You did not enter a valid score (0-100)!")
		valid = False
	return valid


def get_valid_score():
	temp_scores = [0,0,0]
	for j in range(3):
		while True:
			temp_scores[j] = (int(input(f"ENTER score #{j+1}:  ")))
			valid = validate_score(temp_scores[j])
			if valid == False:
				continue
			break
	return temp_scores

def calculate_letter():
	global student_scores
	temp_letters = []
	# DEBUG print(student_scores)
	# DEBUG print("Above is student scores.")
	for i in range(3):
		# DEBUG print(student_scores[i])
# LIST COMPREHENSION
		temp_letters.append(
		"F" if student_scores[i] < 60 else "D" if student_scores[i] < 70 
		else "C" if student_scores[i] < 80 else "B" if student_scores[i] < 90
		else "A"
		)
	return temp_letters


def process_student():
	global user_student_count
	global user_student_list
	global student_scores
	global user_student_list
# Use helper functions
# Get name and 3 scores
# Calculate and return results
	for i in range(user_student_count):
		student_name = input(f"Enter NAME of student {i+1}:  ")
		student_scores = get_valid_score()
		student_letters = calculate_letter()
		user_student_list.append([student_name, student_scores, student_letters])
	print(f"user_student_list =  {user_student_list}")
	print(student_letters)
def display_report(student_list):
	print("GRADE REPORT:")
	for i in range(len(student_list)):
		print(f"Name:     {student_list[i][0]}.")
		for j in range(3):
			print(f"Score 1:  {student_list[1][j+1]} {student_list[2][j+1]}")
			print(f"Score 2:  {student_list[1][j+1]} {student_list[2][j+1]}")
			print(f"Score 3:  {student_list[1][j+1]} {student_list[2][j+1]}")
			print("\n___________________________________")
		print()
			

# Format nicely with student info
def main():
	global user_student_count
	print("Welcome to Student Grade Processor!")
	user_student_count = int(input("ENTER the number of students in classroom:  "))
	
	
# Ask how many students
# Process each student
# Optional: Calculate class average


main()
process_student()
display_report(user_student_list)












