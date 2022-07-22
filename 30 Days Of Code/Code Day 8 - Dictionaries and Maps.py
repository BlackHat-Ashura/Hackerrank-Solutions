def check(ph, test):
    if test in ph:
        print(f"{test}={ph[test]}")
    else:
        print("Not found")
    
if __name__ == '__main__':
    n = int(input())
    ph = {}
    for _ in range(n):
        name_number = input().rstrip().split()
        name = name_number[0]
        number = int(name_number[1])
        ph[name] = number
    while True:
        try:
            test = input()
            check(ph, test)
        except:
            break
