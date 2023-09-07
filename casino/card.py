import os
import tkinter as tk
from tkinter import PhotoImage

assets_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'python-blackjack/assets/'))

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.img = tk.PhotoImage(file=assets_folder + '/Classic/small_' + self.suit[0].lower() + self.value + ".png")
    
    def get_card_name(self):
        return f"{self.value} of {self.suit}"

    def get_file(self):
        return self.img
    
    @classmethod
    def get_back_file(cls):
        cls.back = tk.PhotoImage(file=f"{assets_folder}/Card-Back-04.png")
        return cls.back