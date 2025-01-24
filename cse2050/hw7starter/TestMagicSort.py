import unittest
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort


class Test_linear_scan(unittest.TestCase):
    def test_sorted(self): # test base case sorted list
        L = [1,2,3,4,5,6,7,8,9,10]
        linear_scan(L)
        self.assertEqual(L, [1,2,3,4,5,6,7,8,9,10])
        

    def test_reversed(self): # test reverse scan
        L = [10,9,8,7,6,5,4,3,2,1]
        self.assertEqual(linear_scan(L), [1,2,3,4,5,6,7,8,9,10])

    def test_insertion(self): # test insertion when list < 5
        L = [3,2,4,1]
        self.assertEqual(linear_scan(L), [1,2,3,4])

    def test_quick_and_merge(self): # test quick and merge when list > 5
        L = [10,9,8,7,6,5,4,3,1,2]
        self.assertEqual(linear_scan(L), [1,2,3,4,5,6,7,8,9,10])

class Test_reverse_list(unittest.TestCase):
    def test_reversed(self): # test reverse sort directly
        L = [10,9,8,7,6,5,4,3,2,1]
        reverse_list(L)
        self.assertEqual(L, [1,2,3,4,5,6,7,8,9,10])


class Test_insertionsort(unittest.TestCase):
    def test_insertion(self): # test insertion sort directly
        L = [10,5,3,1,4,6,8,7,9,2]
        
        self.assertEqual(insertionsort(L), [1,2,3,4,5,6,7,8,9,10])

class Test_quicksort(unittest.TestCase):
    def test_quick(self): # test quick sort directly
        L = [1,2,4,3,10,6,8,7,9,5] # makes counter less than max_counter
        self.assertEqual(quicksort(L), [1,2,3,4,5,6,7,8,9,10])

    def test_merge_switch(self): # test quick sort into merge sort
        L = [10,9,8,7,6,5,4,3,2,1] # makes counter greater than max_counter
        self.assertEqual(quicksort(L),[1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(magic_sort(), {'quicksort', 'mergesort'}) # tests that it uses both quick and merge sort
    
class Test_mergesort(unittest.TestCase):
    def test_merge(self): # test merge sort directly
        L = [10,9,8,7,6,5,4,3,2,1]
        mergesort(L)
        self.assertEqual(L, [1,2,3,4,5,6,7,8,9,10])

class Test_magicsort(unittest.TestCase):
    def test_magic1(self): # magic list reverse only
        L = [10,9,8,7,6,5,4,3,2,1]
        linear_scan(L)
        self.assertEqual(magic_sort(), {'reversesort'})

    def test_magic2(self): # magic sort insertion only
        L = [3,2,4,1]
        linear_scan(L)
        self.assertEqual(magic_sort(), {'insertionsort'})

    def test_magic3(self): # magic sort quick only
        L = [1,2,4,3,10,6,8,7,9,5]
        linear_scan(L)
        self.assertEqual(magic_sort(), {'quicksort'})

    def test_magic4(self): # magic sort quick into merge
        L = [10,9,8,7,6,5,4,3,1,2]
        linear_scan(L)
        self.assertEqual(magic_sort(), {'quicksort', 'mergesort'})

unittest.main()