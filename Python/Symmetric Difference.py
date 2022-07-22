M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

p = a.difference(b)
q = b.difference(a)
union_of_difference = p.union(q)
for i in sorted(list(union_of_difference)):
    print(i)
