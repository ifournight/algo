# coding: UTF-8
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
# 实现 LRUCache 类：

# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#  

# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

#  

# 示例：

# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  

# 提示：

# 1 <= capacity <= 3000
# 0 <= key <= 3000
# 0 <= value <= 104
# 最多调用 3 * 104 次 get 和 put


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lru-cache
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class LinkNode(object):
    """
    LRUCache使用的双向链表节点
    key: key
    val: val
    prev: prev node
    next: next node
    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.disconnect()

    def disconnect(self):
        self.prev = None
        self.next = None


class LRUCache(object):
    """
    利用双向链表和散列表实现的的LRUCache（最近最少使用缓存机制）
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        dummy = LinkNode(None, None)
        self.head = dummy
        self.tail = dummy
        if capacity <= 0:
            raise ArgumentError("Capacity must be greater than 0")
        self.capacity = capacity
        self.size = 0
        self.table = {}

    def get(self, key):
        """
        取得key对应的缓存值
        :type key: int
        :rtype: int
        """
        if key in self.table:
            node = self.table[key]
            self.__remove_node(node)
            self.__head_insert(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        插入key,value
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.table:
            node = self.table[key]
            self.__remove_node(node)
            self.__head_insert(node)
            node.val = value
        else:
            if self.size == self.capacity:
                tail = self.tail
                self.__remove_tail()
                self.size -= 1
                del self.table[tail.key]
            new_node = LinkNode(key, value)
            self.__head_insert(new_node)
            self.size += 1
            self.table[key] = new_node

    def __remove_node(self, node):
        """
        从内部的双向链表中删除指定节点node
        :type node: LinkNode
        :rtype None
        """
        if node is None:
            return
        if node == self.tail:
            self.tail = node.prev
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.disconnect()

    def __remove_tail(self):
        """
        从内部的双向链表删除tail
        :rtype None
        """
        if self.head == self.tail:
            # nothing to remove
            return
        self.__remove_node(self.tail)

    def __head_insert(self, new_node):
        """
        将指定节点node插入到内部的双向链表头部
        :type new_node: LinkNode
        """
        if new_node is None:
            return
        if self.head.next is None:
            self.tail = new_node
        next_node = self.head.next
        new_node.prev = self.head
        new_node.prev.next = new_node
        if next_node:
            new_node.next = next_node
            next_node.prev = new_node

    def __str__(self):
        nodes = []
        node = self.head.next
        while node:
            nodes.append(node)
            node = node.next
        return "Linked list {list}, tail {tail}".format(
            list=str([node.val for node in nodes]),
            tail=self.tail.val
        )

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# obj.put(key,value)
# param_1 = obj.get(key)


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)  # 缓存是 {1=1}
    lru.put(2, 2)  # 缓存是 {1=1, 2=2}
    print(str(lru))
    print(lru.get(1))   # 返回 1
    print(str(lru))
    lru.put(3, 3)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    print(str(lru))
    print(lru.get(2))   # 返回 -1 (未找到)
    lru.put(4, 4)  # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    print(lru.get(1))   # 返回 -1 (未找到)
    print(lru.get(3))   # 返回 3
    print(lru.get(4))   # 返回 4

    lru2 = LRUCache(2)
    lru2.put(2, 1)
    lru2.put(2, 2)
    print(lru2.get(2))  # 返回 2
    lru2.put(1, 1)
    lru2.put(4, 1)
    print(lru2.get(2))  # 返回 -1
