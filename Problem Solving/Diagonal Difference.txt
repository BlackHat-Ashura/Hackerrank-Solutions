def diagonalDifference(arr):
    prim = 0
    secon = 0
    for i in range(len(arr)):
        prim += arr[i][i]
        secon += arr[i][-(i+1)]
    return abs(prim - secon)