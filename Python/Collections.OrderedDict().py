import collections

N = int(input())
ordered_dictionary = collections.OrderedDict()
for _ in range(N):
    item_price = input().split()
    item = " ".join(item_price[:-1])
    ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(item_price[-1])

for item in ordered_dictionary:
    print(item, ordered_dictionary[item])
