num = 3278
myMap = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
symbols = [1000, 500, 100, 50, 10, 5, 1]
i = 0
final = ""
temp = []
num = str(num)
lengthNum = len(num) - 1
for index, var in enumerate(num[::-1]):
    ans = 10 ** index
    temp.append(ans * int(var))
temp = temp[::-1]
for inp, key in enumerate(temp):
    if key in myMap:
        final += myMap[key]
    else:
        second = abs(inp - lengthNum)
        first = key // (10 ** second)
        if first == 4 and second != 0:
            final += myMap.get(10 ** second) + myMap.get((10 ** second) + key)
        elif first == 9 and second != 0:
            final += myMap.get(10 ** second) + myMap.get((10 ** second) + key)
        elif first == 4 and second == 0:
            final += 'IV'
        elif first == 9 and second == 0:
            final += 'IX'
        elif first not in [4, 9] and first < 5:
            final += myMap[10 ** second] * first
        elif first not in [4, 9] and first > 5:
            final += myMap[5 * (10 ** second)] + myMap[10 ** second] * abs(first - 5)
print(final)
