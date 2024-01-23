def binary_search(arr, low, high, x ):
    if high >= low:

        mid = (high + low) // 2
        
        if(arr[mid] == x):
            return mid
        elif (arr[mid] > x):
            return binary_search(arr, low, mid -1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1




arr = [2, 5, 7, 10, 13, 15, 18]
x = 13
result = binary_search(arr, 0, len(arr)-1, x)
# print(f"The index 5 found in {result}")
print(result)