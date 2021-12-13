n,k = list(map(int, input().split()))

# raw input as a list of tuples
# [(5, 50), (6, 55) (7, 60)]
inputNumbers = []

for i in range(n):
    temp_list = list(map(int, input().split()))
    inputNumbers.append((temp_list[0], temp_list[1]))

# the numbers from the input
# [50, 55, 60]
numbers = [inputNumbers[i][1] for i in range(len(inputNumbers))]

inputNumbersDict = {inputNumbers[i][1]: inputNumbers[i][0] for i in range(len(inputNumbers))}
# store requests
requests = []

for i in range(k):
    requests.append(int(input()))

def main():
    for q in requests:
        # add q to the list of y values and sort it
        temp_list = list(numbers)
        temp_list.append(q)
        temp_list.sort()

        newindex = temp_list.index(q)
        # if q is placed last, then there are no y bigger than or equal to it
        if newindex == len(temp_list) - 1:
            print(-1)
        else:
            for i in range(newindex,len(temp_list)):
                targetnum = temp_list[i]
                if temp_list[i] >= q and targetnum in numbers:
                    break
            print(inputNumbersDict[targetnum])

def binarySearch(A, elem, l, r):
    if l <= r:
        m = (l + r + 1) // 2

        if l == r:
            return l

        elif A[m] > elem:
            return binarySearch(A, elem, l, m - 1)
        
        else:
            return binarySearch(A, elem, m, r)

def S(x, q):
    if x >= q:
        return True
    else:
        return False

main()

