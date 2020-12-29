# coding: UTF-8
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

# 说明：不允许修改给定的链表。

# 进阶：

# 你是否可以使用 O(1) 空间解决此题？
#  

# 示例 1：


# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 示例 2：


# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例 3：


# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#  

# 提示：

# 链表中节点的数目范围在范围 [0, 104] 内
# -105 <= Node.val <= 105
# pos 的值为 -1 或者链表中的一个有效索引


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow = head
        fast = head
        while True:
            if fast.next is None or fast.next.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next
        return ptr


def parseLinkedList(list, pos):
    nodes = [ListNode(item) for item in list]
    for index, node in enumerate(nodes):
        if index != len(nodes) - 1:
            node.next = nodes[index + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def printLinedList(head):
    current = head
    nodes = []
    while current:
        nodes.append(current)
        current = current.next
    print([node.val for node in nodes])


if __name__ == '__main__':
    list = [1, 2]
    pos = 0
    head = parseLinkedList(list, pos)
    print(Solution().detectCycle(head).val)

    list = [3, 2, 0, -4]
    pos = 1
    head = parseLinkedList(list, pos)
    print(Solution().detectCycle(head).val)
