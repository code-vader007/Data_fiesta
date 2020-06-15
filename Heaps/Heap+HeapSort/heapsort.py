class heap:
    def __init__(self,arbitrary_array):
        self.list=arbitrary_array
        self.build_heap(len(self.list),len(self.list))

    def build_heap(self,length,end):
        index=length//2
        for i in range(index,0,-1):
            self.siftdown(i,end)

    def siftdown(self,i,end):

        current_node=self.list[i-1]

        right_child=self.get_right_child(i)
        left_child=self.get_left_child(i)
        if right_child==None and left_child==None:
            return
        if  (2 * i +1)>end:
            right_child=None
        if  (2 * i)>end:
            left_child=None

        if right_child!=None and left_child!=None:
            if right_child>=left_child:
                if current_node<right_child:
                    temp= self.list[i-1]
                    self.list[i-1]=self.list[2 * i ]
                    self.list[2 * i ]=temp
                    return self.siftdown(2 * i+1,end)


            else:
                if current_node<left_child:
                    temp= self.list[i-1]
                    self.list[i-1]=self.list[2 * i-1]
                    self.list[2 * i-1]=temp
                    return self.siftdown(2 * i-1+1,end)



        else:
            if left_child!=None and current_node<left_child:
                    temp= self.list[i-1]
                    self.list[i-1]=self.list[2 * i-1]
                    self.list[2 * i-1]=temp
                    return self.siftdown(2 * i-1+1,end)
            if right_child!=None and current_node<right_child:
                    temp= self.list[i-1]
                    self.list[i-1]=self.list[2 * i ]
                    self.list[2 * i ]=temp
                    return self.siftdown(2 * i+1,end)


    def get_parent(self,index):
        if (index//2)<=len(self.list):
            return self.list[index//2-1]
        return None

    def get_right_child(self,index):
        if (2 * index + 1)<=len(self.list):
            return self.list[2 * index ]
        return None


    def get_left_child(self,index):
        if (2 * index)<=len(self.list):
            return  self.list[2 * index-1]
        return None
    def __str__(self):
        return str(self.list)

    def heapsort(self):


        for i in range(1,len(self.list)):
            last=self.list[len(self.list)-i]
            first=self.list[0]
            self.list[len(self.list)-i]=first
            self.list[0]=last

            self.build_heap(len(self.list),len(self.list)-i)

#test
a=[6, 4, 9, 7, 6, 10, 1, 5, 2, 3]
b=heap(a)
print(b)
b.heapsort()
print(b)
