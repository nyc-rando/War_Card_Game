print("okay \n" * 100)

# Card Class, to know suit, rank, integer value

import random

values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
          "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} card(s).'

# Game setup
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
    print(f'Round {round_num}.')

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards, player Two wins!')
        game_on = False

    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards, player One wins!')
        game_on = False

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # While at war
    at_war = True

    while at_war:

        if player_one.all_cards[-1] >