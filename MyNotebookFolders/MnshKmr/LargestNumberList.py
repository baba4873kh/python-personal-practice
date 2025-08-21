arr = [1,8,7,56,90]

largest = float("-inf")

for i in arr:
    if largest <= i:
        largest = i

print(largest)