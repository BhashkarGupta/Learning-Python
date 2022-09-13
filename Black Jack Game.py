# Black Jack Game
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def program():
    bet_amount = int(input("\nPlease Enter Bet amount: $"))
    players_card = []
    dealers_card = ["X"]

    def card_selector():
        select_card = random.choice(cards)
        if select_card == 11 and sum(players_card) > 10:
            return 1
        else:
            return select_card

    players_card.append(card_selector())
    players_card.append(card_selector())
    dealers_card.append(card_selector())
    print(f"Your cards: {players_card}. Your Score is {sum(players_card)}.")
    print(f"Dealer Cards: {dealers_card}")
    option = "h"
    while option == "h":
        option = input(
            "Please enter 'h' for HIT(add one more card on your deck) or 's' for STAND(Fix your current card).").lower()
        if option == "h":
            players_card.append(card_selector())
            print(f"Your cards: {players_card}. Your Score is {sum(players_card)}.")
            print(f"Dealer Cards: {dealers_card}")
        elif option == "s":
            dealers_card[0] = card_selector()
            while sum(dealers_card) < sum(players_card) and sum(dealers_card) < 22:
                dealers_card.append(card_selector())

    return {
        "player_score": sum(players_card), "player_card": players_card,
        "dealer_score": sum(dealers_card), "dealer_card": dealers_card,
        "bet_amount": bet_amount
    }


print("Welcome to Black Jack Game")
bank = 500
print(f"You are given ${bank} for this Game. Enjoy !!! ")
while bank > 0:
    output = program()

    if output["player_score"] < 22:
        if output["player_score"] > output["dealer_score"]:
            bank = bank + output["bet_amount"]
            print(f"Player's Card: {output['player_card']}, Score: {output['player_score']}")
            print(f"Dealer's Card: {output['dealer_card']}, Score: {output['dealer_score']}")
            print(f"Congrats!!! You Win.\nBank: ${bank}")

        elif output["player_score"] < output["dealer_score"]:
            bank = bank - output["bet_amount"]
            print(f"Player's Card: {output['player_card']}, Score: {output['player_score']}")
            print(f"Dealer's Card: {output['dealer_card']}, Score: {output['dealer_score']}")
            print(f"You Loose.\nBank: ${bank}")

    elif output["player_score"] > 21:
        bank = bank - output["bet_amount"]
        print(f"Player's Card: {output['player_card']}, Score: {output['player_score']}")
        print(f"You Bust!\nBank: ${bank}")

    elif output["player_score"] == output["dealer_score"]:
        print(f"Player's Card: {output['player_card']}, Score: {output['player_score']}")
        print(f"Dealer's Card: {output['dealer_card']}, Score: {output['dealer_score']}")
        print(f"Its A draw\nBank: ${bank}")

print("You have lost all your Money.\nGAME OVER!!!")
