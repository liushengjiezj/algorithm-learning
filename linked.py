


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

'''
链表的题目:
单链表反转
链表中环的检测
两个有序的链表合并
删除链表倒数第 n 个结点
求链表的中间结点
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    '''
    单链表反转
    '''
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None # last指向上一个结点
        while pHead:
            tmp = pHead.next # 先保存头结点的下一个结点，以免断开链表
            pHead.next = last # 将头结点的指针指向上一个结点
            last = pHead # 将上一个结点移到当前结点
            pHead = tmp # 当当前结点移动到之前保存的下一个结点
        return last

    '''
    链表中环的检测
    思路：
    有两个指针p1和p2，同时从头结点往下遍历链表中的所有结点。
    p1是慢指针，一次遍历一个结点。
    p2是快指针，一次遍历两个结点。
    如果链表中没有环，p1和p2会先后遍历玩所有结点。
    如果链表中有环，p1和p2会先后进入环中，一直在循环，并且一定会在某一次遍历中相遇。
    因此，我们只要发现了p1和p2相遇了，就可以判断链表中一定存在环。
    '''
    def hasCycle(self, head):
        if (head == None):
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False


    '''
    两个有序的链表合并
    思路:
    1，创建一个新的头结点并保存到save
    2，判断两个链表是否为空
    3，不为空，则进行下一步
    4，当L1的结点小于L2的结点时，则将新的头结点的next指针指向L1
    5，然后L1往后移动到下个结点，新的链表也移动到下一个结点
    6，当L1的结点大于L2的结点时，则将新的头结点的next指针指向L2
    7，然后L2往后移动到下个结点，新的链表也移动到下一个结点
    8，当以上的循环结束，判断L1和L2是否为空
    9，当为空的时候，则将新链表的next指向不为空的链表
    10，return save.next
    '''
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tmp = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        tmp.next = l1 or l2
        return head.next


    '''
    删除链表倒数第 n 个结点
    '''
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 快慢两个指针，快指针先往前走n步
        # 然后两个指针同时往后走，直到快指针走到链表尾部
        # 快慢指针相差n步，慢指针的下一步即为倒数第n个数

        # 先判断head是否为空以及n是否为0
        if head == None or n == 0: return head
        # 快指针先往前走n步
        fastHead = head
        while n >= 0 and fastHead != None:
            fastHead = fastHead.next
            n = n - 1
        # 如果快指针为空并且n大于0，则说明n大于链表长度，返回head
        if fastHead == None and n > 0: return head
        # 如果快指针为空并且n等于0，则说明倒数第n个节点即为第一个节点，也就是头节点，返回head.next
        if fastHead == None and n == 0: return head.next
        # 快慢指针同时往后走，直到快指针为空，则慢指针的next即为倒数第n个节点
        slowHead = head
        while fastHead != None:
            slowHead = slowHead.next
            fastHead = fastHead.next
        slowHead.next = slowHead.next.next
        return head


    '''
    求链表的中间结点
    '''
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 快慢指针，快指针2步走，慢指针1步走，当快指针到链表尾部时，慢指针到中间节点
        slowHead = head
        fastHead = head
        while fastHead != None and fastHead.next != None:
            slowHead = slowHead.next
            fastHead = fastHead.next.next
        return slowHead
