import string

n,m = list(map(int, input().split()))
keyword = list(input())
originalText = input()

def main():
    alphabet = list(string.ascii_uppercase)

    tempSpejdList = []

    for char in keyword:
        if char not in tempSpejdList:
            tempSpejdList.append(char)
            alphabet.remove(char)

    for char in alphabet:
        tempSpejdList.append(char)

    spejdDict = {}

    for i in range(13):
        spejdDict[tempSpejdList[i]] = tempSpejdList[13 + i]
        spejdDict[tempSpejdList[13 + i]] = tempSpejdList[i]

    result = ""

    for char in originalText:
        if char.upper() in spejdDict:
            if char.isupper():
                result += spejdDict[char]
            else:
                result += spejdDict[char.upper()].lower()

        else:
            result += char

    print(result)

main()
