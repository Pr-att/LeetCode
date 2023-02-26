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


print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))

# def findJudge(n, trust):
#     # create two arrays to keep track of the number of people trusted and the number of people trusting
#     # each person. Index 0 is unused to make the code more readable.
#     trusted = [0] * (n+1)
#     trusting = [0] * (n+1)

#     # iterate through the trust array to update the trust counts
#     for a, b in trust:
#         trusted[b] += 1
#         trusting[a] += 1

#     # find the person who is trusted by everyone else and trusts nobody
#     for i in range(1, n+1):
#         if trusted[i] == n - 1 and trusting[i] == 0:
#             return i

#     # no town judge was found
#     return -1

# print(findJudge(4, [[1,3],[1,4],[2,3]]))
