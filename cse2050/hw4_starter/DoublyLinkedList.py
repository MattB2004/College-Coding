# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'
    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1
        # add node to dic
        self._nodes[item] = Node(item, _next=self._head, _prev=None)
        
        # if that was the first node
        if len(self) == 1: self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else: self._head._next._prev = self._head

    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1
        # add node to dict
        self._nodes[item] = Node(item, _next=None, _prev=self._tail)
        # if that was the first node
        if len(self) == 1: self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else: self._tail._prev._next = self._tail

    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._head.item

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        #remove from dic
        del self._nodes[item]

        # was that the last node?
        if len(self) == 0: self._tail = None

        else: self._head._prev = None

        return item
        
    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0: raise RuntimeError("cannot remove from empty dll")

        # extract item for later
        item = self._tail.item

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        #remove from dic
        del self._nodes[item]

        # was that the last node?
        if len(self) == 0: self._head = None

        else: self._tail._next = None

        return item
        
    # TODO: Add a docstring and implement
    def __contains__(self, item): # checks if node is in linked list (with dic)
        if item in self._nodes.keys(): # sees if item in dic
            return True # if so return true
        else:
            return False # if so return false

    # TODO: Add a docstring and implement
    def neighbors(self, item):  # checks what nodes are next to item in list (prev and next)
        lst = list(self._nodes.keys()) # turns the dic into list with indexes

        if lst[0] == item: # if begginning of list
            return (None, lst[1])
        
        elif lst[-1] == item: # if end of list
            return (lst[-2], None)

        else: # middle of list
            index = lst.index(item) 
            
            n1 = index - 1 # left of item
            n2 = index + 1 # right of item
            
            return(lst[n1], lst[n2])



    # TODO: Add a docstring and implement
    def remove_node(self, item): # can remove node from list
        if item not in self._nodes: # if item not in the dic
            raise RuntimeError('Not in list')

        if item == self._head: # if start of list
            return self.remove_first(item)

        if item == self._tail: # if end of list
            return self.remove_last(item)
       
        else: # if middle of list
            del self._nodes[item]
            self._len = len(self._nodes)
            return item
