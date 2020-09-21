
"""
// 冒泡排序，a表示数组，n表示数组大小
public void bubbleSort(int[] a, int n) {
  if (n <= 1) return;
 
 for (int i = 0; i < n; ++i) {
    // 提前退出冒泡循环的标志位
    boolean flag = false;
    for (int j = 0; j < n - i - 1; ++j) {
      if (a[j] > a[j+1]) { // 交换
        int tmp = a[j];
        a[j] = a[j+1];
        a[j+1] = tmp;
        flag = true;  // 表示有数据交换      
      }
    }
    if (!flag) break;  // 没有数据交换，提前退出
  }
}
"""

# 冒泡排序，a表示数组，n表示数组长度
def bubbleSort(a, n):
    if (n <= 1): return
    i = 0
    # 每次从第一个元素开始两两比较
    while i < n:
        ++i
        # 如果一轮比较过后没有任何交换，则flag依然为False，就退出比较
        flag = False
        j = 0
        # 每轮比较后都会产生最大的数，所以后面几轮比较可以排除已经比较出的大数
        while j < n-i-1:
            ++j
            if (a[j] > a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
                flag = True
        if flag == False: break

'''
// 插入排序，a表示数组，n表示数组大小
public void insertionSort(int[] a, int n) {
  if (n <= 1) return;

  // 遍历未排序的元素
  for (int i = 1; i < n; ++i) {
    // 未排序的元素
    int value = a[i];
    // 已排序区间
    int j = i - 1;
    // 查找插入的位置
    // 遍历已排序区间，和右边未排序的元素进行比较
    for (; j >= 0; --j) {
      // 已排序元素和未排序元素进行比较
      if (a[j] > value) {
        // 如果已排序元素比未排序元素的值要大，则往后移动一个位置，给更加小的未排序元素让出位置
        a[j+1] = a[j];  // 数据移动
      } else {
        break;
      }
    }
    // 遍历完已排序区间后，将数据插入
    a[j+1] = value; // 插入数据
  }
}
'''

def insertionSort(a, n):
    if (n <= 1): return
    i = 1
    while (i < n):
        value = a[i]
        j = i - 1
        while (j >= 0):
            if (a[j] > value):
                a[j+1] = a[j]
            else:
                break
        a[j+1] = value
        ++i

'''

===============快速排序-挖坑法=================
https://blog.csdn.net/libaineu2004/article/details/82253412

def partition(arr, startIndex, endIndex):
  # 取第一个位置的元素为基准值
  pivot = arr[startIndex]
  left = startIndex
  right = endIndex
  # 坑的位置，初始等于pivot的位置
  index = startIndex
  # 大循环在左右指针重合或交错的时候结束
  while (right >= left):
    # right指针从右向左进行比较
    while (right >= left):
      if (arr[right] < pivot):
        arr[left] = arr[right]
        index = right
        left++
        break
      right--
    # left指针从左右向右进行比较
    while (right >= left):
      if (arr[left] > pivot):
        arr[right] = arr[left]
        index = left
        right--
        break
      left++
  arr[index] = pivot
  return index

======================快速排序-指针交换法=======================
pivot
left
right
1，定好pivot
2，从right开始，如果right符合>pivot的条件，则移动到下一个(right--)，否则停住不动
3，转到left，如果left符合<pivot的条件，则移动到下一个(left++)，否则停住不动
4，然后left和right互换
5，进入到下一轮循环，从right开始
6，重复上面的步骤，直到left和right指针重合
7，交换pivot和重合指针，此时pivot左边的元素小于它，右边的元素大于它

def partition_v2(arr, startIndex, endIndex):
  pivot = arr[startIndex]
  left = startIndex
  right = endIndex
  while (left != right):
    # 移动right，从右到左
    while (right > left && arr[right] > pivot):
      right--
    # 移动left，从左到右
    while (left < right && arr[left] <= pivot):
      left++
    # 交换left和right指向的元素
    if (left < right):
      p = arr[left]
      arr[left] = arr[right]
      arr[right] = p
  # pivot和指针重合点交换
  p = arr[left]
  arr[left] = arr[startIndex]
  arr[startIndex] = p
  return left

def quickSort(arr, startIndex, endIndex):
      if (startIndex >= endIndex):
    return
  pivotIndex = partition(arr, startIndex, endIndex)
  quickSort(arr, startIndex, pivotIndex - 1)
  quickSort(arr, pivotIndex + 1, endIndex)


===================快速排序-极客时间王争的版本======================

partition(A, p, r) {
//取最后一个元素为pivot
  pivot := A[r]
//i从第一个元素开始
  i := p
//j从第一个元素，遍历到数组结尾
  for j := p to r-1 do {
//如果j<pivot，则交换i和j，然后i++移动到下一个位置
    if A[j] < pivot {
      swap A[i] with A[j]
      i := i+1
    }
  }
//最后交换i和r，将pivot移动到中间.
  swap A[i] with A[r]
  return i

'''