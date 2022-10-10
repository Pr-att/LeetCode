s = "leetcode"
hashmap = {}
for i in s:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1
for key, value in hashmap.items():
    if value == 1:
        print(s.index(key))
print(-1)