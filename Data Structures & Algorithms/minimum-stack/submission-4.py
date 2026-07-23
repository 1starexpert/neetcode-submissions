class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = None
        self.small_stack = []

    def push(self, val: int) -> None:
        """
        [2, 5, 0]
        """
        self.stack.append(val)
        if self.smallest is None:
            self.smallest = val
        else:
            if val <= self.smallest:
                self.small_stack.append(self.smallest)
                self.smallest = val

    def pop(self) -> None:
        if self.top() == self.smallest and len(self.small_stack) > 0:
            ## you are cooked
            self.smallest = self.small_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 1:
            return self.top()
        return self.smallest
