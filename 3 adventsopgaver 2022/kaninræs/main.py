def main():
    s = int(input())
    a1, b1 = list(map(int, input().split()))
    a2, b2 = list(map(int, input().split()))

    n1 = 0
    n2 = 0
    
    while not s <= n1* (a1-b1) + b1:
        n1 += 1

    while not s <= n2* (a2-b2) + b2:
        n2 += 1
    
    if n1 == n2:
        print("uafgjort")
    elif n1 < n2:
        print("kanin 1 vinder")
    else:
        print("kanin 2 vinder")

main()

