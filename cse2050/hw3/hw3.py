def find_pairs_naive(lst, target):
    pairs = set() # 1
    for i in range(len(lst)): # n
         for j in range(len(lst)): # n
             if (lst[i]+lst[j]==target) and (lst[i]<=lst[j]) and (lst[i]!=lst[j]): # 2
                  pairs.add((lst[i],lst[j])) # 1
    return pairs # 1
                           # 1 + n(2n) + 1 + 1 = O(n^2)

def find_pairs_optimized(lst, target):
    pairs = set() # 1
    lst1 = lst # 1
    while lst: # n
        number = lst1.pop() # 1
        diff = target - number # 1
        if diff in lst: # 1
            pairs.add((diff, number)) # 1
    return pairs # 1
                        # 1 + 1 + n(1 + 1 + 1(1)) + 1 = O(n)

def measure_min_time(fn, arg1, arg2):
    import time
    results = []
    for x in range(10):
        start_time = time.time()
        fn(arg1, arg2)
        end_time = time.time()
        results.append(end_time - start_time)
    return min(results)


if __name__ == "__main__":
    print('n     naive     optimized')
    print('***************************')
    lst = list(range(0,10))
    lst2 = list(range(0,10))
    n_list = [10, 200, 400, 600, 800, 1000]
    for n in n_list:
        print(f'{n}     {(measure_min_time(find_pairs_naive, lst, n)):.4f}      {(measure_min_time(find_pairs_optimized, lst2, n)):.4f}')
        lst2 = list(range(0,10))
        lst2.extend(range(100,300))
        lst.extend(range(100,300))