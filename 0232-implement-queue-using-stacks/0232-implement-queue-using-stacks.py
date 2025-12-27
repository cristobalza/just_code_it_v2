class MyQueue:
    """ 

    front [] back []

    >> push [1]

    front [] back [1]

    >> push [2]

    front [1] back [2]

    >> peek -> 1

    >> pop -> 1

    front [] back [2]




    """

    def __init__(self):
        self.front = []
        self.back = []
        

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
        return self.front.pop()


    def peek(self) -> int:
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
        return self.front[-1]
        

    def empty(self) -> bool:
        return len(self.front) == 0 and len(self.back) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()