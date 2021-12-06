def main():
    n = int(input())
    bus1 = list(map(int,(input().split())))
    trains = list(map(int,(input().split())))
    bus2 = list(map(int,(input().split())))

    trains.append(0)

    distances = []

    for i in range(n):
        distances.append(bus1[i] + trains[i] + bus2[i])

    shortestDistance = distances[0]

    for i in range(len(distances)):
        if distances[i] <= shortestDistance:
            shortestDistance = distances[i]

    print(shortestDistance)
        
main()
