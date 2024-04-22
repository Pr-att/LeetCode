from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        dead_ends = set(deadends)
        count = 0
        while queue:
            for index in range(len(queue)):
                start = queue.popleft()
                if start == target:
                    return count
                if start in dead_ends or start in deadends:
                    continue
                dead_ends.add(start)
                for val in range(4):
                    a = start[val]
                    first = str((int(a) + 9) % 10)
                    second = str((int(a) + 1) % 10)
                    if val == 0:
                        queue.append(first + start[val + 1:])
                        queue.append(second + start[val + 1:])
                    elif val == 3:
                        queue.append(start[: val] + first)
                        queue.append(start[: val] + second)
                    else:
                        queue.append(start[: val] + first + start[val + 1:])
                        queue.append(start[: val] + second + start[val + 1:])
            count += 1
        return -1


print(Solution().openLock(
    deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
