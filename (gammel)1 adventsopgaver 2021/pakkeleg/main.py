def main():
    inputLst = input()
    inputLst = inputLst.split(" ")

    n = int(inputLst[0])
    m = int(inputLst[1])

    print(m % n)
    
main()