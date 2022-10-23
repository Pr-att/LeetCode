# s1 = "hello"
# s2 = "ooolleoooleh"
# myMap1 = {}
# myMap2 = {}
# for i in s1:
#     if i in myMap1:
#         myMap1[i] += 1
#     else:
#         myMap1[i] = 1
# init, endL = 0, 0
# count = len(s1)
# stack = dict([(key, value) for key, value in myMap1.items()])
# while True:
#     if count == 0 and init <= len(s2):
#         print(True)
#         break
#     elif init >= len(s2) and count > 0:
#         print(False)
#         break
#     if s2[init] in myMap1 and count > 0 and stack[s2[init]] > 0:
#         endL = init
#         stack[s2[init]] -= 1
#         count -= 1
#     else:
#         count = len(s1)
#         stack = dict([(key, value) for key, value in myMap1.items()])
#     init += 1

nums = [1, 2, 1]
k = 1
myMap = {}
for i in nums:
    if i in myMap:
        myMap[i] += 1
    else:
        myMap[i] = 1

