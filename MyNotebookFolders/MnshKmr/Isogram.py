s = 'machine'

# lst = []

# for i in s:
#     lst.append(i)

# if len(lst) == len(set(lst)):
#     print("1")

diction = {}

for i in s:
    occurence = diction.get(i,0)
    if occurence == 0:
        diction[i] = 1
    else:
        print("not a isogram")
        break
else:
    print("isogram")
print(diction)
    