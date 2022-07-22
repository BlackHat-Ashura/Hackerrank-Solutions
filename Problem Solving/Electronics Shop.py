def getMoneySpent(keyboards, drives, b):
    max_ = -1
    for keyboard in keyboards:
        for drive in drives:
            sum_ = keyboard + drive
            if sum_ <= b:
                if max_ < sum_:
                    max_ = sum_
    return max_