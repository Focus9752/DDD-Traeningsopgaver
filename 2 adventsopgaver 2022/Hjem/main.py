# we store the edges in a matrix where the rows and collumns are nodes and the values are 
# the weights of the edges. For example:
#    0 1 2
#    ------
# 0 | 1 2 3
# 1 | 1 1 1
# 2 | 8 6 4

class Graph:
    def __init__(self, n):
        # number of nodes
        self.nodes = n * 3
        # edges and their values. initializes to -1
        self.edges = [[-1 for i in range(n * 3)] for j in range(n * 3)]
        # list of visited edges
        self.visited = []
    
    # adds an edge to the graph
    # parameters: the two nodes the edge connects, as well as the weight of the edge
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

def main():
    n = int(input())
    bus1 = list(map(int,(input().split())))
    trains = list(map(int,(input().split())))
    trains.append(0)
    bus2 = list(map(int,(input().split()))) 
    
    g = Graph(n)

    # Bus 1  -> edges 0 to n
    # Trains -> edges n to n
    # Bus 2  -> edges 2n to 3n
    i = 1
    while i <= n:
        # the lists we want to access are 0-indexed, but we need to be able to divide them properly
        # which is why we use two variables for the loop.
    
        # Bus 1
        g.add_edge(i - 1, i + n - 1, bus1[i - 1])
        g.add_edge(i - 1, i + 2 * n - 1, bus2[i - 1])
        if i != n:
            g.add_edge(i + n - 1, i + n - 1, trains[i])
        else:
            g.add_edge(i + n - 1, i + n - 1, trains[i - 1])

        i += 1

        # 4, 1, 7
        # 5, 2, 8
        # 6, 3, 9

        # 6, 1, 11
        # 7, 2, 12
        # 8, 3, 13
        # 9, 4, 14
        # 10, 5, 15

    print(g.edges)

main()


        
    
