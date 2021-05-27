import random

from characters import Characters

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
        # length of password hardcoded to 7
        for l in length:  
            # random index for chars array
            index1 = int(random.uniform(0, 4))  
            # random index to take within each char group
            index2 = int(random.uniform(0, len(chars[index1])))
            character = chars[index1][index2]
            pw += str(character)
        return pw

