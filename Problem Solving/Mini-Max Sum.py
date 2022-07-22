def miniMaxSum(arr):
    maxarr = arr.copy()
    maxsum = 0
    for i in range(len(maxarr)-1):
        maxsum += max(maxarr)
        maxarr.remove(max(maxarr))
    minarr = arr.copy()
    minsum = 0
    for j in range(len(minarr)-1):
        minsum += min(minarr)
        minarr.remove(min(minarr))
    print(minsum, maxsum)