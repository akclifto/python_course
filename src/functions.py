def calc_age(birth_year, current_year):
    # age = current_year - birth_year
    # print(f"Age: {age}")
    return current_year - birth_year
# a requires two line spaces to make the function distinct, note the two line spaces below.


print("Name: John Smith")
age = "Age: " + str(calc_age(1998, 2021))
print(age)
print("Job: Programming")

# keyword argument, can put in any order in the function parameters as long as all params are done as key/value args
age = "Age: " + str(calc_age(current_year=2021, birth_year=2000))
print(age)