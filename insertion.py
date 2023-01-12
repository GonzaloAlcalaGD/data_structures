from time import perf_counter

def insertion(unsorted: list) -> list:

    # Traverse through 1 to len(arr)
    for i in range(1, len(unsorted)):
  
        key = unsorted[i]
  
        # Move elements of unsorted[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < unsorted[j] :
                unsorted[j + 1] = unsorted[j]
                j -= 1
        unsorted[j + 1] = key
    
    return unsorted


start = perf_counter()
sorted = insertion([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])
stop = perf_counter()
print(sorted)
print(f'Elapsed time: {start} - {stop}')
print(f'Execution time: {stop-start}')

"""

"""