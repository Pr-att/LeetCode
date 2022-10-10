words = ["a", "b", "c"]
pattern = "a"
pat = len(set(pattern))
maps = {}
final = []
p = 0
for k in pattern:
    if k not in maps:
        maps[k] = p
        p += 1
string = ''
for i in pattern:
    string += str(maps[i])
for i in words:
    if len(set(i)) == pat:
        new = {}
        p = 0
        for j in i:
            if j not in new:
                new[j] = p
                p += 1
        newString = ''
        for k in i:
            newString += str(new[k])
        if newString == string:
            final.append(i)
print([*final])
