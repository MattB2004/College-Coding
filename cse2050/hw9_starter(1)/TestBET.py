import unittest
from BET import BETNode, create_trees, find_solutions


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left('A')
        root.add_right('-')
        root.right.add_left('2')
        root.right.add_right('+')
        root.right.right.add_left('3')
        root.right.right.add_right('4')
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self):
        # builds tree
        root = BETNode('+')
        root.add_left('2')
        root.add_right('-')
        root.right.add_left('5')
        root.right.add_right('/')
        root.right.right.add_left('Q')
        root.right.right.add_right('1')

        # evaluation == expected result
        expected_result = -5
        self.assertEqual(root.evaluate(), expected_result)

    def test_evaluate_tree2(self):
        # builds tree
        root = BETNode('+')
        root.add_left('+')
        root.add_right('-')
        root.right.add_left('5')
        root.right.add_right('3')
        root.left.add_left('6')
        root.left.add_right('1')

        # evaluation == expected result
        expected_result = 9
        self.assertEqual(root.evaluate(), expected_result)

    def test_evaluate_tree3(self):
        # builds tree
        root = BETNode('/') # divides 7 by 0 here
        root.add_left('+')
        root.add_right('-')
        root.right.add_left('5')
        root.right.add_right('5')
        root.left.add_left('6')
        root.left.add_right('1')

        # evaluation == expected result
        expected_result = 'Divide by 0'
        self.assertEqual(root.evaluate(), expected_result)

class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        #given hand
        hand = ['4','2','7','9']

        # expected possible trees
        self.assertTrue('4972/+-' in create_trees(hand))
        self.assertTrue('92*74//' in create_trees(hand))
        self.assertTrue('742-/9*' in create_trees(hand))

        # always 7680 trees created no matter the hand
        self.assertEqual(len(create_trees(hand)), 7680)
        
    def test_hand2(self):
        # given hand
        hand = ['Q','A','J','6']

        # expected possible trees
        self.assertTrue('QJA6/+-' in create_trees(hand))
        self.assertTrue('6J*QA+/' in create_trees(hand))
        self.assertTrue('Q6A++J*' in create_trees(hand))

        # always 7680 trees created no matter the hand
        self.assertEqual(len(create_trees(hand)), 7680)
        

class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        # given unsolvable hand
        hand = ['1','1','10','J']

        # expected solutions is 0
        self.assertEqual(len(find_solutions(hand)), 0)

    def test_A23Q(self):
        # given solvable hand
        hand = ['A','2','3','Q']

        # expected solutions is 33
        self.assertEqual(len(find_solutions(hand)), 33)
        
unittest.main()