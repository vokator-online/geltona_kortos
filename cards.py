### KARAS:
import random

class Deck:

    def __innit__(self, rank, suit, sign, weight):
        self.rank = rank
        self.suit = suit
        self.sign = f"{rank}{suit}"
        self.weight = self.calculate_weight()

    def calculate_weight(self):
        weight = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, "Joker": 15}
        return weight[self.rank]


class Cards(Deck):
    def __init__(self):
        ranks = [str(i) for i in range(2, 11)] + ['T', 'J', 'Q', 'K', 'A']
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.cards = [Deck(rank, suit) for rank in ranks for suit in suits]
        self.shuffle_cards()
    
    def shuffle_cards(self):
        random.shuffle(self.cards)

    def print_cards(self):
        list(self.cards)

    def draw_top(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            print("Deck is empty. Start over.")
    
    def draw_bottom(self):
        if self.cards:
            return self.cards.pop(-1)
        else:
            print("Deck is empty. Start over.")

    def draw_random(self):
        if self.cards:
            return self.cards.pop(random)
        else:
            print("Deck is empty. Start over.")
    
    def print_remaining_cards()

def play_war(player1_deck, player2_deck):
    rounds = 0

def print_decks(player1_deck, player2_deck):
    print("\nPlayer 1 Deck:")
    for card in player1_deck.cards:
        print(card.sign, end='')
    print("\n\nPlayer 2 Deck:")
    for card in player2_deck.cards:
        print(card.sign, end='')

def main():
    print("Welcome to WAR\n MENU:")

    while True:
        print('''
-------------------- Welcome To Main WarGame Card Menu --------------------

        0: Exit from game
        1: Start a new game
        2: Shuffle the cards 
        3: Play next round
        4:
        5

---------------------------------------------------------------------
              ''')



# Kortų kaladė
# Korta: objektas
# -- rank (2-9, T, J, Q, K, A)
# -- suit (spades, clubs, hearts, diamonds)
# -- sign (suit + rank)
# -- weight
# Kortų kaladė
# -- cards - sąrašas kortų
# -- shuffle
# -- take from top
# -- take from bottom
# -- take random
# mastom apie žaidimą