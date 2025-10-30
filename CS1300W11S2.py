# Joseph Wilk
# CS1300
# W11S2 Oct 30 2025



# In Python, you must define a function FIRST, then call it.  Is not true in every programming language.

def wake_up(day):
	print("--------")
	print(f"Wake up at 7:00 on {day}")

print(wake_up("Monday"))
print(wake_up("Tuesday"))
print(wake_up("Wednesday"))

def say_hi():
	print("Hi")

say_hi()

def shape_1(times):
	for i in range(times):
		print("+--------+")
		
def shape_2(times):
	for i in range(times):
		print("|        |")

print("\n\n\n")
shape_1(1)
shape_2(2)
shape_1(1)


def print_star():
	print("*")

print_star()
print_star()

def compliment():
	print("You are great!")

compliment()
print("\n\n")


# Multiple values (dynamic typing) can be used in the same function like ints or strings for example.

def add_numbers(x, y): # Two parameters
	result = x + y
	print(f"{x} + {y} = {result}")
add_numbers(3, 5)


#Python uses snake case.  Java uses camel case.


def greet(name):
	print(f"Hello, {name}!")
greet("Joseph")

def times_two(number):
	result = number * 5
	print(result)
times_two(5)

def introduction(first_name, last_name, age):
	print(f"Hi, I'm {first_name} {last_name}, and I'm {age} years old.")
introduction("Joseph", "Wilk", 18)

# A lot of people write Python functions but forget to include a "return" value, says Professor.




def calculate_tax_good(price):
	tax = price * 0.08
	total = price + tax
	return total

# Now we can use it!
bill = calculate_tax_good(100)
print(f"Your bill is ${bill}")

# Can use in calculations
total_bill = calculate_tax_good(50) + calculate_tax_good(30)
print(f"Combined total: ${total_bill}")



def add_five(n):
	answer = n + 5
	return answer

print(add_five(10))

def is_even(n):
	if (n % 2) == 0:
		return True
	else:
		return False

user_even_number = int(input("Please enter an integer if it is EVEN:  "))
print(is_even(user_even_number))

#ADVANCED:  answer is that there is no "return" statement in the program.










