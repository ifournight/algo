class CircleArrayQueue(object):
  def __init__(self, capacity):
    self.array = [None] * capacity
    self.capacity = capacity
    self.head = 0
    self.tail = 0
  def __str__(self):
    if self.head <= self.tail:
      return str(self.array[self.head : self.tail])
    else:
      return str(self.array[self.head:] + self.array[:self.tail])
  def enqueue(self, item):
    if (self.tail + 1) % self.capacity == self.head:
      print('Full queue')
      return False
    self.array[self.tail] = item 
    self.tail = (self.tail + 1) % self.capacity
    return True
  def dequeue(self):
    if self.tail == self.head:
      print('Empty queue')
      return None
    else:
      item = self.array[self.head]
      self.head = (self.head + 1) % self.capacity
      return item

if __name__ == "__main__":
  queue = CircleArrayQueue(10)
  for i in range(10):
    queue.enqueue(i)
    print(queue)
  queue.enqueue(11)
  for i in range(20):
    print('dequeue: %s' % queue.dequeue())
    print('%s, head: %s, tail: %s' % (str(queue), queue.head, queue.tail))
  for i in range(10, 20):
    queue.enqueue(i)
    print('%s, head: %s, tail: %s' % (str(queue), queue.head, queue.tail))
  queue.dequeue()
  print(queue)
    
