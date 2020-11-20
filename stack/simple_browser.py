from stack import Stack

class SimpleBrowser(object):
  # Use 2 stack to implement a simple browswer which can:
  # - visit page
  # - go backward if can
  # - go forward if can
  def __init__(self):
    self.backward = Stack()
    self.forward = Stack()

  def __str__(self):
    return str(self.backward) + '|' + str(self.forward)

  def visit(self, page):
    self.backward.push(page)
    self.forward.clear()
    print('Browser visit %s' % str(page))

  def get_current(self):
    if len(self.backward) == 0:
      return None
    return self.backward.peek()
  
  def go_forward(self):
    if len(self.forward) == 0:
      print("Browser can't go forward")
      return
    page = self.forward.pop()
    self.backward.push(page)
    print('Browser go forward to %s' % str(page))

  def go_backward(self):
    if len(self.backward) <= 1:
      print("Browser can't go backward")
      return
    page = self.backward.pop()
    self.forward.push(page)
    print('Browser go back to %s' % str(self.backward.peek()))

if __name__ == "__main__":
  browser = SimpleBrowser()
  browser.visit('a')
  browser.visit('b')
  browser.visit('c')
  browser.visit('d')
  print(browser)
  browser.go_backward()
  browser.go_backward()
  print(browser)
  browser.go_forward()
  browser.go_forward()
  print(browser)
  browser.go_backward()
  browser.go_backward()
  print(browser)
  browser.visit('e')
  print(browser)
  browser.go_forward()