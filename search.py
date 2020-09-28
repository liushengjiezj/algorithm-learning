

# 二分查找，查找第一个值等于给定值的元素
def bSearchFirstTargetValue(a, n, value):
    low = 0
    high = n - 1
    while (low <= high):
        mid = low + ((high - low) / 2)
        if (a[mid] > value):
            high = mid - 1
        elif (a[mid] < value):
            low = mid + 1
        else:
            if mid == 0 or a[mid - 1] != value:
                return mid
            else:
                high = mid - 1
    return -1

# 二分查找，查找最后一个值等于给定值的元素
def bSearchLastTargetValue(a, n, value):
    low = 0
    high = n - 1
    while (low <= high):
        mid = low + ((high - low) / 2)
        if (a[mid] > value):
            high = mid - 1
        elif (a[mid] < value):
            low = mid + 1
        else:
            if mid == n - 1 or a[mid + 1] != value:
                return mid
            else:
                low = mid + 1
    return -1

# 二分查找，查找第一个大于等于给定值的元素
def bSearchFirstLargeAndEqualValue(a, n, value):
    low = 0
    high = n - 1
    while (low <= high):
        mid = low + ((high - low) / 2)
        if (a[mid] >= value):
            if mid == 0 or a[mid - 1] < value:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1

# 二分查找，查找最后一个小于等于给定值的元素
def bSearchFirstShortAndEqualValue(a, n, value):
    low = 0
    high = n - 1
    while (low <= high):
        mid = low + ((high - low) / 2)
        if (a[mid] <= value):
            if mid == n - 1 or a[mid + 1] > value:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1

# 如果有序数组是一个循环有序数组，比如 4，5，6，1，2，3。针对这种情况，如何实现一个求“值等于给定值”的二分查找算法呢？
