def bubble(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr 


arr = [2, 6, 5, 1, 3, 4,]
result = bubble(arr)
print(result)