import random
import time
from colorama import init
from colorama import Fore
from colorama import Style

print("Indtast n og k, adskildt af mellemrum: ")

n,k = list(map(int, input().split()))

print()

inputNumbers = []
requests = []

print("Generér testdata (0) eller indtast data manuelt (1)?")
if input() == "0":
    print()
    print("Indtast en maksværdi for de tilfældigt genererede tal til testdata: ")
    randomnessRange = int(input())
    print()

    for i in range(n):
        inputNumbers.append([i,i])

    # random values for x and y
    xvalues = random.sample(range(1, randomnessRange), n)
    yvalues = random.sample(range(1, randomnessRange), n)

    # place random values in inputnumbers array
    i = 0
    for list in inputNumbers:
        list[0] = xvalues[i]
        list[1] = yvalues[i]
        i += 1

    for i in range(k):
        requests = random.sample(range(1, randomnessRange), k)
else:
    print()
    for i in range(n):
        temp_list = list(map(int, input().split()))
        inputNumbers.append((temp_list[0], temp_list[1]))

    for i in range(k):
        requests.append(int(input()))


# the numbers from the input
# [50, 55, 60]
numbers = [inputNumbers[i][1] for i in range(len(inputNumbers))]


print(inputNumbers)
print()
print(requests)

