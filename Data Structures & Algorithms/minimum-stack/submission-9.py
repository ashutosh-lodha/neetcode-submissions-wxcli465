class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstk=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstk or val<=self.minstk[-1]:
            self.minstk.append(val)

    def pop(self) -> None:
        top=self.stack.pop()
        if self.minstk and top==self.minstk[-1]:
            self.minstk.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
