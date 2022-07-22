def workbook(n, k, arr):
    pageNo = 1
    result = 0
    for problems in range(n):
        for problemNo in range(1, problems+1):
            if problemNo == pageNo:
                result += 1
            if problemNo == problems or problemNo%k == 0:
                pageNo += 1
    return result