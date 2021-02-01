# coding: UTF-8

import unittest


class LinkNode:
    """
        单向链表节点
    """

    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedQueue:
    """
        用链表实现的没有大小限制的队列
    """

    def __init__(self):
        dummy = LinkNode(None)
        self.head = dummy
        self.tail = dummy

    def enqueue(self, key):
        """
            入队
        """
        node = LinkNode(key)
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        """
            出队
        """
        # 如果队列为空，返回None
        if self.head == self.tail:
            return None
        node = self.head.next
        self.head.next = node.next
        node.next = None
        if node == self.tail:
            self.tail = self.head
        return node.key

    def peekFirst(self):
        """
            取得队列首元素的key，如果队列为空，返回None
        """
        if self.head == self.tail:
            return None
        return self.head.next.key

class TestLinkedQueue(unittest.TestCase):
    def testFIFO(self):
        queue = LinkedQueue()
        for i in range(0, 3):
            queue.enqueue(i)
        for i in range(0, 3):
            self.assertEqual(queue.dequeue(), i)

    def testEmptyDequeue(self):
        queue = LinkedQueue()
        self.assertEqual(queue.dequeue(), None)

    def testPeekFirst(self):
        queue = LinkedQueue()
        for i in range(0, 3):
            queue.enqueue(i)
        self.assertEqual(queue.peekFirst(), 0)

    def testPeekFirstFromEmpty(self):
        queue = LinkedQueue()
        self.assertEqual(queue.peekFirst(), None)

    def testDequeueToEmpty(self):
        queue = LinkedQueue()
        for i in range(0, 3):
            queue.enqueue(i)
        for i in range(0, 3):
            self.assertEqual(queue.dequeue(), i)
        self.assertEqual(queue.dequeue(), None)


if __name__ == "__main__":
    unittest.main()
