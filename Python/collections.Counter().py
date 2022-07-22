import collections

X = int(input())
shoe_size_list = list(map(int, input().split()))
shoe_size_dict = dict(collections.Counter(shoe_size_list))
N = int(input())

total = 0
for i in range(N):
    size, cost = map(int, input().split())
    if size in list(shoe_size_dict.keys()):
        if shoe_size_dict[size] != 0:
            total += cost
            shoe_size_dict[size] = shoe_size_dict[size] - 1

print(total)
