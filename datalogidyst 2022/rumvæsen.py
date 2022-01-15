from functools import cache

def main():
    cyclesList = findCycles()

    for cycle1 in cyclesList:
        cycle1Length = len(cycle1)

        for cycle2 in cyclesList:
            cycle2Length = len(cycle2)
            
            if cycle2 != cycle1:
                if cycle1Length > cycle2Length:
                    if cycle1Length % cycle2Length == 0:
                        cyclesList.remove(cycle2)

                else:
                    if cycle2Length % cycle1Length == 0:
                        cyclesList.remove(cycle1)
    
    for i in range(len(qList)):
        name[qList[i]] = cList[i]
        result = 0

        cycleLenghts = []
        for cycle in cyclesList:
            cycleLenghts.append(getUniqueStrings(cycle))

        result = 1
        for i in range(len(cycleLenghts)):
            result *= cycleLenghts[i]
    
        print(result % 1000000007)

@cache
def getUniqueStrings(cycle):
    cycleKeys = list(cycle.keys())
    # firstLetter = name[cycleKeys[0]]

    # for index in cycleKeys:
    #     if name[index] != firstLetter:
    #         return len(cycle)
    
    # return 1

    changes = 0

    originalStringDict = dict()
    for key in cycleKeys:
        originalStringDict[key] = name[key]
    
    tempString1Dict = dict(originalStringDict)
    tempString2Dict = dict(originalStringDict)
    
    while not(tempString1Dict == originalStringDict and changes > 0):
        for key, value in cycle.items():
            tempString2Dict[value] = tempString1Dict[key]
        
        tempString1Dict = dict(tempString2Dict)
        changes += 1
    
    return changes

def findCycles():
    cyclesListTemp = []
    currentCycle = dict()
    currentIndex = -1

    while len(name_P_dict) > 0:
        currentCycle = dict()
        currentIndex = list(name_P_dict.keys())[0]
        startIndex = currentIndex

        while True:
            currentCycle[currentIndex] = P[currentIndex]
            del(name_P_dict[currentIndex])
            currentIndex = P[currentIndex]

            if currentIndex == startIndex:
                break

        cyclesListTemp.append(currentCycle)

    return cyclesListTemp
        
def calculateStarScore(S, P, score, original_S):
    S = list(S)
    T = S.copy()
    for i in range(N):
        S[P[i] - 1] = T[i]
    
    score += 1

    S = ''.join(str(elem) for elem in S)

    if S == original_S:
        return score
    else:
        return calculateStarScore(S, P, score, original_S)

def changeName(S, q, c):
    S = list(S)
    S[q - 1] = c

    S = ''.join(str(elem) for elem in S)

    return S

N, Q = list(map(int, input().split()))
name = list(input())
P = list(map(int, input().split()))
P = [num - 1 for num in P]

name_P_dict = dict()

for i in range(len(name)):
    name_P_dict[i] = P[i]

{0: 2,
1: 3}

qList = []
cList = []

for i in range(Q):
    inputList = input().split()
    qList.append(int(inputList[0]) - 1)
    cList.append(str(inputList[1]))

main()
