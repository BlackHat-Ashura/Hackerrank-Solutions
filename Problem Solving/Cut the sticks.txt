def cutTheSticks(arr):
    a = []
    while arr != []:
        count = 0
        mini = min(arr)
        for i in range(len(arr)):
            if arr[i] >= mini:
                arr[i] = arr[i] - mini
                count += 1
        arr = [i for i in arr if i > 0]
        a.append(count)
    return a