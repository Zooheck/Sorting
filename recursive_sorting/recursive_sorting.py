# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a_index = 0
    b_index = 0
    for i in range(0, len(merged_arr)):
        if len(arrA) - 1 < a_index:
            merged_arr[i] = arrB[b_index]
            b_index += 1
        elif len(arrB) - 1 < b_index:
            merged_arr[i] = arrA[a_index]
            a_index += 1
        elif arrA[a_index] > arrB[b_index]:
            merged_arr[i] = arrB[b_index]
            b_index += 1
        else:
            merged_arr[i] = arrA[a_index]
            a_index += 1

    return merged_arr


print(merge([1, 2, 3], [0.5, 4, 5, 6]))

# TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort(arr):
#     # TO-DO

#     return arr


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr


# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr
