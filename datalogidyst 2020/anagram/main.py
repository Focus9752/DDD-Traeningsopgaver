import string

# store alphabet as a dictionary of letters and their position in the alphabet
alphabet = dict(zip(string.ascii_uppercase, range(1,27)))

# finds the number of swaps required to get from one letter to another letter
def letterDistance(a, b):
    return abs(alphabet[a] - alphabet[b])

S1 = list(input())
S2 = list(input())



N1 = []
N2 = []

for letter in S1:
    N1.append(alphabet[letter])

for letter in S2:
    N2.append(alphabet[letter])


answer = 0

for i in range(len(N1)):
    answer += abs(N1[i] - N2[i])

print(S1,S2)
print(N1,N2)

N1.sort()
N2.sort()

print(N1,N2)
print()

print(answer)
