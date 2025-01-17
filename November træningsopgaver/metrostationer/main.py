import random
import time
from colorama import init
from colorama import Fore
from colorama import Style
from alive_progress import alive_bar

init(convert=True)

print("Please enter n and q: ")

# Seperate n and q
lst1 = input()
lst1 = lst1.split(" ")
n = int(lst1[0])
q = int(lst1[1])

time0 = time.time()
print("Please wait, generating test cases...")
print()

# Format requests
requests = []

stations = []

print("Generating station list...")
with alive_bar(n) as bar:
    for i in range(n):
        stations.append(random.randint(1,10**9))
        bar()

print("Generating request list...")
with alive_bar(q) as bar:
    for i in range(q):
        requests.append([random.randint(1, n), random.randint(1, n)])
        bar()

# i = 0
# while i < q:
#     requests.append(list(input().split(" ")))
#     i += 1

# i = 0
# while i < q:
#     requests[i] = list(map(int, list(filter(None, requests[i]))))
#     i += 1

totalPairs = len(requests)

time1 = time.time()
print(Fore.YELLOW)
print("Generating test cases took approximately {} s".format(str(round(time1 - time0,1))))
print(Style.RESET_ALL)

def main():
    fastDistances = []
    slowDistances = []

    usedHeuristic = False
    heuristicCounter = 0

    t0 = None
    t1 = None

    fastTime = 0
    slowTime = 0

    if input("Choose which method to use ('prefixsum' / 'heuristic'): ").lower() == "prefixsum":
        print("Calculating the distances using the prefix sum method...")
        print("Generating prefix sum list...")
        t0 = time.time()
        # sumList = [sum(stations[ : i + 1]) for i in range(len(stations))]
        sumList = getSumlist(stations)
        totalLength = sumList[len(stations) - 1]
        tprefixsum = time.time()
        print("Calculating distances...")
        with alive_bar(q) as bar:
            for pair in requests:
                fastDistances.append(int(getDistanceFast(pair[0], pair[1], sumList, totalLength)))
                bar()
        t1 = time.time()
        fastTime = round(t1 - t0,3)
    else:
        acceptanceVal = float(input("Please enter an acceptance value (0.00 - 1.00): "))
        print()
        print("Calculating the distances using the heuristic method...")
        t0 = time.time()
        with alive_bar(q) as bar:
            for pair in requests:
                # Stores answer and wether or not heuristic was used
                tempHeuristicList = getHeuristicDistance(pair[0], pair[1], acceptanceVal)
                fastDistances.append((tempHeuristicList[0]))
                if(tempHeuristicList[1] == True):
                    heuristicCounter += 1
                bar()
        t1 = time.time()
        fastTime = round(t1 - t0,3)
        usedHeuristic = True
    

    print("Success!")
    print(Fore.YELLOW)
    if(usedHeuristic == False):
        print("Generating the prefix sum list took {} s".format(str(round(tprefixsum - t0,1))))
        print("Calculating the distances took approximately {} s".format(str(round(t1 - tprefixsum,1))))
    else:
        print("Calculating the distances took approximately {} s".format(str(round(t1 - tprefixsum,1))))
    print(Style.RESET_ALL)

    if(input("Check for errors? (y/n): ").lower() != "y"):
        return
    print()

    print("Please wait, checking for errors...")
    
    t0 = time.time()
    with alive_bar(q) as bar:
        for pair in requests:
            slowDistances.append(int(getDistanceSlow(pair[0], pair[1])))
            bar()
    t1 = time.time()
    slowTime = round(t1 - t0,3)
    print("Success!")

    print(Fore.YELLOW)
    timeDiff = round((abs(slowTime - fastTime)),1)
    print("Checking for errors using the slow method took approximately {} s".format(str(slowTime)))
    print("The time difference between the two methods was approximately {} s".format(str(timeDiff)))
    print(Style.RESET_ALL)

    errorsFound = getErrors(fastDistances, slowDistances)

    if(usedHeuristic):
        print("Used heuristic in {} out of {} cases ({} %)".format(str(heuristicCounter), str(totalPairs), str(round((heuristicCounter / totalPairs) * 100,1))))

    print("The fast method made {} erros in {} attempts.".format(errorsFound, len(requests)))
    print("The error percentage was {}".format(str(round((errorsFound / len(requests) * 100),1))) + "%" + " compared to the slower method.")
    print()

    if input("Print and compare results? (y/n): ").lower() == "y":
        for i in range(len(slowDistances) - 1):
            if fastDistances[i] == slowDistances[i]:
                print(Fore.GREEN)
                print("Output:   " + str(fastDistances[i]))
                print("Expected: " + str(slowDistances[i]))
                print()
            else:
                print(Fore.RED)
                print("Output:   " + str(fastDistances[i]))
                print("Expected: " + str(slowDistances[i]))
    

# Gets distance using a slower method
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


def heuristic(a,b):
    return (abs(a - b)) / len(stations)

# Gets distance using heuristics
def getHeuristicDistance(a, b, acceptanceVal):
    
    forwardLoopFinished = False
    backwardLoopFinished = False
    forwardDistance = 0
    backwardDistance = 0
    smallestDistance = 0

    usedHeuristic = False

    # Cache the heuristic
    heuristicVal = heuristic(a, b)

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
                usedHeuristic = True
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
                usedHeuristic = True
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
        
    return [smallestDistance, usedHeuristic]
         
def getDistanceFast(a, b, sumList, totalLength):
    small = None
    big = None

    if(a < b):
        small = a - 1
        big = b - 1
    else:
        small = b - 1
        big = a - 1

    # Hvis vi ikke skal bevæge os
    if(small == big):
        return 0

    # Hvis begge stationer ligger i "enderne" af metroen
    elif small == 0 and big == len(stations) - 1:
        forwardDist = sumList[big - 1]

    # Hvis vi skal fremad
    elif small == 0:
        forwardDist = sumList[big - 1]
    
    # Hvis vi skal bagud
    elif big == len(stations) - 1:
        forwardDist = sumList[big - 1] - sumList[small - 1]
    
    else:
        forwardDist = sumList[big - 1] - sumList[small - 1]

    backDist = totalLength - forwardDist

    if(backDist > forwardDist):
        return forwardDist
    else:
        return backDist

# Gets the prefix sum list
def getSumlist(stations):
    tempSumlist = [0] * len(stations)
    with alive_bar(len(stations)) as bar:
        for index in range(len(stations)):
            if index == 0:
                tempSumlist[index] = stations[index]
            else:
                tempSumlist[index] = stations[index] + tempSumlist[index - 1]
            bar()
    return tempSumlist

# Calculates errors using a slow method
def getErrors(fastDist, slowDist):
    errors = 0
    for index in range(len(fastDist)):
        if(fastDist[index] != slowDist[index]):
            errors += 1
    return errors

main()


