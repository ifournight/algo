class LinkNode(object):
  def __init__(self, val):
    self.val = val
    self.disconnect()

  def disconnect(self):
    self.next = None

class LinkedStack(object):
  def __init__(self):
    self.top = None

  def __str__(self):
    s = []
    curr = self.top
    while curr:
      s.append(curr.val)
      curr = curr.next
    s.reverse()
    return ' '.join(str(item) for item in s)


  def push(self, val):
    node = LinkNode(val)
    if self.top:
      node.next = self.top
    self.top = node

  def peekPop(self):
    return self.top
  
  def pop(self):
    if self.top:
      top = self.top
      self.top = self.top.next
      top.disconnect()
      return top.val
    else:
      return None

if __name__ == "__main__":
  stack = LinkedStack()
  for i in range(9):
    stack.push(i)
  print(stack)
  for _ in range(3):
    stack.pop()
  print(stack)
  for i in range(3):
    stack.push(i)
  print(stack)
  