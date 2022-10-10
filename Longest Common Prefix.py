strs = ["a", "ae"]
j = 0
count = 0
s = ''
while True:
    try:
        p = [i[j] for i in strs]
        if len(set(p)) > 1:
            break
        else:
            s += p[0]
        j += 1
    except IndexError:
        break
print(s)
