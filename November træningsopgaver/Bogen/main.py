from collections import Counter

def main():
    # Input
    N = int(input())
    linje = str(input()).lower()

    # Teksten deles op i enkelte ord
    textArr = linje.split(" ")

    # Vi gemmer tekstens oprindelige længde
    originalLength = 0

    for word in textArr:
        originalLength += int(len(word))
    
    # Vi definerer en variable der gemmer den kortest mulige længde af teksten
    shortestLength = 0

    # Vi gemmer hvor mange gange de enkelte ord optræder i teksten
    c = Counter(textArr)

    # Den korteste længde af teksten er summen af de ideelle længder for alle ord
    for k,v in c.items():
        shortestLength += idealLength(str(k), v)

    print(int(shortestLength))

# Vi indfører en funktion der giver os den "ideelle længde" for et ord, 
# dvs. det antal tegn som alle ordets forekomster kan kortes ned til
def idealLength(word, occurences):
    originalWordLength = len(word) * occurences
    newWordLength = (len(word) + 5) + (occurences - 1) * 3
    if(originalWordLength > newWordLength):
        return newWordLength
    else:
        return originalWordLength

main()


