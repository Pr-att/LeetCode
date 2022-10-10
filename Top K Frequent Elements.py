nums = [1, 2, 2, 2, 4, 4, 6]
k = 2
d = {}
for i in nums:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
y = sorted(d.values())
y.reverse()
ans = []
for j in range(k):
    for key, value in d.items():
        if value == y[j]:
            ans.append(key)
            d[key] = 0
            break
print(ans)
