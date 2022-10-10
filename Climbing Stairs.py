hashmaP = {}


def stairs(n, hmaP):
    if n in hmaP:
        return hmaP[n]
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        hashmaP[n] = stairs(n - 1, hmaP) + stairs(n - 2, hmaP)
        return hashmaP[n]


print(stairs(50, hashmaP))
