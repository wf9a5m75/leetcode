class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.isS1 = False
        self.total = 0

    def _flip(self):
        if (self.isS1):
            while(self.s1):
                self.s2.append(self.s1.pop())
        else:
            while(self.s2):
                self.s1.append(self.s2.pop())
        self.isS1 = not self.isS1

    def push(self, x: int) -> None:
        if (not self.isS1):
            self._flip()
        self.s1.append(x)
        self.total += 1

    def pop(self) -> int:
        if (self.isS1):
            self._flip()

        self.total -= 1
        return self.s2.pop()

    def peek(self) -> int:
        if (self.isS1):
            self._flip()

        return self.s2[-1]


    def empty(self) -> bool:
        return self.total == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
