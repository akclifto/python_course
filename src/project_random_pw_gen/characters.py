import string

class Characters:
    def __init__(self, symbols):
        self.symbols = symbols

    def capital_alphabets(self):
        capital_letters = list(string.ascii_uppercase)
        return capital_letters

    def small_alphabets(self):
        small_letters = list(string.ascii_lowercase)
        return small_letters

    def numbers(self):
        numbers = list(string.digits)
        return numbers


    # potato symbols hardcoded in signs
    def symbols(self):
        symbols = self.symbols
        return symbols.split(" ")


