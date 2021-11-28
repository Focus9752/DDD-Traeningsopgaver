# Input
lst1 = input()
lst1 = lst1.split(" ")
n = int(lst1[0])
q = int(lst1[1])

stations = input().split(" ")
stations = list(filter(None, stations))
stations = list(map(int, stations))

requests = []

i = 0
while i < q:
    requests.append(list(input().split(" ")))
    i += 1

i = 0
while i < q:
    requests[i] = list(map(int, list(filter(None, requests[i]))))
    i += 1

totalPairs = len(requests)


def main():
    sumList = [sum(stations[ : i + 1]) for i in range(len(stations))]
    totalLength = sumList[len(stations) - 1]

    for pair in requests:
        print(getDistance(pair[0] - 1, pair[1] - 1, sumList, totalLength))
         
def getDistance(a, b, sumList, totalLength):
    if(a < b):
        small = a
        big = b
    else:
        small = b
        big = a

    # Hvis vi ikke skal bevæge os
    if(small == big):
        return 0

    # Hvis begge stationer ligger i "enderne" af metroen
    if small == 0 and big == len(stations) - 1:
        forwardDistance = sumList[big - 1]

    # Hvis vi skal fremad
    if small == 0:
        forwardDistance = sumList[big - 1]
    
    # Hvis vi skal bagud
    if big == len(stations) - 1:
        forwardDistance = sumList[big - 1] - sumList[small - 1]

    backwardDistance = totalLength - forwardDistance

    if(backwardDistance > forwardDistance):
        return forwardDistance
    else:
        return backwardDistance

# 1 2 3 4 5
# 1 3 6 10 15
# 1 2
# 2 5
# 5 4
# 2 2

# 1
# 6
# 4
# 0

# 3 7 1 20
# 3 10 11 31
# 1 2
# 1 3
# 2 4

# 3
# 10
# 8

main()