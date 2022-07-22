if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    list_ = list(arr)
    max_ = -100
    runner = -100
    
    for i in list_:
        if max_ < i:
            max_ = i
        for j in list_:
            if j < max_ and j > runner:
                runner = j

    print(runner)


#####################################################

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    list_ = list(set(list(arr)))
    list_.sort()
    print(list_[-2])
