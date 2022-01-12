"""
Two intervals [A1, B1] and [A2, B2] are considered overlapping if A1 <= A2 <= B1

1.  Sort intervals based on lowest time (from lowest to highest)

2.  Insert 1st interval into stack

3.  Look at the next interval. 
    If it overlaps with the interval at the top of the stack, we merge the two intervals.
    We do this backwards (making the new merged interval as small as possible)
    
    If it doesn't overlap, then we add this interval to the stack as the new top.
    We can be sure that no other intervals will overlap with the ones in the stack, 
    since the intervals are sorted.

4.  We repeat step 3 until we have processed all of the intervals. 
    We return the stack, which now contains the new, merged intervals.
"""

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