# principal_amount = int(input("Enter principal amount: "))
# rate_of_annual_interest = float(input("Enter roi: "))
# taotal_tenure = int(input("Enter tenure in years: "))

# amount = principal_amount+principal_amount*(rate_of_annual_interest*0.01*taotal_tenure)

# print(amount)


# number = int(input("Enter the number: "))

# if number % 2 == 0:
#     print("Even")

# else:
#     print("odd")


# age = int(input("Enter your age: "))

# if age < 13:
#     print("Child")
# elif age >= 13 and age<=19:
#     print("Teenager")
# elif age >= 20:
#     print("Adult")


# username = "admin"
# password = "1234"

# user = input("Enter your username: ")
# pwd = input("Enter your password: ")

# if username == user and password == pwd:
#     print("Login successful")
# else:
#     print("Invalid credentials")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# largest = a

# if a <= b:
#     largest = b
#     if b <= c:
#         largest = c
#     else:
#         largest = b
# else:
#     largest = a
#     if a <= c:
#         largest = c
#     else :
#         largest = a

# print(f"Lagest number is: {largest}")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a >= b and a >= c:
# print("Largest number is:", a)
# elif b >= a and b >= c:
# print("Largest number is:", b)
# else:
# print("Largest number is:", c)

 
# Celsius = float(input("Enter the temperature to convert in celcius: "))

# farenheit = (Celsius * 9/5)+32

# print(f"{Celsius} C is equal to {farenheit} F")


# number = float(input(" Enter the number: "))

# if number < 0:
#     print("Negative")

# elif number > 0:
#     print("Positive")

# else:
#     print("Zero")


# password = input("Enter the password: ")

# if len(password) < 6:
#     print("Weak Password")
# elif len(password)>=6 and len(password)<=10:
#     print("Moderate password")
# else:
#     print("Strong password")

# 9- Leap Year Checker : Ask the user to enter a year.

# Print whether it is a leap year or not.

# Rules:

# A year is a leap year if:

# It is divisible by 4 and

# Not divisible by 100 unless it's also divisible by 400

# Example:

# 2000 → Leap year

# 1900 → Not a leap year

# 2024 → Leap year

# year = int(input("Enter the year you want to check: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")


# if (year%4==0 and year%100 !=0 and year%400 != 0) or (year%4 == 0 and year%100 ==0 and year%400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


bill_amount = float(input("Enter bill amount: "))
tip_percentage = float(input("Input tip percent: "))
number_of_people = float(input("Input number of people: "))

tip_amount = (bill_amount * tip_percentage)/100

total_amount = bill_amount + tip_amount

per_person_share = total_amount / number_of_people

print(f"Tip: {tip_amount}")
print(f"Total Bill (with tip): {total_amount}")
print(f"Each person should pay: {per_person_share}")