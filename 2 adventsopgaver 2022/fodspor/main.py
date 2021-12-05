def main():
    board = [
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".",".","."]
        ]

    # Input
    x,y = list(map(int, input().split()))

    x -= 1
    y -= 1

    movements = list(input())

    print(movements)

    board[y][x] = "#"

    tempX = x
    tempY = y

    for i in range(len(movements)):
        currentMove = movements[i]

        if currentMove == "O":
            y -= 1
            board[y][x] = "#"

        elif currentMove == "N":
            y += 1
            board[y][x] = "#"

        elif currentMove == "V":
            x -= 1
            board[y][x] = "#"

        elif currentMove == "H":
            x += 1
            board[y][x] = "#"

        for i in range(len(board)):
            print(board[i])
        print("---------")

    
    for i in range(len(board)):
        output = ""
        for j in range(10):
            output += board[i][j]
        print(output)
    

main()
