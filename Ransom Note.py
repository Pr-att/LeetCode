ransomNote = "a"
magazine = "b"
map1, map2 = {}, {}
for i in ransomNote:
    if i in map1:
        map1[i] += 1
    else:
        map1[i] = 1
for i in magazine:
    if i in map2:
        map2[i] += 1
    else:
        map2[i] = 1
count, l = 0, 0
for key, value in map1.items():
    count += 1
    if key in map2 and value <= map2[key]:
        l += 1
if count == l:
    print(True)
else:
    print(False)