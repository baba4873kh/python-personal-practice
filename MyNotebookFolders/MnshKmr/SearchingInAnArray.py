arr = [9,7,16,16,4]
k = 1


for i in range(len(arr)):
    if arr[i] == k:
        print(i)
        break
else:
    print("-1")