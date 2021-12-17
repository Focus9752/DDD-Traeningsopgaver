import string

# store alphabet as a dictionary of letters and their position in the alphabet
alphabet = dict(zip(string.ascii_uppercase, range(1,27)))

# finds the number of swaps required to get from one letter to another letter
def letterDistance(a, b):
    count = 0
    while a != b:
        a += 1
        if a > 26:
            a = 1
    return count

# S1 = list(input().strip())
# S2 = list(input().strip())

N1 = []
N2 = []

for letter in S1:
    N1.append(alphabet[letter])

for letter in S2:
    N2.append(alphabet[letter])

N1.sort()
N2.sort()

answer = 0

for i in range(len(N1)):
    firstletter = N1[i]
    secondletter = N2[i]

    count = 0
    while firstletter != secondletter:
        firstletter += 1
        count += 1
        if firstletter > 26:
            firstletter = 1

    answer += count



print()
