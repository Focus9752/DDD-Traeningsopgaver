inputArr = list(map(int, input().split()))

# the key is the denomination of the coin 
# the value is the amount of coins that have that denomination
coinsDict = {5: inputArr[0], 10: inputArr[1], 20: inputArr[2]}

def main():
    result = 0
    change = 0
    sum = 0

    result += coinsDict[20] - (coinsDict[20] % 3)
    coinsDict[20] = coinsDict[20] % 3

    if coinsDict[20] == 2:

        pass
    elif coinsDict[20] == 1:
        
        pass
    else:
        pass

main()
