class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = [2 ** 31]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minn.append(val if val < self.minn[-1] else self.minn[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1]
        
