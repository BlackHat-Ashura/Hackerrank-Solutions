import collections

entries = int(input())
spread_sheet = collections.namedtuple("spread_sheet", input())
marks = [int(spread_sheet(*input().split()).MARKS) for _ in range(entries)]
print(sum(marks)/entries)
