from collections import defaultdict
import heapq
from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:

        def _heappush_max(heap, item):
            heap.append(item)
            heapq._siftdown_max(heap, 0, len(heap)-1)

        def _heappop_max(heap):
            """Maxheap version of a heappop."""
            lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
            if heap:
                returnitem = heap[0]
                heap[0] = lastelt
                heapq._siftup_max(heap, 0)
                return returnitem
            return lastelt

        cache = defaultdict(int)
        res = []
        temp = []
        heapq._heapify_max(temp)
        for i in range(len(nums)):
            cache[nums[i]] += freq[i]
            _heappush_max(temp, (cache[nums[i]], nums[i]))
            while cache[temp[0][1]] < temp[0][0]:
                _heappop_max(temp)
            res.append(temp[0][0])
        return res


print(Solution().mostFrequentIDs([2, 3, 2, 1], [3, 2, -3, 1]))
