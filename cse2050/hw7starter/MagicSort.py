from math import log2
import math

global reverse
global insertion
global quick
global merge

reverse = False
insertion = False
quick = False
merge = False

def linear_scan(L):

    if sorted(L) == L: # Base Case if already sorted just return original list
        return L
    
    if sorted(L, reverse = True) == L: #if reversed apply reverse_list()
        return reverse_list(L)
    
    if sum(x != y for (x, y) in zip(sorted(L), L)) <= 5: # if list has < 5 elements
        return insertionsort(L) # insertionsort it
    
    if sum(x != y for (x, y) in zip(sorted(L), L)) >= 5: # if list has > 5 elements
        return quicksort(L) # quicksort it

def reverse_list(L):
    global reverse
    global insertion
    global quick
    global merge

    insertion = False
    quick = False
    merge = False
    reverse = True # make reverse True as you use it


    for i in range(len(L) // 2):
        L[i], L[-i-1] = L[-i-1], L[i] # switches order of first and last index, then second and second to last index and so on

    return L



def insertionsort(L, left = 0, right = None):
    global reverse
    global insertion
    global quick
    global merge

    reverse = False
    insertion = True # makes insertion equal True
    quick = False
    merge = False


    if right != None: # if there's a bound on right side
        L = L[left: right] # apply bounds
    
    else:
        L = L[left:] # else just use applied left bound to end of list

    for i in range(len(L)): # for all values in list

        for j in range(len(L)-i, len(L)): # all values next to one another

            if L[j-1] > L[j]: # if first value bigger than second value
                L[j], L[j-1] = L[j-1], L[j] # swap indexes
    
    return L

def quicksort(L, counter = 0):
    global reverse
    global insertion
    global quick
    global merge

    reverse = False
    insertion = False
    quick = True # makes quicksort equal True
    merge = False

    if len(L) < 2: # Base Case
        return L
    
    max_counter = math.log2(len(L))+1 # best case maximum depth

    if counter > max_counter: # if above best case max depth
        counter = 0
        return mergesort(L) # finish with mergesort

    pivot = L[-1] # last index pivot
    LT = [e for e in L if e < pivot] # Less than pivot
    ET = [e for e in L if e == pivot] # equal to pivot
    GT = [e for e in L if e > pivot] # greater than pivot

    counter += 1 # sort LT and GT lists
    A = quicksort(LT, counter)
    B = quicksort(GT, counter)
    

    return A + ET + B # finished list

def mergesort(L):
    global merge # only one global variable as it's usually called from quicksort
    merge = True # makes mergesort equal True
   #Base Case
    if len(L) == 1:
        return L
    
    #Divide
    mid = len(L)//2
    A = L[:mid]
    B = L[mid:]

    #Conquer
    mergesort(A)
    mergesort(B)

    #Combine 
    i , j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+j] = A[i]
            i = i +1
        else:
            L[i+j] = B[j]
            j = j +1
    L[i+j:]  = A[i:] + B[j:]
    return L
def magic_sort():
    magic = set() # sets the set
    global reverse
    global insertion
    global quick
    global merge
    if reverse == True: # if reverse sorted add to set
        magic.add('reversesort')

    if insertion == True: # if insertion sorted add to set
        magic.add('insertionsort')
    
    if quick == True: # if quick sorted add to set
        magic.add('quicksort')

    if merge == True: # if merge sorted add to set
        magic.add('mergesort')

    return magic # return set