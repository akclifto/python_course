class Laptop:
    def type(self):
        print("Computer")

    def color(self):
        print("grey")


class Calculator:
    def type(self):
        print("Computer")
    
    def color(self):
        print("green")


# polymorphism here using the object param
def Computer(obj):
    obj.type()
    obj.color()


laptop = Laptop()
calc = Calculator()

Computer(laptop)
Computer(calc)