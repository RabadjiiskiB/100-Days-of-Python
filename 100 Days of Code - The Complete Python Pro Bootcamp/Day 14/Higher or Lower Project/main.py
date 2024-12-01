import random

import game_data as game

firstCard = random.randint(1, len(game.data)-1)
secondCard = random.randint(1, len(game.data)-1)

playerIsRight = True
while playerIsRight == True:
    print(
        f"Is {game.data[firstCard]['name']}, a {game.data[firstCard]['description']} from {game.data[firstCard]['country']}")
    print(game.data[firstCard]["follower_count"])
    print(
        f"Higher or lower than {game.data[secondCard]['name']}, a {game.data[secondCard]['description']} from {game.data[secondCard]['country']}")
    print(game.data[secondCard]["follower_count"])
    playerInput = input("type h/l: ").lower()
    if playerInput == "l":
        if game.data[firstCard]['follower_count'] > game.data[secondCard]['follower_count']:
            print("You guessed right")
            firstCard = secondCard
            secondCard = random.randint(1, len(game.data) - 1)
        else:
            print("You guessed wrong")
            playerIsRight = False
    elif playerInput == "h":
        if game.data[firstCard]['follower_count'] < game.data[secondCard]['follower_count']:
            print("You guessed right")
            firstCard = secondCard
            secondCard = random.randint(1, len(game.data) - 1)
        else:
            print("You guessed wrong")
            playerIsRight = False