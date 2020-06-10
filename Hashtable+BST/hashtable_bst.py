class BST:
    class __Node:
        def __init__(self,val,key,left=None,right=None):
            self.key=key
            self.val = val
            self.left = left
            self.right = right
            self.parent=None
        def getVal(self):
            return self.val
        def setVal(self,newval):
            self.val = newval
        def getLeft(self):
            return self.left
        def setLeft(self,newleft):
            self.left = newleft
        def getRight(self):
            return self.right
        def setRight(self,newright):
            self.right = newright
        def setKey(self,newkey):
            self.key=newkey
        def getKey(self):
            return self.key
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
            yield self.val
            if self.right != None:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None
    def insert(self,val,key):
        ind=hash(key)
        def __insert(root,val,ind):
            if root == None:
                return BST.__Node(val,ind)
            if ind < root.getKey():
                root.setLeft(__insert(root.getLeft(),val,ind))
            else:
                root.setRight(__insert(root.getRight(),val,ind))
            return root
        self.root = __insert(self.root,val,ind)
    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()
    def find(self,key):
        def __find(root,key):

            if root == None:
                return False
            if key == root.getKey():
                return True
            if key < root.getKey():
                return __find(root.getLeft(),key)
            else:
                return __find(root.getRight(),key)
        return __find(self.root,key)

    def delete(self,key):
        def __merge(leftnode,rightnode):
            if rightnode == None:
                return leftnode
            if rightnode.getLeft() == None:
                rightnode.setLeft(leftnode)
                return rightnode
            __merge(leftnode,rightnode.getLeft())
            return rightnode
        def __delete(root,key):
            if root == None:
                return root
            if key == root.getKey():
                return __merge(root.getLeft(),root.getRight())
            if key < root.getKey():
                root.setLeft(__delete(root.getLeft(),key))
                return root
            root.setRight(__delete(root.getRight(),key))
            return root
        __delete(self.root,key)
    ## Add a function to print out the tree intuitionistically
    def print_BST(self):
        ret = self.print_tree(self.root, 0, 0,{})
        ret = sorted(ret.items(), key=lambda x: x[1])
        cur_x = 0
        cur_y = 0
        for item in ret:
            x = item[1][1]
            y = item[1][0]
            parent = item[1][2]
            for i in range(cur_y, y):
                print('\n')
                cur_x = 0
            for i in range(cur_x, x):
                print(' ', end='')
            print(item[0], end='')
            print('('+str(parent)+')',end = '')
            cur_x = x+1
            cur_y = y
        print('\n')

    # helper function
    def print_tree(self, root, x, y, ret):
        # none do nothing and return
        if(root == None):
            return ret
        if(root.left == None and root.right == None): # leaf node
            ret[str(root.key)] = (y, x, root.parent.key)
            return ret
        # otherwise, the left or right node is not None
        if(x-8 < 0):
            x = 8
        if(root.left != None):
            root.left.parent = root
            ret = self.print_tree(root.left, x-8, y+1, ret)
            leftChild = str(root.left.key)
            if(root == self.root):
                x = ret[leftChild][1]+16 # to distinct left and right tree
            else:
                x = ret[leftChild][1]+8
        if(root.parent == None):
            ret[str(root.key)] = (y, x, None)
        else:
            ret[str(root.key)] = (y, x, root.parent.key)
        if(root.right != None):
            root.right.parent = root
            if(root == self.root):
                ret = self.print_tree(root.right, x+16, y+1, ret) # to distinct left and right tree
            else:
                ret = self.print_tree(root.right, x+8, y+1, ret)
        return ret

    def printPost(self,root):
        if root:
            self.printPost(root.left)
            print((root.key,root.val))
            self.printPost(root.right)
