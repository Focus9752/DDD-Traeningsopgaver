
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

def main():
    for pair in requests:
        print()
        print("current pair: ")
        print(pair)
        print()
        distance(pair[0], pair[1])
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

def distance(a, b):

    smallestDistance = 10**1000000

    iFinished = False
    jFinished = False
    kFinished = False
    lFinished = False

    i = a - 1
    j = b - 1
    k = a - 1
    l = b - 1

    forwardDistance = 0
    invForwardDistance = 0
    backwardDistance = 0
    invBackwardDistance = 0

    forwardDistanceTemp = 0
    invForwardDistanceTemp = 0
    backwardDistanceTemp = 0
    invBackwardDistanceTemp = 0

    while not(iFinished and jFinished and kFinished and lFinished):


        # Forward distance
        if((i == b - 1) and iFinished == False):
            iFinished = True
            forwardDistance = forwardDistanceTemp

        if(i >= len(stations) - 1):
            forwardDistanceTemp += stations[n - 1]
            i = 0

        else:
            forwardDistanceTemp += stations[i]
            i += 1
            

        
        # Inverse forward distance
        if((j == a - 1) and jFinished == False):
            jFinished = True
            invForwardDistance = invForwardDistanceTemp

        if(j > len(stations) - 1):
            invForwardDistanceTemp += stations[n - 1]
            j = 0

        else:
            invForwardDistanceTemp += stations[j]
            j += 1

        # Backward distance
        if((k == b - 1) and kFinished == False):
            kFinished = True
            backwardDistance = backwardDistanceTemp
            
        if(k < 0):
            backwardDistanceTemp += stations[n - 1]
            k = n - 1

        else:
            backwardDistanceTemp += stations[k]
            k -= 1

        # Inverse backward distance
        if((l == a - 1) and lFinished == False):
            lFinished = True
            invBackwardDistance = invBackwardDistanceTemp

        if(l < 0):
            backwardDistanceTemp += stations[n - 1]
            l = n - 1

        else:
            backwardDistanceTemp += stations[l]
            l -= 1
    
    smallestDistance = min([forwardDistance, invForwardDistance, backwardDistance, invBackwardDistance])

    print("forwardDistance: "+ str(forwardDistance))
    print("invForwardDistance: "+ str(invForwardDistance))
    print("backwardDistance: " + str(backwardDistance))
    print("invBackwardDistance: " + str(invBackwardDistance))
    print("smallestDistance: " + str(smallestDistance))


main()

