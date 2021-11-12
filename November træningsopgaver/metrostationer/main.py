def main():
    # Skil n og q ad
    lst1 = input()
    lst1 = lst1.split(" ")
    n = int(lst1[0])
    q = int(lst1[1])

    # Lav en list med stationerne og sørg for at objekterne i listen er heltal
    global stations
    stations = input().split(" ")
    stations = list(filter(None, stations))
    stations = list(map(int, stations))
        
    # Til debug
    print()
    print("n: " + str(n))
    print("q: " + str(q))
    print("stations: ")
    print(stations)
    print()

    # Formatér forspørgslerne
    requests = []

    i = 0
    while i < q:
        requests.append(list(input().split(" ")))
        i += 1
    
    i = 0
    while i < q:
        requests[i] = list(map(int, list(filter(None, requests[i]))))
        i += 1

    
    # Til debug
    print()
    print("n: " + str(n))
    print("q: " + str(q))
    print("stations: ")
    print(stations)
    print()

    print("requests: ")
    print(requests)
    print()
    isForwardQuickest(1)

def processRequest(stationPair):
    1

def isForwardQuickest(stationPair):
    halfwaypoint = round(n / 2)
    print(halfwaypoint)
    


main()


