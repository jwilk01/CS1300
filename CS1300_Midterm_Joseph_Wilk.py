# Joseph Wilk
# CS 1300
# Midterm
# Oct 9, 2025



print("\tPROBLEM 1: STRING PROCESSING")
print(" #" * 10 + "\n\n")

full_name = "Joseph Michael Wilk"
email = "jwilk@university.net"
phone = "555-123-9876"

#Task1.1
print(full_name[0:6])

#Task1.2
print(full_name[-4:])

#Task1.3
print(f"{full_name[0]}.{full_name[7]}.{full_name[-4]}.")

#Task1.4
if "university" in email:
	print("Yes, \"university\" is in the student's email.")
else:
	print("No, \"university\" is not in the student's email.")

#Task1.5
phone = phone.replace("-", " ")
print(phone)



print("\n\n\n\n\nPROBLEM 2: RESTAURANT RATING CALCULATOR\n")

# rating: 0 to 5
atmosphere = 4.5
food = 3.4
service = 2.5
cleanness = 3.0

#Task2.1
average_rating = round((atmosphere + food + service + cleanness) // 4, 1)

#Task2.3
if average_rating >= 4.0:
	print("The restaurant is at least a 4/5 star rating.")
elif average_rating >= 3.0:
	print("The restaurant is at least a 3/5 and below 4/5 star rating.")
elif average_rating >= 2.0:
	print("The restaurant is at least a 2/5 and below 3/5 star rating.")
elif average_rating >= 1.0:
	print("The restaurant is at least a 1/5 and below 2/5 star rating.")
else:
	print("The restaurant rating is POOR: below 1/5 stars!")
	




print("\n\n\n\n\nPROBLEM 3: MOVIE REVIEW NUMBER MANAGEMENT\n")

# Task 3.1 (2 points): Create a list with these movie review numbers
numbers = [3, 5, 4, 3, 2, 1, 3]

# Task 3.2
numbers.extend([4])

# Task 3.3
numbers[2] = 4

# Task 3.4
del numbers[5]

# Task 3.5
numbers.insert(2, 3)

# Task 3.6
print(numbers[0:4])

# Task 3.7
print(len(numbers))
print(numbers[0])
print(numbers[-1])




print("\n\n\n\n\nPROBLEM 4: SHOPPING CART SYSTEM\n")

# Initial setup (DO NOT MODIFY):
items = ["bread", "milk", "eggs", "cheese", "apples"]
prices = [2.50, 3.99, 2.99, 5.49, 4.99] # Matching prices for each item
cart = []
cart_total = 0.0

# Task4.1
if "milk" in items:
	# ERROR items.find("milk")
	cart.append("milk")
	cart_total += 3.99
	print(cart)
	
# Task4.2
cart.append("eggs")
cart_total += 2.99
print(cart)

# Task4.3
if "cookies" in items:
	print("Cookies are in the item list.")
else:
	print("Cookies have been added to the item list.")
	items.append("cookies")
	print(items)
	
# Task4.4
if cart_total > 6.00:
	print(f"Original total: {cart_total}")
	cart_total = cart_total * 0.90
	print(f"New total: {cart_total:.2f}")

# Task4.5
print(f"Items in cart: {len(cart)}")
print(f"Number of items: {len(items)}")
print(f"Final total: {cart_total:.2f}")

print("\n\nEND MIDTERM EXAM\n")
	



