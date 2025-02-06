def selection_sort(arr):
    #Bedingung mit zwei for schleifen 
    for i in range(0, len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
test_array = [64, 34, 25, 12, 22, 11, 90]

print(selection_sort(test_array))
