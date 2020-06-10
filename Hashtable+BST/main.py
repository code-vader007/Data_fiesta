from hashtable_bst import BST

data={'a':1,'b':2,'c':3,'d':4,'e':5}
Bst=BST()
for i in data.keys():
    print((hash(i),data[i]))
    Bst.insert(data[i],i)

Bst.printPost(Bst.root)
