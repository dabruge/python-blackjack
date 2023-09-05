import os
import random
import tkinter as tk

assets_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets/'))

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def get_card_name(self):
        return f"{self.value} of {self.suit}"
    
    @classmethod
    def get_back_file(cls):
        cls.back = tk.PhotoImage(file=f"{assets_folder}/Card-Back-04.png")
        return cls.back
    
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ["Clubs", "Diamonds", "Hearts", "Spades"] for value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "Ace":
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -= 10
    
    def get_value(self):
        self.calculate_value()
        return self.value
    
class GameState:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)

        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
        
        self.has_winner = ''
    
    def player_is_over(self):
        return self.player_hand.get_value() > 21
    
    def bj_occurred(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        
        if player and dealer:
            return 'both'
        elif player:
            return 'player'
        elif dealer:
            return 'dealer'
        
        return False
    
    def hit(self):
        self.player_hand.add_card(self.deck.deal())
        if self.bj_occurred() == 'player':
            self.has_winner = 'player'
        if self.player_is_over():
            self.has_winner = 'dealer'

        return self.has_winner