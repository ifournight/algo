# Queue implemented with array, whose time complexity of enqueue is O(1)
# and amotized time complexity of dequeue is O(1)
class ArrayQueue(object):
  def __init__(self, capacity):
    self.array = []
    self.capacity = capacity
    self.head = 0
    self.tail = 0
  
  def __len__(self):
    return self.tail - self.head

  def __str__(self):
    return str(self.array)
    # return str(self.array[self.head:self.tail])

  def enqueue(self, item):
    if self.tail == self.capacity:
      if self.head == 0:
        print('Queue is full, enqueue failed.')
        return
      else:
        self.array = self.array[self.head:self.tail]
        self.tail = self.tail - self.head
        self.head = 0
    self.array.append(item)
    self.tail += 1
  
  def dequeue(self):
    if self.tail == self.head:
      print('Queue is Empty, dequeue failed.')
      return None
    item = self.array[self.head]
    self.array[self.head] = None
    self.head += 1
    if self.tail == self.head:
      del self.array[:self.head]
      self.head = 0
      self.tail = 0
    return item

if __name__ == "__main__":
  queue = ArrayQueue(10)
  for i in range(10):
    queue.enqueue(i)
    print(queue)
  queue.enqueue(11)
  for i in range(5):
    print('dequeue: %s' % queue.dequeue())
    print('%s, head: %s, tail: %s' % (str(queue), queue.head, queue.tail))
  for i in range(10, 20):
    queue.enqueue(i)
    print('%s, head: %s, tail: %s' % (str(queue), queue.head, queue.tail))
  queue.dequeue()
  print(queue)

  