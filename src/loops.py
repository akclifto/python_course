# while loops
i = 1
while i <= 5:
    print(i)
    i += 1
print("end of while loop")

# for loops
lang = "python"
for item in lang:
    print(item)

print("\nRange print\n")
for item in range(3, 10, 2): # range begin (3), range end(10), incr step(2)
    print(item)
    #prints 3, 5, 7, 9

# exercise
prices = [40, 50, 75, 100]
total = 0

for n in prices:
    total += n
print(total)

# Nested loops: coordinates example
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

print("Nested loop exercise: gen X's for each number value")

numbers = [6,2,6,2,6,2]

# this is a python specific way to do this.
for n in numbers: 
    print("X" * n)  
print()
# write an algo not using this method above
for n in numbers: 
    result = ""
    for count in range(n): #since dealing with ints, can use range to get value at each n-position
        result += "X"
    print(result)