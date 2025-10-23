# Joseph Wilk
# CS1300
#W10S2








# MINI UNIT 2


for i in range(1, 11):
	print(i)
	if i >= 5:
		break


numbers = [3, 7, 9, 2, 11, 4, 13]
for i in numbers:
	if i % 2 == 0:
		print(f"{i} is the first even number.")
		break


system_password = "pass123"
max_attempts = 3
while max_attempts > 0:
	user_password = input("Enter the password:  ")
	if user_password == system_password:
		print("User password matches.  Permission granted.")
		break
	else:
		max_attempts -= 1
		print("you have not entered the correct password.")
else:
	print("You have incorrectly entered the password three times.  System locked.")




#MINI UNIT 3

print("\n\n\n")
for i in range(1, 6):
	if i == 3:
		continue
	else:
		print(i)


### EXTEND DOES NOT WORK HERE, ONLY   APPEND   WORKS HERE!!!
scores = [85, -5, 92, 150, 78, 45, 200]
valid_scores = []
for i in scores:
	if 0 <= i <= 100:
		valid_scores.append(i)
else:
	print(f"List of valid scores:  {valid_scores}")


