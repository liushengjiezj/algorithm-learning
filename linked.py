


'''
数组 a
数组长度 n
要查找的值 key
给出一个key，查找到key在数组a中的位置。（哨兵模式）
1, 当数组为空或者数组长度小于等于0时，返回false；
2, 判断数组最后一个值是否和key是否相等，是则返回位置；
3, 将数组最后一个值赋值给变量tmp，将key赋值给数组最后一个位置；
4, 遍历数组a，查找key；
5, 恢复数组最后一个位置的值；
6, 判断数组中是否查找到key。
'''
def find_key_in_array(a, n, key):
    if (len(a) != n):
        return -1
    
    if (a[n-1] == key):
        return n-1
    
    tmp = a[n-1]
    a[n-1] = key

    i = 0
    while (a[i] != key):
        i += 1

    a[n-1] = tmp

    if (i == n-1):
        return -1
    else:
        return i
'''
a = [4, 2, 3, 5, 9, 6]
n = 6
key = 3
result = find_key_in_array(a,n,key)
print(result)
'''
