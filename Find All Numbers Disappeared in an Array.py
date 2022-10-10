nums = [1, 1]
array = {i for i in range(1, len(nums) + 1)}
print(list(array - set(nums)))
