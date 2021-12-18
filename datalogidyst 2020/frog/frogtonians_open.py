import sys
sys.setrecursionlimit(10**9)
# check if a move to square (i,j) is valid, 
# given the previous moves
def is_valid(i, j, moves):
    if i >= 1 and i <= N and j >= 1 and j <= N and moves[i][j] == -1:
        return True
    else:
        return False
    
# arrays storing the possible moves
x_moves = [-3, -2, -2, 0, 0, 2, 2, 3]
y_moves = [0, 2, -2, -3, 3, 2, -2, 0]

def frogtonian(moves, x, y, step_count, x_moves, y_moves):
    # check if we have found a solution
    # a solution will always have N^2 steps
    if step_count == N*N + 1:
        return True

    # iterate over the possible moves array
    # and find all of the possible moves
    for k in range(8):
        next_x = x + x_moves[k]
        next_y = y + y_moves[k]

        if is_valid(next_x, next_y, moves):
            moves[next_x][next_y] = step_count
            # return if we are done with the tour
            # (if the last run returned True)
            if frogtonian(moves, next_x, next_y, step_count + 1, x_moves, y_moves):
                return True
            moves[next_x][next_y] = -1
    
    return False

def start_frogtonian():
    print("---")
    moves = []
    # initialize the "moves" matrix with all positions at -1
    for i in range (N+1):
        moves.append([0]+([-1]*N))

    # arrays storing the possible moves
    x_moves = [-3, -2, -2, 0, 0, 2, 2, 3]
    y_moves = [0, 2, -2, -3, 3, 2, -2, 0]

    # start at the top left
    moves[1][1] = 1

    
    if frogtonian(moves, 1, 1, 2, x_moves, y_moves):
        for x in range(1, N + 1):
            for y in range(1, N + 1):
                if moves[x][y] == N*N:
                    legitSolution = False
                    for k in range(8):
                        next_x = x + x_moves[k]
                        next_y = y + y_moves[k]

                        if next_x >= 1 and next_x <= N and next_y >= 1 and next_y <= N and moves[next_x][next_y] == 1:
                            legitSolution = True
                    
                    if legitSolution == False:
                        start_frogtonian()
                        return

            answer = ""
            for elem in moves[x][1:]:
                answer += str(elem) + " "
            print(answer)
        return True
    return False

N = int(input())

start_frogtonian()

