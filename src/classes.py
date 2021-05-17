class Car:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def brand(self):
        print("Audi")
    
    def color(self):
        print("black")

    def move(self):
        print("move")

# without a ctor
# car = Car()

# car.brand()
# car.color()
# car.move()

# car.start = "start"
# car.stop = car.start
# print(car.start)

# with a ctor
car2 = Car("Start", "Stop")
print(car2.start)

print("exercise dogs ctors")

class Dog:
    def __init__(self, breed, gender):
        self.breed = breed
        self.gender = gender
    
    def bark(self):
        print("bark")


dog = Dog("Lab", "Male")
print(dog.breed)
print(dog.gender)
dog.bark()

# inheritance
class Bird:
    def fly(self):
        print("Fly")


class Parrot(Bird):
    pass # pass means we are not populating the class with anything, without it, python will throw error


class Sparrow(Bird):
    def noise(self):
        print("make noise")


p = Parrot()
p.fly()
s = Sparrow()
s.fly()
s.noise()