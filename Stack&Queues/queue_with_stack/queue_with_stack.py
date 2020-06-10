
##A queuu implemented with two stacks

class Stack:
    def __init__(self,size=20):
        self.items = [None] * size
        self.numItems = 0
        self.size = size

    def top(self):
        if self.numItems != 0:
            return self.items[self.numItems-1]
        raise Error("Stack is empty")

    def push(self,item):
        if self.numItems == self.size:
            self.allocate()
        self.items[self.numItems] = item
        self.numItems += 1

    def allocate(self):
        newlength = 2 * self.size
        newStack = [None] * newlength
        for i in range(self.numItems):
            newStack[i] = self.items[i]
        self.items = newStack
        self.size = newlength

    def pop(self):
        if self.numItems == self.size / 4:
            self.deallocate()
        if self.numItems != 0:
            topelement = self.items[self.numItems-1]
            self.numItems -= 1
            return topelement
        raise Error("Stack is empty")

    def deallocate(self):
        newlength = self.size // 2
        newStack = [None] * newlength
        for i in range(self.numItems):
            newStack[i] = self.items[i]
        self.items = newStack
        self.size = newlength

    def isEmpty(self):
        if self.numItems != 0:
            return False
        return True
class MyQueue:
    def __init__(self,size=20):
        self.s1=Stack()
        self.s2=Stack()
        self.numItems=0
        self.size=size
    def enqueue(self,item):
        if(self.s1.numItems==self.size):
            return "Overflow"
        self.s1.push(item)
        self.numItems+=1
    def dequeue(self):
        if(self.numItems==0):
            return "Queue empty"
        while(self.s1.isEmpty()==False):
            self.s2.push(self.s1.pop())
        result=self.s2.pop()
        while(self.s2.isEmpty()==False):
            self.s1.push(self.s2.pop())
        self.numItems-=1
        return result

que=MyQueue()
for i in range(10):
    que.enqueue(i)

for i in range(10):
    print(que.dequeue())
