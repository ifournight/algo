class Stack(object):
  def __init__(self):
    self.array = []
  def __len__(self):
    return len(self.array)
  def __str__(self):
    return str(self.array)
  def push(self, item):
    self.array.append(item)
  def peek(self):
    return self.array[-1]
  def pop(self):
    return self.array.pop()
  def clear(self):
    self.array = []

if __name__ == "__main__":
  stack = Stack()
  for i in range(9):
    stack.push(i)
  print(stack)
  for _ in range(3):
    stack.pop()
  print(stack)
  for i in range(3):
    stack.push(i)
  print(stack)