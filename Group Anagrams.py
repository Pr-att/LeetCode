strs = ["hhhhu", "tttti", "tttit", "hhhuh", "hhuhh", "tittt"]
d = {}

for i in strs:
    v = ''.join(sorted(i))

    if v in d:
        d[v].append(i)
    else:
        d[v] = [i]

array = []
# print(d)
for i in d:
    array.append(d[i])
print(array)
