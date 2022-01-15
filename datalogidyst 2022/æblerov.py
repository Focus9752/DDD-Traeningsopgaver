def main():
    currentGarden = ""
    currentHeight = initialHeight
    switches = 0
    path = []
    
    gardenA = gardenAGlobal
    gardenB = gardenBGlobal

    while len(gardenA) > 0 or len(gardenB) > 0:
        highestPossibleA = getHighestPossibleHeight(gardenA, currentHeight)
        highestPossibleB = getHighestPossibleHeight(gardenB, currentHeight)

        if len(gardenA) > 0:
            smallestTreeA = gardenA[0][0]
        else:
            smallestTreeA = float("inf")

        if len(gardenB) > 0:
            smallestTreeB = gardenB[0][0]
        else:
            smallestTreeB = float("inf")

        if smallestTreeA > currentHeight and smallestTreeB > currentHeight:
            print(-1)
            return

        if currentGarden == "A" and smallestTreeA <= currentHeight and len(gardenA) > 0:
            currentHeight = highestPossibleA
            visitTemp = visit(gardenA, highestPossibleA)
            gardenA = visitTemp[0]
            subPath = visitTemp[1]
            for i in range(len(subPath)):
                path.append("spis " + str(subPath[i] + 1))
            continue
        elif currentGarden == "B" and smallestTreeB <= currentHeight and len(gardenB) > 0:
            currentHeight = highestPossibleB
            visitTemp = visit(gardenB, highestPossibleB)
            gardenB = visitTemp[0]
            subPath = visitTemp[1]
            for i in range(len(subPath)):
                path.append("spis " + str(subPath[i] + 1))
            continue

        if len(gardenA) != 0:
            if highestPossibleA > highestPossibleB:
                path.append("have A")
                if currentGarden == "A":
                    currentGarden = "A"
                else:
                    currentGarden = "A"
                    switches += 1

                currentHeight = highestPossibleA
                visitTemp = visit(gardenA, highestPossibleA)
                gardenA = visitTemp[0]
                subPath = visitTemp[1]
                for i in range(len(subPath)):
                    path.append("spis " + str(subPath[i] + 1))
                continue

        if len(gardenB) != 0:
            path.append("have B")
            if currentGarden == "B":
                currentGarden = "B"
            else:
                currentGarden = "B"
                switches += 1

            currentHeight = highestPossibleB  
            visitTemp = visit(gardenB, highestPossibleB)
            gardenB = visitTemp[0]
            subPath = visitTemp[1]
            for i in range(len(subPath)):
                path.append("spis " + str(subPath[i] + 1))
            continue

    print(switches)
    for action in path:
        print(action)


def visit(garden, heightLimit):
    pathTemp = []
    removeList = []

    for tree in garden:
        if tree[0] <= heightLimit:
            pathTemp.append(tree[2])
            removeList.append(tree)

    for i in range(len(removeList)):
        garden.remove(removeList[i])

    return [garden,pathTemp]


def getHighestPossibleHeight(garden, currentHeightTemp):
    gardenCopy = list(garden)

    if len(garden) == 0:
        return currentHeightTemp

    smallestTreeHeight = gardenCopy[0][0]
    while len(gardenCopy) > 0 and smallestTreeHeight <= currentHeightTemp:
        for tree in gardenCopy:
            if tree[0] <= currentHeightTemp:
                currentHeightTemp += tree[1]
                gardenCopy.remove(tree)
                if len(gardenCopy) > 0:
                    smallestTreeHeight = gardenCopy[0][0]
                break
    return currentHeightTemp

n,m,initialHeight = list(map(int, input().split()))

gardenAGlobal = []
for i in range(n):
    treeHeight,growthFactor = list(map(int, input().split()))
    gardenAGlobal.append([treeHeight,growthFactor,i])
gardenAGlobal.sort(key=lambda x: (x[0], -x[1]))

gardenBGlobal = []
for i in range(m):
    treeHeight,growthFactor = list(map(int, input().split()))
    gardenBGlobal.append([treeHeight,growthFactor,i])
gardenBGlobal.sort(key=lambda x: (x[0], -x[1]))


main()
