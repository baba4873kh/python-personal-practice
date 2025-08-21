arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3

# Get positions to swap
leading_index = k - 1           # 0-based index from start
lagging_index = -(k)            # 0-based index from end

# Swap the elements
arr[leading_index], arr[lagging_index] = arr[lagging_index], arr[leading_index]

print(arr)


