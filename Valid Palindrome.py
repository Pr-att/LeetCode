s = " "
newS = ''
for i in s:
    if i.isalnum():
        newS += i
newS = newS.lower()
j, k = 0, len(newS) - 1
count = 0
while k - j > 0:
    if newS[j] == newS[k]:
        j += 1
        k -= 1
    else:
        count = 1
        break
if count == 0:
    print(True)
else:
    print(False)
