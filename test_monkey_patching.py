import collections
from random import shuffle

Card = collections.namedtuple ('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card


def main():
    deck = FrenchDeck()

    for card in deck[:5]:
        print(card)

    print('\n' + '='*10 + 'SHUFFLE' + '='*10 + '\n')

#    def set_card(deck, position, card):
#        deck._cards[position] = card
#
#    FrenchDeck.__setitem__ = set_card

    shuffle(deck)

    for card in deck[:5]:
        print(card)
    

if __name__ == '__main__':
    main()


