# Joseph Wilk
# CS1300
# Oct 18 2025
# HMWK 6




# Example shown for you:
# Create a list of three colors
example_colors = ["red", "blue", "green"]
print("Example:", example_colors)
# Now you try:
# 1. Create a list called 'my_classes' with 4 class names (like "English", "Math",
#etc.)
my_classes = ["English", "Math", "Literature", "Programming"]
# 2. Create a list called 'my_grades' with 5 test scores (use any numbers between
#60-100)
my_grades = [97, 74, 92, 88, 90]
# 3. Create an empty list called 'my_notes'
my_notes = []
# 4. Print all three of your lists
print(my_classes, my_grades, my_notes)



# Lists can hold different types of data!
# 1. Create a list called 'about_me' with:
# - Your first name (string)
# - Your age (integer)
# - Your height in feet (decimal number like 5.5)
# - Whether you like pizza (True or False)
# 2. Create a list called 'mixed_bag' with:
# - The number 42
# - The word "Hello"
# - The value 3.14
# - Another list containing [1, 2, 3]
# 3. Print both lists

about_me = ["Joseph", 18, 5.67, True]
mixed_bag = [42, "Hello", 3.14, [1,2,3]]
print(about_me, mixed_bag)




zeros = [0] * 10
letters = list("HELLO")
pattern = [1, 2] * 3
print(zeros, letters, pattern)



months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
"Nov", "Dec"]
print("The list:", months)
print("List length:", len(months))
print(months[0])
print(months[5])
print(months[len(months) - 1])
print(months[-1])
print(months[11])
print(months[-12])




# # # # # # # # # # # # # # # # # # # # # # # #
print("\n\n\n")
# You're tracking daily temperatures for a week
temperatures = [72, 75, 71, 73, 74, 76, 70] # Sunday through Saturday
print("Original temperatures:", temperatures)
temperatures[1] = 77
print(temperatures[1])
temperatures[5] = 78
temperatures[0] = 74
temperatures[-1] = 72
temperatures[len(temperatures) - 1] = 75
print("Corrected temperatures:", temperatures)
print(f"There are {len(temperatures)} days in the week.")
print(temperatures[6])




print("\n\n\n")
# Given this small list:
colors = ["red", "blue", "green", "yellow"]
# 1. Check if index 1 exists before accessing it
if 1 < len(colors):
	print("Color at index 1:", colors[1])
else:
	print("Index 1 doesn't exist")
# 2. Now you try: Check if index 5 exists before trying to access it
# 3. Check if the list is empty before accessing the first element
# 4. Safely access the last element (check if list has at least 1 item first)
# 5. Try to print the element at index -4 (but check if it's valid first)
# Hint: negative indices from -len(list) to -1 are valid
# 6. What's the smallest valid negative index for this list? Print it.
if 5 < len(colors):
	print("Color at index 5:", colors[5])
else:
	print("Index 5 doesn't exist")
if 1 < len(colors):
	print(colors[-1])
else:
	print("Index 1 doesn't exist")
if 4 < len(colors):
	print(f"Index -4 is:  {colors[-4]}")
else:
	print("There are not 4 indexes in your color list.")
print(colors[-1])





print("\n\n\n")
# Slicing lets us get multiple elements at once!
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list:", numbers)
#print("Remember: list[start:end] gives elements from start up to \(but not
#including\) end")
# Example:
print("Example - numbers[0:3]:", numbers[0:3]) # Gets indices 0, 1, 2
# Now you try:
# 1. Get the first 4 numbers
print(numbers[0:4])
# 2. Get the last 3 numbers (use negative indices)
print(numbers[-3:])
# 3. Get numbers from index 2 to index 6 (30, 40, 50, 60)
print(numbers[2:7])
# 4. Get all numbers from index 5 to the end
print(numbers[5:])
# 5. Get all numbers from start up to index 4
print(numbers[:5])
# 6. Make a complete copy of the list using [:]
print(numbers[:])
# 7. Get an empty slice (like numbers[3:3]) and see what happens
print(numbers[5:5])





print("\n\n\n")
# We can use a step value: list[start:end:step]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
print("Alphabet:", alphabet)
# Example:
print("Every other letter:", alphabet[::2]) # Start to end, step by 2
# Now you try:
# 1. Get every third letter starting from 'a' (indices 0, 3, 6, 9, 12)
print(alphabet[::3])
# 2. Get every other letter starting from 'b' (indices 1, 3, 5, 7, ...)
print(alphabet[1::2])
# 3. Reverse the entire list using slicing (hint: use step of -1)
print(alphabet[::-1])
# 4. Get the first half of the alphabet
# Hint: Calculate middle index using len() // 2
print(alphabet[:((len(alphabet) - 1 ) // 2)])
# 5. Get the second half of the alphabet
print(alphabet[((len(alphabet) - 1 ) // 2):])
# 6. Get letters from index 2 to 8, but only every other one
print(alphabet[2:9:2])
# 7. Reverse just the first 5 letters (get them, then reverse)
print(alphabet[:5:-1])




print("\n\n\n")
# You have hourly temperature readings for a day (24 hours)
hourly_temps = [55, 54, 53, 52, 52, 54, 58, 62, 66, 70, 73, 75,
76, 77, 77, 76, 74, 71, 68, 65, 62, 59, 57, 55]
print(f"24-hour temperature data ({len(hourly_temps)} readings)")
# 1. Get morning temperatures (first 6 hours, 12am-5am)
print(f"First 6 hours: {hourly_temps[:6]}")
# 2. Get afternoon temperatures (12pm-5pm, which is indices 12-17)
print(f"12pm to 5pm:  {hourly_temps[12:17]}")
# 3. Get evening temperatures (last 6 hours, 6pm-11pm)
print(f"Last 6 hours:  {hourly_temps[-6:]}")
# 4. Get every other hour's temperature for the whole day
print(f"Every other temperature hour:  {hourly_temps[::2]}")
# 5. Get the middle 4 hours of the day (hours 10-13, so indices 10-14)
print(f"Middle 4 temperatures:  {hourly_temps[(((len(hourly_temps)) // 2) - 2):(((len(hourly_temps)) // 2) + 2)]}")
# 6. What were the temperatures for hours 6-9am? (indices 6-9)
print(f"Temperatures from 6 to 9AM:  {hourly_temps[7:11]}")





print("\n\n\nSECTION 4\n")
# append() adds ONE item to the end of a list
shopping_list = []
print("Starting with empty list:", shopping_list)
# Add these items one at a time using append():
# 1. Add "milk"
shopping_list.append("Milk")
# 2. Add "bread"
shopping_list.append("Bread")
# 3. Add "eggs"
shopping_list.append("Eggs")
# 4. Add "cheese"
shopping_list.append("Cheese")
# 5. Add "apples"
shopping_list.append("Apples")
print("Final shopping list:", shopping_list)
# 6. What happens if you try to append two items at once?
#shopping_list.append("Milk", "Butter")
    #    YOU GET AN ERROR MESSAGE!
# Try: shopping_list.append("butter", "yogurt")
# Comment out the line after you see the error!
# 7. Create a list with your 3 favorite foods using append()
favorites = []
# Add your three favorites here
print("My favorites:", favorites)
favorites.append("Pizza")
favorites.append("Eggs")
favorites.append("Salad")
print(favorites)



print("\n\n\n")
# insert() adds an item at a specific position
line = ["Alice", "Bob", "Charlie"]
print("Original line:", line)
# 1. David cuts to the front! Insert "David" at index 0
line.insert(0, "David")
print("After David cuts:", line)
# 2. Eve joins between Alice and Bob (what index?)
line.insert(2, "Eve")
print("After Eve joins:", line)
# 3. Frank joins at the end (what index? Use len())
line.insert(len(line), "Frank")
print("Final line:", line)
# Now create a schedule:
schedule = ["Math", "History", "Science"]
print("\nOriginal schedule:", schedule)
# 4. Add "Lunch" between History and Science
schedule.insert(2, "Lunch")
# 5. Add "Homeroom" at the beginning
schedule.insert(0, "Homeroom")
print("Updated schedule:", schedule)



print("\n\n\nSECTION 5\n")
# extend() adds ALL items from another list
primary_colors = ["red", "blue", "yellow"]
print("Primary colors:", primary_colors)
# 1. Create a list of secondary colors
secondary_colors = ["green", "orange", "purple"]
# 2. Add all secondary colors to primary_colors using extend()
print("All colors:", primary_colors)
# Compare append vs extend:
list1 = [1, 2, 3]
list2 = [1, 2, 3]
# 3. Append [4, 5] to list1 (this adds the list as one item!)
list1.append([4, 5])
print("After append([4, 5]):", list1)
# 4. Extend list2 with [4, 5] (this adds each item separately)
list2.extend([4, 5])
print("After extend([4, 5]):", list2)
# 5. Create your own example showing the difference
my_list = ["a", "b"]
# Try both append and extend with ["c", "d"] and print results




