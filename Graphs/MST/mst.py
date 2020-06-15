import numpy as np
def Kruskal(n):
    # Generate a random undirected graph
    # The range of weight is [1, 20]
    mat = np.random.randint(1, 21, (n, n))
    edge_lst = [] # Each edge is stored in the form of (cost, vertex1, vertex2), where vertex1 < vertex2
    # Set the cost matrix symmetric about the diagonal
    for i in range(n):
        for j in range(n):
            if i == j:
                mat[i, j] = 0
            elif i > j:
                mat[i, j] = mat[j, i]
            else:
                edge_lst.append((mat[i, j], i, j))
    print("Cost Matrix:\n", mat)

    # Sort the edge list
    edge_lst = sorted(edge_lst,key=lambda x:x[0])
    edge_lst.reverse()
    print("Edge List:\n", edge_lst)

    # We use index from 0 to n - 1
    CC_lst = [[i] for i in range(n)]
    MST_edges = []
    while len(CC_lst) > 1:
        curr_edge = edge_lst.pop(0)
        for CC in CC_lst:
            if curr_edge[1] in CC:
                CC_1 = CC.copy()

            if curr_edge[2] in CC:
                CC_2= CC
            print(CC_1,CC)
        # Merge two connected component
        if CC_1 == CC_2:
            continue
        CC_lst.remove(CC_1)
        CC_lst.remove(CC_2)
        CC_1.extend(CC_2)
        CC_lst.append(CC_1)
        MST_edges.append((curr_edge[1], curr_edge[2]))

    # Output the result
    print("MST:\n", MST_edges)
