for _ in range(int(input())):
    A = int(input())
    a = set(map(int, input().split()))
    B = int(input())
    b = set(map(int, input().split()))
    print(len(a.difference(b)) == 0)
