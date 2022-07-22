def migratoryBirds(arr):
    types = [0]*5
    for i in arr:
        types[i-1] += 1
    return types.index(max(types))+1