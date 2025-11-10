# Joseph Wilk
# CS1300
# Nov 10, 2025
# Week 13 Session 1


# First In, Last Out.  The stack and the way it works is a limitation of functions.  

# Python used to be a scripting language.  Older versions used to be able to retrieve data from removed "plates" of nested functions.

# RECURSIVE FUNCTION: a function that calls itself.  We will talk about this much more in CS1350.

# The nested functions work just like in BASH and Java.


# SECTION 1:
# 1) prints:  A,  C,  then B

# 2) stack:  [f1, f2, f3 prints]

# 3) Recursion:  when n = 0, then the function is no longer called and the program continues.
     #  The n<= 0 is the "base case", to keep function from endlessly looping, and is what makes recursion very powerful says PROF.  There is "overhead" in recursion where you can manipulate the stack layers.
	 # If you are doing the factorial of a million, the overhead will be a problem through recursion and you will run out of memory or take 20 minutes if you execute it.  You want to be cautious when using recursion.
	 




# LOCAL VARIABLES:  is like Vegas:  what happens within a function stays in the function.  There can be local variables with the same names in different functions and they will be independent of each other, as long as they
# are defined within the different functions and not from a lower layer of functions or from the base.

# SECTION 2

def test():
	x = 5
	print(x)
	
test()

# It prints "5"

#Fixed errors.
def calculate():
	result = 10 * 2
	return result
# Fix: make result available outside
result_1 = calculate()
print(result_1) # Currently errors - fix it!

# THIS CODE HERE WORKS!  WHAT HAPPENS IN THE FUNCTION STAYS THERE!  "name" works only in the function since there is no "global" keyword used.
def get_user_name():
	name = input("Enter your name: ")
	return name
name = get_user_name()
print(f"Hello, {name}")





# "Overshadowing" = a local variable is defined in a function with the same name as a global variable name.  The local variable trumps the global variable and the global variable remains unchanged when 
# the main layer is executed again.


x = "global"
def outer():
	x = "outer"
	def inner():
		print(x)
	inner()
outer() # What prints and why?
# "outer" is printed because outer overshadows the value "global"

count = 1
def update_counter():
	count = 10 # This shadows the global count
	print(f"Local count: {count}")
update_counter()
print(f"Global count: {count}")
# It first prints 10, then prints 1.  The local variable overshadowed the value of 1, and the 1 value remains unchanged as the function exits.



# "global" keyword allows you to modify the variable from within a function as well.  You CAN define a global within a function.

x = 10
def change_x():
	global x
	x = 20
print(x) # This prints 10
change_x()
print(x) # This prints 20


balance = 1000

def withdraw(amount):
	# Modify to update global balance
	global balance
	# Should reduce balance by amount
	balance = balance - amount
	pass

withdraw(100)
print(balance)


count_2 = 0

def increment(count_2):
	count_2 += 1
	return count_2

print(increment(count_2))



# SECTION 5
#  1) From the "B" level
#  2) It prints at the "E" level.
#  3) below:
print("Hello")
hw = "Hello World!"
print(hw)
def hello_world():
	hw = "Enclosing"
	print(hw)
	def hello_world_2():
		print(hw)
		def hello_world_3():
			global hw
			hw = "HeLlO WoRlD global"
		hello_world_3()
	hello_world_2()
hello_world()
print(hw)	


