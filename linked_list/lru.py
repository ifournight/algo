# coding: UTF-8

import unittest


class LinkNode:
    """
        双向链表节点
    """

    def __init__(self, key) -> None:
        self.key = key
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return str(self.key)


class LRUCache:
    """
        用散列表和双向列表实现的LRU缓存
    """

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.size = 0
        dummy = LinkNode(None)
        self.__head = dummy
        self.__tail = dummy
        self.__node_table = {}

    def __str__(self) -> str:
        return "node_table: " + str(self.__node_table)

    def insert(self, key):
        """
            插入key到缓存
        """
        node = self.__find_node(key)
        if node:
            if node == self.__tail:
                return
            else:
                self.__delete_node(node)
                self.__insert_to_tail(node)
        else:
            node = LinkNode(key)
            if self.size == self.capacity:
                self.__delete_from_head()
                self.__insert_to_tail(node)
            else:
                self.__insert_to_tail(node)
                self.size += 1
            self.__node_table[key] = node

    def delete(self, key):
        """
            从缓存中删除key并返回，如果不存在，返回None
        """
        node = self.__find_node(key)
        if node:
            self.__delete_node(node)
            del self.__node_table[key]
            self.size -= 1
            return node.key
        else:
            return None

    def find(self, key):
        """
            从缓存中查找key，如果存在，返回key，不存在返回None
        """
        node = self.__find_node(key)
        return node.key if node else None

    def __find_node(self, key):
        """
            从缓存中查找key的节点，如果不存在，返回None
        """
        return self.__node_table.get(key, None)

    def __delete_node(self, node):
        """
            将节点从双向链表中删除
        """
        return node

    def __insert_to_tail(self, node):
        """
            将节点插入双向链表尾，表示最近使用（Recently Used）
        """
        self.__tail.next = node
        node.prev = self.__tail
        self.__tail = node
        return None

    def __delete_from_head(self):
        """
            将节点从双向链表头 (Least Recently) 删除, 并返回节点
        """
        node = self.__head.next
        self.__head.next = node.next
        if node.next:
            node.next.prev = self.__head
        node.next = None
        node.prev = None
        if node == self.__tail:
            self.__tail = self.__head
        return node


class TestLRUCache(unittest.TestCase):
    def testInsert(self):
        lru = LRUCache(5)
        for i in range(0, 3):
            lru.insert(i)
        self.assertEqual(lru.size, 3)
        for i in range(0, 3):
            self.assertEqual(lru.find(i), i)

    def testInsertAfterFull(self):
        lru = LRUCache(5)
        for i in range(0, 5):
            lru.insert(i)
        for i in range(5, 8):
            lru.insert(i)
        self.assertEqual(lru.size, 5)
        for i in [3, 4, 5, 6, 7]:
            self.assertEqual(lru.find(i), i)
        self.assertEqual(lru.size, 5)

    def testInsertExisted(self):
        lru = LRUCache(5)
        for i in range(0, 3):
            lru.insert(i)
        lru.insert(2)
        self.assertEqual(lru.size, 3)
        for i in range(0, 3):
            self.assertEqual(lru.find(i), i)

    def testInsertExistedAfterFull(self):
        lru = LRUCache(5)
        for i in range(0, 5):
            lru.insert(i)
        lru.insert(2)
        self.assertEqual(lru.size, 5)
        for i in range(0, 5):
            self.assertEqual(lru.find(i), i)
        self.assertEqual(lru.size, 5)

    def testDelete(self):
        lru = LRUCache(3)
        for i in range(0, 3):
            lru.insert(i)
        for i in range(0, 3):
            self.assertEqual(lru.delete(i), i)
        self.assertEqual(lru.size, 0)

    def testDeleteNoExisted(self):
        lru = LRUCache(3)
        for i in range(0, 3):
            lru.insert(i)
        self.assertEqual(lru.delete(4), None)
        self.assertEqual(lru.size, 3)

    def testFind(self):
        lru = LRUCache(3)
        for i in range(0, 3):
            lru.insert(i)
        self.assertEqual(lru.find(2), 2)

    def testFindNoExisted(self):
        lru = LRUCache(3)
        for i in range(0, 3):
            lru.insert(i)
        self.assertEqual(lru.find(4), None)


if __name__ == "__main__":
    unittest.main()
