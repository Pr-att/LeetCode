class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        Map = {}
        start = 0
        if len(s) != len(pattern):
            return False
        for idx in s:
            if idx in Map:
                if Map[idx] == pattern[start]:
                    pass
                else:
                    return False
            else:
                if pattern[start] in Map.values():
                    return False
                Map[idx] = pattern[start]
            start += 1
        return True
