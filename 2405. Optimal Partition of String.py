def partitionString(s) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 2
    if len(s) > 2:
        Set = set()
        count = 1
        for j in range(0, len(s)):
            if s[j] not in Set:
                Set.add(s[j])
            else:
                Set.clear()
                Set.add(s[j])
                count += 1
        return count
    return 0


print(partitionString("ssssss"))
