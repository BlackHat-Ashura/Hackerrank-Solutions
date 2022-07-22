n = int(input())
for _ in range(n):
    try:
        a, b = list(map(int, input().split()))
        print(a//b)
    except ZeroDivisionError as D:
        print("Error Code:", D)
    except ValueError as V:
        print("Error Code:", V)
