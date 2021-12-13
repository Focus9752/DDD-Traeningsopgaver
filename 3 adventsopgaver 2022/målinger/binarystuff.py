def binarySearch(A, elem, l, r):
    if l <= r:
        m = (l + r + 1) // 2

        if l == r:
            return l

        elif A[m] > elem:
            return binarySearch(A, elem, l, m - 1)
        
        else:
            return binarySearch(A, elem, m, r)

# Input
A = list(map(int, input().split()))
requests = list(map(int, input().split()))

for request in requests:
    l = binarySearch(A, request, 0, len(A) - 1)

    if(A[l] == request):
        print(l + 1)
    else:
        print(-1)


