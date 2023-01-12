from time import perf_counter

def partition(list, low, high):

    # Choose the right most element as the pivot
    pivot = list[high]
    # Pointer for the greater element 
    i = low-1 

    # Traverse the whole list and compare with the pivot
    for j in range(low, high):
        if list[j] <= pivot:
            # If an element smaller than our pivot it's found swap it with the greater element
            i += 1
            # Swapping element i for element j
            list[i], list[j] = list[j], list[i]
    # Swap our pivot to the greater element
    list[i+1], list[high] = list[high], list[i+1]

    return i+1 # Return the position from where the partition has been done.

def quickSort(list, low, high):

    if low < high:

        # Find pivot element such that smaller elements than the pivot are on the left
        # And greater elements that the pivot are on the right
        pivot = partition(list, low, high)

        # Recursive call on the left side of the pivot
        quickSort(list, low, pivot-1)
        # Recurvise call on the right side of the pivot
        quickSort(list, pivot+1, high)

    return list

unsorted = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

start = perf_counter()
sorted = quickSort(unsorted, 0, len(unsorted)-1)
stop = perf_counter()
print(sorted)
print(f'Elapsed time: {start} - {stop}')
print(f'Execution time: {stop-start}')