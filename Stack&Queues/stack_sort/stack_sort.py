
##Sorting a stack without the hel of other data structures.
class Stack:
    def __init__(self,size=20):
        self.items = [None] * size
        self.numItems = 0
        self.size = size

    def top(self):
        if self.numItems != 0:
            return self.items[self.numItems-1]
        return("Stack is empty")

    def push(self,item):
        #if self.numItems == self.size:
        #    self.allocate()
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
        #if self.numItems == self.size / 4:
        #    self.deallocate()
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
    def printstk(self):
        for i in range(self.numItems):
            print(self.items[i])

    def sort(self):
        stemp=Stack()
        a=self.numItems
        for i in range(0,a):
            min=self.top()
            k=0
            while(self.isEmpty()==False):
                if(self.top()<=min):
                    min=self.top()
                stemp.push(self.pop())
            while(stemp.isEmpty()==False):
                if(stemp.top()==min):
                    k=stemp.pop()
                else:
                    self.push(stemp.pop())
            stemp.push(k)

            while(self.isEmpty()==False and self.top()<=min):
                    stemp.push(self.pop())
        while(stemp.isEmpty()==False):
            self.push(stemp.pop())

stk=Stack()
for i in [10,8,1,5,6]:
    stk.push(i)
stk.printstk()
stk.sort()
stk.printstk()
