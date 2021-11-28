import random
from ticktock import tick
import time

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

totalPairs = len(requests)
totalHeuristics = 0

def main():

    totalLength = None
    for i in range(len(stations)):
        totalLength += stations[i]
        
    
def getDistance(a,b):
    a -= 1
    b -= 1

    shortestDist = None
    
    while shortestDist < totalHeuristics / 2:

# slå op: python sum prefix!!!

main()