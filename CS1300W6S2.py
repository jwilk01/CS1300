# CS1300
# Joseph Wilk
# Sep 25 2025


# TODO: Create a store system with these features:
# 1. Display a menu of 5 items with prices
# 2. Let user select one item
# 3. Ask for quantity
# 4. Apply discounts:
# - 10+ items: 10% off
# - Member: additional 5% off
# 5. Calculate tax (8%)
# 6. Show final receipt
""" WE DO NOT YET HAVE TO DO ARRAYS AS WE HAVE NOT COVERED THOSE YET"""







# TODO: Create a health advisor with these features:
# 1. Ask for age, weight, height
# 2. Ask about exercise (none/light/moderate/heavy)
# 3. Ask about sleep hours
# 4. Ask about water intake (glasses per day)
# 5. Calculate BMI
# 6. Provide personalized recommendations based on all inputs
# 7. Give an overall health score (0-100)











# TODO: Create a character creator with:
# 1. Choose class (Warrior/Mage/Rogue)
# 2. Allocate 20 skill points among:
# - Strength, Intelligence, Agility
# 3. Validate point allocation
# 4. Calculate derived stats:
# - Health = 100 + (Strength * 10)
# - Mana = 50 + (Intelligence * 15)
# - Speed = 5 + (Agility * 2)
# 5. Assign starting equipment based on class
# 6. Display complete character sheet

video_game_character = input("ENTER a class of video game character (Warrior/Mage/Rogue):  ")
if video_game_character == "Warrior" or video_game_character == "Mage" or video_game_character == "Rogue":
	print("There are three ability options: Strength, Intelligence, Agility.")
	print("You are allowed 20 total points for all three abilities.")
	strength = int(input("Please choose the total number for Strength (int):  "))
	if strength > 20 or strength <= 0:
		print("You did not enter a valid integer")
	else:
		intelligence = int(input("Please choose the total number for Intelligence(integer):  "))
		if intelligence > 20 or intelligence <= 0:
			print("You did not enter a valid integer")
		else:
			agility = int(input("Please choose the total number for Agility(integer):  "))
			if agility > 20 or agility <= 0:
				print("You did not enter a valid integer")
			else:
				total_skills = strength + intelligence + agility
				if total_skills > 20:
					print("Your total skill points is above 20.")
				else:
					health = 100 + (strength * 10)
					mana = 50 + (intelligence * 15)
					speed = 5 + (agility * 2)
					if video_game_character == "Warrior":
						equipment = "Sword"
					elif video_game_character == "Mage":
						equipment = "Staff"
					else:
						equipment = "Stick"
					print("+" * 25)
					print("\nCHARACTER SHEET:\n")
					print(f"  YOUR CHARACTER: {video_game_character}.")
					print(f"  YOUR ABILITY LIST---   Health: {health}")
					print(f"                         Mana:   {mana}")
					print(f"                         Speed:  {speed}")
					print(f"  YOUR EQUIPMENT: {equipment}")
					print("\n" + "+" * 25)
else:	
	print("You did not enter a valid video game character type!")








