nums = [3, 2, 1, 0, 4]
lastNo = len(nums) - 1
total, c = nums[0], 1
for i in range(1, len(nums)):
    if i > total:
        c = 0
        break
    elif total >= lastNo:
        c = 1
        break
    j = i + nums[i]
    total = max(total, j)
    c = 0

if c == 1:
    print(True)
elif c == 0:
    print(False)
