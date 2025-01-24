class Card:
    def __init__(self, value, suit): # sets value and suit
        self.value = value
        self.suit = suit
    
    def repr(self):
        rep =  f'Card({self.value} of {self.suit})'
        return str(rep) # represents card in suit in string

    def __lt__(self, other):
        if self.suit == 'clubs' and (other.suit == 'diamonds' or other.suit == 'hearts' or other.suit == 'spades'): # clubs least valuable
            return True
        elif self.suit == 'diamonds' and (other.suit == 'hearts' or other.suit == 'spades'):
            return True
        elif self.suit == 'hearts' and other.suit == 'spades': # spades most valuable
            return True
        elif self.suit == other.suit: # goes my value after suit
            if self.value < other.value:
                return True
        else:
            return False


class Deck:
    def __init__(self, values = [1,2,3,4,5,6,7,8,9,10,11,12,13], suits = ['clubs','diamonds','hearts','spades'], card_list = []): # default deck of cards (52 cards)
        self.values = values
        self.suits = suits
        self.card_list = []
        for i in range (0, len(self.values)): # combines values and suits to make cards
            for j in range (0, len(self.suits)):
                Card = (self.values[i], self.suits[j])
                self.card_list.append(Card)

    def __len__(self): # how many cards in a deck
        return len(self.card_list)

    def sort(self): # puts cards in order by value
        return self.card_list.sort()
    
    def __repr__(self): # represents deck
        rep = []
        for i in range (0, len(self.values)):
            for j in range (0, len(self.suits)):
                return repr("Card("+ str(self.values[i]) + ' ' + 'of' + ' ' + self.suits[j] + ')')

    def shuffle(self): # shuffles deck in random order
        import random
        return random.shuffle(self.card_list)

    def draw_top(self): # draws top of card and removes it from deck
        return self.card_list.pop()

class Hand(Deck):
    def __init__(self, hand = []): # chooses hand from deck
        self.hand = hand
    
    def __repr__(self): # represents hand
        rep = [self.hand]
        return repr(rep)

    def play(self, play): # plays card from hand and removes it
        return self.hand.pop(play)
