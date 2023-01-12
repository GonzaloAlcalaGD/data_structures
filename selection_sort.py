def selection_sort(unsorted) -> list:
    length = len(unsorted) # Get length of our list
    i = 0 # Start index at 0
    while i < length: # Traverse the list
        min_val = unsorted[i] # Min value starts at the beggining of our list
        idx = i # Set idx to 0
        for j in range(i+1, length): # Traverse the list accessing the next element in list
            if unsorted[j] < min_val: # If the next element in line it's lesser than our current min value 
                idx = j # Idx of minimum value becomes the the next element 
                min_val = unsorted[j] # Min value becomes the next element                
        unsorted[i], unsorted[idx] = unsorted[idx], unsorted[i] # Swap
        i += 1 

    return unsorted

sorted = selection_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])
print(sorted)

"""
44 < 99 
[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
6 < 44 
[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
2 < 6 
[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
1 < 2 
[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
0 < 1 
[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0] 
6 < 44 
[0, 44, 6, 2, 1, 5, 63, 87, 283, 4, 99] - 0 becomes our minimum value and gets swapped to the first idx
2 < 6 
[0, 44, 6, 2, 1, 5, 63, 87, 283, 4, 99]
1 < 2 
[0, 44, 6, 2, 1, 5, 63, 87, 283, 4, 99] 
2 < 6 
[0, 1, 6, 2, 44, 5, 63, 87, 283, 4, 99] - 1 becomes our minimum value and gets swapped to the second idx
5 < 6 
[0, 1, 2, 6, 44, 5, 63, 87, 283, 4, 99] - 2 becomes our minimum value and gets swapped to the third idx
4 < 5 
[0, 1, 2, 6, 44, 5, 63, 87, 283, 4, 99]
5 < 44 
[0, 1, 2, 4, 44, 5, 63, 87, 283, 6, 99] - 4 becomes our minimum value and gets swapped to the fourth idx
6 < 44 
[0, 1, 2, 4, 5, 44, 63, 87, 283, 6, 99]  - 5 becomes our minimum value and gets swapped to the fifth idx
44 < 63 
[0, 1, 2, 4, 5, 6, 63, 87, 283, 44, 99] - 6 becomes our minimum value and gets swapped to the sixth idx
63 < 87 
[0, 1, 2, 4, 5, 6, 44, 87, 283, 63, 99] - 44 becomes our minimum value and gets swapped to the seventh idx
87 < 283 
[0, 1, 2, 4, 5, 6, 44, 63, 283, 87, 99] - 63 becomes our minimum value and gets swapped to the eighth idx
99 < 283 
[0, 1, 2, 4, 5, 6, 44, 63, 87, 283, 99] - 87 becomes our minimum value and gets swapped to the ninth idx
[0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283] - 283 becomes our minimum value and gets swapped to the tenth idx
"""