# Robin Hood hashing. Here it is checked for two elements competing for the same position,
# how far away they are stored from the ideal position given by their hash value.
# Then the chaining search is applied to the element closer to this ideal position.
class RHHashSet:
    class __Placeholder:
        def __init__(self):
            pass
        def __eq__(self,other):
            return False
    def __init__(self,contents=[]):
        self.items = [None] * 20
        self.numItems = 0
        self.PSLs = [0] * 20
        # distance from the ideal position
        for e in contents:
            self.add(e)
    def add(self,item):
        if RHHashSet.__add(item,self.items,self.PSLs):
        # it will return false if the item is already in
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = RHHashSet.__rehash(self.items,[None]*2*len(self.items))
    def __add(item,items,PSLs):
        index = hash(item) % len(items)
        PSL = 0
        while items[index] != None and type(items[index]) != RHHashSet.__Placeholder:
            if items[index] == item:
                #already in, then return false
                return False
            if PSL > PSLs[index]:
                R1 = items[index]
                items[index] = item
                item = R1
                R1 = PSLs[index]
                PSLs[index] = PSL
                PSL = R1
            PSL += 1
            index = (index + 1) % len(items)
        items[index] = item
        PSLs[index] = PSL
        return True
    # same from lecture
    def __rehash(olditems,newitems):
        for e in olditems:
            if e != None and type(e) != RHHashSet.__Placeholder:
                HashSet.__add(e,newitems)
        return newitems
    def __contains__(self,item):
        index = hash(item) % len(self.items)
        PSL = 0
        while self.items[index] != None:
            if PSL > self.PSLs[index]:
                return False
            if self.items[index] == item:
                return True
            PSL += 1
            index = (index + 1) % len(self.items)
        return False
    def delete(self,item):
        if HashSet.__remove(item,self.items):
            self.numItems -= 1
            load = max(self.numItems,20) / len(self.items)
            if load <= 0.25:
                self.items = RHHashSet.__rehash(self.items,[None]*(len(self.items)//2))
        else:
            raise KeyError("Item not in HashSet")
    def __remove(item,items):
        index = hash(item) % len(items)
        while items[index] != None:
            if items[index] == item:
                nextIndex = (index + 1) % len(items)
                if items[nextIndex] == None:
                    items[index] = None
                else:
                    items[index] = RHHashSet.__Placeholder()
                return True
            index = (index + 1) % len(items)
        return False
