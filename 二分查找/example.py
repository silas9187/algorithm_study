"""二分查找
使用条件：列表是有序时"""
import math


def binary_search(arr, item):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = math.ceil(((low + high) / 2))  # 计算出数组的索引中间值，当结果带有小数时，利用ceil函数向上取整
        # print(type(mid))
        # 把要查找的值与搜寻的列表的中间元素进行比较
        if item < arr[mid]:  # 查找的值比中间元素小了
            high = mid-1
        elif item > arr[mid]:  # 查找的值比中间元素大了
            low = mid+1
        elif item == arr[mid]:
            return mid

    return None  # 没有这个值


list = [11, 14, 16, 19, 56]
print(binary_search(list, 6))