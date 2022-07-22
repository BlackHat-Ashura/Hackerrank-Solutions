def binary(n):
    if n>=0:
            if n in (0, 1):
                return n
            else:
                return binary(n//2)*10 + n%2    

def countOnes(n):
    c = 0
    max_ = 0
    for i in str(n):
        if i is '1':
            c += 1
            if max_ < c:
                max_ = c
        else:
            c = 0
    print(max_)    

if __name__ == '__main__':
    n = int(input())
    countOnes(binary(n))