# check which command was entered and execute it
# loop breaks when "sluk" command is entered

# store days and money earned on those days in a dict
days = {i + 1: 0 for i in range(24)}

# initialize current day as December 1st
currentDay = 1

while True:
    # store command and parameter in list
    command = input().split()
    
    # check for all possible commands
    if command[0] == "sluk":
        break

    elif command[0] == "ny-dag":
        currentDay = int(command[1])

    elif command[0] == "salg":
        days[currentDay] += int(command[1])

    elif command[0] == "returnering":
        days[currentDay] -= int(command[1])

    elif command[0] == "indtjening":
        startDay = int(command[1])
        endDay = int(command[3])

        output = 0
        for j in range(startDay, endDay + 1, 1):
            output += days[j]
        print("indtjeningen fra {} til {} er {}".format(startDay, endDay, output))

    