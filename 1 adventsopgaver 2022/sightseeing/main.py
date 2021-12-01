def main():
    n = int(input())
    mountains = []
    for i in range(n):
        mountains.append(input())

    tempMountains = sorted(mountains, key=int, reverse=True)

    print(mountains.index(tempMountains[1]) + 1)

main()
