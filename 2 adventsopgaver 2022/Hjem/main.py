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

# convert the graph to an adjacency matrix
g = graphs.adjacency_matrix(graphs.Graph(nodes,edges,True))

graphs.matrixPrint(g)

visited = []


def dijkstra(start_vertex):
        D = {v:float('inf') for v in range(len(nodes))}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            visited.append(current_vertex)

            for neighbor in range(len(nodes)):
                if edges[current_vertex][neighbor] != -1:
                    distance = edges[current_vertex][neighbor]
                    if neighbor not in visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return 
    
print(D = dijkstra(0))

# for vertex in range(len(D)):
#     print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])

        
    
