numRows = 5
default = [[1], [1, 1]]
if numRows == 1:
    print([[1]])
elif numRows == 2:
    print([[1], [1, 1]])
else:
    p = 2
    for i in range(numRows - 2):
        default.append([1])
        for j in range(i + 1):
            default[p].append(sum(default[p - 1][j:j + 2: 1]))
        default[p].append(1)
        p += 1
print(default)