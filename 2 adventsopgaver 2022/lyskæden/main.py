n,k = list(map(int, input().split()))
christmasLights = list(map(int, input().split(" ")))

# store the original indexes of each element as a list of tuples
# [(element: index), (element: index)...]
christmasLightsOriginal = [(christmasLights[index], index) for index in range(len(christmasLights))]

def sort():
    count = 0
    # we loop through the list backwards in steps of k
    i = n
    while i > 0:
        j = 0
        # we loop through the list forwards (until we reach i - k, the last element at k distance from i)
        while j < i - k:
            # we check if any elements need to be swapped
            if christmasLights[j] > christmasLights[j + k]:
                # if they do, we swap them and increase the swap counter
                christmasLights[j], christmasLights[j + k] = christmasLights[j + k], christmasLights[j]
                count += 1

            j += 1
        
        # then we look at the rest of the elements (i - k to i) and check if they need to be swapped
        while j < i - 1:
            # if they do, then we return -1, since we can't swap elements that are closer to i than distance k
            if christmasLights[j] > christmasLights[j + 1]:
                return -1
        
            j += 1

        # we do this until we have looped through the entire list backwards
        i -= k
    return count


print(sort())
