# coding: UTF-8


class MinStack(object):
    """支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈"""

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        将元素压入栈
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        """
        删除并返回栈顶元素
        :rtype: None
        """
        if len(self.stack) == 0:
            return None
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        """
        获取栈顶元素
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        返回最小元素，如果不存在返回None
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
