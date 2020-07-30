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
    
    def remove_duplicates(self):
        tmp1=self.first.next
        tmp2=tmp1.next
        while(tmp1.item!=None):
            if(tmp1.item==tmp2.item):
                count=0
                while(tmp2.next.item==tmp1.item):
                    count+=1
                    tmp2=tmp2.next
                tmp1.next=tmp2.next
                tmp1=tmp1.next
                tmp2=tmp1.next
                self.numItems-=count+1
            else:
                tmp1=tmp1.next
                tmp2=tmp2.next


list=LinkedList([1,1,1,2,2,2,2,3,3,4,5,5,5,5,5,5,5,5])
list.printList()
list.remove_duplicates()
list.printList()