from math import *
n = 50
prime_numbers = []

for i in range(2,n+1):

    is_prime = True

    for j in range(2,floor(i**0.5)+1):
        if i % j == 0:
            is_prime = False
            break

#     if is_prime == True:
#         prime_numbers.append(i)
# print(prime_numbers)

    else:
        prime_numbers.append(i)
print(prime_numbers)


