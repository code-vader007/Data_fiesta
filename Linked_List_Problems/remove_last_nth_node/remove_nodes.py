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
    
    def remove_nodes(self,n):
        n_front=self.numItems-n+1
        ptr1=self.first
        ptr2=self.first.next
        count=1
        while(count!=n_front):
            ptr1=ptr1.next
            ptr2=ptr2.next
            count+=1
        ptr1.next=ptr2.next
        self.numItems-=1



list=LinkedList([1,2,3,4,6])
list.printList()
list.remove_nodes(3)
list.printList()