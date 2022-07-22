def isPrime(num):
    for i in range(2, int(num**0.5 + 1)):
        if num % i is 0:
            return False
    return True
    
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        i =int(input())
        if i >= 2 and isPrime(i):
            print("Prime")
        else:
            print("Not prime")