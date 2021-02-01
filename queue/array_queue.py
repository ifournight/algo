# Queue implemented with array, whose amotized time complexity of enqueue is O(1)
# and time complexity of dequeue is O(1)
import unittest


class ArrayQueue(object):
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.tail - self.head

    def __str__(self):
        return str(self.array)

    def enqueue(self, item):
        if self.tail == self.capacity:
            if self.head == 0:
                print('Queue is full, enqueue failed.')
                return False
            else:
                self.array[0: self.tail -
                           self.head] = self.array[self.head: self.tail]
                self.tail -= self.head
                self.head = 0
        self.array[self.tail] = item
        self.tail += 1
        return True

    def peek(self):
        return self.array[self.head]

    def dequeue(self):
        if self.tail != self.head:
            item = self.array[self.head]
            self.array[self.head] = None
            self.head += 1
            return item
        else:
            print('Queue is Empty, dequeue failed.')
            return None


class TestQueue(unittest.TestCase):
    def testFIFO(self):
        queue = ArrayQueue(5)
        for i in range(3):
            queue.enqueue(i)
        for i in range(3):
            self.assertEqual(queue.dequeue(), i)

    def testPeek(self):
        queue = ArrayQueue(5)
        for i in range(3):
            queue.enqueue(i)
        for i in range(3):
            self.assertEqual(queue.peek(), i)
            queue.dequeue()

    def testDequeueFromEmptyQueue(self):
        queue = ArrayQueue(5)
        self.assertEqual(queue.dequeue(), None)

    def testPeekFromEmptyQueue(self):
        queue = ArrayQueue(5)
        self.assertEqual(queue.peek(), None)

    def testMovingInsideEnqueue(self):
        queue = ArrayQueue(5)
        for i in range(3):
            queue.enqueue(i)
        queue.dequeue()
        queue.dequeue()
        for i in range(3):
            queue.enqueue(i)
        for i in [2, 0, 1, 2]:
            self.assertEqual(queue.dequeue(), i)

    def testFullQueueEnqueue(self):
        queue = ArrayQueue(5)
        for i in range(5):
            queue.enqueue(i)
        queue.enqueue(0)
        for i in range(5):
            self.assertEqual(queue.dequeue(), i)
        


if __name__ == "__main__":
    unittest.main()
