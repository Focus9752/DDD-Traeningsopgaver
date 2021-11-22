import random
from ticktock import tick
import time

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

totalPairs = len(requests)
totalHeuristics = 0

print("Please enter an acceptance value for the heuristic function (0 - 100).")
userAcceptanceVal = (int(input("Acceptance value: ")) / 100)
print()

def main():
    heuristicDistances = []
    slowDistances = []

    print("Calculating the distances using the fast method...")

    t0 = time.time()
    for pair in requests:
        heuristicDistances.append(int(getDistance(pair[0], pair[1])))
    t1 = time.time()

    print("Calculating the distances took approximately {} s".format(str(round(t1 - t0,3))))
    print()

    print("- - - - - - - - - - - - -")
    print("Please wait, checking for errors...")

    t0 = time.time()
    for pair in requests:
        slowDistances.append(int(getDistanceSlow(pair[0], pair[1])))
    t1 = time.time()
    print("Checking for errors using the slow method took approximately {} s".format(str(round(t1 - t0,3))))
    print()

    print("- - - - - - - - - - - - -")
    print("Used heuristic in {} out of {} cases ({} %)".format(str(totalHeuristics), str(totalPairs), str(((totalHeuristics / totalPairs) * 100))))
    

    errorsFound = getErrors(heuristicDistances, slowDistances)

    print("The heuristic method made {} erros in of {} attempts.".format(errorsFound, len(stations)))
    print("The error percentage was {}".format(str((errorsFound / len(stations) * 100))) + "%" + " compared to the slower method.")

    

    

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
    
def heuristic(a,b):
    return (abs(a - b)) / len(stations)

def getDistance(a, b):
    
    forwardLoopFinished = False
    backwardLoopFinished = False

    forwardDistance = 0
    backwardDistance = 0

    smallestDistance = 0

    # Cache the heuristic
    heuristicVal = heuristic(a, b)

    # Heuristic acceptance value
    acceptanceVal = userAcceptanceVal
    # if(len(stations) <= 1000):
    #     acceptanceVal = 0.005
    # elif(len(stations) <= 10000):
    #     acceptanceVal = 0.10
    # else:
    #     acceptanceVal = 0.20

    i = a - 1
    j = a - 1

    count = 0

    # If the target station is ahead of the start station, we check if the value of the
    # heuristic is below some level (5% for example)
    if(a <= b and (heuristicVal <= acceptanceVal or heuristicVal >= (1 - acceptanceVal))):
        # We only do the forward loop.
        while True:
            # Condition to end the loop
            if(i == b - 1):
                smallestDistance = forwardDistance
                global totalHeuristics
                totalHeuristics += 1
                break
            
            if(i + 1 > n - 1):
                forwardDistance += stations[n - 1]
                i = 0

            else:
                forwardDistance += stations[i]
                i += 1

    elif((a >= b) and (heuristicVal <= acceptanceVal or heuristicVal >= (1 - acceptanceVal))):
        # We only do the backward loop
        while True:
            if(j == b - 1):
                smallestDistance = backwardDistance
                # global totalHeuristics
                totalHeuristics += 1
                break

            if(j - 1 == (-1)):
                j = n - 1
                backwardDistance += stations[n - 1]
        
            else:
                j -= 1
                backwardDistance += stations[j]
        

    else:
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
    
    
    # print(smallestDistance)
    return smallestDistance

# Gets distance without using heuristics
def getDistanceSlow(a, b):
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
    
    # print(smallestDistance)
    return smallestDistance
    
def getErrors(fastDist, slowDist):
    errors = 0
    for index in range(len(fastDist)):
        if(fastDist[index] != slowDist[index]):
            errors += 1
    
    return errors

        

main()