def average(array):
    distinct_heights = set(array)
    average = sum(distinct_heights)/len(distinct_heights)
    return average
