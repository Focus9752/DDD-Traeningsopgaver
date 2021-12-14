arabicnumber = int(input())

romanNumeralsDict = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1};


romanNumeral = ''

while arabicnumber > 0:
    for letter in romanNumeralsDict:
        if romanNumeralsDict[letter] <= arabicnumber:
            romanNumeral += letter
            arabicnumber -= romanNumeralsDict[letter]
            break;

print(romanNumeral)
