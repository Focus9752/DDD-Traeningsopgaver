def main():
    N = int(input())
    runnerIntervals = []
    overlapsList = [[] for _ in range(N)]

    for i in range(N):
        runnerIntervals.append(list(input().split(" ")))

    for i in range(N):
        runnerIntervals[i] = list(map(int, list(filter(None, runnerIntervals[i]))))

    runnerIntervals.sort()

    print(runnerIntervals, overlapsList)



    for i in range(N):
        firstInterval = runnerIntervals[i]
        for j in range(N):
            if overlaps(firstInterval, runnerIntervals[j]) and j != i:
                overlapsList[i].append(j)

    print(runnerIntervals, overlapsList)

def overlaps(a,b):
    return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]

main()