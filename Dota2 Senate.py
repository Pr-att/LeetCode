from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        r = queue.count("R")
        d = queue.count("D")
        d_count = 0
        r_count = 0
        while True:
            length = len(queue)
            if length < 1 or (length == r) or (length == d):
                break
            if queue[0] == "D":
                if d_count > 0:
                    queue.popleft()
                    d -= 1
                    d_count -= 1
                else:
                    queue.popleft()
                    queue.append("D")
                    r_count += 1
            else:
                if r_count > 0:
                    queue.popleft()
                    r -= 1
                    r_count -= 1
                else:
                    queue.popleft()
                    queue.append("R")
                    d_count += 1

        if queue[0] == "R":
            return "Radiant"
        else:
            return "Dire"


print(Solution().predictPartyVictory("DDRRR"))
# print(Solution().predictPartyVictory("DDDDDDRDDRRDDRDRDDRDDDDDDRRDDDRRRDDDDRRDDRRDDRRRRRDRDDRRDDRRDDDDRRDRRRDDRRDDDDDRDDRDDDRDRRDRDRDRRDDDDDDRRRDRRRRRDRDDDRRRDRDDDRRRDDRDDDRRDDRDRDRRDRDRDRDDDDRDRDRRDRDDRDDDDRRDRDRDDRDDDRDRDDRRRDRRRRDDRRRRDDRDDDRDRDRDDDDRRRDDDRRRRDRDDDDDRRRDDRDRRRDRDDDDDRDDRRDDRRRRRRRDDDDDDRDRRRDRRDDRDRDDRDDRRRDDDDDRDRDDDDDRRDDDDDDDRDRRDDRRRDRDRRRRDDDDRDDRRRRRRRDRRDDRRDDRDDDDRDRRDDDDDDRRDRDRDDRRDRRDDRRRDRDDRRDDRDRDRRRDDRRDRDRRDRRRDDRRDRDDRDRDRDRDRRDDRDDRRDDRDDRRDDDDDRRRDRDRRRRDRDRRDDDRDDRDDDRDDDDDDDDDDDRRRDDDDDDRRRDRDDDRDRRRDDRDRDRDDDRRRRRRRDRRDRDDDRRDDRRDRDRRRDRDRDRRDRRRDDRRRDDRDRRDDDDDDDDRRRDRRDRRRRRRDDDDDRRDRRRDDRRDRRRRRRDDDRRDRRDDRDDRDRDDDRRDRRRRDDRRRDRRRDRDDRRDRDRDDDRDDRRRRRDDDRDRRDDRDDDRDRDRRRDRDRDDRDRDDRRRRRDRRRDDRDDRDRDRDDDRDDDDRDDDRDRDDDRRRRRRDDRDDRDRDRDDRRRDRRDDDDDRRRRDRRDRRRDDDDRRDRRRRRRRRRRRDRDDRRDRDRRDRDDDDDRDDRRDDDDRRRRRRDDDDRDDRRRRDDRDDDRDDRRRDDDRDRRRRDRDDRDDDDRDDDDDRDDDDRRRDDDRRRRDRDRDRDDDDRRRDDRDDDRDDDDRDRRDRRDDRDRRRDRRRRDRRDRDRDRRRRDDDRDRDDRDRDRDRDDRDDDRRRDRDRDRRDDRDRRDRRRRRRDDDRDRRDDRRRDDRDDDDDRRRRRRRRDRDRRDRDRDDRRRDDDRDRRRDRRRRRRDRRRDDDDRDRRDDRRDRDRDRRRRRDDDDDRRDRDRDDRRDDDRRRRRDDDRDDRRDDDRDRRRDDDRDDDRRDDRDDDRDDDRDRDDDRDDRDDRRDDRDDDRDDRRDRDDRDDRDRDRDRDRRRRRRDRDDRRRRDDRRDDDDRRRRRRRDRRDDRDDDRRDDDRRDDRDDDRDDRRRRDDRRRDDRRRDDRDRRRDRDDDRRDRRRDRDDRDRDDRRRDDDRDRRDDRDDRRRDDDDDRDDDRDDRRRDDRRDRDRRRDRDRDRDRDRRDRDRDRRRRDDDDRDRRRDDDRDDDRRDDRDDRRDDDRRRRRDDDDRDRDRDRDRDRRDRDDRDDDRRRDRDRDRRDRRDRDRRDRDRRRRRDRDRRRRDRRDRDRRDRRDDDDRRRDDDRRDDRRRDDDDDRRRDDRDDRDRDDDRDDRDRRRDRRRDDDRDDDRDRDRRRDDDRRRRDRDRRDDRDDDDRDRDDRRDRDDRDRRDRDRRRDRDDRRDDDDRDRRRDDDDRRDRDRRDDDRDDRDRDDRDRDDRDDRRRDRDRDRRRRRRDRRDRDDRDRRRDRDRRDRDRRRDRRRRDRRDRDRRRRRDRRDDRDRRRRRRDDRDDRRDRDRRDDDDDDDRRDDDDRDRRRRRDRRDRRRRDDDDDDRRDDRDDDDRRRDDDDRDDRRDRRRDDDRDDDRRRRDRDDDRRRDRRRDRDDRRRDDDRDRDRRDRDRDDRRRRDRDRDRRDRDRDDDRDDRRRDDDRDRRRDDDRRDDRRRRRDRRRRRDRDDRDDDRRRRRRDDDDRDRDDRRDDRRDRDDDDDDRDDRRDDRRRDDDDRRRDRRRRRRDDRRRRRDDDRRRRRRDDRRRDDRDDRRRDDDDRDDRRRRRDRDRDDDRRDDDDDDRRDRDDDRDRDRDRRRDRRDDRRDDRRRRRDRRDDDDRRDDDDRRRDDDRDDDRRRDRRRRRRDDDRDRDDDRDDRRDRRDDRDDDRDDDDRDRDDDRRDDDRDDDRRDDDDRDRDRRDRRRRRDRDRRDDRDDDDDRRDDDDRRDDRRDRDRRRRRDRRRDDRDRDRDDRRRDDDDDDDRDRRDRRRRRDDDRDRDDRRRDRDDRRRDRRRRRDRRDDDDRRRDDRRDRRDRDDRRRDRRDDRRRRDDRDRDDRDDDDDRDDRRRRRRRDDRRRRRDDDRDRDRDRRDDDDDRRRRRRDDDRRRRDRDDRRRDDDDDRRDDDDDRRRDDDRRDRRRDDDDDRRDDDDRRDRDDRRRRDRDDDDDRRRRDDDRDRDDRDRRRRDDDRRDDDRRDDRRRDRDRRRDRRDRRRRDDRDRRDRDDRDDDRRDDDDDRRDDDDRDRRDDRRRRDDRRDDRDDDRDRDDRRDRRRDRDRRDDDRRRRRRDRDDRRRDDRRRDDDRDDDRRDDDRDRDRDRRRRDRDRRDRDRRDDRRRDRRDDRRRRDRDDDDRDRRDRDDDRDRDDRDRRDRDRRRRRRDRRRRRDRDRRDRDRDRDDDRDDRDDRRRRDDDRRRDRDDRDRDRRDRDDRRDRDRDRDRDDRDDDRRDRRDRRDDDDDRDRDRRDDRDRDDDRDDRDDRRDRRDRDRRDDRDRDDDDRRRRRDDRRDDDDDRDDRDRDDDDDDDRRRRDDRDRRRRRDDDRRDRRDDDDDDDDDRDDRDDRDRDRRDDRDDDDDRRRDDRDDRDDRDRRDRRRDRRRDRRDRDDRDDDRRDRRDDDDDDRDRDRRRRDDRDRDDDRDDRDDRDRDDRRRDRDRDRRDRRDDDDRRDDDRRRRDRDRDRDRDRDRDRDDDDRDDRDRRRDRDRRDRDRRDDRRRDRDRRRRRRDRRDRDRDDRRDRDDDRRRRDDDRDRDRDRDRDRDRDRDDDRRRDDDRRRDDRRRRRRRRDDDDDRDRRRDRRRRDRDRRRDRDDRRDDRDDDRDRDDRDDRDDDRDDDRRDDRDRRDRDRRRRRDDRRDDDRDDRDDDRRRDDDRRRDDDRDDRDRDDRRRRRRDRRRRDRRRDRRRDDDRRRRRDRDDRRDDRDRRDDRRDRRRRDDDDDDRDDRRDDRDRRDRRDRDDDDDRDDRRDRRRRRDRDDDRRRRDDDRDDDDRDRDRRDDRDRDDRRDRRDRRRDDDRDDDRDDRRRDRDRRDDRDRDDDRDRDRDRRDRDRRRRRRRDDDRDDDRDRDDDDDDRRDDRRDRRDRDDDDDRDDDRRDRDRRRRDRDRRRRRRDRRRDDRRDDDDDDRRDDRRDDDDRDDRRRDDDRDRRDDDDRRDRDDDRRRDDRRDRDRRDDDRRRRRRDRDRRRDRRDDDRRDDRRDDDRRDDRDDDDDRRDRDDRRDDRDDRRDDRRRDRRRRRRRRRRDDDDRRRRRRRRRDRDRRRDRRRDDDDDDRDDDDRRRDRRDDRRRRRRRDDDDRRDRRRRDRRRRDRDDDRRDRDRDDRDDDDDRDDDRDDDRRDRDRDDDRRRDDDRDDRRDDDRRRDRDRRDDRDRDRRDDDRDRRRDRRDRRRDRRDRDRRRDDDDRRDRRDDRDRRRRRDDRRRRRRDRDRDRDDDRRRDRRRRRRRDDDRDRRRDRRDDRRRDDRRRRRRRRRDRRDDRDRDDRDRDRRRRDRRRRRRRRDRRDRRDDRDRDDRDRDRRDDDRRRRDRRRRRDDDDDDDDDRRRDRRRRRRDRRRRDDRDRRDDRDDDRDDRRRRDDRRRDRRDRDRDRDDRDRDDDDDDRRRRRRRRDDDRDDRDDRDRDRDDRDDRRRRDDRDDRRRDDRRDDDRRDRDDDDDDRRRRRDDDDRRRRDDDDDRDRDRDDRRRRRDDDDRRRRDDDDDRDRDDRDRDRDDDRDRDDRDDDDDRDRRRDRRDRRRRDRRRDRDDDDRRRDDRDRRDDDDDRDRDDRDDDRRDDDRRDDRDRDDRDRDRRDRDRRRRRDDRRRRDDDRRRDDRDRRDDRRDDDRRRDRDDRDDDDDDRDRRDDRDDRDDRRDRDRRDDDRRDDRDRDDDDDRRDRDDDDRRRDRRDDRRDRDRRDRRDDRRRRRRDRDDRRDDDDRRDDDDRRRRRDRRDRRRDDRRRRDRRDDRRRDDDRRRRRRDRDRDRRDDRRDRDRDRDRRDDDRRDRDDRDDRDDDDDRRRDDRRDRRRDRDRRDRRDRDRDRRDRRDRDDDRDDRDDRDRRRRDDDRRRRDRDDRRRDRRDRRDDDRDDRDDRRRDRDRRRRRDDRDRRDRRRRDRRRDDRDDRDRRRRDDDDDRDDDDDDDDDDDRDDRRDDRDRDRRDDRRRDRRDDDRRRRRDRDDDRRDDRDDRDRDRRDDRDDDDDDRRRRDRDRRDRDDDRRDRDRDDRRDRDDRRDRRDRDRRDRDRRRDDDRDDRDDRDRRRRDRRDRDDDDRRDRRRRDDDRDDRRRRRRDDDRRDDDDDDRDRDRRDRRDRDDDDDRDDRRDRRDRDRRRRDDDDDDRRDRDDRDDRDRDDDDRDDDRDDDRRRRRDDDDDRDDRDRDRDRRRRDDDRRRRRDDRDRRRRRRRRRRDDDDDRDRDRDDRRDDRDRRRDRDRDDDDDDDRDRRDDRDRRDDRRDDRRRDRRDDDDRDRRDRDRDRDDDDRRDDRRDDDDRRDRRRRRRRDRRRDRRRDDDDDRRDRRDRRDRDRDDDRDDRRRRRRDDRRRRRDRRRDRDDRRDDRDDDDRRDRDRRRDRDDDRDDRRDDRDDRDDDDRDDDDRRDDDRDDRRRDDRRRRDDRRRRRDRDDDDDDDDDRDRRRDDDRDDRDRRDDDRRRRDDRDDDDDDRRDDRRRDRDDRRDDRRRDDDRRDDRRRRRRDDRRDDRRDDDDRRRDDRRRDRRDDRRRDDRRRRRRRRDRDDRDDDRDDDRRDRRDRDDRRDDRDDRRDDDRRRDRRDDRDDDRDRRDDRDRDRDRRRDDRRDRRDDDRDRRRDRRDDRRDRRRDDDRDRDDRDDRRRDDDRRRRDRRDDDDDRDRDDRRRDDRDDRDRDRDDRDRDDRRDRDDDDRDDRDDDRDRDRDRDRRRRRRRRRRDDDDDRDRRDDDRRDRDDDDRDDDDRRDRRDRDDDRDDRDRRDDRRRRRDDDRDRDDRDRDDRDRDRRRRDDRRDRRDDRDDDDDRRDRDRRRRRRRDRRDDRRRDDDDRRDDRDRDRRRDRDDDRDRRRDRDRDDRRDRDRDDRRDRDRRDRRRRRRRRRRRDDDDRRRDDRRDRRDDDDRRDRDDDDRRDDDDDRDDDDRDRDDDRRRRDDDRDRRDDRRRDRRDRRDRRRRRDRDRRRDRRRDDDRRRRDRDDDDDDDRRRRRRDRRDRDRDRDRRRDDRDRDDRRDRDDRDRDDDDRRDDDRDRDRDRRDDDRRRDRDRDDDDRRDRRRDDRDRRDDDDDRRRDRDDRRRRRRRRDDDRDRRDDDDDDRDRRDRRDRRDRRRRRRRRDRDDDDDDRDRRRDDRDRRDDDRDRRDRRRRRRDRRRRRDRRRDDRRDDDDRDRRRDRDDRDDDDDDRDRDDDDDDDRRRRDDDDDRDRDDRDDRRRRDRRRRRDRDRDRRDRRDRDRRRRRRDDDRDRRRRRDDRRDDRDDDRRRRRRRDDRRRRDDRDDRDRRRDRDDDDRDRRRRRDDRRDRRRRDDRDDDDRDRRDDDDDDRRRRDDDRDRDDDRDDRRRDDDDRDDDDDRDRDRDRDRRRDDDDDDDDRRDDRDRDDRRRDRDRRDDRDDRDDDRDRDRDRDRDDRDRDRRRDRDRRRRDRDDRDRRDDDDRDDRDRDDRDDRDRDDRDRDDDRDDRDDDRDDDRRRRRDDDRDDRRDDRRDDRDDRDDDRDDDDDRRDRRDDRDDRRRDRDDRRRDRDRRRDDDRRDDDRDRRRRRRDDRDRDDRRDRDRDRRDRDRDDDRRRRRRDRRRDDRDRRRRRDDRRDRDDDDRDDDDDRRRRRDDDDDRRDRDRDDRRDDDDDDRRDDRRDDDRDDDDRRDRDDDRRDRRDDDDDDRDDRDRDDRRRRRRRDRDDRRRDRDRDDRDDRDDRRDDRRRDDRDDDRRDDDDDDRRDDDDRRDRRDRDRDDRDRRRDRDRRDDRDDRRRDDDDRDDDDRRRDRRRDRRDRDRRDRDRDRDDDRDRRRDRRRDDDRDRRRRDRDRRDDRRRDRDRRDRRDRRDRDRDRDRDDDDDRDDDRRDRRDRDRDRRDDRDRDDDDDDDDRDRRDDRDDDDRRDDRDDDDRDRDRDDRDRRDRDDRRDRDDRDRDDRRRDDRDDRRRDDDRDRDRRRRRDDDRDRRDDRDRRDDRRDRDRRDDRRDDRDRDRRRDDDRRRDRRRRDRDRRRDDDRRRDDDDRRDDDRDRDRDDDDDDRDDRRRRDDDRRRRRDDDRDRDDRDDDRRDDRRDDDRDRDRDDDDDDRRRDDDDDRRRDDRDDDRDRDDDDRDDDRRDDRDRDDRRRDRRDDRDDDRDDRDRDRDRDRRRRDRDRRDRDDRRDRRDRDDRDRDDDRRDDDRDRRRDRDDRRRDDDDDRRDDDDRDDRRRRRDDRRRDRDDRDDDRDRDRDRRRRRDRDRDRDDDRRDDRDDDDDDDDRRDRRDDDRRRDDDDDDDDDDRDRDRRRRDRDRRRDRDRRRDRRRRRRRRRRDDRDRRRDDDDRRDDDDDDRDDDRDDRRRDDDRRRDDRDRRDDRRDRDDRDDRRDRRRDDRRRRRRDDRDDDDRRDDRRDDRDRRDRDRRDRRRDRRRDDDRDDDDDDDRRRRRRDDDDRDRDRDRRDRRRDDDRDRDRDDRDRDDDRRRRRRDRDDDDRRDRDDRDRDDDRRDRRDDDRDDDDDRDRRRDDDDRRRRRRDDDDDDRDDDDDDDDDDDRRRDRDRRRRDDRRDRRDRDRRRRRDDDRDRDRRRDDDRRDDDRDDDRDDDDRRRRDDDDRDRRDDDRDDRDDRRDDDRDDRDRDDRDRDDDDRRRRDRDDRDRRDRDRDDRRDDRDDRDDRRDRRDRRDDRDDDDRRRRDRDRDDRRRDDRRRDDRDRRRRDDDDDRRDRRRDRRRRRRRRDRRDDDRRRDDDDRDRDDDDRRDRRDDDDRDRRDRDDDRRDRDRDRRRRDRDDRRDDRDDDRDDDRRRDDDRRDDDRDRRRDRDRRRRRDDRDDRRDRDRDDRDRRDRRDDDRRRRRDRDRRDDRRRRRDRRDDRRDRDDDRDDDRDDDRRDRRDDDDRDDRDDRRRDRDDRRRRDRRDDDDRRDDRDDRRRRDDDDRRDRRRDDDRRRRDRDDDDDDDDDRRRDRRDRDDRDDDRDDRRRRDRDDDDDDDDRRDRRDRRRDRDDRRRRDDRDDRDRRDDDRDDDRDRDDDDRRRRDRDDDRDDRRRRRDRDDRRRDRRRRRDDDDRRRRDRRRDDRRRDDDDRRRDDRDRDRRRRRRDRDRRRRDDRRRRDRRDDRDRRRDDRDDRRRRDDRRRDRDDRRRRDDRRRRDDRRRRRRDRRRDRRRDDRRRRDDRDDRDDDDRDRDDRDRRRDDDDRDRDDDDDDRRRDRDRDDDRRDRRDDRDRDRDRRDDDDDRRDRRRRDDDRDRDRDRRRRDRRDDRRDDDRRRDRRDDDRDRRDDDRDRDDRDRRDDRDDDDDDDRRDRDRDDRRDDRRDRDDRRRRRDRDDDRRRRDRDRDRDDRRDRRDRRRRRDDDDDDRRDRRRDDDRRDDDRDDDRDDDDDDRRDDRRDRRDRRRRDDDDRDRDRRDDDRDRRRDRDDRRRRRRDDDRRDRDRDDRDRRDRRDRRDRRRRRDDRDRDDRDRRRDRDDDRDRDDRRRDDRDRRRRDDRRRDRRDRRDDDRDDRDDRRRDRDDDRRDDRRDRDDDDDRDDDDRDDDRDRRDDDDDDDDDDDDDDDDRRDDRDRRDRDRDDRRRRRRDRDRDRRRRDRRDDRRDDRDRDRDDRDRRRDDDRDDDDRRRDRRRRDRRRRDRDDDRDDDRRDRRDDDRRRRRRRRRDRDDDDDRRRRDRRRRRRRDRRRDRRRDDDDRRDRDRDRRRRDDDRRRRDRRRRRDRRDDRDRRRRRDDRDRRDDRDRDDDDRRDRDDRDDRDRDDRRRRRRRDRRRRDRDRRRDDRRRRDDRRRDRRRRDDDDRRRRRDDRRRRRRRDRRDRDRRDDDDRRDDRDRDRDRDRDDDRDRDDRRDDDDRDRRDRRDRDDDRDDRDDRDDRDRDDDDRRDDRDRRRDDRRRDRDRDDDDDDDDRDDRDRDDRRRDRRDDDRRDDDDDDRRDDDDRRRRDRDDDRRRDDRDDRDRDDDDDRDRDRDDRRRRRDDRRDRDDDDRRDDDRRRRDRRDDRDRDRRRDDRRRRRRDRDDDRDRDDDDDRDDDDDDRRRRRDDRRRRDRRDDRRRDDRDDRRRDRDRRRDRRDDRRRDRRDDDDDDRRDRDRRRRDRDRRRDRDDDRRRDDRDDRDDRRDDDDDRRRRRDRRDDRDRRDRDDRRRRRRDRRDRDDRRDRRDDDRRDDRDRDRDDRRDRRDDRDRRRDDRDDDRDDRRDRRRRDDRRDDRDRDDRRDRRRDRRDDRDDRRRDDDDRDRRRRDRRRDRRDDRDDRDDDDDRDRRDRDRDRRDRRDRRRRDRRRDRDDDRDDDRRRRRDDDRRRRDRDDRDRRRRDDRDDRDDDDRDDRRRRDDRRDDDDDDRRDDDRRRRRRRDDDRRRRDDDRRRDDRRRDDRRRRRRDRDDRRDDRRDDRDRRRRDRDDRRRDRDDDRDRDRDDDDDRDRRRRDDDRRDDDDDRDDRDRRDDDRDRRDDDRRRDDRRDRDRDRDRRRRRDRDDRDRDDRDRRDDRRDRRRDRDRRRDRDRDRRDDDDRDDRDRDRDRDDRRRDRRDRDRDRRRRRRDRDRRDDDRDDDDRDDRRRDRRRRRRRDRRRRDDDRRRRRDDRDDRDRRDRDRDRRRRDRDDRRRDDDRDDRDRRDRDRDDRRRDRDDRDRDDDRRRRDDRRDDRRDDDRDRRRRDDDRDDRRDDDRDRDRDRDDDRDRDRRDRDRRDRDDDDDDDRRDRRRRDDDDDDDDRRRRDDRDDRRDRDDDRRRRDDRDDDDRDRRRDDDDRDRRDRRDDDDRRRDRDDRDDDRRDRDRRDRRDDRRDRDRDDRRRRRDDRDDRRDRRDDRRRRDRRRDRDDDDDDDDRDRDDDRDRDDRRRDDDRRRDDDRDDRDDRRDDRRDRRDRRDDRRDDRDRRDRRRDDDRRRDDRDDRRDDDRDRRRDRDDRDRDDRDDDRDRDDRRDDRDRDDDRDRRRDRRDDRRRDRDDDRRDDRDDDRRRDDRDDDRRRRRRDDRDDRDRDRDRRDDDDDRRRDRDDRRRRRRRRRRRRDDDDRRRRDRRRRRRRDDDRRRRRRRRDDRRRRDRDDDDRDRDRDDRRRDDDRRRDDDDDRRRDDRDRDDRDDRDDDRRRRRRDRDRRRRRDRRRRDRRDRRDDDDDDDRRDRDDRDRDDDDRRDDRDRRRDDDDDRRDRRRDRDDRDDRRRRDRDRDDDRDRRRDRDRRDRDDRRRDDRDRRDRRDRRRDRRRRRDRRRRDRRRDDRRDDDDRDDRRRRDRDRDRDRDDRDRDDRRDDDDDRRRDRDRRDRRRRDDRRRRRRDRRDRDDDDRDDDRRRDDDDDDDRRRDRRDRRRDDDDDDDRDDDDDRRDRDDRDDDRDDDDDRRRDDRRRDRRRDRRRDDDRRDRDRRDRDRRRRDRDDRRRDRDRRRRDDDDDRDDRDRDDDDRDDDRRRDRDRRDRDRRDDRRDRDRDRDRRDDDRDDRDRDRRRRRDDDDRRRRDRDRDRRDDRRRDRRRDRDDRRRDDDRDDRDDDDRDDDDDRRRRRRDRDRRRDRRRRDRRDRDRDDDRDRRDDDRDRRDDDRDDRDRDDRDDRDRDDDRRDRRRDDRRDRRDDRDRRRRDRDRDRDDRRDDDRDRDRRRRRRRRDRRDDRRRDRRDDDRDDRRRRDRRDRRRDRDRRRDRRDDDDDDRDDRDRRRDDRRDRRRRDDRDRRDDDDDDRRRRDDDDDRDRRDRDRRRDDDDDDDRRRRRDRRDRDRDRDDRDRRRRDDRDDDRRRDDRDRDRDRRDDRDRDRRDDDRDRRDRRRDRRRDDDDDDDDRRDDDRDDRRRRRRRRRDDRDRRDRRDDRDDRRRRDRRRRRDDRRDRDDRRDDRDRDRRRDRRDRDDD"))