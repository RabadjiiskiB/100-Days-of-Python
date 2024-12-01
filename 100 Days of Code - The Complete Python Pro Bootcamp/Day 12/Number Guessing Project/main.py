import random

easyDiffTurns = 10
hardDiffTurns = 5
def setDifficulty():
    if input("Choose your difficulty level:") == "easy":
        return easyDiffTurns
    else:
        return hardDiffTurns


print("Choose your difficulty level:")
print("1. Easy")
print("2. Hard")
guesses = setDifficulty()
print("Hello Im thinking of a number between 1 and 100")
number = random.randint(1,100)
print(f"Spoiler: {number}")
player_guess = int(input("Guess a number between 1 and 100: "))
while guesses > 0:
    if player_guess == number:
        print("You have guessed the correct number!")
        break
    elif player_guess > number:
        print("Your guess is too high!")
        guesses -= 1
    elif player_guess < number:
        print("Your guess is too low!")
        guesses -= 1
    print(f"You have {guesses} guesses left.")
    player_guess = int(input("Guess again!"))
print("Thank you for playing!")