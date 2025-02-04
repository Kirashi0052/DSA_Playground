def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for n in range(0, len(arr) - 1):
            if arr[n] >= arr[n + 1]:
                temp = arr[n]
                arr[n] = arr[n + 1]
                arr[n + 1] = temp
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  


# Expected Output [11, 12, 22, 25, 34, 64, 90]

#lastcoded: 04.02.2025 15:23