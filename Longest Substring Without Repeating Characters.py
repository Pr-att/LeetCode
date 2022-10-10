s = "au"
# print(len(s))
if 0 < len(s) < 2:
    print(1)
elif len(s) == 0:
    print(0)
else:
    hashmap = {}
    count, i, j = 1, 0, 1
    hashmap[s[i]] = 1
    maX = -1 * float("inf")
    while j < len(s):
        if s[j] in hashmap:
            hashmap = {}
            maX = max(count, maX)
            count = 1
            i += 1
            j = i + 1
            hashmap[s[i]] = 1
        else:
            hashmap[s[j]] = 1
            count += 1
            j += 1
            maX = max(count, maX)
    print(maX)

"""
pwpwww
"""
