from blockchain import Transaction, Block, Ledger, Blockchain
from hashmap import hashtable
import unittest

class TestHashmap(unittest.TestCase):
    def test_adduser(self):
        #make a hash table of 100
        t1 = hashtable(100)

        #Add user assigned to a certain value
        t1.add_user('Phil', 100)
        #test if user and value is in the hash table
        self.assertTrue([('Phil', 100)] in t1.hash_table)

        t1.add_user('Ash', 34)
        self.assertTrue([('Ash', 34)] in t1.hash_table)

        t1.add_user('George', 72521)
        self.assertTrue([('George', 72521)] in t1.hash_table)

        #updates certain users value to different value
        t1.add_user('George', 100)
        self.assertFalse([('George', 72521)] in t1.hash_table) # original value should now be false
        self.assertTrue([('George', 100)] in t1.hash_table) # updated value now true

    def test_getuser(self):
        #makes hash table of 100
        t1 = hashtable(100)

        #adding three different users to the table
        t1.add_user('Phil', 100)
        t1.add_user('Ash', 34)
        t1.add_user('George', 72521)

        #testing get_user function if it obtains correct value for each user
        self.assertEqual(t1.get_user('Phil'), 100)
        self.assertEqual(t1.get_user('Ash'), 34)
        self.assertEqual(t1.get_user('George'), 72521)

    def test_deleteuser(self):
        #makes hash table of 100
        t1 = hashtable(100)

        #adding three different users to the table
        t1.add_user('Phil', 100)
        t1.add_user('Ash', 34)
        t1.add_user('George', 72521)

        #deletes each user and tests if user is no longer in hash
        t1.del_user('Phil')
        self.assertTrue(('Phil', 100) not in t1.hash_table)

        t1.del_user('Ash')
        self.assertTrue(('Ash', 34) not in t1.hash_table)

        t1.del_user('George')
        self.assertTrue(('George', 72521) not in t1.hash_table)


class TestBlockchain(unittest.TestCase):
    
    def test_Transaction(self):
        #makes transaction between two users
        t1 = Transaction('Phil', 'Ash', 50)

        #testing which user to which user and the amount
        self.assertEqual('Phil', t1.from_user)
        self.assertEqual('Ash', t1.to_user)
        self.assertEqual(50, t1.amount)

        t2 = Transaction('Ash', 'George', 61)

        self.assertEqual('Ash', t2.from_user)
        self.assertEqual('George', t2.to_user)
        self.assertEqual(61, t2.amount)

    def test_block(self):
        #makes block from transaction
        trans1 = Transaction('Phil', 'Ash', 50)
        block1 = Block([trans1])
        
        #tests if transaction was successfully added to block
        self.assertEqual(block1.transactions, ('Phil', 'Ash', 50))
        
        trans2 = Transaction('George', 'Phil', 90)
        block1.add_transaction(trans2)

        self.assertEqual(block1.transactions, [('Phil', 'Ash', 50), ('George', 'Phil', 90)])

    def test_ledger(self):
        # sets ledger and hash table of 100
        ledger1 = Ledger()
        t1 = hashtable(100)

        #adds three different users to the hash table
        t1.add_user('Phil', 100)
        t1.add_user('Ash', 34)
        t1.add_user('George', 72521)

        #tests if each user has enough funds
        self.assertTrue(ledger1.has_funds(t1,'Phil', 50))
        self.assertTrue(ledger1.has_funds(t1, 'George', 500))
        self.assertTrue(ledger1.has_funds(t1, 'Ash', 20))

        #tests if each user doesn't have enough funds
        self.assertFalse(ledger1.has_funds(t1, 'Phil', 200))
        self.assertFalse(ledger1.has_funds(t1, 'George', 100000))
        self.assertFalse(ledger1.has_funds(t1, 'Ash', 90))

        #deposits coins into a users balance
        ledger1.deposit(t1, 'Phil', 20)
        self.assertEqual(t1.get_user('Phil'), 70)

        #withdraws coins from a users balance
        ledger1.transfer(t1, 'Ash', 15)
        self.assertEqual(t1.get_user('Ash'), 5)



    def test_blockchain(self):
        #creates hash table of 100
        t1 = hashtable(100)

        #adds three users to the hash table
        t1.add_user('Phil', 100)
        t1.add_user('Ash', 34)
        t1.add_user('George', 72521)
        
        #create the first block
        trans1 = Transaction('Phil', 'Ash', 50)
        block1 = Block([trans1])

        #create a second block
        trans2 = Transaction('Ash', 'George', 100)
        block2 = Block[trans2]

        #creates the blockchain
        chain = Blockchain()

        #tests if block is successfully added to change
        chain.add_block(block1)
        self.assertTrue(block1 in chain._blockchain)

        #tests edge case of if block is invalid
        self.assertFalse(chain.add_block(block2))



unittest.main()