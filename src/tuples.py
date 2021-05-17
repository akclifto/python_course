# tuples are immutable, cannot change item assignment or mutate
numbers = (5,6,7,8)
# use tuples to make sure you don't accidentally modify a list
print(numbers)

# UNPACKING
"""
Use unpacking for vars that will be reused throughout program multiple times,
see example
"""
coords = (1,2,3)
# long way to reuse multi use cases of these coords
x = coords[0]
y = coords[1]
z = coords[2]
result = x*y*z
print(result)

# unpacking way 
x,z,y = coords
result = x*y*z
print(result)

# DICTIONARIES
"""
Use dictionaries to store key/value pairs, ex:
John Smith:
Name = "John Smith"
Age = 30
Gender = Male
...
"""
# This is similar to JSON formatting
person = {
    "name" : "John Smith",
    "age": 30,
    "gender": "Male",
    "is_married": True
}
print(person["name"]) #case sensitive on the key name, will throw error if key DNE

# use get method instead to make sure you don't throw errors
print(person.get("as;lkdjf")) # returns "None", meaning this key doesn't exist
# Supply a default value to a key if it DNE
print(person.get("birthdate", "December 1, 1901"))
# To update a value, get the key and update it
person["name"] = "ADAM"
print(person)

print("\n\nExercise for Dictionaries")
user_input = input("Type a number to convert to text: ")

# mapping dictionary
digit_to_text = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
result = ""
for n in user_input:
    result += digit_to_text.get(n, "...") + " "
print(result)
