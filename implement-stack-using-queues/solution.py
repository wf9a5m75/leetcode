class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.n = 0
        self.isQ1 = True

    def push(self, x: int) -> None:
        if self.isQ1 == False:
            self._flip()
        self.queue1.append(x)
        self.n += 1

    def pop(self) -> int:
        if self.isQ1:
            self._flip()
        self.n -= 1
        return self.queue2.pop(0)

    def _flip(self):
        if self.isQ1:
            # from
            #    queue1 = [(1), (2), (3), (4)]
            # to
            #    queue2 = [(4), (3), (2), (1)]
            for i in range(self.n):
                self.queue2.append(self.queue1.pop())
            self.isQ1 = False
        else:
            # from
            #    queue2 = [(4), (3), (2), (1)]
            # to
            #    queue1 = [(1), (2), (3), (4)]

            for i in range(self.n):
                self.queue1.append(self.queue2.pop())
            self.isQ1 = True


    def top(self) -> int:
        if self.isQ1:
            self._flip()
        return self.queue2[0]


    def empty(self) -> bool:
        return self.n == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
