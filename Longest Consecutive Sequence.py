nums = [100, 4, 200, 1, 3, 2]
array = []
n = sorted(list(set(nums)))
count, i = 1, 0
if len(n) == 1:
    print(1)
elif len(n) == 0:
    print(0)
else:
    while i != len(n) - 1:
        try:
            if n[i] - n[i + 1] == -1:
                count += 1
                i += 1
            else:
                i += 1
                count = 1
            array.append(count)
        except IndexError:
            break
    print(max(array))
