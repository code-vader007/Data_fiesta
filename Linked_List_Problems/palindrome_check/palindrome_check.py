class LinkedList:
    class __Node:
        def __init__(self,item,next=None):
            self.item=item
            self.next=next
        def getItem(self):
            return self.item
        def getNext(self):
            return self.next
        def setItem(self,item):
            self.item = item
        def setNext(self,next):
            self.next = next

    def __init__(self,contents=[]):
        self.first = LinkedList.__Node(None,None)
        self.numItems = 0
        self.first.setNext(self.first)
        self.last = self.first
        for e in contents:
            self.append(e)

    def printList(self):
        tmp = self.first.next
        nodes = []
        for i in range(self.numItems):
            nodes.append(str(tmp.item))
            tmp = tmp.next
        print(' -> '.join(nodes))

    def append(self,item):
        lastNode = self.last
        newNode = LinkedList.__Node(item,self.first)
        lastNode.setNext(newNode)
        self.last = newNode
        self.numItems += 1
    def palindrome(self):
        A=[]
        B=[]
        stack=Stack()
        queue=Fifo()
        curs=self.first.next
        for i in range(self.numItems):
            stack.push(str(curs.item))
            queue.pushback(str(curs.item))
            curs=curs.next
        curs=self.first.next
        for i in range(self.numItems):
            A.append(stack.pop())
            B.append(queue.popfront())
            curs=curs.next
        for i in range(self.numItems):
            if(A[i]!=B[i]):
                return False
        return True
#list=LinkedList([1,2,2,2,2,3,4,5,5])
#list.printList()
#list.duplicates()
#list.printList()
class Fifo:
    def __init__(self,size=20):
        self.items = [None] * size
        self.first = 0
        self.last = -1
        self.size = size
        self.length = 0
    def isEmpty(self):
        if self.length != 0:
            return False
        return True
    def front(self):
        if self.length != 0:
            return self.items[self.first]
        raise ValueError("Queue is empty")
    def back(self):
        if self.length != 0:
            return self.items[self.last]
        raise ValueError("Queue is empty")
    def pushback(self,item):
        if self.length == self.size:
            self.allocate()
        self.last = (self.last + 1) % self.size
        self.items[self.last] = item
        self.length += 1
    def popfront(self):
        if self.size > 20 and self.length == self.size / 4:
            self.deallocate()
        if self.length != 0:
            frontelement = self.items[self.first]
            self.first = (self.first + 1) % self.size
            self.length -= 1
            return frontelement
        raise ValueError("Queue is empty")
    def allocate(self):
        newlength = 2 * self.size
        length = self.length
        newQueue = [None] * newlength
        for i in range(self.size):
            pos = (i + self.first) % self.size
            newQueue[i] = self.items[pos]
        self.items = newQueue
        self.first = 0
        self.last = self.size - 1
        self.size = newlength
        self.length = length
    def deallocate(self):
        newlength = self.size // 2
        length = self.length
        newQueue = [None] * newlength
        length = self.length
        for i in range(length):
            pos = (i + self.first) % self.size
            newQueue[i] = self.items[pos]
        self.items = newQueue
        self.first = 0
        self.last = length - 1
        self.size = newlength
        self.length = length
    def __iter__(self):
        rlast = self.first + self.length
        for i in range(self.first,rlast):
            yield self.items[i % self.size]
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


list=LinkedList([])
list.printList()
print(list.palindrome())
