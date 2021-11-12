def main():
    # Skil n og q ad
    lst1 = input()
    lst1 = lst1.split(" ")
    n = int(lst1[0])
    q = int(lst1[1])

    # Lav en list med stationerne og sørg for at objekterne i listen er heltal
    stationer = input().split(" ")
    stationer = list(filter(None, stationer))
    stationer = list(map(int, stationer))
        
    # Til debug
    print()
    print("n: " + str(n))
    print("q: " + str(q))
    print("stationer: ")
    print(stationer)
    print()

    # Formatér forespørgslerne
    forespørgsler = []

    i = 0
    while i < n:
        forespørgsler.append(list(input().split(" ")))
        i += 1
    
    i = 0
    while i < n:
        forespørgsler[i] = list(map(int, list(filter(None, forespørgsler[i]))))
        i += 1

    
    # Til debug
    print()
    print("n: " + str(n))
    print("q: " + str(q))
    print("stationer: ")
    print(stationer)
    print()

    print("Forespørgsler: ")
    print(forespørgsler)
    print()

main()