def pickingNumbers(a):
    dictionary = {}
    """
    dictionary = {1: <number of 1s>, 2: <number of 2s>,.....,99: <number of 99s>}
    """
    for i in a:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
            
    for i in range(1, 100):
        if i not in a:
            dictionary[i] = 0
    
    max_subarr = 0
    for i in range(1, 99):
        max_subarr = max(max_subarr, dictionary[i]+dictionary[i+1])
    
    return max_subarr