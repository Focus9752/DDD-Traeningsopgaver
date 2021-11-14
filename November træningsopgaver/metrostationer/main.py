
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
        # print()
        # print("current pair: ")
        # print(pair)
        # print()
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
    smallestDistance = 10000

    iFinished = False
    jFinished = False
    kFinished = False
    lFinished = False

    anyLoopFinished = False

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

    while not(iFinished and kFinished):

        # If any of the other loops are finished
        if(anyLoopFinished):
            # Check if what they found is smaller than the current value
            if(forwardDistanceTemp >= smallestDistance):
                # Stop searching if it is
                iFinished = True

        # if(anyLoopFinished):
        #     if(invForwardDistanceTemp >= smallestDistance):
        #         jFinished = True

        if(anyLoopFinished):
            if(backwardDistanceTemp >= smallestDistance):
                kFinished = True

        # if(anyLoopFinished):
        #     if(invBackwardDistanceTemp >= smallestDistance):
        #         lFinished = True

        if(iFinished and kFinished):
            break

        # Forward distance loop

        # If the loop has finished (for the first time)
        if((i == b - 1) and iFinished == False):
            iFinished = True
            anyLoopFinished = True
            # Check against smallest distance
            if(forwardDistanceTemp <= smallestDistance):
                smallestDistance = forwardDistanceTemp

        if(i >= len(stations) - 1):
            forwardDistanceTemp += stations[n - 1]
            i = 0

        else:
            forwardDistanceTemp += stations[i]
            i += 1
            
        # Inverse forward distance loop

        # if((j == a - 1) and jFinished == False):
        #     jFinished = True
        #     anyLoopFinished = True

        #     if(invForwardDistanceTemp <= smallestDistance):
        #         smallestDistance = invForwardDistanceTemp

        # if(j >= len(stations) - 1):
        #     invForwardDistanceTemp += stations[n - 1]
        #     j = 0

        # else:
        #     invForwardDistanceTemp += stations[j]
        #     j += 1

        # Backward distance loop

        if((k == b - 1) and kFinished == False):
            kFinished = True
            anyLoopFinished = True

            if(backwardDistanceTemp <= smallestDistance):
                smallestDistance = backwardDistanceTemp
            
        if(k <= 0):
            backwardDistanceTemp += stations[n - 1]
            k = n - 1

        else:
            backwardDistanceTemp += stations[k - 1]
            k -= 1

        # Inverse backward distance loop

        # if((l == a - 1) and lFinished == False):
        #     lFinished = True
        #     anyLoopFinished = True

        #     if(invBackwardDistanceTemp <= smallestDistance):
        #         smallestDistance = invBackwardDistanceTemp

        # if(l < 0):
        #     invBackwardDistanceTemp += stations[n - 1]
        #     l = n - 1

        # else:
        #     invBackwardDistanceTemp += stations[l - 1]
        #     l -= 1
        
        # print("invForwardDistanceTemp: %s" % (str(invForwardDistanceTemp)))
        
        
        
        # print()
        # smallestDistance = min([forwardDistance, invForwardDistance, backwardDistance, invBackwardDistance])

        # print("forwardDistanceTemp: %s" % (str(forwardDistanceTemp)))
        # # print("smallestDistance: %s" % (str(smallestDistance)))
        # print("backwardDistanceTemp: %s" % (str(backwardDistanceTemp)))
        # print("k: %s" % (str(k)))
        # # print("invBackwardDistanceTemp: %s" % (str(invBackwardDistanceTemp)))
        # print("smallestDistance: " + str(smallestDistance))
        # print("anyLoopFinished: "+ str(anyLoopFinished))
        # print()
    
    print(int(smallestDistance))
    # print()

main()

