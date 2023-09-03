import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def get_card_name(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ["Clubs", "Diamonds", "Hearts", "Spades"] for value in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)