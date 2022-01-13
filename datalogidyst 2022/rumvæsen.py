from audioop import reverse
from collections import namedtuple
import itertools

def main():
    cyclesList = findCycles()

    for i in range(len(cyclesList)):
        for j in range(len(cyclesList)):
            if len(cyclesList[i]) % len(cyclesList[j]) == 0:
                 cyclesList.remove(cyclesList[j])
    
    for i in range(len(qList)):
        name[qList[i]] = cList[i]
        result = 0

        cycleLenghts = []
        for cycle in cyclesList:
            cycleLenghts.append(getUniqueStrings(cycle))

        result = 1
        for i in range(len(cycleLenghts)):
            result *= cycleLenghts[i]
    
        print(result)

def getUniqueStrings(cycle):
    cycleKeys = list(cycle.keys())
    firstLetter = cycleKeys[0]

    for index in cycleKeys:
        if name[index] != firstLetter:
            return len(cycle)
    
    return 1

def findCycles():
    cyclesListTemp = []
    currentCycle = dict()
    currentIndex = -1

    while len(name_P_dict) > 0:
        currentCycle = dict()
        currentIndex = list(name_P_dict.keys())[0]
        startIndex = currentIndex

        while True:
            currentCycle[currentIndex + 1] = P[currentIndex] + 1
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
