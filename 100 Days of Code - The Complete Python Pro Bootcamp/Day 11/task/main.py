import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def AddCard(hand, count, total_sum):
    for i in range(count):
        card = random.choice(cards)
        if card == 11:
            if total_sum + 11 > 21:
                total_sum += 1
            else:
                total_sum += 11
        else:
            total_sum += card
        hand.append(card)
    return total_sum


playerHand = []
computerHand = []
computerSum = 0
playerSum = 0

playerSum = AddCard(playerHand, 2, playerSum)
computerSum = AddCard(computerHand, 2, computerSum)

playerPrint = f"You have [{playerHand[0]}] [{playerHand[1]}] "
computerPrint = f"Comp has [{computerHand[0]}] [{computerHand[1]}] "
print(playerPrint)
print(f"Cards total: {playerSum}")
print(f"Computer has [{computerHand[1]}]")

while input("Hit or Stand?").title() == "Hit":
    nextCard = random.choice(cards)
    if nextCard == 11 and playerSum + 11 > 21:
        nextCard = 1
    playerHand.append(nextCard)
    playerSum += nextCard
    playerPrint += f"[{nextCard}] "
    print(playerPrint)
    print(f"Card total: {playerSum}")
    if playerSum > 21:
        print("Bust!")
        break

while computerSum < 17:
    computerSum = AddCard(computerHand, 1, computerSum)
print(computerPrint)
print(f"Computer's card total: {computerSum}")

if playerSum < computerSum and computerSum < 21:
    print("You lose")
elif playerSum > computerSum and playerSum < 21:
    print("You win")
elif playerSum == computerSum and computerSum <= 21:
    print("Tie")
elif playerSum < computerSum and computerSum > 21:
    print("You win")
