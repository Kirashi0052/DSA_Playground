def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while(j >= 0 and arr[j] > temp):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp
      
    return arr



arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))