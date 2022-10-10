nums = [-1, 1, 0, -3, 3]
no_of_zeros = nums.count(0)
ans = 1
for i in nums:
    if i != 0:
        ans *= i

a = []
for i in nums:
    if no_of_zeros < 1:
        a.append(ans // i)
    elif no_of_zeros == 1:
        if i != 0:
            a.append(0)
        else:
            a.append(ans)
    else:
        a.append(0)
print(a)
