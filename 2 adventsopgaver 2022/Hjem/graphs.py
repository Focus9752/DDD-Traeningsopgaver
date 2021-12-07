from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges","is_directed"])

g = Graph([0,1,2,3,4,5,6,7,8],[
    (0,3,1),
    (1,4,2),
    (2,5,3),

    (3,4,1),
    (4,5,1),

    (6,3,8),
    (7,4,6),
    (8,5,4)

],True)

def adjacency_dict(graph):
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    
    return adj

def adjacency_matrix(graph):
    adj = [[-1 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1, node2, weigth = edge[0], edge[1], edge[2]
        adj[node1][node2] = weigth
        if not graph.is_directed:
            adj[node2][node1] = weigth
    
    return adj

def matrixPrint(mat):
    print(" ", " ".join([str(x) for x in range(len(mat))]))
    for i, x in enumerate(mat):
        print (i, " ".join([str(y) for y in x]))  # or  if elements are not string



