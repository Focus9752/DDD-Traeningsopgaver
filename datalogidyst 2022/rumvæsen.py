import sys

sys.setrecursionlimit(10**9)


def calculateStarScore(S, P, score, original_S):
    S = list(S)
    T = S.copy()
    for i in range(N):
        S[P[i] - 1] = T[i]
    
    score += 1

    S = ''.join(str(elem) for elem in S)

    if S == original_S:
        return score
    else:
        return calculateStarScore(S, P, score, original_S)

def changeName(S, q, c):
    S = list(S)
    S[q - 1] = c

    S = ''.join(str(elem) for elem in S)

    return S

N, Q = list(map(int, input().split()))
name = input()
P = list(map(int, input().split()))

qList = []
cList = []

for i in range(Q):
    inputList = input().split()
    qList.append(int(inputList[0]))
    cList.append(str(inputList[1]))

for i in range(Q):
    name = changeName(name, qList[i], cList[i])
    print(calculateStarScore(name, P, 0, name))
