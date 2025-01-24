import unittest
from Cards import Card, Deck, Hand

class TestCard(unittest.TestCase):
    def test_init(self):
        c1 = Card(3, 'clubs') # set card to 3 of clubs
        self.assertEqual(c1.value, 3, 'Value is wrong') #Testing the value and the suit equal 3 and clubs
        self.assertEqual(c1.suit, 'clubs', 'Suit is wrong')

    
    def test_repr(self):
        c1 = Card(5, 'hearts') # set card equal to 5 of hears
        self.assertEqual(c1.repr(), 'Card(5 of hearts)', 'Card is wrong') #Function testing

    def test_lt(self):
        c1 = Card(3,'clubs') # set 3 types of cards
        c2 = Card(2,'hearts')
        c3 = Card(5, 'clubs')
        self.assertFalse(c2 < c1) # makes sure suits are set alphabetically
        self.assertTrue(c1 < c3) # makes sure if suits are same sorts by value

class TestDeck(unittest.TestCase):
    def test_init(self):
        d1 = Deck() # creates deck
        self.assertEqual(d1.values[4], 5) # makes sure values, suits, and the list are working
        self.assertEqual(d1.suits[2], 'hearts')
        self.assertEqual(d1.card_list[0], (1, 'clubs'))
        
        d2 = Deck([1, 2, 3], ['snakes','bats'], []) # creates unique deck
        self.assertEqual(d2.values[1], 2) # tests unique deck
        self.assertEqual(d2.suits[0], 'snakes')
        self.assertEqual(d2.card_list[0], (1, 'snakes'))

    def test_len(self):
        d1 = Deck()
        self.assertEqual(len(d1), 52) # makes sure default deck has 52 cards

        d2 = Deck([1, 2, 3], ['snakes','bats'], [])
        self.assertEqual(len(d2), 6) # unique deck has 6 different cards

    def test_sort(self):
        d1 = Deck()
        d1.shuffle() #firsts shuffles
        d1.sort() # then sorts
        self.assertEqual(d1.card_list[0], (1, 'clubs')) # test if sorts properly

    def test_repr(self):
        d1 = Deck([1, 2, 3], ['snakes','bats'], [])
        self.assertEqual(repr(d1), "'Card(1 of snakes)'") #repr function testing
        

    def test_shuffle(self):
        d1 = Deck()
        d1.sort() # first sorts
        d1.shuffle() # then shuffles
        self.assertNotEqual(d1.card_list[0], (1, 'clubs')) # tests that first card is diferent

    def test_draw_top(self):
        d1 = Deck()
        d1.sort()
        d1.draw_top() # calls function
        self.assertNotEqual(d1.card_list[-1], (13, 'spades')) #13 of spades was drawn
        self.assertEqual(d1.card_list[-1], (13, 'hearts')) # 13 of hearts is next
        d1.draw_top() # repeats function
        self.assertNotEqual(d1.card_list[-1], (13, 'hearts'))

class TestHand(unittest.TestCase):
    def test_init(self):
        d1 = Hand([(value, 'hearts') for value in range(1, 4, 1)]) # unique hand
        self.assertEqual(d1.hand[0], (1, 'hearts')) # tests init

    def test_repr(self):
        d1 = Hand([(value, 'hearts') for value in range(1, 4, 1)])
        self.assertEqual(repr(d1), "[[(1, 'hearts'), (2, 'hearts'), (3, 'hearts')]]") # tests repr

    def test_play(self):
        d1 = Hand([(value, 'hearts') for value in range(1, 5, 1)])
        d1.play(-1) # plays last card in hand
        self.assertEqual(d1.hand[-1], (3, 'hearts')) # card no longer in hand

    

    








unittest.main()