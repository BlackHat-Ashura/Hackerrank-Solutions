import collections

K = int(input())
rooms = list(map(int, input().split()))

family_rooms = collections.Counter(rooms)
print(*[key for key in family_rooms if family_rooms[key] == 1])
