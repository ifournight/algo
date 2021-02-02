# coding: UTF-8
from typing import Counter
import unittest


class LinkNode:
    """
        单向链表节点
    """

    def __init__(self, key) -> None:
        self.key = key
        self.next = None


def parseLinkFromList(l):
    """
        读取指定数列，创建单链表，并返回链表头
    """
    if l is None:
        return None
    nodes = [LinkNode(key) for key in l]
    for i, node in enumerate(nodes):
        if i == 0:
            continue
        prev_node = nodes[i - 1]
        prev_node.next = node
    return nodes[0] if nodes else None


def reverseLink(root):
    """
        反转链表
    """
    if root is None or root.next is None:
        return root

    dummy = LinkNode(None)
    dummy.next = root

    current = dummy
    next_node = root
    while next_node:
        next_next = next_node.next
        next_node.next = current
        current = next_node
        next_node = next_next

    root.next = None
    return current


def findMiddleNode(root):
    """
        找到链表的中间节点
    """
    if root is None or root.next is None:
        return root

    slow = root
    fast = root
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergeOrderedTwo(first, second):
    """
        合并两个有序链表
    """
    dummy = LinkNode(None)
    current = dummy

    while first and second:
        if first.key < second.key:
            current.next = first
            current = first
            first = first.next
        else:
            current.next = second
            current = second
            second = second.next

    current.next = first if first else second
    return dummy.next


class TestLinkedList(unittest.TestCase):
    def testParseLink(self):
        l = []
        root = parseLinkFromList(l)
        self.assertEqual(root, None)

        l = None
        root = parseLinkFromList(l)
        self.assertEqual(root, None)

        l = [1, 2, 3]
        root = parseLinkFromList(l)
        self.assertEqual(root.key, 1)
        self.assertEqual(root.next.key, 2)

    def testReverseLink(self):
        l = []
        root = parseLinkFromList(l)
        reversed_root = reverseLink(root)
        self.assertEqual(reversed_root, None)

        l = [1]
        root = parseLinkFromList(l)
        reversed_root = reverseLink(root)
        self.assertEqual(reversed_root, root)

        l = [1, 2, 3]
        root = parseLinkFromList(l)
        reversed_root = reverseLink(root)
        self.assertEqual(reversed_root.key, 3)

    def testFindMiddle(self):
        l = []
        root = parseLinkFromList(l)
        middle = findMiddleNode(root)
        self.assertEqual(middle, None)

        l = [1]
        root = parseLinkFromList(l)
        middle = findMiddleNode(root)
        self.assertEqual(middle.key, 1)

        l = [1, 2]
        root = parseLinkFromList(l)
        middle = findMiddleNode(root)
        self.assertEqual(middle.key, 1)

        l = [1, 2, 3]
        root = parseLinkFromList(l)
        middle = findMiddleNode(root)
        self.assertEqual(middle.key, 2)

        l = [1, 2, 3, 4]
        root = parseLinkFromList(l)
        middle = findMiddleNode(root)
        self.assertEqual(middle.key, 2)

        l = [1, 2, 3, 4, 5]
        root = parseLinkFromList(l)
        middle = findMiddleNode(root)
        self.assertEqual(middle.key, 3)

    def testMergeOrderedTwo(self):
        first = parseLinkFromList([])
        second = parseLinkFromList([])
        merged = mergeOrderedTwo(first, second)
        self.assertEqual(merged, None)

        first = parseLinkFromList([1])
        second = parseLinkFromList([])
        merged = mergeOrderedTwo(first, second)
        self.assertEqual(merged.key, 1)

        first = parseLinkFromList([1])
        second = parseLinkFromList([2])
        merged = mergeOrderedTwo(first, second)
        self.assertEqual(merged.key, 1)
        self.assertEqual(merged.next.key, 2)

        first = parseLinkFromList([1, 3, 5])
        second = parseLinkFromList([2, 4])
        merged = mergeOrderedTwo(first, second)

        current = merged
        for key in [1, 2, 3, 4, 5]:
            self.assertEqual(current.key, key)
            current = current.next


if __name__ == "__main__":
    unittest.main()
