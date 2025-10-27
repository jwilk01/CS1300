# Joseph Wilk
# CS1300
# Week 11 Session 1
# Oct 27 2025 Monday



# Section 1
#Quiz
#  #1  prints 1 and 2 not 0
#  #2  prints 0 only

numbers = [1, -3, 4, 5, -7, 8, 9]
for num in numbers:
	if num > 0:
		if num % 2 == 1:
			print(num)

print("\n")
#Print only the first positive number divisible by 3
numbers = [1, -6, 7, 9, -12, 4]
result = None
for num in numbers:
	if num < 0:
		continue
	if num % 3 == 0:
		print(num)
		break



# Section 2

colors = ["red", "blue"]
sizes = ["S", "M", "L"]
for c in colors:
	for s in sizes:
		print(f"Color: {c}.  Size: {s}")

counter = 0
for n in range(1, 5):
	for y in range(1, 5):
		counter += 1
		print(f"{counter} ", end="")
		if counter % 4 == 0:
			print("\n", end="")

#Find number pairs that add up to 10.  There is an incorrect way to do this that looks similar to the correct below:
numbers = [2, 7, 3, 8, 5]
for i in range(len(numbers)-1):
	for j in range(i+1, len(numbers)):
		if numbers[i] + numbers[j] == 10:
			print(f"({numbers[i]}, {numbers[j]}) = 10")



# Section 3

rows = ["A", "B", "C"]
seats = [1, 2, 3, 4]
for i in range(len(rows)):
	for j in range(len(seats)):
		print(f"{rows[i]}{seats[j]}", end=",")
	print()





x = 1
for i in range(4):
	for j in range(i + 1):
		print(f"{x}", end=' ')
		x += 1
	print()



# Section 4

text = "Hello World 2024!"
uppercase_only = ""
for char in text:
	if char.isupper():
		uppercase_only += char
print(uppercase_only)

# Calculate sum of even numbers and product of odds
numbers = [2, 3, 4, 5, 6]
even_sum = 0
odd_product = 1
for num in numbers:
	if num % 2 == 0:
		even_sum += num
	else:
		odd_product += num
print(f"{even_sum} {odd_product}")




