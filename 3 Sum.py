nums = [1, -1, 1, -1, 0, 0]
nums.sort()
k = 0
bigArray = []
prev = -1 * float("inf")
if len(nums) >= 3:
    while k != len(nums) - 2:
        if nums[k] == prev:
            k += 1
            continue
        i, j = k + 1, len(nums) - 1
        a = nums[k]
        if a >= 0:
            req = a
        else:
            req = -1 * a
        while i < j:
            if sum([nums[i], nums[j]]) > req:
                j -= 1
            elif sum([nums[i], nums[j]]) < req:
                i += 1
            else:
                bigArray.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
        k += 1
        prev = nums[k - 1]
    new = []
    for i in bigArray:
        if i not in new:
            new.append(i)
    print(new)
else:
    print([])