# coding: UTF-8

# 编写一个程序，找到两个单链表相交的起始节点。

# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# 注意：

# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def getLinkNodeLen(head):
            len = 0
            curr = head
            while curr:
                len += 1
                curr = curr.next
            return len

        len_a = getLinkNodeLen(headA)
        len_b = getLinkNodeLen(headB)
        if len_a == 0 or len_b == 0:
            return None

        inter = None
        curr_a = headA
        curr_b = headB
        i = 0
        if len_a > len_b:
            while i < len_a - len_b:
                curr_a = curr_a.next
                i += 1
        else:
            while i < len_b - len_a:
                curr_b = curr_b.next
                i += 1
        while curr_a and curr_b:
            print("curr_a {curr_a} curr_b {curr_b}".format(
                curr_a=curr_a.val, curr_b=curr_b.val))
            if curr_a == curr_b:
                inter = curr_a
                break
            curr_a = curr_a.next
            curr_b = curr_b.next

        return inter


def parseLinkedList(list_a, list_b, skip_a, skip_b):
    if len(list_a) == 0 and len(list_b) == 0:
        return None
    nodes_a = [ListNode(val) for val in list_a[0:skip_a]]
    nodes_b = [ListNode(val) for val in list_a[0:skip_b]]
    nodes_c = [ListNode(val) for val in list_a[skip_a:]]
    for i in range(0, len(nodes_a) - 1):
        nodes_a[i].next = nodes_a[i + 1]
    for i in range(0, len(nodes_b) - 1):
        nodes_b[i].next = nodes_b[i + 1]
    for i in range(0, len(nodes_c) - 1):
        nodes_c[i].next = nodes_c[i + 1]
    if len(nodes_c):
        nodes_a[-1].next = nodes_c[0]
        nodes_b[-1].next = nodes_c[0]
    return (nodes_a[0], nodes_b[0])


if __name__ == '__main__':
    listA = [2, 6, 4]
    listB = [1, 5]
    skipA = 3
    skipB = 2
    print("list_a {list_a} list_b {list_b}".format(list_a=listA, list_b=listB))
    headA, headB = parseLinkedList(listA, listB, skipA, skipB)
    inter = Solution().getIntersectionNode(headA, headB)
    can = "Can" if inter else "Can not"
    print("{can} find inter in listA {listA} and listB {listB}, inter: {inter}".format(
        can=can, listA=listA, listB=listB, inter=inter
    ))

    listA = [4, 1, 8, 4, 5]
    skipA = 2
    skipB = 3
    listB = [5, 0, 1, 8, 4, 5]
    print("list_a {list_a} list_b {list_b}".format(list_a=listA, list_b=listB))
    headA, headB = parseLinkedList(listA, listB, skipA, skipB)
    inter = Solution().getIntersectionNode(headA, headB)
    can = "Can" if inter else "Can not"
    print("{can} find inter in listA {listA} and listB {listB}, inter: {inter}".format(
        can=can, listA=listA, listB=listB, inter=inter.val
    ))
