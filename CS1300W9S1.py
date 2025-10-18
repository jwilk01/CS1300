# Joseph Wilk
# CS 1300 Computer Science I
# 2025-10-16 Thursday
# Lab and notes


# PROFESSOR explains there is a need for test-taking skills as only opposed to knowing the material.




#    LOOPS
# Loops have scalability =  the same line of code can print 100 or 10,000 lines of code.


for cookie_number in [1,2,3,4,5]:
	print(f"Cookie {cookie_number}: $2.50")


count = 5
while count < 0:
	print("Hello")
	count -= 1

print("\n\n")


# NOTE: the variable "number01" is used just for iterating through the loop
number_list = [1,2,3,4,5,6,7]
for number01 in number_list:
	print("Hello")
print("\n")

#    The    loop-variable    topic is complex.

for i in [1,2,3,4,5,6,7]:
	print(f"Day {i}")


#   for     keyword signals start of loop
#   item    holds current value
#   in  keyword    connects variable to sequence
#   Sequence       collection of items to iterate over
#   :              marks start of loop body
#   INDENTED BLOCK 		code that repeats


# NOTE in python3.9 that there is an   ELSE   clause attached to the loop:

# If you put fruits instead of i then the whole list prints
fruits = ["apples", "bananas", "kiwi", "oranges", "grapefruit"]
for i in fruits:
	pass   #  There is no error in code, so this is ignored.
	if i == "bananas":
		continue    # The loop continues to the next iteration.
	print(i)
	if i == "oranges":
		print(i)
		break   # The loop ends here and grapefruit is not printed.
else:
	print("This is not printed if the \"break\" statement is present in loop")



# If the loops are not indented properly, you get an ERROR.

# This is just strictly index 0 to 9:

for i in range(10):
	print(i + 1)    # This prints 1 to 10, from index 0.








# LAB EXERCISE


print("\n\nLAB EXERCISE")
numbers = [12, 5, 18, 3, 20, 7]
for i in numbers:
	print(i)
	if i > 10:
		print("big")
	elif 5 <= i <= 10:
		print("medium")
	else:
		print("small")

print("\n")
for i in range(10):
	print(i + 1)    # This prints 1 to 10, from index 0.
for i in range(5):
	print(i)


# RANGE is very common to use in python3.
print("\n")
for i in range(0, 10, 2):
	print(i)
for i in range(10, 0, -1):
	print(i)














