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
    
    def display(self):
        if self.dealer:
            print("Hidden")
            print(self.cards[1].get_card_name())
        else:
            for card in self.cards:
                print(card.get_card_name())
            print("Value: ", self.get_value())

class Game:
    def __init__(self):
        playing = True
        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
            
            print("Player's hand:")
            self.player_hand.display()
            print()
            print("Dealer's hand:")
            self.dealer_hand.display()

            game_over = False

            while not game_over:
                player_has_bj, dealer_has_bj = self.check_for_bj()
                if player_has_bj or dealer_has_bj:
                    game_over = True
                    self.show_bj_results(player_has_bj, dealer_has_bj)
                    continue
                choice = input("Would you like to [H]it or [S]tick?\n").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Please choose whether to hit or stick.\n").lower()
                if choice in ["h", "hit"]:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("You've gone over, you lose!")
                        game_over = True
                else:
                    print("Final results:")
                    print(f"Your hand: {self.player_hand.get_value()}")
                    print(f"Dealer's hand: {self.dealer_hand.get_value()}")
                    if self.player_hand.get_value() > self.dealer_hand.get_value():
                        print("You win!")
                        game_over = True
                    else:
                        print("Dealer wins!")
                        game_over = True
            
            play_again = input("Play again? [Y/N]\n").lower()
            while play_again not in ["y", "yes", "n", "no"]:
                play_again = input("Please enter Y / N\n")
            if play_again in ["n", "no"]:
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False
    
    def check_for_bj(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        return player, dealer
    
    def show_bj_results(self, player_has_bj, dealer_has_bj):
        if player_has_bj and dealer_has_bj:
            print("Both players have blackjack! Draw!")
        elif player_has_bj:
            print("You have blackjack! You win!")
        elif dealer_has_bj:
            print("Dealer has blackjack! Dealer wins!")

    def player_is_over(self):
        return self.player_hand.get_value() > 21

if __name__ == "__main__":
    game = Game()
    