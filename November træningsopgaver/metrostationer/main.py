from ticktock import tick

# Seperate n and q
lst1 = input()
lst1 = lst1.split(" ")
n = int(lst1[0])
q = int(lst1[1])

# Store the stations in a list and format them
# stations = input().split(" ")
# stations = list(filter(None, stations))
# stations = list(map(int, stations))
    
# Debug
# print()
# print("n: " + str(n))
# print("q: " + str(q))
# print("stations: ")
# print(stations)
# print()

# Format requests
requests = []

stations = []
import random
i = 0
while i < n:
    stations.append(random.randint(1,10**9))
    i += 1

i = 0
while i < q:
    requests.append([random.randint(1, n), random.randint(1, n)])
    i += 1

# i = 0
# while i < q:
#     requests.append(list(input().split(" ")))
#     i += 1

# i = 0
# while i < q:
#     requests[i] = list(map(int, list(filter(None, requests[i]))))
#     i += 1

def main():
    clock = tick()
    for pair in requests:
        # print()
        # print("current pair: ")
        # print(pair)
        # print()
        getDistance(pair[0], pair[1])
    clock.tock()
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
    


def getDistance(a, b):
    
    forwardLoopFinished = False
    backwardLoopFinished = False

    forwardDistance = 0
    backwardDistance = 0

    smallestDistance = 0

    i = a - 1
    j = a - 1

    count = 0

    while not(forwardLoopFinished and backwardLoopFinished):
        # Loop for the forward distance

        # If this loop finishes for the first time
        if((i == b - 1) and not(forwardLoopFinished)):
            forwardLoopFinished = True

            # If the other loop hasn't finished, then the smallest value is the current value
            if(not(backwardLoopFinished)):
                smallestDistance = forwardDistance

            # If it has, then check to see which is smaller and exit the loop
            elif(forwardDistance <= smallestDistance):
                smallestDistance = forwardDistance
                break
    
        # Stop the loop if the other loop is finished and has found a smaller value
        if(backwardLoopFinished):
            if(forwardDistance >= smallestDistance):
                forwardLoopFinished = True

        if(i + 1 > n - 1):
            forwardDistance += stations[n - 1]
            i = 0

        else:
            forwardDistance += stations[i]
            i += 1

        # Loop for the backward distance

        if((j == b - 1) and not(backwardLoopFinished)):
            backwardLoopFinished = True

            if(not(forwardLoopFinished)):
                smallestDistance = backwardDistance

            elif(backwardDistance <= smallestDistance):
                smallestDistance = backwardDistance
                break
            
        # Stop the loop if the other loop is finished and has found a smaller value
        if(forwardLoopFinished):
            if(backwardDistance >= smallestDistance):
                backwardLoopFinished = True

        if(j - 1 == (-1)):
            j = n - 1
            backwardDistance += stations[n - 1]
        
        else:
            j -= 1
            backwardDistance += stations[j]

        count += 1

        # print()
        # print("Current loop number: %s" % (str(count)))
        # print("i: %s" % (str(i)))
        # print("j: %s" % (str(j)))
        # print("forwardLoopFinished: %s" % (str(forwardLoopFinished)))
        # print("backwardLoopFinished: %s" % (str(backwardLoopFinished)))
        # print("forwardDistance: %s" % (str(forwardDistance)))
        # print("backwardDistance: %s" % (str(backwardDistance)))
        # print("smallestDistance: %s" % (str(smallestDistance)))

    # print("-------------------------")
    # print("Pair: [%s, %s]" % (str(a), str(b)))
    # print("Number of loops: %s" % (str(count)))
    # print("i: %s" % (str(i)))
    # print("j: %s" % (str(j)))
    # print("smallestDistance: %s" % (str(smallestDistance)))
    
    
    print(smallestDistance)


main()
