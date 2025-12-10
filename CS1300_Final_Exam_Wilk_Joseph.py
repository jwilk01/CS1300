# Joseph Wilk
# CS 1300
# Final Exam
# Dec 10, 2025


# ALL TEST CASES HAVE PASSED


# PROBLEM 1

user_list_numbers = []

def count_positive(numbers):
	count = 0
	for i in range(len(numbers)):
		if numbers[i] > 0:
			count += 1
	return count


while True:
	user_list_numbers.append(input("ENTER a list of numbers ('done' to quit):  "))
	if user_list_numbers[-1] == "done" or user_list_numbers[-1] == "DONE":
		user_list_numbers.pop()
		break
	user_list_numbers[-1] = int(user_list_numbers[-1])
# DEBUG print(user_list_numbers)
final_count = count_positive(user_list_numbers)
print(f"Number of positive numbers in list:  {final_count}")



# PROBLEM 5

user_list_5 = []

def reverse_list(items):
	items.reverse()
	return items




while True:
	user_list_5.append(input("ENTER a list to have reversed ('done' to quit):  "))
	if user_list_5[-1] == "done" or user_list_5[-1] == "DONE":
		user_list_5.pop()
		break
	if isinstance(user_list_5[-1], int):
		user_list_5[-1] = int(user_list_5[-1])

reversed_list = reverse_list(user_list_5)
print(reversed_list)





# PROBLEM 4

def create_pattern(n):
	
	for i in range(1, n+1):
		for j in range(1, n+1):
			if i >= j:
				print(f"{j} ", end="")
		print()


user_count_rows = int(input("ENTER number of rows for the number pattern:  "))
create_pattern(user_count_rows)




# PROBLEM 3

def is_palindrome(word):
	for i in range(1, len(word)+1):
		if word[i-1].lower() != word[-i].lower():
			print("WORD is not a palindrome.")
			return False
	print("WORD is a palindrome.")
	return True

user_word = input("ENTER a word and check if it is a palindrome:  ")
palindrome_bool = is_palindrome(user_word)
print(f"Is your word a palindrome -->  {palindrome_bool}")

