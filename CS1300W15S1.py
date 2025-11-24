# Joseph Wilk
# CS1300
# 2025-Nov-24
# Week 15 Session 1


numbers = [45, 12, 78, 34]
result = numbers.sort() # Returns None!
print(numbers) # [12, 34, 45, 78] - list is changed
print(result) # None

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# Sort by grade (second element)
students.sort(key=lambda student: student[1])  # 'student' is like a temp variable assigned to sort the list of tuples.
print(students) # Sorted by grade: Charlie, Alice, Bob

# UNIT 1
# BEGINNER
scores_1a = [78, 92, 85, 88, 75, 95, 82]
scores_1a.sort(reverse=True)
print(scores_1a)
index_1a = scores_1a.index(88)
print(index_1a) # Correctly prints the index as 2.


# INTERMEDIATE
list_1b = [("Emma", 88), ("Liam", 92), ("Olivia", 85), ("Noah",
95), ("Ava", 82)]
print(list_1b)
# sort by alphabetical order
list_1b.sort(key=lambda student: student[0])
print(list_1b)
# sort by grade in highest to lowest
list_1b.sort(key=lambda grade: grade[1], reverse=True)
print(list_1b)

#ADVANCED
list_1c = [19.95, 14.95, 9.95, 12.95, 100.00, 49.95, 5.00, 20.00, 26.70, 7.35]
print(min(list_1c), max(list_1c))
list_1c_sorted = sorted(list_1c)
print(list_1c_sorted)





#  DON'T FORGET ABOUT  ZIP  !!!!
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]
for name, score, grade in zip(names, scores, grades):
	print(f"{name}: {score} ({grade})")

combined = zip(names, scores)
print(f"Type: {type(combined)}")
print(f"zip on combined = {zip(names, scores)}")
combined_list = list(zip(names, scores))
print(f"Combined: {combined_list}")

# NOTE WHEN LIST LENGTHS ARE UNEVEN IN LENGTH!!
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c']
paired = list(zip(numbers, letters))
print(paired) # [(1, 'a'), (2, 'b'), (3, 'c')]
# Note: 4 and 5 are ignored!



#UNIT 2 LAB
# BEGINNER
list_2a = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
reversed_2a = reversed(list_2a)
print(reversed_2a)
names_2a = ['Alex', 'Beth', 'Carl']
ages_2a = [19, 20, 19]
for name, age in zip(names_2a, ages_2a):
	print(f"Name:  {name}____age = {age}")

#INTERMEDIATE
items_2b = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
prices_2b = [899.99, 25.99, 79.99, 299.99]
stock_2b = [5, 15, 8, 3]
total_value = 0
for item, price, stock in zip(items_2b, prices_2b, stock_2b):
	total_value += (price * stock)
	print(f"ITEM:__{item:9}    PRICE:__${price:7}    STOCK:__{stock:2}")
print(f"TOTAL VALUE OF ITEMS:  {total_value:.2f}")

#ADVANCED
def create_rankings(names, scores):
# THIS ONLY SORTS THE SCORES AND NOT THE LIST OF NAMES:
#	for name, score in zip(names, sorted(scores, reverse=True)):
# YOU CANNOT USE ENUMERATE BECAUSE IT ONLY ACCEPTS TWO ARGUMENTS NOT THREE.
# NOTE THE LAB ASKS FOR ZIP AND SORTED IN ONE LINE OF CODE:
	rank = 0
	list_rankings = []
	for name, score in sorted(list(zip(names, scores)), key=lambda s: s[1], reverse=True):
		rank += 1
		print(rank, name, score)
		list_rankings.append([rank, name, score])
# DEBUG	print(list_rankings)
	working_tuple = tuple(list_rankings)
	return working_tuple
		
names_2c = ["Larry", "Hilary", "Bob", "Alice", "Charlie"]
scores_2c = [88, 93, 81, 91, 94]
tuple_2c = create_rankings(names_2c, scores_2c)
print(tuple_2c)
	




#UNIT 3 LAB
#BEGINNER
temperatures_3a = [0, 10, 20, 30, 40]
# ROUND is functionless here but is how you include ROUND
converted_3a = list(map(lambda x: round((x * (9/5) + 32), 2), temperatures_3a))
print(converted_3a)
filtered_converted_3a = list(filter(lambda x: x > 50, converted_3a))
print(filtered_converted_3a)


#INTERMEDIATE
prices_3b = [12.99, 8.50, 15.75, 22.00, 9.99, 30.50, 5.25]
under_10_3b = list(map(lambda x: round(x * 1.1, 2), filter(lambda x: x < 10, prices_3b)))
print(under_10_3b)
print(sum(under_10_3b))
print(min(under_10_3b))
print(max(under_10_3b))


#ADVANCED










