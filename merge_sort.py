from time import perf_counter

def merge(left, right) -> list:
    """
    Iterates over the two pointers of left and right
    and compares them to check which is lesser than and appends them to the output list and moves the corresponding pointer.
    """
    output = [] # Initialize our empty list were results are going to be placed.
    i = j = 0 # Initialize both pointers. 

    # Loop while i and j pointers are less than the lenght of our left and right lists.
    while i < len(left) and j < len(right):
        if left[i] < right[j]: # Compare both elements from each list for each iteration
            output.append(left[i]) # Append the lesser value
            i += 1 # Move the left pointer 
        else:
            output.append(right[j]) # Append the lesser value
            j += 1 # Move the right pointer 
    
    # Remnant values are picked from the current pointer and place into the end of their respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def merge_sort(list) -> list:
    """
    Receives a list as an input and brokes down the list in two partitions (left and right) according to the middle
    element in our list, using recursion.
    """
    length = len(list) # Get length of list

    if length == 1: return list # If the size of the list it's 1 then it's already sorted

    midpoint = length//2 # Get the middle element of our list
    
    left_partition = merge_sort(list[:midpoint]) # Broke down left list components calling the merge_sort with recursion
    right_partition = merge_sort(list[midpoint:]) # Broke down right list components calling the merge_sort with recursion

    return merge(left_partition, right_partition)

start = perf_counter()
sorted = merge_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])
stop = perf_counter()
print(sorted)
print(f'Elapsed time: {start} - {stop}')
print(f'Execution time: {stop-start}')