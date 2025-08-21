# s = "Geeks"

s = "GeeksforGeeks"

new_s =""

for i in range(len(s)):
    if i%2 == 0:
        new_s = new_s + s[i]
    else:
        continue
print(new_s) 