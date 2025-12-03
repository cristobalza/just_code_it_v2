class MinStack:

    def __init__(self):
        self.max_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.max_stack.append(val)
        if self.min_stack:
            curr_min_val = self.min_stack[-1]
            self.min_stack.append(min(curr_min_val, val))
        else:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        self.min_stack.pop()
        self.max_stack.pop()
        

    def top(self) -> int:
        return self.max_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()