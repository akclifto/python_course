# lists
cars = ["Chevy", "Ford", "Ram", "Dodge"]
print(cars)
print(cars[1:3])

cars[3] = "GMC"
print(cars)
cars.append("Dodge")
print(cars)
#  insert via index, then item
cars.insert(0,"Buick")
print(cars)
cars.remove("Buick")
print(cars)
print("index of RAM is: " + str(cars.index("Ram"))) # index is case sensitive, so "RAM" will throw error

cars.sort()
cars2 = cars.copy()
print(cars)
cars.clear()
print(cars)
print(cars2)


# 2D lists
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
# iterate through matrix
for rows in matrix:
    for item in rows:
        (print(item))

print("\n\nExercise: Remove duplicates in list")
numbers = [1,1,3,3,7,6,3,4,6,7]
sole_numbers = []

for n in numbers:
    if n not in sole_numbers:
        sole_numbers.append(n)

sole_numbers.sort()
print(sole_numbers)