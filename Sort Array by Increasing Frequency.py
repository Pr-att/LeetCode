nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
maps = {}
for i in nums:
    if i in maps:
        maps[i] += 1
    else:
        maps[i] = 1

u = list(maps.keys())
for i in range(len(u)):
    for k in range(i + 1, len(u)):
        if maps.get(u[k]) > maps.get(u[i]):
            pass
        elif maps.get(u[k]) < maps.get(u[i]):
            u[k], u[i] = u[i], u[k]
        else:
            u[k], u[i] = min(u[k], u[i]), max(u[k], u[i])

new = []
for i in u:
    for k in range(maps[i]):
        new.append(i)
print([*new])
