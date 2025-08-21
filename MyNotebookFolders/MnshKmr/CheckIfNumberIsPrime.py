from math import floor
n = int(input("Enter a number to check if it is prime: "))

# sqrt = n**0.5

# print(floor(sqrt))

for i in range(2,floor(n**0.5)+1):
    if n % i == 0:
        print("False")
        break
else:
    print("True")