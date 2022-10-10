import math
x = 120
y = str(abs(x))
t = int(y[::-1])
if x < 0:
    t = -1 * t
_l = -1 * (math.pow(2, 31))
l = math.pow(2, 31) - 1
if _l < t < l:
    print(t)
else:
    print(0)
