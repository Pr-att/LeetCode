words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
myMap = {}
for i in words:
    if i in myMap:
        myMap[i] += 1
    else:
        myMap[i] = 1
newMap = sorted(myMap.items(), key=lambda x: x[1], reverse=True)
length = []
for k in range(len(myMap)):
    if newMap[k][1] not in length:
        length.append(newMap[k][1])
final = []
for rt in range(len(length)):
    new = []
    for o in range(len(newMap)):
        if newMap[o][1] == length[rt]:
            new.append(newMap[o][0])
        new.sort()
    final += new
print(final[:k + 1])