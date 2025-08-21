s = "GeeksforGeeks"

print(s[::-1])

reversed_s = ""

print(len(s))

for i in range(len(s)-1,-1,-1):
    reversed_s = reversed_s + s[i]
print(reversed_s)


for i in range(len(s)-1,-1,-1):
    print(i)