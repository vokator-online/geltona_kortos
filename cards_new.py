### Kortų žaidimas "KARAS":

import random

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.sign = f"{rank} {suit}"
        self.weight = self.calculate_weight()

    def calculate_weight(self):
        weights = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        if self.rank in weights:
            return weights[self.rank]
        else:
            return int(self.rank)


class CardDeck:

    def __init__(self):
        ranks = [str(i) for i in range(2, 11)] + ['T', 'J', 'Q', 'K', 'A']
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self, count=1):
        if self.cards:
            taken_cards = self.cards[:count]
            self.cards = self.cards[count:]
            return taken_cards
        else:
            print("Deck is empty.")
            return []

    def take_from_bottom(self, count=1):
        if self.cards:
            taken_cards = self.cards[-count:]
            self.cards = self.cards[:-count]
            return taken_cards
        else:
            print("Deck is empty.")
            return []

    def take_random(self, count=1):
        if self.cards:
            taken_indices = random.sample(range(len(self.cards)), count)
            taken_cards = [self.cards[i] for i in taken_indices]
            self.cards = [card for i, card in enumerate(self.cards) if i not in taken_indices]
            return taken_cards
        else:
            print("Deck is empty.")
            return []

def initialize_hands():
    shared_deck = CardDeck()
    shared_deck.shuffle()

    player1_cards = []
    player2_cards = []

    for _ in range(26):
        player1_cards.extend(shared_deck.take_from_top())
        player2_cards.extend(shared_deck.take_from_top())

    player1_hand = CardDeck()
    player1_hand.cards = player1_cards

    player2_hand = CardDeck()
    player2_hand.cards = player2_cards

    return player1_hand, player2_hand

def play_war(player1_hand, player2_hand):
    table_cards = []

    while True:
        draw_option = input("Player 1, choose how to draw a card (1: Top, 2: Bottom, 3: Random): ")
        if draw_option == '1':
            player1_card = player1_hand.take_from_top()[0]
        elif draw_option == '2':
            player1_card = player1_hand.take_from_bottom()[0]
        elif draw_option == '3':
            player1_card = player1_hand.take_random()[0]
        else:
            print("Invalid draw option. Drawing from the top.")
            player1_card = player1_hand.take_from_top()[0]

        player2_card = player2_hand.take_from_top()[0]

        table_cards.extend([player1_card, player2_card])

        print(f"\nPlayer 1 plays: {player1_card.sign}")
        print(f"Player 2 plays: {player2_card.sign}")

        if player1_card.weight > player2_card.weight:
            print("Player 1 wins the round!")
            player1_hand.cards.extend(table_cards)
            break
        elif player1_card.weight < player2_card.weight:
            print("Player 2 wins the round!")
            player2_hand.cards.extend(table_cards)
            break
        else:
            print("It's a tie! The round continues.")

    return table_cards

def print_decks(player1_hand, player2_hand):
    print(f"\nPlayer 1 Hand: {len(player1_hand.cards)} cards")
    print(f"Player 2 Hand: {len(player2_hand.cards)} cards")

def main():
    print('''
-------------------- Welcome To Main WarGame Card Menu --------------------

        .-. . .-.   .--.   .----.    .---.    .--.   .-.   .-. .----.
        | |/ \\| |  / {} \\  | {}  }  /   __}  / {} \\  |  `.'  | | {_  
        |  .'.  | /  /\\  \\ | .-. \\  \\  {_ } /  /\\  \\ | |\\ /| | | {__
        `-'   `-' `-'  `-' `-' `-'   `---'  `-'  `-' `-' ` `-' `----'
          

                           1. Play the next round
          
                              2. Display hands
          
                                  3. Quit
       
---------------------------------------------------------------------------
              ''')





    player1_hand, player2_hand = initialize_hands()

    while True:
        choice = input("Select the menu item you would like to do: ")

        if choice == '1':
            table_cards = play_war(player1_hand, player2_hand)
            if table_cards:
                print(f"\nTable cards: {[card.sign for card in table_cards]}")
        elif choice == '3':
            print("\nThanks for playing! Goodbye!")
            break
        elif choice == '2':
            print_decks(player1_hand, player2_hand)
        else:
            print("Wrong choice. Please select the correct menu item!")

if __name__ == "__main__":
    main()


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