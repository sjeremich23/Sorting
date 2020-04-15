# TO-DO: Complete the selection_sort() function below
def insertion_sort(arr):
    # current index is greater than the the next index
    # If true then swap else selet next index to the right
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr


print("sort", insertion_sort([1, 2, 3, 4, 2, 6, 6, 9, 4, 1]))

# TO-DO:  implement the Bubble Sort function below
# bubble up the largest number to the end of array
# start at the first and second index
# is the first index larger than the second?
#   If yes than swap else if NO then
# is the second larger than the third? NO


def bubble_sort(arr):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_swapped = True

    return arr


print("sort", bubble_sort([1, 2, 3, 4, 2, 6, 6, 9, 4, 1]))
# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
