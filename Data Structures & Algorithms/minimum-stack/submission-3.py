class MinStack:

    def __init__(self):
        self.stack = []
        self.minvalprefix = []

    def push(self, val: int) -> None:
        if len(self.minvalprefix) == 0:
            self.minvalprefix = [val]
        elif len(self.minvalprefix) > 0 and self.minvalprefix[-1] > val:
            self.minvalprefix.append(val)
        else:
            self.minvalprefix.append(self.minvalprefix[-1])

        self.stack.append(val)

    def pop(self) -> None:
        self.stack = self.stack[0:-1] # .remove(self.stack[-1])
        self.minvalprefix = self.minvalprefix[0:-1] #.remove(self.minvalprefix[-1])

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvalprefix[-1]
        
