# we store the edges in a matrix where the rows and collumns are nodes and the values are 
# the weights of the edges. For example:
#    0 1 2
#    ------
# 0 | 1 2 3
# 1 | 1 1 1
# 2 | 8 6 4

import graphs
from queue import PriorityQueue


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

    # trains
    elif i < 2 * n:
        # fires if we are at the last train station in the list
        # we can't go to the next station
        if i == 2 * n - 1:
            pass

        else:
            edges.append((i, i + 1, trains[i - n]))

    # bus2list
    elif i < 3 * n:
        edges.append((i, i - n, bus2list[i - 2 * n]))
    
    # add the start and end nodes
    else:
        for j in range(n):
            edges.append((n * 3, j, bus1list[j]))
            edges.append((n * 3 + 1, j + 2 * n, bus2list[j]))

# converts the graph to an adjacency matrix
g_mat = graphs.adjacency_matrix(graphs.Graph(nodes,edges,True))

# converts the graph to an adjacency dictionary
g_dict = graphs.adjacency_dict(graphs.Graph(nodes,edges,True))

#graphs.matrixPrint(g_mat)
print(g_dict)

distances = g_dict

unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = 0
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)


# for vertex in range(len(D)):
#     print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])



