def main():
    # Seperate n and q
    lst1 = input()
    lst1 = lst1.split(" ")
    n = int(lst1[0])
    q = int(lst1[1])

    # Store the stations in a list and format them
    stations = input().split(" ")
    stations = list(filter(None, stations))
    stations = list(map(int, stations))
        
    # Debug
    # print()
    # print("n: " + str(n))
    # print("q: " + str(q))
    # print("stations: ")
    # print(stations)
    # print()

    # Format requests
    requests = []

    i = 0
    while i < q:
        requests.append(list(input().split(" ")))
        i += 1
    
    i = 0
    while i < q:
        requests[i] = list(map(int, list(filter(None, requests[i]))))
        i += 1

    
    # Debug
    # print()
    # print("n: " + str(n))
    # print("q: " + str(q))
    # print("stations: ")
    # print(stations)
    # print()

    # print("requests: ")
    # print(requests)
    # print()

    for pair in requests:
        processRequest(pair, stations, n, q)
    

def processRequest(stationPair, stations, n, q):
    
    a = stationPair[0]
    b = stationPair[1]

    # Find the distance when traveling forwards from station a to station b
    i = a - 1
    forwardDistance = 0

    while True:
        if(i == b - 1):
            break
        if(i > len(stations) - 1):
            i = 0
        forwardDistance += stations[i]
        i += 1

    # Do the same when traveling backwards

    i = a - 1
    backwardDistance = 0

    while True:
        if(i < 0):
            i = n - 1
        if(i == b - 1):
            break
        backwardDistance += stations[i - 1]
        i -= 1

    # Debug
    # print("Requested pair: ")
    # print(stationPair)
    # print()

    # print("forwardDistance: " + str(forwardDistance))
    # print("backwardDistance: " + str(backwardDistance))
    # print()
    
    # if(forwardDistance > backwardDistance):
    #     print("Final distance between station '%s' and station '%s' is: %s" % (str(stationPair[0]), str(stationPair[1]), str(backwardDistance)))
    # else:
    #     print("Final distance between station '%s' and station '%s' is: %s" % (str(stationPair[0]), str(stationPair[1]), str(forwardDistance)))

    # Print the result

    if(forwardDistance > backwardDistance):
        print(backwardDistance)
    else:
        print(forwardDistance)
    












    
    

    
    


main()


