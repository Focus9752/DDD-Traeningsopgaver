import random
import time
from colorama import init
from colorama import Fore
from colorama import Style

init(convert=True)

print("Indtast n og k, adskildt af mellemrum: ")

n,k = list(map(int, input().split()))

print()

inputNumbers = []
requests = []

print("Generer testdata automatisk ('j'/'n')?")
if input() == "j":
    print()
    print("Indtast en maksværdi for de tilfældigt genererede tal til testdata.")
    print(("Værdien skal være større end n og k (mindst {}):").format(str(max(n,k) + 1)))
    randomnessRange = int(input())
    print()
    if randomnessRange >= 100000:
        print(Fore.RED)
        print("Advarsel: Det kan tage lang tid at generere testdata med en stor maksværdi (over 10^5).")
        print("Vil du fortsætte? ('j'/'n')")
        print(Style.RESET_ALL)
        if input().lower() == "n":
            print()
            print("Indtast en ny maksværdi:")
            randomnessRange = int(input())
            print()

    print("Genererer testdata...")
    t0 = time.time()
    for i in range(n):
        inputNumbers.append([i,i])
        

    # random values for x and y
    xvalues = random.sample(range(1, randomnessRange), n)
    yvalues = random.sample(range(1, randomnessRange), n)

    # place random values in inputnumbers array
    i = 0
    for pair in inputNumbers:
        pair[0] = xvalues[i]
        pair[1] = yvalues[i]
        i += 1

    for i in range(k):
        requests = random.sample(range(1, randomnessRange), k)
    t1 = time.time()
    print(Fore.YELLOW)
    print("Testdata genereret ({} s)".format(str(round(t1 - t0,3))))
else:
    print()
    for i in range(n):
        temp_list = list(map(int, input().split()))
        inputNumbers.append((temp_list[0], temp_list[1]))

    for i in range(k):
        requests.append(int(input()))


t0 = time.time()
numbers = [inputNumbers[i][1] for i in range(len(inputNumbers))]

inputNumbersDict = {inputNumbers[i][1]: inputNumbers[i][0] for i in range(len(inputNumbers))}
t1 = time.time()
print(Fore.YELLOW)
print("Data transformeret ({} s)".format(str(round(t1-t0,3))))
print(Style.RESET_ALL)

fastanswer = []
slowanswer = []

def fastmethod():
    t0 = time.time()
    step1duration = 0
    step2duration = 0

    for q in requests:
        # add q to the list of y values and sort it
        temp_list = list(numbers)
        temp_list.append(q)
        temp_list.sort()

        newindex = temp_list.index(q)
        # if q is placed last, then there are no y bigger than or equal to it
        if newindex == len(temp_list) - 1:
            slowanswer.append(-1)
            pass
        else:
            step1t0 = time.time()
            for i in range(newindex,len(temp_list)):
                targetnum = temp_list[i]
                if temp_list[i] >= q and targetnum in numbers:
                    break
            step1t1 = time.time()
            fastanswer.append(inputNumbersDict[targetnum])
            step2t1 = time.time()
            
            step1duration += (step1t1 - step1t0)
            step2duration += (step2t1 - step1t1)

    t1 = time.time()

    print(Fore.YELLOW)
    print("Hurtig metode færdig ({} s)".format(str(round(t1 - t0,3))))
    print("Trin 1 ({} s)".format(str(round(step1duration,3))))
    print("Trin 2 ({} s)".format(str(round(step2duration,3))))
    print(Style.RESET_ALL)

def slowmethod():
    t0 = time.time()
    step1duration = 0
    step2duration = 0
    for q in requests:
        # add q to the list of y values and sort it
        temp_list = list(numbers)
        temp_list.append(q)
        temp_list.sort()

        newindex = temp_list.index(q)
        # if q is placed last, then there are no y bigger than or equal to it
        if newindex == len(temp_list) - 1:
            slowanswer.append(-1)
            continue
        else:
            step1t0 = time.time()
            for i in range(newindex,len(temp_list)):
                targetnum = temp_list[i]
                if temp_list[i] >= q and targetnum in numbers:
                    break
            step1t1 = time.time()
            for pair in inputNumbers:
                if pair[1] == targetnum:
                    slowanswer.append(pair[0])
                    break
            step2t1 = time.time()

            step1duration += (step1t1 - step1t0)
            step2duration += (step2t1 - step1t1)

    t1 = time.time()

    print(Fore.YELLOW)
    print("Langsom metode færdig ({} s)".format(str(round(t1 - t0,3))))
    print("Trin 1 ({} s)".format(str(round(step1duration,3))))
    print("Trin 2 ({} s)".format(str(round(step2duration,3))))
    print(Style.RESET_ALL)


def compare_errors(ans1, ans2):
    errors = 0
    for i in range(len(ans1)):
        if ans1[i] != ans2[i]:
            errors += 1
    return errors

fastmethod()
slowmethod()

print("Udskriv svar og fejl?")

print("Den hurtige metode lavede {} fejl.".format(str(compare_errors(fastanswer, slowanswer))))
print()
