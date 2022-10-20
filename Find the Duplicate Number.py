nums = [1, 3, 2, 2, 4]
myMap = {}


def solution():
    for i in nums:
        if i in myMap:
            myMap[i] += 1
        else:
            myMap[i] = 1
    for key, value in myMap.items():
        if value > 1:
            return key

print(solution())