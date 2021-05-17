"""
This is a multi line comment 
"""

age = 22

if age <= 18:
    print("You're age is 18 or lower")
elif age > 35:
    print("You're older than 35")
else:
    print("Your age is higher than 18")

x = "python"

# operator logic and or and not operators
if "s" not in x:
    print("can use `not in` operator for boolean logic")

has_funds = True
has_results = True

if has_funds and has_results:
    print("Logical AND operation because has_funds is " + str(has_funds) + " and has_results is " + str(has_results))

has_results = False

if has_funds or has_results:
    msg = f"Logical OR operation because has_funds is {has_funds} and has_results is {has_results}"
    print(msg)

if has_funds and not has_results:
    msg = f"Logical NOT operation because has_funds is {has_funds} and has_results is {has_results}"
    print(msg)