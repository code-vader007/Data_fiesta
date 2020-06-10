
##Implement three stacks using only one array
class Stack:
    def __init__(self,size=20):
        self.items = [None] * size
        self.numItems = 0
        self.size = size
        self.top1=-1
        self.top2=self.size//2 - 1
        self.top3=self.size

    def top1(self):
        if self.top1==-1:
            return "Stack is empty"
        return self.top1
    def top2(self):
        if self.top2==self.size//2 - 1:
            return "Stack is empty"
        return self.top2
    def top3(self):
        if self.top3==self.size:
            return "Stack is empty"
        return self.top3
    def pop1(self):
        if(self.top1==-1):
            return "Stack empty"
        topelement=self.items[self.top1]
        self.items[self.top1]=None
        self.top1-=1
    def pop2(self):
        if(self.top1==self.size//2 - 1):
            return "Stack empty"
        topelement=self.items[self.top2]
        self.items[self.top2]=None
        self.top2-=1
    def pop3(self):
        if(self.top1==self.size):
            return "Stack empty"
        topelement=self.items[self.top3]
        self.items[self.top3]=None
        self.top2+=1
    def isEmpty(self):
        if self.numItems != 0:
            return False
        return True
    def push1(self,item):
        if(self.top1==self.top3-1):
            return "Stack 1 filled"
        ind=self.items.index(self.top)
    def push1(self,item):
        if(self.numItems==self.size):
            return "Overflow"
        if(self.top1<self.size//2 - 1):
            self.top1+=1
            self.items[self.top1]=item
            self.numItems+=1
            return "Successful"
        else:
            if(self.top2<self.top3-1):
                for i in range(self.top2+1,self.top1,-1):
                    self.items[i]=self.items[i-1]
                self.top2+=1
                self.top1+=1
                self.items[self.top1]=item
                self.numItems+=1
                return "Successful"
            else:
                return "Overflow"
    def push2(self,item):
        if(self.numItems==self.size):
            return "Overflow"
        if(self.top2<self.top3 - 1):
            self.top2+=1
            self.items[self.top2]=item
            self.numItems+=1
            return "Successful"
        else:
            if(self.top1<self.size//2 - 1):
                for i in range(self.top1+1,self.top2):
                    self.items[i]=self.items[i+1]
                self.items[self.top2]=item
                self.numItems+=1
                return "Successful"
            else:
                return "Overflow"
    def push3(self,item):
        if(self.numItems==self.size):
            return "Overflow"
        if(self.top2<self.top3 - 1):
            self.top3-=1
            self.items[self.top3]=item
            self.numItems+=1
            return "Successful"

    def printstk(self):
        for i in self.items:
            print(i)
#stk=Stack()
#print(stk.top1)
#print(stk.top2)
#print(stk.top3)
#for i in range(7):
#    stk.push1(i)
#for i in range(4):
#    stk.push3(i)
#for i in range(4):
#    stk.push2(i)
#stk.push2(10)
#stk.push2(11)
##stk.push2(12)
#stk.push2(13)
#stk.push2(14)
#print(stk.top1)
#print(stk.top2)
#print(stk.top3)

#stk.printstk()
