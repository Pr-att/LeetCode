n = 19
hset = set()
while n != 1:
    if n in hset: 
        print(False)
        break
    hset.add(n)
    n = sum([int(i) ** 2 for i in str(n)])
else:
    print(True)