# overview of all the basics from athe udemy course
import math

print('this is the beginning')
# not going to go over the variable deeply, you already know this. 
age = 34
print(age)
print(type(age)) # prints an int as the type

# get user input and print out
name = input("input your name or something: ")
print("Hello " + name)

# type conversions
current_year = int(input("What is the Current year? "))
years = 2023 - current_year
print(years)


# exercise pounds to kilograms conversions
lbs = float(input("what is your weight? "))
kgs = 0.45 * lbs
print("Your weight in Kgs is: " + str(kgs) + " kgs")

# multi line strings
greet = """
 This is a multi-line string
 welcome to the course
"""
print(greet)

# substrings
lang = "english"
print(lang[1:4]) # ngl (end char non-inclusive)

# formatted string
first_name = "john"
last_name = "english"
msg = f"{first_name} {last_name} is done using a formatted string!"
print(msg)

# len = gets length of string
# lower() = converts to lower case
# upper() = converts to upper cases
# title() = capitalized the first letter of each word
# find('<character/string>') = returns index of first instance of char or substring", returns -1 if not found
# replace("<character/string>", "<replacement>") find and replace char or string in something.
# in operator (print("jo" in first_name)) = returns true if "jo" is present in first_name var above.  case sensitive


# Maths

print(7 / 3) # division
print(7 // 3) # division floor
print(7 % 3) # modulus/remainder only
print(7 * 3) # multiplication
print(7 ** 3) # math.pow operator, returns (7^3)
print(abs(-46.3)) # absolute value
print(round(-46.50)) # absolute value  **.50 rounds down, **.51 rounds up
print(round(-46.51)) # absolute value  **.50 rounds down, **.51 rounds up

# for complex math, import the math module
print(math.exp(2)) # exponential value base set to e (recall calc)
# check documentation for all the available functions in the math module


