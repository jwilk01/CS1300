# CONCATENATION means add at the end.  in python you can CONCATENATE strings to be added at end of other strings with + sign.

first = "Python"
second = "Programming"

result = first + "" + second
print(result)


# YOU CAN DO MULTIPLICATION WITH STRINGS
#THIS IS A VERY VERY COMMON THING IN PYTHON

pattern = "Ha"
laugh = pattern * 3
line = "_" * 20
print(laugh)
print(line)


text = "Python Programming"
print("Python" in text) # true or false?  TRUE
print("python" in text) # true or false? FALSE
print("gram" in text) # true or false? TRUE

print("cat" == "Cat") # FALSE
print("apple" > "Apple") # TRUE
print("100" > "99") # FALSE !!!!!!


text02 = "Mississippi"

print(len(text02))
print(text02[0])
print(text02[-1])
print(text02[(len(text02)-1)//2]) # THIS PRINTS THE MIDDLE CHARACTER, IS SELF-EXPLANATORY UPON THE //2 PORTION.


email = "student@example.com"

print(email[0:7])
print(email[8:15])
print(email[-3:])  # THE LAST THREE CHARACTERS


letters_ab = "ab" * 3
print(letters_ab)

string_123 = "123"
string_123 = string_123 + string_123[::-1]  #123321
print(string_123)



string_hello = "Hello".upper()
print(string_hello) # HELLO

print("123.45".isdigit()) # FALSE, because of the period.
print("".isspace()) # FALSE, there is NO space in here!
print("\t".isspace()) # TRUE, Python3.9 recognizes the TAB.
print("HELLO!".isupper()) # TRUE



text03 = "Hello World!"
print(text03.find("World")) # in 6th position
print(text03.find("o"))  # Gives you the first instance, at position 4.
print(text03.find("xyz"))  # -1, meaning DNE.


text04 = "Mississippi"
print(text04.count("s"))  # 4
print(text04.count("ss"))  # 2
print(text04.count("pip"))  # 0

print(text04.find("pip") < 0)  # TRUE

print(text03.replace("o", "0"))  # Hell0 World!
print(text03.replace("!", "")) # Returns Hello World

# PYTHON IS A GREAT LANGUAGE FOR STRING MANIPULATION



messy = "Python Programming"

print(messy)
print(messy.strip())
print(messy.rstrip())
print(messy.lstrip())

text05 = "I like cats. Cats are nice."
print(text05.lstrip())




print('Hi'.center(10))  #    Hi     #
print('Hi'.ljust(10))  #Hi        #
print('Hi'.rjust(10))  #       Hi#


print('42'.zfill(5))  # 00042


print("Name".ljust(15, '*') + "Score".rjust(10, '-'))


messy02 = "PyThOn PRoGRamming"


""" IT IS VERY IMPORTANT TO USE .STARTSWITH(PREFIX) AND .ENDSWITH(PREFIX) TO CHECK EITHER BEGINNING OR END IN THE PROFESSIONAL SETTING.
"""

filename = "report.pdf"
print(filename.endswith("pdf"))  # TRUE




"""
LAB WEEK 4 SESSION 2
"""

user_input = "Hello123"
print(user_input.isalnum())
user_input = user_input.upper()
print(user_input)


name = "jOHn  DOE"
print(name.replace(" ", ""))
print(name.title())


url = "https://www.example.com"
print(url.startswith("https"))
print(url.replace("//", ""), url.replace("www.", ""))


text = "Hello World!  How  are  you?"
print(" ".join(text.split()))






















