# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
    #     # TO-DO: find next smallest element
    #     # (hint, can do in 3 loc)
    #     min_array = min(i: len(arr) - 1)
    #     min_index = arr.index(min_array)
        # TO-DO: swap
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest = min(arr[i:])
        smallest_index = arr.index(smallest)
        if smallest < arr[cur_index]:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
