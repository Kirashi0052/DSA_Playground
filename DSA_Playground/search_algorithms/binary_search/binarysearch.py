def binary_search(arr, search_value):
    minimum = 0
    maximum = len(arr) - 1
    while minimum <= maximum:
        mid = (maximum + minimum) // 2
        if arr[mid] == search_value:
            return True
        else:
            if search_value < arr[mid]:
                maximum = mid - 1
            else:
                minimum = mid + 1
    return False
            

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(sorted_array, 7))