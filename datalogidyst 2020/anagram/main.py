import string

# store alphabet as a dictionary of letters and their position in the alphabet
alphabet = dict(zip(string.ascii_uppercase, range(1,27)))

S1 = list(input().strip())
S2 = list(input().strip())

N1 = []
N2 = []

# we convert the strings we are given to two lists of numbers
for letter in S1:
    N1.append(alphabet[letter])

for letter in S2:
    N2.append(alphabet[letter])

count = 0
i = 0
while len(N2) > 0:
    # if we encounter an element that is present in both strings, we remove it
    # (the loop ends when there are no elements left in the list)
    if N1[i] in N2:
        N2.remove(N1[i])
        N1.remove(N1[i])
        # we increment our iterator and check if it is still within bounds
        i += 1
        if i > len(N1) - 1:
            i = 0
        # and return to the top of the loop
        continue

    # otherwise, we add 1 to the element and increment the counter

    # we also check if the element = 26 (if it is the letter "Z"), 
    # in which case we need to return to the start of the alphabet
    if N1[i] == 26:
        N1[i] = 1
        count += 1
    else:
        N1[i] += 1
        count += 1

    # we increment our iterator and check if it is still within bounds
    i += 1
    if i > len(N1) - 1:
            i = 0

print(count)
