# Joseph Wilk
# CS1300
# Week 14 Session 2
# Nov 20, 2025




# You can have multiple data types in a TUPLE.   (10,)  = correct syntax for a TUPLE.
#												 (10)   = integer

# TUPLES ARE IMMUTABLE!  This prevents accidental modifications.

# (month, day, year)  the dates cannot change in a TUPLE.  (255, 0, 0)  RGB values cannot change, good for tuples.

# PROF says twice the way tuples are notated are against intuition.

locations = []
locations.append((10, 20))
locations.append((30, 40))
print(locations)  # [(10, 20), (30, 40)]

weird_tuple = ([1, 2, 3], "fixed text")
weird_tuple[0].append(4)
print(weird_tuple)  # ([1, 2, 3, 4], 'fixed text')

# The double-indexing of tuples is like the 2D arrays from Java:  weird_tuple[0][3] brings 4.  first number is the row, second number is the column.


# A HUGE advantage of Python is not needing a "temp" variable for SWIPPING:
"""
a = 10
b = 20
# Traditional swap needs temporary variable
temp = a
a = b
b = temp

# Tuple swap is elegant
a, b = b, a # Swap in one line!
"""
#
#
#

# BEGINNER
rgb_color = (255, 128, 0)
print(f"Red channel = {rgb_color[0]}")
print(f"Green channel = {rgb_color[1]}")
print(f"Blue channel = {rgb_color[2]}")
palette = []
palette.append(rgb_color[0])
palette.append(rgb_color[1])
palette.append(rgb_color[2])
print(palette)

# INTERMEDIATE
student_records = (("John Doe", 12, 17), ("Jane Smith", 10, 16), ("Taylor Jones", 11, 16))
"""
student_records.append("John Doe", 12, 17)
student_records.append("Jane Smith", 10, 16)
student_records.append("Taylor Jones", 11, 16)
"""
classroom = []
classroom.append(student_records[0])
classroom.append(student_records[1])
classroom.append(student_records[2])
print(classroom)




# TUPLES ARE PASSED BY VALUE,
# LISTS ARE PASSED BY REFERENCE!

def add_bonus_safe(grades, bonus):
###Returns new list, keeps original safe
	return [grade + bonus for grade in grades]
scores = [85, 90, 78]
# GOES THROUGH FUNCTION TO ADD 5 POINTS TO EACH SCORE.  THE RESULT IS A CHANGED COPY OF THE LIST.
new_scores = add_bonus_safe(scores, 5)
print(new_scores)



def calculate_average(*numbers):
#Accepts 1, 2, 3, or more numbers
	if len(numbers) == 0:
		return 0
	return sum(numbers) / len(numbers)
avg1 = calculate_average(85)
avg2 = calculate_average(85, 90)
avg3 = calculate_average(85, 90, 78, 92)
print(avg3) # 86.25



print("\n=== Passing Lists to Functions ===")
def boost_grades(scores, bonus):
#Modifies original list
	for i in range(len(scores)):
		scores[i] += bonus
	print(f" Inside function: {scores}")

grades = [85, 90, 78]
print(f"Before: {grades}")
boost_grades(grades, 5)
print(f"After: {grades}") # Original changed!
print("\n=== Safe Function (Returns New List) ===")
def boost_grades_safe(scores, bonus):
#Returns new list
	return [score + bonus for score in scores]
original = [85, 90, 78]
print(f"Original: {original}")
boosted = boost_grades_safe(original, 5)
print(f"Boosted: {boosted}")
print(f"Original unchanged: {original}")



# UNIT 2
# BEGINNER
grades_2 = [91, 88, 86]
date_2 = (11, 20, 2025)

def boost_grades_2(scores, bonus):
	for i in range(len(scores)):
		print(scores[i])
		scores[i] += bonus
		print(scores[i])
	return scores

new_grades_2 = boost_grades_2(grades_2, 5)
print(new_grades_2)


# INTERMEDIATE
test_scores_2 = [3, 4, 5]
def calc_avg_2(*args):
	list = []
	print(args)
	if len(args) == 0:
		return 0
	for i in range(len(args)):
		list += args[i]
	calc_avg_2_tuple = ((min(list)), (max(list)))
	return calc_avg_2_tuple

tuple_2 = calc_avg_2(test_scores_2)
print(tuple_2)

#ADVANCED
def calculate_statistics_2c(*args):
# returns: count, sum, avg
# split
	print(f"args = {args}")
	avg = sum(args[1])/args[0]
# DEBUG	print(f"avg: {avg}")
	tuple = (args[0], args[1], avg)
	return tuple
	
	
	
#def update_student_records(old_tuple, bonus):
	
	
	

scores_2c = []  # this is for the three nested loops to filter non 0-100 scores.
loop_c = False
while True:
	count_2c = int(input("ENTER number of students (1-5):  "))
	if count_2c < 1 or count_2c > 5:
		continue
	break
while True:
	for i in range(count_2c):
#		THE FINAL DEBUG removing this -->  scores_2c = []
#		print(f"DEBUG start of \"for\" loop.  loop_c = {loop_c}")
		if loop_c == True:
			break
#		loop_c = False    # not needed in multiple places
		while True:
			if loop_c == True:
				break
#			print(f"loop_c = {loop_c}")
			loop_c = False
			scores_2c.append(int(input(f"ENTER the score of student {i+1} (0-100):  ")))
			if scores_2c[i] < 0 or scores_2c[i] > 100:
				scores_2c = []   # This helps restart user input for the i-number of scores.
				loop_c = True
				continue
#			print("DEBUG END OF LOOP C")
			break
		if loop_c == True:
			break
#		print("DEBUG END OF LOOP B")
	if loop_c == True:
		loop_c = False
		continue
#	print("DEBUG END OF LOOP A")
	break


tuple_2c_1 = calculate_statistics_2c(count_2c, scores_2c)
print(f"tuple_2c_1 = {tuple_2c_1}")
#bonus_2c = int(input("ENTER a bonus number (int):  "))
#tuple_2c_bonus = update_student_records(tuple_2c_1, bonus_2c)


"""
This is more Pythonic:
for row in grid:
	for value in row:
		print(value, end=' ')
	print() # New line after each row
"""

"""
This is more C/C++   INDEX-BASED:
for i in range(len(grid)):
	for j in range(len(grid[i])):
		print(grid[i][j], end=' ')
	print()
"""


squares = [x**2 for x in range(1, 6)]  # Done in one line!
print(squares)









# 3x3 multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# Result: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]



# WITH THE FIELD OF "BIG DATA",   PYTHON   IS A NATURALISTIC CHOICE


# List comprehension (greedy)
numbers_list = [x**2 for x in range(10)] # Creates entire list
# Generator expression (lazy)
numbers_gen = (x**2 for x in range(100)) # Creates generator
print(numbers_list)
print()
print(numbers_gen)



# LIST COMPREHENSION IS GOING TO BE IN THE FINAL.
# GENERATORS MIGHT BE ON THE FINAL
# 
# GENERATORS ARE USEFUL FOR LARGE SUMS
# GENERATORS ARE AN ADVANCED FEATURE OF PYTHON3.
# The generator tells you the location block of the generator.
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))


print("\n=== Memory Comparison ===")
import sys
big_list = [x for x in range(10000)]
big_gen = (x for x in range(10000))
print(f"List memory: {sys.getsizeof(big_list)} bytes")
print(f"Generator memory: {sys.getsizeof(big_gen)} bytes")
print(f"Generator saves: {sys.getsizeof(big_list) - sys.getsizeof(big_gen)} bytes")
# Generator useful for large sums
large_sum = sum(x**2 for x in range(100000))
print(f"\nSum of squares (0-99999): {large_sum}")




# UNIT 3
# BEGINNER

three_by_three = [[1,2,3],[10,11,12],[19,18,17]]
print(three_by_three)
print(len(three_by_three))
print(three_by_three[(len(three_by_three))//2][(len(three_by_three[0]))//2])  # MIDDLE VALUE 11
for i in range(len(three_by_three)):
	for j in range(len(three_by_three[0])):
		print(three_by_three[i][j], end=" ")
	print()	

# INTERMEDIATE
list_3b = [45, 78, 92, 61, 88, 73, 55, 90, 82]
passing_grades_3b = []
passing_grades_3b = [i for i in list_3b if i > 60]
print(passing_grades_3b)

passing_grades_3b_letter = ["D" if i < 70 else "C" if i < 80 else "B" if i < 90 else "A" for i in passing_grades_3b]
print(passing_grades_3b_letter)

# ADVANCED

table_3c = [[i * j for j in range(1, 5)] for i in range(1, 5)]
for i in range(len(table_3c)):
	for j in range(len(table_3c[0])):
		print(f"{table_3c[i][j]:4}", end="")
	print()



















