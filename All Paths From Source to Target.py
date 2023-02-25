# def allPathsSourceTarget(graph):
#     d = {}
#     target = len(graph) - 1
#     for index, val in enumerate(graph):
#         d[index] = val
#     final = []

#     def dfs(d, root):
#         if root == target:
#             final.append(temp.copy())
#             return 
#         for n in d[root]:
#             temp.append(n)
#             dfs(d, n)
#             temp.pop()
#     temp = [0]
#     dfs(d, 0)
#     return final

# print(allPathsSourceTarget([[3,1],[4,6,7,2,5],[4,6,3],[6,4],[7,6,5],[6],[7],[]]))
# # print(allPathsSourceTarget([[4,3,1,8,6],[2,4,7],[8,4,6,5,3],[8,6,5,4],[7,6,5,8],[6,7],[7],[8],[]]))


