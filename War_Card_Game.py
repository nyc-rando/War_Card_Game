from War_Card_Game import *

# Game setup and Play
print("Game Started")
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()

# Split the desk, deal out all chards to both players:
for card in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

# Game Play Logic: while loop for game on
while game_on:
    round_num += 1
    # print(f'Round {round_num}.')

    if len(player_one.all_cards) == 0:
        print(f'Player One is out of cards, player **TWO** wins in round {round_num}!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(f'Player Two is out of cards, player **ONE** wins in round {round_num}!')
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # While at war
    at_war = True

    while at_war:

        # print("war one", len(player_one.all_cards))
        # print("war one", len(player_two.all_cards))

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            # print("player 1 wins round")
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            # print("player 2 wins round")
            at_war = False

        else:
            print("WAR ! ! ! ")

            if len(player_one.all_cards) < 5:
                print("Player One has run out of material... \n")
                print(f"Player Two wins in round {round_num}.")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two has run out of material... \n")
                print(f"Player One wins in round {round_num}.")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

print('Game Over')

# Key Take-aways:
#  1) The Deck Class can use instances of the Card Class.
#  2) The Player class could hold instances of the Card class as well within it's own card list.