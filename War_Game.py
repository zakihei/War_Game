#!/usr/bin/python env
#-*- coding utf-8 -*-

from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,
             "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        """ suits and value is integer """
        self.value = value
        self.suit = suit

    def __lt__(self, c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_cards(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


           
card1 = Card(10, 2)
card2 = Card(11, 3)

#Step1
#print(card1 < card2)
#print(card1)

#Step2
deck = Deck()
for card in deck.cards:
    print(card)

#2018/11/15

print("See you!!")

