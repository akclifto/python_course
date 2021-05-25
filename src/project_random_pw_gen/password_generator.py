import string
import random


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


class Password:
    def generate_pw(self):
        signs = "!@#$%^&*()+-/[]{~}`'<>=.,:;_|"
        ch = Characters(signs)
        capital_letters = ch.capital_alphabets()
        small_letters = ch.small_alphabets()
        numbers = ch.numbers()
        symbols = str(ch.symbols)

        chars = [capital_letters, small_letters, numbers, symbols]
        pw = ""
        length = range(int(input("how long should the password be? ")))
        for l in length:  # length of password hardcoded to 7
            index1 = int(random.uniform(0, 4))  # random index for chars array
            # random index to take within each char group
            index2 = int(random.uniform(0, len(chars[index1])))
            character = chars[index1][index2]
            pw += str(character)
        return pw
        # print(ch.capital_alphabets())
        # print(ch.small_alphabets())
        # print(ch.numbers())
        # print(str(ch.symbols))

# password = Password()
# print(password.generate_pw())

def main():
    ps = Password()
    password = ps.generate_pw()
    print(f"password: {password}")
    return password