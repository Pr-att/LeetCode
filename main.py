def factors(num):
    length = 0
    myList = []
    for i in range(1, num + 1):
        if num % i == 0:
            length += 1
            myList.append(i)
    if length == 2:
        return myList[0]
    else:
        return myList[length // 2]

count = 0
def downToZero(n):
    global count
    if n == 1:
        return count + 1
    temp = factors(n)
    if  temp == 1:
        n -= 1
        count += 1
        return downToZero(n)
    else:
        n = max(temp, n // temp)
        count += 1
        return downToZero(n)

print(downToZero(4))