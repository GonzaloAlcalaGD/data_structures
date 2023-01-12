def bubble_sort(my_list = []) -> list:
    length = len(my_list) # Get length of our list
    for i in range(length): # Traverse the list

        swap = False 

        for j in range(0, length-i-1):
            if my_list[j] > my_list[j+1]: # Compare our value with the next value in the list
                swap = True
                temp = my_list[j] # Save current value
                my_list[j] = my_list[j+1] # Switch the next value to our current value position
                my_list[j+1] = temp  # Switch our current value with the next value position
        if not swap: # If not swap stop the traversing
            break
    return my_list

sorted_list = bubble_sort([9,8,7,6,5,4,3,2,1])
print(sorted_list)
"""
-2 > 45 - False
[-2, 45, 0, 11, -9]
45 > 0 - True Swap
[-2, 0, 45, 11, -9]
45 > 11 - True Swap
[-2, 0, 11, 45, -9]
45 > -9 - True Swap
[-2, 0, 11, -9, 45]
-2 > 0 - False
[-2, 0, 11, -9, 45]
0 > 11 - False
[-2, 0, 11, -9, 45]
11 > -9 - True
[-2, 0, -9, 11, 45]
-2 > 0 - False
[-2, 0, -9, 11, 45]
0 > -9 - True Swap
[-2, -9, 0, 11, 45]
-2 > -9 - True Swap
[-9, -2, 0, 11, 45] - Sorted
"""