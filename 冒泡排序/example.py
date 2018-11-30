"""冒泡排序"""
# arr = [54, 34,676,45, 23]
arr = [1, 2, 3, 4]

def bubblesort(arr):
    for i in range(len(arr)-1, 0, -1):
        # 判断是否输入的是有序数列
        count = 0
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
        if count == 0:
            return

    # print(arr)


bubblesort(arr)
# print(arr)
