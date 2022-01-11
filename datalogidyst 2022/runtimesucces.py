def main():
    N = int(input())
    runnerIntervals = []
    # We just use a list for the stack
    stack = []

    for i in range(N):
        runnerIntervals.append(list(input().split(" ")))

    for i in range(N):
        runnerIntervals[i] = list(map(int, list(filter(None, runnerIntervals[i]))))

    # Sort intervals
    runnerIntervals.sort()

    # Append the first interval to the stack
    stack.append(runnerIntervals[0])

    for i in range(1, N, 1):
        # Cache current interval
        currentInterval = runnerIntervals[i]

        # Set temp to top element in stack
        temp = stack[len(stack) - 1]

        if temp[0] <= currentInterval[0] <= temp[1]:
            if temp[1] < currentInterval[1]:
                temp = [currentInterval[0], temp[1]]
            else:
                temp = [currentInterval[0], currentInterval[1]]
            
            stack.pop()
            stack.append(temp)

        else:
            stack.append(currentInterval)

    print(len(stack))

main()