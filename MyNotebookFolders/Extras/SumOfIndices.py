arr =[0,1,2,3,4,5,6,7,8]

k = 5

lst = []

for i in range (0,len(arr)):
    for j in range (i+1,len(arr)):
        if arr[i] + arr[j] == k:
            lst.append((arr[i],arr[j]))
        else:
            continue

print(lst)

