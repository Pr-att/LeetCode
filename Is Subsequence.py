s = "abc"
t = "ahbgdc"
i, j = 0, 0
count = 0
while i != len(s) - 1:
    if j >= len(t):
        break
    if s[i] == t[j]:
        count += 1
        i += 1
        j += 1
    else:
        j += 1
if len(s) == count:
    print(True)
else:
    print(False)