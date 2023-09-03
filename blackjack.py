class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def get_card_name(self):
        return f"{self.value} of {self.suit}"