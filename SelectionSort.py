


# GIVEN ARRAY
arr= [0,12,32,1,22,4,23,12,2,9,3,0,-12]
print(f"Given Array: arr={arr}")


# SELECTION SORT
# Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest
#  (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 
# The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the 
# first element of the unsorted portion. This process is repeated for the remaining unsorted portion of the list until the entire
#  list is sorted. One variation of selection sort is called “Bidirectional selection sort” which goes through the list of elements 
# by alternating between the smallest and largest element, this way the algorithm can be faster in some cases.


def SelectionSort(arr):
    for x in range(len(arr)):
        min_index = x
        for y in range(x+1,len(arr)):
            if arr[min_index] > arr[y]:
                min_index = y
        arr[x],arr[min_index] = arr[min_index],arr[x]
    return arr



print(f"Sorted Array: arr={SelectionSort(arr)}")

