def nonDivisibleSubset(k, s):
    rem = [0]*k
    '''
    rem holds remainder as index.
    index 0 = 0 remainder
    .
    .
    .
    index k-1 = k-1 remainder
    '''

    for i in s:
        rem[i%k] += 1
        '''
        This for loop is for assigning count of remainders.
        '''
    
    max_len = 0
    max_len += min(rem[0], 1)
    '''
    If any number divisible by k exists, then only one of them can
    exist in subset as the sum of both is divisible by k.
    '''
    
    if k%2 == 0:
        max_len += min(rem[k//2], 1)
        '''
        if k is even,
        Then sum of 2 numbers leaving remainder k/2 add up to be divisible by k.
        '''
    
    for i in range(1, k//2+1):
        if i != k-i:
            max_len += max(rem[i], rem[k-i])
            '''
            i starts from 1 as zero remainder is neglected.
            The concept if this loop is that
            1 remainder numbers and k-1 remainder numbers add up to be
            divisible by k.
            If k is even, odd number of remainders are compared.
                eg:- for k=6; 1, 2, 3, 4, 5 remainders are compared.
                     i -> 1 to 3
                     Last case: i != k-i --> 3 != 3
            If k is odd, even number of remainders are compared.
                eg:- for k=5; 1, 2, 3, 4 remainders are compared.
                     i -> 1 to 2
                     Last case: i != k-i --> 2 != 3
            '''
    
    return max_len