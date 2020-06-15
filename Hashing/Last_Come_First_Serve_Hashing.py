# Last-come-first-served hashing. Here an element to be inserted is always placed
# in the position given by its hash value. If this position is occupied, the current
# “resident” is moved to another position using the search procedure defined for HashSet.
class LCFSHashSet:
    class __Placeholder:
        def __init__(self):
            pass
        def __eq__(self,other):
            return False
    def __init__(self,contents=[]):
        self.items = [None] * 20
        self.numItems = 0
        for e in contents:
            self.add(e)
    def add(self,item):
        if LCFSHashSet.__add(item,self.items):
        # it will return false if the item is already in
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = LCFSHashSet.__rehash(self.items,[None]*2*len(self.items))
    # __add partly
    def __add(item,items):
        index = hash(item) % len(items)
        position = index
        if items[index] != None:
            location = -1
            resident = items[index]
            index = (index + 1) % len(items)
            while items[index] != None:
                if items[index] == item:
                    return False
                if location < 0 and type(items[index]) == LCFSHashSet.__Placeholder:
                    location = index
                index = (index + 1) % len(items)
            if location < 0:
                location = index
            items[location] = resident
        items[position] = item
        return True
    #__rehash
    def __rehash(olditems,newitems):
        for e in olditems:
            if e != None and type(e) != LCFSHashSet.__Placeholder:
                HashSet.__add(e,newitems)
        return newitems
    #__contains__
    def __contains__(self,item):
        index = hash(item) % len(self.items)
        while self.items[index] != None:
            if self.items[index] == item:
                return True
            index = (index + 1) % len(self.items)
        return False
    #delete
    def delete(self,item):
        if HashSet.__remove(item,self.items):
            self.numItems -= 1
            load = max(self.numItems,20) / len(self.items)
            if load <= 0.25:
                self.items = LCFSHashSet.__rehash(self.items,[None]*(len(self.items)//2))
        else:
            raise KeyError("Item not in HashSet")
    #__remove
    def __remove(item,items):
        index = hash(item) % len(items)
        while items[index] != None:
            if items[index] == item:
                nextIndex = (index + 1) % len(items)
                if items[nextIndex] == None:
                    items[index] = None
                else:
                    items[index] = LCFSHashSet.__Placeholder()
                return True
            index = (index + 1) % len(items)
        return False
