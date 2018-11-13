# -*- coding:utf8 -*-
# 选择排序的代码


def findsmallest(arr):
    """
    找到最小值并记录下索引
    :param arr:
    :return: 最小值的索引
    """
    # 储存最小的值
    smallest = arr[0]
    # 储存最小值的索引
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    # 返回索引值
    return smallest_index

def slectionsort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr


# 测试
print(slectionsort([9, 4, 2, 6, 7]))
# print(findsmallest([5, 4, 3]))
