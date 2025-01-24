# TODO: implement the 4 functions (as always, include docstrings & comments)

def find_zero(L):
    if len(L) == 0:
        raise RuntimeError('0 Not Found in List')
    low = 0
    high = len(L) - 1
    mid = 0

    while low <= high:
 
        mid = (high + low) // 2
 
        if L[mid] < 0: # If mid is negative, ignore left half
            low = mid + 1
 
        elif L[mid] > 0: # If mid is positive, ignore right half
            high = mid - 1
 
        else: # means 0 is present at mid
            return mid
    
def bubble(L, left, right): 
    lst = L[left: right] # slices list to fit the halfsort
    swapped = False
    for iterator in range(len(lst) - 1): # for all the values in list 

        for j in range(len(lst) - 1 - iterator):

            if lst[j] > lst[j+1]: # if first index bigger than next index
                swapped = True # swapped
                lst[j], lst[j+1] = lst[j+1], lst[j] # swap takes place

        if not swapped: # breaks loop
            return

def selection(L, left, right):
    L = L[left: right] # slices list to fit the halfsort

    for i in range(len(L) - 1): # for all values in list
        max_index = 0 # max_index 0 default
        for j in range(len(L) - 1):

            if L[j] > L[max_index]: # if value bigger than max_index
                max_index = j # new max_index

        L[-1-i], L[max_index] = L[max_index], L[-1-i] # swap max_index and current value

def insertion(L, left, right):
    L = L[left: right] # slices list to fit the halfsort

    for i in range(len(L)): # for all values in list

        for j in range(len(L)-i, len(L)): # all values next to one another

            if L[j-1] > L[j]: # if first value bigger than second value
                L[j], L[j-1] = L[j-1], L[j] # swap indexes
                
def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, bubble)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    sort(L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half