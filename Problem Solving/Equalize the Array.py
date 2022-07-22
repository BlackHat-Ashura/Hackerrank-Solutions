def equalizeArray(arr):
    ar = dict()
    for i in arr:
        if i in ar:
            ar[i] += 1
        else:
            ar[i] = 1
    return len(arr) - max(ar.values())