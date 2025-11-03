# Joseph Wilk
# CS1300
# Week 12 Session 1
# Nov 3, 2025


# Default parameters are somewhat advanced feature of Python3.  Sometimes you want a parameter to have a default.
"""
def greet(name="Guest"):
	print(f"Hello, {name}!")
"""
# If you call nothing, the name "Guest" will be used.  You can have multiple default parameters.

"""
#
#
#
# CORRECT: Regular params first, then defaults   # # # # #
#
#
#
def order_coffee(size, flavor="regular", temp="hot"):
	print(f"{temp} {size} {flavor} coffee")
# WRONG: Default before regular
def bad_function(x=10, y): # ERROR!
	return x + y
"""

# UNIT 1

def multiply(a, b, c):
	return(a * b * c)
print(multiply(2, 3, 4))


# Define function
def format_date(mon, day, year):
	return(f"{mon}/{day}/{year}")
# Handle single-digit months/days with leading zero
print(format_date(5, 3, 2024)) # Should print "03/05/2024"
print(format_date(15, 12, 2024)) # Should print "12/15/2024"


# UNIT 2

def welcome(name="Student"):
	print(f"Welcome, {name}!")
welcome(input("Enter your first name:  "))


def power(base, exp = 1): # Add default here
	return base ** exp
print(power(5)) # Should print 25 (5²)
print(power(5, 3)) # Should print 125 (5³)


def calculate_discount(price, discount=10, tax=8):
	# Calculate discounted price with tax
	discounted = price * (1 - discount/100)
	final = discounted * (1 + tax/100)
	return final
print(calculate_discount(50))


# UNIT 3

def divide(dividend, divisor):
	return dividend / divisor
print(divide(dividend = 20, divisor = 4))

"""
UNIT 3 ADVANCED:

def process(a, b, c):
return a + b + c
# Why does this fail?
result = process(a=1, 2, c=3) # SyntaxError!

It fails because the value b is supposed to be placed before a=1 and c=3
"""


# UNIT 4
def greet(first, last="User", title=""):
	print(f"{title} {first} {last}")
greet(first="John")
greet("John", "Doe", "Mr.")

#Beginner questions: A, B, AND C ARE CORRECT.
#INTERMEDIATE:
def configure_game(width, height, fullscreen=False,
	volume=50, difficulty="normal"):
	pass
configure_game(800, 600, fullscreen=True, volume=75, difficulty="hard")

#ADVANCED:
def print_info(name, age=18, city="New York", job="Computer Technician"):
	print(f"Name: {name}, age: {age}, city: {city}, job: {job}")
# Print any extra keyword arguments
print_info("Alice", age=25, city="Boston", job="Engineer")











