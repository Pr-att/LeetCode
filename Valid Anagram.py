s = "anagram"
t = "nagaram"
mapS, mapK = {}, {}
for i in s:
    if i in mapS:
        mapS[i] += 1
    else:
        mapS[i] = 1
for i in t:
    if i in mapK:
        mapK[i] += 1
    else:
        mapK[i] = 1
if mapK == mapS:
    print(True)
else:
    print(False)
