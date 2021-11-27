# Arealet af en trekant ud fra tre punkter:
# A = (1/2) * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

def main():

    PRaw = input()
    QRaw = input()
    RRaw = input()

    P = int(PRaw.split(" ")[0]), int(PRaw.split(" ")[1])
    Q = int(QRaw.split(" ")[0]), int(QRaw.split(" ")[1])
    R = int(RRaw.split(" ")[0]), int(RRaw.split(" ")[1])

    area = (1/2) * abs(P[0] * (Q[1] - R[1]) + Q[0] * (R[1] - P[1]) + R[0] * (P[1] - Q[1]))
    print(area)

main()
