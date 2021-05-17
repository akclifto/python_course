"""
Weight conversion exercise
"""

user_weight = float(input("What is your weight? "))
unit = input ("Pounds(L) or kilograms(K)? ")

if unit.upper() == "L":
    converted_weight = user_weight * 0.45
    print(f"{converted_weight} Kilograms")
else:
    converted_weight = user_weight / 0.45 
    print(f"{converted_weight} Pounds")
