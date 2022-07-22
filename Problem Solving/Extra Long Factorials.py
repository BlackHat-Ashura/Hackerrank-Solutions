def extraLongFactorials(n):
    '''Direct Method'''
    f = 1
    for i in range(2, n+1):
        f *= i
    print(f)

def extraLongFactorials(n):
    '''Using Arrays'''
    arr = [None]*1000
    length = 1
    carry = 0
    arr[0] = 1
    for i in range(2, n+1):
        for j in range(length):
            multiple = i*arr[j] + carry
            digit = multiple % 10
            arr[j] = digit
            carry = multiple // 10
        while carry:
            digit = carry % 10
            arr[length] = digit
            length += 1
            carry = carry//10
    
    for k in range(length):
        print(arr[length-(k+1)], end="")