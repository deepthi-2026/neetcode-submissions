class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        return self.items.append(x)
        

    def pop(self) -> int:
        x = self.items.pop(0)
        return x
        

    def peek(self) -> int:
        return self.items[0]
        

    def empty(self) -> bool:
        if len(self.items)==0:
            return True
        return False

que = MyQueue()
que.push(1)
que.push(2)
print(que.peek())
que.pop()
que.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()