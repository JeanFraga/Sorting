# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # print(merged_arr)
    for j in range(len(arrA)):
        # print(j)
        merged_arr[j] = arrA[j]
    for j in range(len(arrB)):
        # print(j)
        merged_arr[j+len(arrA)] = arrB[j]
    return merged_arr

arrayA = [1,2,3,5,4,8,9]
arrayB = [5,6,9,7,8,5]

# print(merge(arrayA, arrayB))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # sortedarr = [0] * len(arr)
    if len(arr) > 1:
        arr1 = arr[:len(arr)//2]
        # print(arr1)
        arr2 = arr[len(arr)//2:]
        # print(arr2)
        merge_sort(arr1)
        merge_sort(arr2)
        left = mid = right = 0
        # if arr[0] > sortedarr[i]:
        #     i+=1
        #     sortedarr.append(arr)
        while left < len(arr1) and mid < len(arr2):
            if arr1[left] < arr2[mid]:
                arr[right] = arr1[left]
                left+=1
            else:
                arr[right] = arr2[mid]
                mid+=1
            right+=1
        while left < len(arr1):
            arr[right] = arr1[left]
            left+=1
            right+=1
        while mid < len(arr2):
            arr[right] = arr2[mid]
            mid+=1
            right+=1
    return arr
    
    # return sortedarr
    



# merge_sort(arrayA)
# print(arrayA)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
