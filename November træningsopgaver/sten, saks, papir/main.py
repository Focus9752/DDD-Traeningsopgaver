def main():

    #print("Indgiv den første spillers navn.")

    player1 = str(input())

    #print("Den første spillers navn er: " + player1)

    #print("\n")



    #print("Indgiv den første spillers valg.")

    player1Choice = str(input()).lower()

    #print("Den første spillers valg er: " + player1Choice)

    #print("\n")



    #print("Indgiv den anden spillers navn.")

    player2 = str(input())

    #print("Den anden spillers navn er: " + player2)

    #print("\n")



    #print("Indgiv den anden spillers valg.")

    player2Choice = str(input()).lower()

    #print("Den anden spillers valg er: " + player2Choice)

    #print("\n")

    #kontrollér input
    # if (player1Choice not in ["sten", "saks", "papir"]) or (player1Choice not in ["sten", "saks", "papir"]):
    #     print("Indgiv venligst gyldigt input!")
    #     return

    if player1Choice == player2Choice:

        print("uafgjort")
        return "uafgjort"

    elif player1Choice == "sten":

        if player2Choice == "saks":
            print(player1)
            return player1

        else:
            print(player2)
            return player2

    elif player1Choice == "papir":

        if player2Choice == "sten":
            print(player1)
            return player1

        else:
            print(player2)
            return player2

    elif player1Choice == "saks":

        if player2Choice == "papir":
            print(player1)
            return player1

        else:
            print(player2)
            return player2

main()



