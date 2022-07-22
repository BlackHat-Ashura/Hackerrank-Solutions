total_swaps = 0
for i in range(n-1):
    swaps = 0
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swaps += 1
    if swaps == 0:
        break
    total_swaps += swaps
print(f"Array is sorted in {total_swaps} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")