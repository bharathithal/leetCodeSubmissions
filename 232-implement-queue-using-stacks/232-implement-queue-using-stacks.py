class MyQueue:

    def __init__(self):
        self.stack = []
        self.index = 0

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.index += 1
        return self.stack[self.index-1]

    def peek(self):
        return self.stack[self.index]

    def empty(self):
        return self.index >= len(self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()