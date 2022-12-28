import heapq

piles = [2695, 9184, 2908, 3869, 3779, 391, 2896, 5328]
k = 10
queue = []
for num in piles:
    heapq.heappush(queue, -num)
ans = 0
while k > 0:
    top = heapq.heappop(queue)
    heapq.heappush(queue, top // 2)
    k -= 1
print(abs(sum(queue)))
