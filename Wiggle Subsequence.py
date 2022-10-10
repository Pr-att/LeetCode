import random

nums = [random.randint(0, 155) for _ in range(100)]
print(nums)
maxi = float("-inf")
increase = 1
decrease = 1
for i in range(1, len(nums)):
    if nums[i - 1] > nums[i]:
        increase = decrease + 1
    elif nums[i - 1] < nums[i]:
        decrease = increase + 1
if increase >= decrease:
    maxi = increase
else:
    maxi = decrease
print(maxi)
