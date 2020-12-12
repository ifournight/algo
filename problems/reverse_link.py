# encoding: UTF-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """反转一个单链表。"""

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        before = None
        current = head
        while current:
            next_node = current.next
            current.next = before
            before = current
            current = next_node
        return before


if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]
    dummy = ListNode(None)
    current = dummy
    for num in input:
        new_node = ListNode(num)
        current.next = new_node
        current = new_node
    print("Linked list assembled")
    reversed = Solution().reverseList(dummy.next)
    print("Linked list reversed")
    output = []
    current = reversed
    while current:
        output.append(current.val)
        current = current.next
    print(output)
