
# GIVEN ARRAY
arr= [0,12,32,1,22,4,23,12,2,9,3,0,-12]
print(f"Given Array: arr={arr}")


#Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as 
#its average and worst-case time complexity is quite high.

for x in range(len(arr)):
    for y in range(0,len(arr)-1):
        if arr[y]>arr[y+1]:
            arr[y],arr[y+1]= arr[y+1],arr[y]
        
    
print(f"Sorted Array: arr={arr}")