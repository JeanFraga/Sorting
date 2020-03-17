# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
        # cur_index = i
        # smallest_index = cur_index
        # # TO-DO: find next smallest element
        # # (hint, can do in 3 loc)
        # if arr[cur_index] < arr[smallest_index]:
        
    # i indicates how many items were sorted
    for i in range(len(arr)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(arr)-1):
            # Update the min_index if the element at j is lower than it
            if arr[j] < arr[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        arr[i], arr[min_index] = arr[min_index], arr[i]
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
listarray = [5,4,9,6,4,7,5,3,6]
print(selection_sort(listarray))
print(selection_sort(listarray))

# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr