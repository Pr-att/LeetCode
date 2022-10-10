nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
l, r = 0, 0
res = 0
while r < (len(nums) - 1):
    maxJump = 0
    for i in range(l, r + 1):
        maxJump = max(maxJump, i + nums[i])
    l = r + 1
    r = maxJump
    res += 1
print(res)
