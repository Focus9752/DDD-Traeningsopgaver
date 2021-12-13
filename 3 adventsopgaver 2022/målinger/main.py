n,k = list(map(int, input().split()))

# raw input as a list of tuples
# [(5, 50), (6, 55) (7, 60)]
inputyValues = []

for i in range(n):
    temp_list = list(map(int, input().split()))
    inputyValues.append((temp_list[0], temp_list[1]))

# a sorted list containing the y values from the input
# [50, 55, 60]
yValues = [inputyValues[i][1] for i in range(len(inputyValues))]
yValues.sort()

# a dicitonary of corresponding y and x values {y: x}
inputyValuesDict = {inputyValues[i][1]: inputyValues[i][0] for i in range(len(inputyValues))}
inputyValuesDict = {yValues[i]: inputyValuesDict[yValues[i]] for i in range(len(yValues))}

# store requests
requests = []
for i in range(k):
    requests.append(int(input()))

def main():
    for q in requests:
        # use binary search to find the index we should place q at in order to keep the list sorted
        newindex = find_index(yValues, q)
        # if that index is greater than the max index, then there are no y-values larger than q
        # which means we print -1
        if newindex > len(yValues) - 1:
            print(-1)
        else:
            # we look up the corresponding x value in our dicitonary
            print(inputyValuesDict[yValues[newindex]])

# binary search implementation to find the index 
# where a new number should be placed in a sorted list
def find_index(list, K):
    l = 0
    r = len(list) - 1

    while l <= r:
        mid = (l + r) // 2

        if list[mid] == K:
            return mid

        elif list[mid] < K:
            l = mid + 1
        
        else:
            r = mid - 1
    
    return r + 1

main()
