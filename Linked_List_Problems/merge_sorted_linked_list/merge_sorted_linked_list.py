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

def heapify(arr, n, i): 
    largest = i; # Initialize largest as root 
    l = 2 * i + 1; # left = 2*i + 1 
    r = 2 * i + 2; # right = 2*i + 2 
    if l < n and arr[l] > arr[largest]: 
        largest = l; 
    if r < n and arr[r] > arr[largest]: 
        largest = r;  
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]; 
        heapify(arr, n, largest); 

def buildHeap(arr, n):  
    startIdx = n // 2 - 1; 
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i);

    return arr

def sorted(list1,list2):
    l1=LinkedList(list1)
    l2=LinkedList(list2)
    list3=[]
    prqueue=[]
    ptr=l1.first.next
    while(ptr.item!=None):
        prqueue.append(ptr.item)
        ptr=ptr.next
    ptr2=l2.first.next
    while(ptr2.item!=None):
        prqueue.append(ptr2.item)
        ptr2=ptr2.next

    while(len(prqueue)!=0):
        prqueue=buildHeap(prqueue,len(prqueue))
        maxi=prqueue.pop(0)
        list3.insert(0,maxi)
    l3=LinkedList(list3)

    return l3
    

list1=[7,8,9,10]
list2=[1,2,2,3]
list3=sorted(list1,list2)
list3.printList()