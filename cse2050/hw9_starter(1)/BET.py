class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self, value): 
        if self.left == None: # makes sure nothing is left
            self.left = BETNode(value) # makes value a left node in tree
            return self.left
        
        else: self.left.add_left(value) # if left exists add left node to already existing left node

    def add_right(self, value): 
        if self.right == None: # makes sure nothing is right
            self.right = BETNode(value) # makes value a right node in tree
            return self.right
        
        else: self.right.add_right(value) # if right exists add right node to already existing right node

    def evaluate(self): 
        # base calculations
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x / y}

        # if an operation is called
        if self.value in BETNode.OPERATORS:

            # recursive call Left and Right Sums
            LeftSum = self.left.evaluate()
            RightSum = self.right.evaluate()

            # edge case of dividing by 0
            if RightSum == 0 and self.value == '/':
                return 'Divide by 0'
            
            # calculate operation
            else:
                return op[self.value](LeftSum, RightSum)
        
        # return the value if no operation is called
        else:
            return self.CARD_VAL_DICT.get(self.value)

    
    def __repr__(self):
        # if operation called recursuve call the unevaluated operation
        if self.value in BETNode.OPERATORS:
            return f'({repr(self.left)}{self.value}{repr(self.right)})'
            
        # else return said value if no operation is called    
        else:
            return f'{self.value}'


def create_trees(drawn_cards = []):
    import itertools

    # makes list of every possible combination of operations and hand orders
    ops = ['+','-','*','/']
    op_combs = [''.join(op_comb) for op_comb in itertools.product(ops, repeat=3)]

    card_combs = [''.join(drawn_cards) for drawn_cards in itertools.permutations(drawn_cards)]

    # seperates all 5 shapes of a possible tree
    shape1 = []
    shape2 = []
    shape3 = []
    shape4 = []
    shape5 = []


    # generates all possible trees for shape1
    for i in range(len(card_combs)):
        for j in range(len(op_combs)):
            tree = card_combs[i] + op_combs[j]
            parts = list(tree)
            tree = parts[0] + parts[1] + parts[4] + parts[3]+ parts[2] + parts[5] + parts[6]
            shape1.append(tree)

    # generates all possible trees for shape2
    for i in range(len(card_combs)):
        for j in range(len(op_combs)):
            tree = card_combs[i] + op_combs[j]
            parts = list(tree)
            tree = parts[0] + parts[1] + parts[5] + parts[3]+ parts[4] + parts[2] + parts[6]
            shape2.append(tree)

    # generates all possible trees for shape3
    for i in range(len(card_combs)):
        for j in range(len(op_combs)):
            tree = card_combs[i] + op_combs[j]
            parts = list(tree)
            tree = parts[0] + parts[1] + parts[2] + parts[5]+ parts[4] + parts[3] + parts[6]
            shape3.append(tree)

    # generates all possible trees for shape4
    for i in range(len(card_combs)):
        for j in range(len(op_combs)):
            tree = card_combs[i] + op_combs[j]
            parts = list(tree)
            tree = parts[0] + parts[1] + parts[2] + parts[4]+ parts[3] + parts[5] + parts[6]
            shape4.append(tree)
    
    # generates all possible trees for shape5
    for i in range(len(card_combs)):
        for j in range(len(op_combs)):
            shape5.append(card_combs[i] + op_combs[j])

    # combines total amount of trees into one set
    total_trees = shape1 + shape2 + shape3 + shape4 + shape5

    # returns set
    return total_trees


    
    

def find_solutions(drawn_cards = []):
    # creates all possible trees for given hand
    total_trees = create_trees(drawn_cards)

    # trees that add to 34
    trees24 = []


    # Applies BETNode to make possible trees into functioning python trees
    for i in range(len(total_trees)):
        tree = list(total_trees[i])
        root = BETNode(tree[6])

        root.add_right(tree[5])
        
        # for shape1, shape4, shape5
        if tree[5] not in drawn_cards:

            # shape1 tree
            if tree[4] in drawn_cards and tree[3] in drawn_cards:
                root.right.add_right(tree[4])
                root.right.add_left(tree[3])

                if tree[2] not in drawn_cards:
                    root.add_left(tree[2])

                    root.left.add_right(tree[1])
                    root.left.add_left(tree[0])

            # shape4 tree
            if tree[4] in drawn_cards and tree[3] not in drawn_cards:
                root.right.add_right(tree[4])
                root.right.add_left(tree[3])

                root.right.left.add_right(tree[2])
                root.right.left.add_left(tree[1])
                
                root.add_left(tree[0])

            # shape5 tree
            if tree[4] not in drawn_cards and tree[3] in drawn_cards:
                root.right.add_right(tree[4])
                root.right.add_left(tree[1])

                root.right.right.add_right(tree[3])
                root.right.right.add_left(tree[2])

                root.add_left(tree[0])



        # for shape2 and shape3
        if tree[5] in drawn_cards:
            root.add_left(tree[4])

            # shape2 tree
            if tree[3] in drawn_cards:
                root.left.add_right(tree[3])
                root.left.add_left(tree[2])
                root.left.left.add_left(tree[0])
                root.left.left.add_right(tree[1])

            # shape3 tree
            if tree[3] not in drawn_cards:
                root.left.add_right(tree[3])
                root.left.right.add_left(tree[1])
                root.left.right.add_right(tree[2])
                root.left.add_left(tree[0])
                

        # if given tree evaluates to 24 it adds tree to possible solutions
        if root.evaluate() == 24:
            valid_tree = root.__repr__()
            trees24.append(valid_tree)


    
    # returns all possible solutions
    return trees24
