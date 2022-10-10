s = "AB"
k = 1
if 0 < len(s) < 2:
    print(1)
elif len(s) == 0:
    print(0)
else:
    i, j, c, maX = 0, 0, 0, float("-inf")
    hashmap = {}
    while j < len(s):
        if s[j] in hashmap:
            hashmap[s[j]] += 1
            maX = (j - i + 1) - max(hashmap.values())
        else:
            hashmap[s[j]] = 1
            maX = (j - i + 1) - max(hashmap.values())
        j += 1
        if maX > k:
            hashmap[s[i]] -= 1
            i += 1
        maX = j - i

    print(maX)

"""
In this Sliding window problem , we calculated the longest string possible while using entire k.
We calculated max value of any key in hashmap and determined the value of (j - i) - max value,
this gave us the value which we check with the k value provided , so as to keep to a check whether it exceeded it 
or not. If it did exceed k , we increased k by 1 and decreased the count of element i - 1 in the hashmap.
"""