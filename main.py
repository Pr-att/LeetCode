# import random
# import time
# start = time.time()
# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1
#     for j in range(low, high):
#         if array[j] <= pivot:
#             i = i + 1
#             (array[i], array[j]) = (array[j], array[i])
#     (array[i + 1], array[high]) = (array[high], array[i + 1])
#     return i + 1
# def quick_sort(array, low, high):
#     if low < high:
#         pi = partition(array, low, high)
#         quick_sort(array, low, pi - 1)
#         quick_sort(array, pi + 1, high)
# array = [random.randint(0, 10000) for i in range(500000)]
# quick_sort(array, 0, len(array) - 1)
# end = time.time()
# print(end - start)


