class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        return self.items.append(val)

    def pop(self) -> None:
        if len(self.items) == 0:
            return "cannot pop stack is empty"
        x = self.items.pop(-1)
        return x

    def top(self) -> int:
        if len(self.items)==0:
            return "cannot pop stack is empty"
        return self.items[-1]
        

    def getMin(self) -> int:
        if len(self.items)==0:
            return "cannot pop stack is empty"
        return min(self.items)
        
