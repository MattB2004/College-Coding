from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        dll = DLL(range(6))
        self.assertTrue(dll.__contains__(4)) # dict contains 4
        self.assertTrue(dll.__contains__(2)) # dict contains 2
        self.assertTrue(dll.__contains__(0)) # dict contains 0
        self.assertFalse(dll.__contains__(6)) # dict does not contains 6
        self.assertFalse(dll.__contains__(10)) # dict does not contains 10
    def test_neighbors(self):
        dll = DLL(range(6))
        self.assertEqual(dll.neighbors(4), (3, 5)) # 4 has neighbors of 3 and 5
        self.assertEqual(dll.neighbors(2), (1, 3)) # 2 has neighbors of 1 and 3
        self.assertEqual(dll.neighbors(5), (4, None)) # end of list so 5 has neighbors of 4 and None
        self.assertEqual(dll.neighbors(0), (None, 1)) # beginning of list so 0 has neighbors of None and 1
    def test_remove_item(self):
        dll = DLL(range(6))
        self.assertEqual(dll._len, 6) # length of list is 6
        self.assertEqual(dll.remove_node(3), 3) # removes 3
        self.assertEqual(dll._len, 5) # length of list is now 5
        self.assertEqual(dll.remove_node(5), 5) # removes 5 (tail of list)
        self.assertEqual(dll._len, 4) # length of list is now 4
        self.assertEqual(dll.remove_node(0), 0) # removes 0 (head of list)
        self.assertEqual(dll._len, 3) # length of list is now 3

        

unittest.main()
