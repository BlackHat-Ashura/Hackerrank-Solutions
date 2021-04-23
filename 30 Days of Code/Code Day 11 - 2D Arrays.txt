def Hour(arr):
    rn = len(arr)
    cn = len(arr[0])
    max_ = 0
    for row in range(rn-2):
        for col in range(cn-2):
            count = sum(arr[row][col:col+3]) + arr[row+1][col+1] + sum(arr[row+2][col:col+3])
            if row == 0 and col == 0:
                max_ = count
            if max_ < count:
                max_ = count
    return max_

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(Hour(arr))
