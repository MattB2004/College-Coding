from hashmap import hashtable

class Transaction():
    def __init__(self, from_user, to_user, amount):
        #distinguashes users and amounts
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount

    def __str__(self):
        # makes Transaction an object
        return self.from_user, self.to_user, self.amount
    
class Block():
    def __init__(self, transactions=None):
        self.transactions = transactions
        self.previous_block_hash = None

    def add_transaction(self, transaction):
        #if there are no transactions currently in block make it a list so transaction can be added
        if self.transactions == None:
            self.transactions = []
        
        #adds transaction
        self.transactions.append(transaction)
        self.previous_block_hash = transaction

        

class Ledger():
    def __init__(self):
        pass
    
    def has_funds(self, hash, user, amount):
        #edge case if user isn't in the table
        if user not in hash.hash_table:
            return False
        
        #gets current amount of coins from user
        balance = hash.get_user(user)

        #tests if user has sufficent amount of coins
        if balance >= amount:
            return True # if so true
        
        else:
            return False # if not false

    def deposit(self, hash, user, amount):

        #gets current balance from user
        balance = hash.get_user(user)

        #deposits indicated amount
        balance += amount

        #updates users balance
        hash.add_user(user, balance)


    def transfer(self, hash, user, amount):
        
        #gets current balance from user
        balance = hash.get_user(user)

        #withdraws amount from current balance
        balance -= amount

        #updates users balance
        hash.add_user(user, balance)


class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to 
        provide initial balances to one or more users.'''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    # TODO - add the rest of the code for the class here

    def add_block(self, block):
        
        # if user doesn't have proper funds block is invalid
        if self._bc_ledger.has_funds(block[0]) == False:
            return False

        # if block is valid add it to chain
        if self.validate_chain(block, self.last_block) == True:
            self._blockchain.append(block)
        




    def validate_chain(self, current_block, previous_block):

        #if current index of block matches the previous, it's invalid
        if current_block.index != previous_block.index + 1:
            return False

        #if current hash of block matches the previous, it's invalid
        if current_block.previous_hash != previous_block.hash:
            return False

        #returns True if block is valid
        return True