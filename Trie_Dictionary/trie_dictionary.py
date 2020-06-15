class Trie:
    class TrieNode:
        #The initialisation of the trienode
        def __init__(self,item,next=None,last=None):
            self.item=item
            self.next=next
            self.last=last
            self.ch=[None]*26
            self.endofword=None
    #Initialisation
    def __init__(self):s
        self.head = None
    #Pseudo for insert
    def insert(self,item):
        item = list(item)
        self.head = Trie.insert_real(self.head,item+['#'])
    #Pseudo for search
    def __search__(self,item):
        item = list(item)
        return Trie.search_real(self.head,item+['#'])
    #The actual insert method in the trie tree
    def insert_real(node,s):
        if s == []:
            return None
        if node == None:
            k = s.pop(0)
            new = Trie.TrieNode(k)
            new.last = Trie.insert_real(new.last,s)
            return new
        else:
            k = s[0]
            if node.item == k:
                k = s.pop(0)
                node.last = Trie.insert_real(node.last,s)
            else:
                node.next = Trie.insert_real(node.next,s)

            return node
    #The actual search method in the trie tree
    def search_real(node,key):
        if key == []:
            return True
        if node == None:
            return False
        k = key[0]
        if node.item == k:
            k = key.pop(0)
            return Trie.search_real(node.last,key)
        else:
            return Trie.search_real(node.next,key)
    #The compsearch inshort for complete search completes a search for the word by one symbol if that
    #word doesnot already contain in the trie
    def compsearch(self,item):
        item = list(item)
        comp= Trie.compsearch_real(self.head,item+['#'])
        if type(comp) == list:
            if comp != []:
                for i in range(len(comp)):
                    comp[i] = "".join(item) + comp[i]
                return comp
            else:
                return False
        else:
            return comp
    #The actual compsearch method
    def compsearch_real(node,key):
        if (node == None) and (key != ['#']):
            return False
        if key == ['#']:
            if Trie.search_real(node,['#']):
                return True
            else:
                value = []
                temp_node = node
                while temp_node != None:
                    if Trie.search_real(temp_node.last,['#']):
                        comp = temp_node.item
                        value.append(comp)
                    temp_node = temp_node.next
                return value
        k = key[0]
        if node.item == k:
            k = key.pop(0)
            return Trie.compsearch_real(node.last,key)
        else:
            return Trie.compsearch_real(node.next,key)

    #The presearch which is in short for prefix search return suggestions for a word not found in the trie
    #by suggesting words which have the desired word as the prefix
    def presearch(self,item):
        item = list(item)
        value = Trie.presearch_real(self.head,item+['#'])

        if type(value) == list:
            if value == []:
                return False
            else:
                list_value = []
                if 1 in value:
                    list_value.append("".join(item[0:len(item)-1]))
                if 2 in value:
                    list_value.append("".join(item[0:len(item)-2]))
                return list_value
        else:
            return value

    def presearch_real(node,key):

        if (len(key) >= 4) and key == None:
            return False
        if len(key) == 3:
            temp_key = key[:]
            if Trie.search_real(node,temp_key):
                return True
            else:
                return_list = []
                if Trie.search_real(node,list(key[0])+['#']):
                    return_list.append(1)
                if Trie.search_real(node,['#']):
                    return_list.append(2)
                return return_list
        k = key[0]
        if k == node.item:
            k = key.pop(0)
            return Trie.presearch_real(node.last,key)
        else:
            return Trie.presearch_real(node.next,key)

    #The suggsearh inshort for suggesting search returns words which have only one character altered or changed.
    def suggsearch(self,item):
        item = list(item)
        return Trie.suggsearch_real(self.head,item+['#'])

    def suggsearch_real(node,key):
        temp_key = key[:]
        value = Trie.search_one(node,temp_key,0)
        if value == True:
            return True
        else:
            index = min(int(value),len(key)-2)
            result = []
            for i in range(index+1):
                new_key =key[0:i] + ['$'] + key[i+1:]
                return_list = Trie.search_two(node,new_key)
                for element in return_list:
                    joint_list = key[0:i]+[element]+key[i+1:]
                    result.append("".join(joint_list[0:len(joint_list)-1]))
            return result
    #Helper function for suggsearch
    def search_one(node,item,index):
        if item == []:
            return True
        if node == None:
            return str(index)
        key = item[0]
        if node.item == key:
            key = item.pop(0)
            return Trie.search_one(node.last,item,index+1)
        else:
            return Trie.search_one(node.next,item,index)
    #Helper function for suggsearch
    def search_two(node,item):
        if item[0] == '$':
            return_list = []
            while node != None:
                if Trie.search_real(node.last,item[1:]):
                    return_list.append(node.item)
                node = node.next
            return return_list
        key = item[0]
        if key == node.item:
            key = item.pop(0)
            return Trie.search_two(node.last,item)
        else:
            return Trie.search_two(node.next,item)
