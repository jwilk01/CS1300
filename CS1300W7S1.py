#Joseph Wilk
#CS1300
#Week7 Session1



# In Python, "elements" can be of  ANY  type, unlike most other programming languages.  You can have a list of mixed elements in Python.
# A VERY IMPORTANT CONCEPT IN PYTHON  ===  A LIST CAN BE EMPTY !!!!!  IS VERY SPECIAL IN PYTHON.  WE CAN COMPARE IN TWO WAYS:
	#  IF A LIST HAS AN ELEMENT (with length of 0)  empty_list = []
	#  LISTS CAN CONTAIN LISTS.   nested = [[1,2], [3,4]]  This here is a 2d matrix.  

#   student_list = [1,3,5]
#   student_list[0] is equal to 1.  
#			      <-- there can only be one number here, as this is for a 1d array. two_d_array[0,4] is a 2d matrix.



# Create a list called 'colors' with three color names
# Your code here:
# Create a list called 'numbers' with the values 10, 20, 30
# Your code here:
# Print both lists

#1a
color_list = ["red", 'blue', "green"]
number_list = [1,20,19]
print(color_list, number_list)


# Create a list called 'my_info' that contains:
# - Your name (string)
# - Your age (integer)
# - Your height in feet (float)
# - Whether you like pizza (boolean)
# Your code here:
# Print the entire list
# Print the type of the list itself
list_2a = ["Joseph", 18, 71.2, True]
print(list_2a)
print(type(list_2a))



# Given this list:
inventory = ["pen", "pencil", "eraser", "ruler", "notebook"]
# Without using loops (not covered yet):
# 1. Print how many items are in inventory
# 2. Check if "pencil" is in the list (print True/False)
# 3. Create a new list with the first and last items only
# Hint: Use len(), in operator, and indexing
print(len(inventory))
# NOT this:  print(inventory.find("pencil"))
#

#

print("pencil" in inventory)
#

#

inventory_2 = [inventory[0], inventory[-1]]   #Remember that this points to the heap location of the   inventory   list.  
print(inventory_2)





# PYTHON STRINGS ARE    IMMUTABLE !!!!!  You cannot change the value of strings.  You must create a new object, with all variables in python being objects.
# name = "Alice"
# name[0] = "B"  # THIS WILL CAUSE AN ERROR !!!


# Mutable types are lists and dictionaries and sets.
# names = ["Alice", "Bob"]
# names[0] = "Charlie"   # This will edit the actual ***reference*** of memory, eliminating "Alice".

# x = 5
# x = x + 1  # this will give you 6 and replaces the old value


# For each variable, predict if it's mutable or immutable:
a = 42 # Mutable or Immutable?
# immutable
b = "Python" # Mutable or Immutable?
# immutable
c = [1, 2, 3] # Mutable or Immutable?
# mutable
d = 3.14 # Mutable or Immutable?
# immutable
e = True # Mutable or Immutable?
# immutable
# Test your predictions by trying to change them



# Create a string variable called 'greeting' with value "Good"
# Try to add " Morning" to it two ways:
# 1. Using + (creating new string)
# 2. Try to modify the first character to 'F' (will fail)
# Create a list called 'temps' with values [72, 75, 78]
# 1. Change the first element to 70
# 2. Print to verify it changed

variable = "Morning"
variable = "Good " + variable
# This will fail!   variable[0] = "A"
print(variable)

temps = [72, 75, 78]
temps[0] = 70
print(temps)


#UNDERSTANDING ALIASING

# Predict what will print:
original = [10, 20, 30]
copy1 = original
copy2 = original
copy1[1] = 200
copy2[2] = 300
# What are the values of:
# original?
# copy1?
# copy2?
# Explain why


from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
print(from_string)

# THIS IS VERY INTERESTING
zeros = [0] * 5
print(zeros)


grid = [[1,2],[3,4],[5,6]]
print(grid)



#NAMING CONVENTION
#When naming a list, use a plural ending with  's'  like students or numbers or names.  NOT 's' 'temp' 'stuff'


# THE TWO LINES OF CODE DO THE SAME THING
empty1 = []
empty2 = list()

letters = list("PYHTON")  # ["P", "Y", "T", "H", "O", "N"]
print(letters)



#3a
# Create these lists:
# 1. An empty list called 'tasks'
# 2. A list of three pets: "dog", "cat", "fish"
# 3. A list of temperatures: 72.5, 68.0, 75.3
# 4. Print all three lists
tasks = []
pets = ["dog", "cat", "fish"]
temperatures = [72.5, 68.0, 75.3]
print(tasks, pets, temperatures)


#3b
# Create these lists:
# 1. Use list() to convert the string "HELLO" to a list
# 2. Create a list of five 7's using repetition
# 3. Create a list mixing your name, age, and favorite color
# 4. Create a 2x2 nested list representing a tic-tac-toe board
greetings = list("HELLO")
sevens = [7] * 5
demographics = ["Joseph", 18, "Green"]
tic_tac_toe_list = [['x', 'o', 'x'],['x','x','o'],['x','o','o']]
print(greetings,sevens,demographics)
print(tic_tac_toe_list[0])
print(tic_tac_toe_list[1])
print(tic_tac_toe_list[2])


# Without using loops:
# 1. Create a list of the first 10 even numbers (use range and list)
# 2. Create a checkerboard pattern: [0,1,0,1,0,1]
# 3. Create a list that contains three empty lists
# 4. Create a list from the string "1,2,3" that gives [1, 2, 3]
# Hint for #4: Use split() then convert strings to integers manually
#evens = [0,2,4,6,8,10,12,14,16,18]  NOT THIS
#
#empty_lists = []*3 NOT THIS
#print(empty_lists)
#list_threes = list("123")
#print(list_threes)









fruits = ['apples','bananas','oranges','grapes']
# INDEX   -4        -3       -2        -1
# fruits[-1] is 'grapes'
# YOU CAN MODIFY ELEMENTS

"""
if len(my_list) > 0:
	first = my_list[0]
this is so that if your list does not have any values, we do not always know.
"""









# Given this list:
animals = ["cat", "dog", "bird", "fish", "hamster"]
# Using indexing, print:
# 1. The first animal
# 2. The last animal
# 3. The middle animal (bird)
# 4. Change "dog" to "puppy" and print the list
print(animals[0], animals[-1], animals[int((len(animals))/2)])
animals[1] = "puppy"
print(animals)

# Given this list:
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# Using ONLY negative indices:
# 1. Print the last month
# 2. Print the first month
# 3. Change the second-to-last month to "MAY"
# 4. Print the third-from-last month
print(months[-1])
print(months[-6])
months[-5] = "MAY"
print(months[-3])
print(months)

# Given these lists:
list1 = [10, 20, 30, 40, 50]
list2 = []
list3 = [100]
# Write code to:
# 1. Safely print the first element of each list (handle empty)
# 2. Safely change the last element to 999 (if it exists)
# 3. Swap first and last elements of list1
# 4. Calculate the middle index of list1 and print that element
if len(list1) > 0:
	print(list1[0])
	list1[-1] = 999
	temp_list1 = [0]
	temp_list1[0] = list1[0]
	list1[0] = list1[-1]
	list1[-1] = temp_list1[0]
	print(list1[int((len(list1))/2)])
if len(list2) > 0:
	print(list2[0])
	list2[-1] = 999
	temp_list2 = [0]
	temp_list2[0] = list2[0]
	list2[0] = list2[-1]
	list2[-1] = temp_list2[0]
if len(list3) > 0:
	print(list3[0])
	list3[-1] = 999
	temp_list3 = [0]
	temp_list3[0] = list3[0]
	list3[0] = list3[-1]
	list3[-1] = temp_list3[0]
	
	




# how to reverse a list=
# numbers[::-1]

# copy = numbers[:]  # This creates a complete copy of the list













