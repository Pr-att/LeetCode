nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

"""
# BruteForce : O(N**3)

ans = sum(nums)
i, j = 0, len(nums) - 1
while True:
    temp = [nums[i] for i in range(i, j + 1)]
    if i == len(nums) - 1 and j == len(nums) - 1:
        new_Ans = sum(temp)
        if new_Ans > ans:
            ans = new_Ans
        break
    if len(temp) == 1:
        new_Ans = sum(temp)
        if new_Ans > ans:
            ans = new_Ans
        j = len(nums) - 1
        i += 1
    else:
        new_Ans = sum(temp)
        if new_Ans > ans:
            ans = new_Ans
        else:
            j -= 1
print(ans)

"""
'XX----------------------------------------------------------------XX '

"""
Kadane's Algorithm: O(N)


maxSum = float('-inf')
total = 0
for n in nums:
    if total < 0:
        total = 0
    total += n
    maxSum = max(maxSum, total)
print(maxSum)

"""

'XX----------------------------------------------------------------XX '
