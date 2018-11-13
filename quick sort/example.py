# -*- coding: utf-8 -*
# 快速排序
import random


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        # 随机选择用作基准的元素
        pivot = arr[random.randint(0, len(arr)-1)]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 4]))
