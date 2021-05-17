import random

print("Hangman with Continents")
print("Cat: Geography | Type: Continents")

continents = ("Asia", "North America", "South America", "Africa", "Europe", "Australia")
secret_word = random.choice(continents)
losing_threshold = 0
guess_count = 3

word = "Word:" + " _" * len(secret_word)
print(word)

while guess_count > losing_threshold:
    guess = input("Guess the world: ").title()
    guess_count -= 1
    print(f"Guesses left: {guess_count}")

    if guess == secret_word:
        print("You won the game")
        break
    elif guess != secret_word:
        print("Wrong guess")
else:
    print("You lose, game over!")
    print(f"The world was {secret_word}")