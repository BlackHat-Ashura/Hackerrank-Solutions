def beautifulTriplets(d, arr):
    count = 0
    for num in arr:
        if num+d in arr and num+2*d in arr:
            i = arr.index(num)
            j = arr.index(num+d)
            k = arr.index(num+2*d)
            if i < j < k:
                count += 1
    return count