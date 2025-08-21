from math import floor

arr = [1,2,3,4,2,1]


for i in range(floor(len(arr)/2)+1):
    print(arr[i], arr[-(i+1)])
    if arr[i] == arr[-(i+1)]:
        continue
    else:
        print("not a pallindrome")
        break
else:
    print("pallindrome")