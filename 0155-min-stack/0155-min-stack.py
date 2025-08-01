class MinStack:

    def __init__(self):
        self.top_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.top_stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.top_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.top_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()