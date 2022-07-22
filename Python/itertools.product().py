import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))
AxB = list(itertools.product(A, B))
print(*AxB)
