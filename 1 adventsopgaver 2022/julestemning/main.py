def getTrees(child):
    stepsize = child[0]
    startingLocation = child[1] - 1

    visitedTrees = []
    largestTree = 0

    # Vi looper igennem listen af træer
    i = startingLocation - 1
    while True:
        # Hvis vi er nået forbi slutningen af listen skal vi tilbage til starten
        if i > len(trees):
            i = abs(i - (len(trees) - 1))
        
        # Gem det nuværende træ i cache
        currentTree = trees[i]

        if currentTree in visitedTrees:
            if currentTree > largestTree:
                largestTree = currentTree
                break
            else:
                break

        elif currentTree > largestTree:
            largestTree = currentTree

        visitedTrees.append(currentTree)
        i += stepsize
        

    return largestTree
        
n,q = list(map(int, input().split()))

trees = list(map(int, input().split()))

children = []

for i in range(q):
    children.append(list(map(int, input().split())))

for child in children:
    print(getTrees(child))
