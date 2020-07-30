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
            self.sort_list_append(e)

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
    def sort_list_append(self,item):
        newNode = LinkedList.__Node(item,self.first)
        tmp1=self.first
        tmp2=tmp1.next
        while(tmp2.item!=None):
            if(self.numItems==0):
                self.append(item)
                return
            if(tmp2.item>item):
                tmp1.setNext(newNode)
                newNode.setNext(tmp2)
                self.numItems+=1
                return 
            else:
                tmp1=tmp1.next
                tmp2=tmp2.next
        if(tmp2.item==None):
            self.append(item)


list=LinkedList([5,4,10,6,11])
list.printList()
