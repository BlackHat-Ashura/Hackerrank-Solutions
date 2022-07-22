import collections
D = collections.deque()

for _ in range(int(input())):
    eval("D.{0}({1})".format(*input().split() + [' ']))

print(*D)
