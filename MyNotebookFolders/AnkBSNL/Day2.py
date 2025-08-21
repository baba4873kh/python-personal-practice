# sentence = input("Enter the sentence: ")

# vowels = 'aeiou'
# dict = {}
# for vowel in vowels:
#    count = 0
#    count = sentence.lower().count(vowel)
#    dict[vowel] = dict.get(vowel,0) + count

# print(dict)



# sentence = input("Enter the sentence: ")

# vowels = 'aeiou'

# dict = {}
# for vowel in vowels:
#    counter = 0
#    for letter in sentence:
#       if vowel == letter.lower():
#          counter += 1
#       else:
#          continue
#    dict[vowel] = dict.get(vowel,0) + counter

# print(dict)


# sentence = input("Enter the sentence: ")

# vowels = 'aeiou'

# counter = 0

# for letter in sentence:
#     if letter.lower() in vowels:
#         counter += 1
#     else:
#         continue
# print(counter)


## Counting number of occurence of each letter

# sentence = input("Enter the sentence: ")
# dict = {}
# for letter in sentence:
#     if dict.get(letter) == None:
#         dict[letter] = dict.get(letter,0) + sentence.lower().count(letter)
#     else:
#         continue

# print(dict)

# sentence = input("Enter the sentence: ")
# print(set(sentence))
# for letter in set(sentence):
#     print(letter)

# letter_count = {letter: sentence.lower().count(letter) for letter in set(sentence)}
# print(letter_count)


# name = input("Enter your name: ")

# name = name.replace("a","b")

# print(name)


# name = input("Enter your name: ")
# new_name = ""

# for i in range(len(name)):
#     if name[i] == "a":
#         new_name += "b"
#     else:
#         new_name += name[i]

# print(new_name)

# # strings are immutable. therefore you can make advantage of string concatanation through string addition using plus symbol
    


# for i in range(len(name)):
#     if name[i] == "a":
#         new_name = new_name + "b"
#     else:
#         new_name = new_name + name[i]
         

# word = input("Enter a word to check if it is pallindrome: ")

# if word == word[::-1]:
#     print("Pallindrome")
# else:
#     print("Not a Pallindrome")

# word = input("Enter a word to check if it is pallindrome: ")

# reversed_word = ""

# for i in range (len(word)-1,-1,-1):
#     reversed_word += word[i].lower()
# print(f"Reversed word: {reversed_word}")

# if word.lower() == reversed_word.lower():
#     print("Pallindrome")
# else:
#     print("Not a pallindrome")

# city_name = input("Enter the city name; ")

# # print(city_name.capitalize())

# print(city_name[0].capitalize()+city_name[1::1].lower())

# baba = [1,4,7,0,4,2]
# print(baba)

# baba_zeros = [0]*(len(baba)+1)
# for i in range(len(baba)):
#     if i < 3:
#         baba_zeros[i] = baba[i]
#     elif i== 3:
#         baba_zeros[i] = "a"
#     else:
#         baba_zeros[i+1] = baba[i]
# print(baba_zeros)

# baba = [1,4,7,0,4,2]
# print(baba[:3]+["a"]+baba[4:])

# name = input("Enter your name: ")

# def finding_occurance(name):
#     if name.find("a"):
#         return name.find("a")
#     else:
#         return -1

# print(finding_occurance(name))

# baba = input("Enter your name: ")



# def finding_occurance(baba):
#     found = -1
#     for i in range(len(baba)):
#         if baba[i] == "a":
#             found = i
#             break
#         else:
#             continue
#     return found
# print(finding_occurance(baba))


# my_word = "antidisestablishmentarianism"

# counter = 0
# for i in range(len(my_word)):
#     if my_word[i] == "a":
#         counter += 1
#     else:
#         continue
# print(counter)

# info = input("Enter your information: ")

# first_name = info.split(",")[0].capitalize()
# last_name = info.split(",")[1].capitalize()
# age = info.split(",")[2]

# print(f"My name is {first_name} {last_name} and I am {age} years old")

# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# company = input("Enter company name: ")

# print(first_name[:2].lower()+last_name[len(last_name)-3:len(last_name)].lower()+"@"+company+".com")


# number = int(input("Enter a number: "))

# for i in range(1,number):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue

# number = int(input("Enter a number: "))

# for i in range(0,number,2):
#     if i == 0:
#         continue
#     else:
#         print(i)

# email = input("Enter your email: ")
# username = email.split("@")[0]
# print(username)

# print(username[0]+"*"*(len(username)-1)+username[-1]+"@"+email.split("@")[1])

# email = input("Enter your email: ")

# username = email.split("@")[0]
# domain = email.split("@")[1]
# lst = email.split("@")

# print(username,domain,lst)

# masked = ""

# for i in range(len(username)):
#     if i == 0 or i == len(username)-1:
#         masked = masked + username[i]
#     else:
#         masked = masked + "*"
# masked_email = masked +"@"+ domain
# print(masked_email)

# password = input("Enter your password: ")

# total_chars = len(password)
# uppercase = 0
# lowercase = 0
# digits = 0
# special_chars = 0

# for i in password:
#     if i.isupper():
#         uppercase = uppercase + 1
#     elif i.islower():
#         lowercase = lowercase + 1
#     elif i.isdigit():
#         digits = digits + 1
#     else:
#         special_chars = special_chars + 1
# print(f"total_chars: {total_chars}")
# print(f"uppercase: {uppercase}")
# print(f"lowercase: {lowercase}")
# print(f"digits: {digits}")
# print(f"special_chars: {special_chars}")



# password = input("Enter your password: ")

# uppercase = lowercase = digits = special_chars = 0

# for char in password:
#     if char.isupper():
#         uppercase += 1
#     elif char.islower():
#         lowercase += 1
#     elif char.isdigit():
#         digits += 1
#     else:
#         special_chars += 1

# print(f"total_chars: {len(password)}")
# print(f"uppercase: {uppercase}")
# print(f"lowercase: {lowercase}")
# print(f"digits: {digits}")
# print(f"special_chars: {special_chars}")

# password = input("Enter your password: ")

# counts = {"length":0,"upper":0,"lower":0,"num":0,"special":0}

# if len(password) >= 8:
#     counts["length"] = len(password)
# else:
#     counts["length"] = 0

# for i in password:
#     if i.isupper():
#         counts["upper"] += 1
#     elif i.islower():
#         counts["lower"] += 1
#     elif i.isdigit():
#         counts["num"] += 1
#     else:
#         counts["special"] += 1
# print(counts)

# for key, value in counts.items():
#     if counts[key] > 0:
#         counts[key] = 1
#     else:
#         counts[key] = 0

# total_count = 0

# for value in counts.values():
#     total_count += value

# print(total_count)

# if total_count == 5:
#     print("Strong password")
# elif total_count == 3 or total_count == 4:
#     print("Moderate password")
# else:
#     print("Weak password")

# print(counts)


# password = input("Enter your password: ")

# counts = {
#     "length": int(len(password) >= 8),
#     "upper": 0,
#     "lower": 0,
#     "num": 0,
#     "special": 0
# }

# for char in password:
#     if char.isupper():
#         counts["upper"] = 1
#     elif char.islower():
#         counts["lower"] = 1
#     elif char.isdigit():
#         counts["num"] = 1
#     else:
#         counts["special"] = 1

# total_score = sum(counts.values())

# print(f"Score: {total_score}")
# print(f"Breakdown: {counts}")

# if total_score == 5:
#     print("Strong password")
# elif total_score >= 3:
#     print("Moderate password")
# else:
#     print("Weak password")


# pwd = input("Enter password: ")
# len_flag = False
# upper = False
# lower = False
# digit = False
# special = False
# if len(pwd) >= 8:
#     len_flag = True
# for ch in pwd:
#     if ch.isupper():
#         upper = True
#     elif ch.islower():
#         lower = True
#     elif ch.isdigit():
#         digit = True
#     elif not ch.isalnum():
#         special = True

# # Count how many rules are satisfied
# score = 0
# for flag in [len_flag, upper, lower, digit, special]:
#     if flag:
#         score += 1
# if score == 5:
#     print("Strong Password")
# elif score >= 3:
#     print("Moderate Password")
# else:
#     print("Weak Password")


# list1=[1,2,3,4,5,6,7,8]

# new_list = []

# for i in range (len(list1)):
#     if i % 2 == 0:
#         continue
#     else:
#         new_list.append(list1[i])
# print(new_list)


# ipl= ['CSK','MI','KKR','LSG','PBKS']

# element = input("Enter team name you want the list to be bifurcated at: ")
# new_list = []

# # print(ipl[2:])

# for i in range (len(ipl)):
#     if ipl[i] == element:
#         new_list = ipl[i:]
#         break
#     else:
#         continue
# print(new_list)


# ipl= ['CSK','MI','KKR','LSG','PBKS']

# replacement = input("Enter the index position and value to be replaced at that position as comma sepered values: ")

# ipl[int(replacement.split(",")[0])] = replacement.split(",")[1]

# print(ipl)


# ipl= ['CSK','MI','KKR','LSG','PBKS']

# find_team = input("Enter the name of the tam to be searched in the list: ")

# status = False

# for team in ipl:
#     if find_team == team:
#         status = True
#         break
#     else:
#         continue
# print(status)


# ipl= ['CSK','MI','KKR','LSG','PBKS']

# addition = input("Enter index and value to be inserted: ")

# index = int(addition.split(",")[0])
# team = addition.split(",")[1]

# new_ipl = ipl[:index]+addition.split(",")[1:]+ipl[index:]

# print(new_ipl)

# ipl= ['CSK','MI','KKR','LSG','PBKS']

# addition = input("Enter index and value to be inserted: ")

# index = int(addition.split(",")[0])
# team = addition.split(",")[1]

# new_ipl =[]

# for i in range (len(ipl)):
#     if i != index:
#         new_ipl.append(ipl[i])
#     else:
#         new_ipl.append(team)
#         new_ipl.append(ipl[i])

# print(new_ipl)


# list1= [1,3,4] 
# list2 = [2,4,6]

# new_list = list1 + list2

# print(new_list)

# list1= [1,3,4] 
# list2 = [2,4,6]

# new_list = []

# for i in list1:
#     new_list.append(i)
# for j in list2:
#     new_list.append(j)

# print(new_list)

# list1= [1,3,4] 
# list2 = [2,4,6]

# list1.extend(list2)

# print(list1)


# sentence = input("Enter the sentence: ")
# min_size = int(input("Enter the minimum length of the word: "))

# splitted_sentence = sentence.split(" ")

# for word in splitted_sentence:
#     if len(word) >= min_size:
#         print(word)

# for i in range (1,6):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()

# height = 5
# for i in range(1, height+1):
#     print("*" * i)

# height = 5
# for i in range(height,0,-1):
#     print("*" * i)


# height = 5
# for i in range(1, height+1):
#     print(" "*(height-i)+"*" * i)

# print("Ba"*2+"saheb")

# print(["Ba"]*2+["Saheb"])

# my_list = [10, 30, 40, 65, 90]
# val = int(input("Enter value: "))
# for i in range(len(my_list)):
#     if val < my_list[i]:
#         my_list.insert(i, val)
#         break
# else:
#     my_list.append(val)
# print(my_list)


# list1 = [3, 4, 6, 7]
# new_list1 = []

# number = int(input("Enter a number to be inserted: "))

# inserted = False

# for i in range(len(list1)):
#     if not inserted and number < list1[i]:
#         new_list1.append(number)
#         inserted = True
#     new_list1.append(list1[i])

# # If the number is greater than all elements
# if not inserted:
#     new_list1.append(number)

# print(new_list1)

# statement = "SQL is a powerful language used to manage and query relational databases. With SQL  you can easily retrieve specific data using SELECT statements, update records with UPDATE, or remove unwanted entries using DELETE. Learning sql is essential for data analysts, as most data stored in companies resides in SQL based systems. Advanced SQL techniques like window functions and common table expressions allow for more complex data manipulation. Whether you're building dashboards or running reports, SQL is the foundation of effective data analysis."

# stmt_list = statement.split(" ")

# counter = 0

# for word in stmt_list:
#     if word.lower() == "sql" or word.lower() == '.sql' or word.lower() == "sql.":
#         counter += 1

# print(counter)
    
# print(".SQL.".lower())

# words = para.split()
# count = 0
# for word in words:
#     cleaned = word.strip(",.").lower()
#     if cleaned == "sql":
#         count += 1
# print("SQL count:", count)


s = {1, 2, 3}

print(s)

