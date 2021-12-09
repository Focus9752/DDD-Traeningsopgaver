from collections import namedtuple
from os import close
import statistics

Graph = namedtuple("Graph", ["nodes", "edges","is_directed"])

def adjacency_dict(graph):
    adj = {node: {} for node in graph.nodes}
    for edge in graph.edges:
        node1, node2, weigth = edge[0], edge[1], edge[2]
        adj[node1][node2] = weigth
        if not graph.is_directed:
            adj[node2][node1] = weigth
    
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



n = int(input())
bus1list = list(map(int,(input().split())))
trains = list(map(int,(input().split())))
trains.append(0)
bus2list = list(map(int,(input().split()))) 

# define the nodes
# the 2nd last and last element are the start and stop locations respectively
nodes = [i for i in range(0,n * 3 + 2)]

# define the edges as a list of touples (n1, n2, weight)
# and add all edges
edges = []
for i in range(len(nodes)):
    # bus1list
    if i < n:
        edges.append((i, n + i, bus1list[i]))
        edges.append((3 * n, i, 0))

    # trains
    elif i < 2 * n:
        # fires if we are at the last train station in the list
        # we can't go to the next station so we only append the bus to the destination
        if i == 2 * n - 1:
            edges.append((i, n + i, bus2list[i - n]))

        else:
            edges.append((i, i + 1, trains[i - n]))
            edges.append((i, n + i, bus2list[i - n]))

    # bus2list
    elif i < 3 * n:
        edges.append((i, 3 * n + 1, 0))

# converts the graph to an adjacency matrix
g_mat = adjacency_matrix(Graph(nodes,edges,False))

# converts the graph to an adjacency dictionary
g_dict = adjacency_dict(Graph(nodes,edges,False))

#graphs.matrixPrint(g_mat)

distances = g_dict

def dijkstra(nodes, edges, source, destination, is_directed=False):
    # initialize pathlength as a dict with a path length for each node
    # at the start all path lengths are inf
    pathlengths = {n: float("inf") for n in nodes}
    # we set the path length of the source node to 0
    pathlengths[source] = 0

    # # we initialize a nested dictionary to store the adjacent nodes for each node
    # adjacent_nodes = {n: {} for n in nodes}
    # # we add adjacent nodes to the dictionary
    # for (u, v), w_uw in edges.items():
    #     adjacent_nodes[u][v] = w_uw
    #     adjacent_nodes[v][u] = w_uw

    adjacent_nodes = adjacency_dict(Graph(nodes,edges,is_directed))

    # this list will contain nodes that we have yet to check
    # the program is done once the list is empty
    temporary_nodes = [n for n in nodes]
    while len(temporary_nodes) > 0:
        # we find the path length to each node in the list of remaining nodes
        upper_bounds = {n: pathlengths[n] for n in temporary_nodes}
        # and find the node with the smallest path length
        u = min(upper_bounds, key=upper_bounds.get)

        # we remove the smallest node (the node that we are considering)
        # from the list of temporary nodes that we have yet to check
        temporary_nodes.remove(u)

        # we look at all the adjacent nodes for u and update their path lengths
        for n, weigth in adjacent_nodes[u].items():
            pathlengths[n] = min(pathlengths[n], pathlengths[u] + weigth)
        
        if u == destination:
            return pathlengths[u]
    
    return pathlengths

dist_to_goal = dijkstra(nodes, edges, nodes[n * 3], nodes[n * 3 + 1], True)

print(dist_to_goal)

