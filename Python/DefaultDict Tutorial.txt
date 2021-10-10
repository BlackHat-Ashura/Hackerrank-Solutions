import collections

n, m = list(map(int, input().split()))
A = collections.defaultdict(list)
B = list()

for i in range(n):
    A[input()].append(i+1)

for _ in range(m):
    B_item = input()
    if B_item in A:
        print(" ".join(map(str, A[B_item])))
    else:
        print("-1")
