elementsString = list(str((input())))

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
    nextElement = False

    temp = ""
    for index, char in enumerate(elementsString):

        if(index == len(elementsString) - 1):
            if(nextElement):
                temp = char
            else:
                temp += char
            password += str(elementDict[temp])

        # If we need to switch to the next element
        if(nextElement):
            password += str(elementDict[temp])
            temp = char

        elif(not(nextElement)):
            temp += char

        # If the next character is upper case, we need to start looking for the next element
        if(index < (len(elementsString) - 1)):
            if(elementsString[index + 1].isupper()):
                nextElement = True
            else:
                nextElement = False
        
        print("Index: " + str(index))
        print(nextElement)
        print("Password: " + password)
        print("Temp: " + temp)

        
        



main()

