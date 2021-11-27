elementString = list(str((input())))

def main():
    elementDict = {
        "H": 1,
        "He": 2,
        "Li": 3,
        "Be": 4,
        "B": 5,
        "C": 6,
        "N": 7,
        "O": 8,
        "F": 9,
        "Ne": 10
    }

    password = ""
    temp = ""

    i = 0
    while i < len(elementString):

        temp = ""

        temp = elementString[i]
        if(not(i + 1 > len(elementString) - 1)):
            temp += elementString[i + 1]

        if(not(temp in elementDict)):
            password += str(elementDict[elementString[i]])
            i += 1
        else:
            password += str(elementDict[temp])
            i += 2

    print(password)
        
        

main()

