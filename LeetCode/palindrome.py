def max_hourglass_sum(arr):
    # Initialize the maximum hourglass sum to a very small number
    max_sum = -float('inf')
    
    # Loop through each possible hourglass starting position
    for i in range(4):
        for j in range(4):
            # Calculate the hourglass sum for the current position
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] + 
                arr[i+1][j+1] + 
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            # Update the maximum hourglass sum if the current one is greater
            if current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum

# Example 6x6 array
A = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

# Calculate and print the maximum hourglass sum
print(max_hourglass_sum(A))
