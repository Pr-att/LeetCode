nums = [2, 1, 1, 2]
if len(nums) < 2:
    print(nums)
elif len(nums) == 2:
    print(max(nums))
else:
    mex = float("-inf")
    for i in range(2, len(nums)):
        if nums[i - 2] >= mex:
            mex = nums[i - 2]
        nums[i] += mex
    print(max(nums))
