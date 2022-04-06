def main():
    n = int(input())

    answer = []
    side = "left"

    for i in range(n):
        if i % 2 == 0:
           answer.append("X" * n)
        else:
            if side == "left":
                answer.append("." * (n-1) + "X")
                side = "right"
            else:
                answer.append("X" + "." * (n-1))
                side = "left"

    for line in answer:
        print(line)



main()




