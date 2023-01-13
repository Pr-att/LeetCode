nums = [2]

def pFinder(n):
    co = 0
    for k in range(1, n + 1):
        if n % k == 0:
            co += 1
    if co == 2:
        return True
    else:
        return False

if len(nums) == 1:
    if pFinder(nums[0]):
        print(1)
    else:
        print(0)

Dividend = 1
for cup in nums:
    Dividend *= cup

def pfFinder(n):
    factors = []
    for num in range(2, n + 1):
        count = 0
        for i in range(2, num):
            if num % i == 0:
                count += 1
        if count == 0:
            factors.append(num)
    return factors

array = pfFinder(int(Dividend ** (0.5)))

ans = 0
for key in array:
    if Dividend % key == 0:
        ans += 1
print(ans)