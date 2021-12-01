def main():

    string = input()

    if len(string) % 2 != 0:
        print("der er ugler i mosen")
        return
    
    else:
        for i in range(0,len(string), 2):
            if string[i] + string [i + 1] != "ho":
                print("der er ugler i mosen")
                return
        print("den er god nok")

main()
