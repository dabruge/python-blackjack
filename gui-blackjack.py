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