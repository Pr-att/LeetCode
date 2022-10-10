height = [1, 1]
i, j = 0, len(height) - 1
maX = -1 * float("inf")
while i <= j:
    if height[i] < height[j]:
        maX = max(maX, height[i] * (j - i))
        i += 1
    elif height[i] > height[j]:
        maX = max(maX, height[j] * (j - i))
        j -= 1
    else:
        maX = max(maX, height[j] * (j - i))
        j -= 1
        i += 1
print(maX)
