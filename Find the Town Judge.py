def findJudge(n, trust):
    length = len(trust)
    if length == 0 and n > 1:
        return -1
    elif length == 0 and n == 1:
        return 1
    array = [0] * n
    for i in range(length):
        array[trust[i][0] - 1] = -1
        if array[trust[i][1] - 1] == -1:
            pass
        else:
            array[trust[i][1] - 1] += 1
    Max = float("-inf")
    res = 0
    countOne = 0
    for index, value in enumerate(array):
        if value != 0:
            countOne += 1
        if value > Max:
            Max = value
            res = index
    if Max == countOne - 1:
        return res + 1
    else:
        return - 1
print(findJudge(3, [[1,3],[2,3],[3,1]]))