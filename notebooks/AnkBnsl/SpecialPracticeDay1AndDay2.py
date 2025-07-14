# para = '''Babasaheb is a good boy. Babasaheb is known for his expertise in DE'''

# print(para.replace("Babasaheb","Nilam").replace("his","her").replace("boy","girl").replace("DE","PV"))
# print()
# print(f"old_para: {para}")

# para_list = para.split(" ")

# print(f"para_list: {para_list}")

# new_para_list = []

# for word in para_list:
#     if word == "Babasaheb":
#         new_para_list.append("Nilam")
#     else:
#         new_para_list.append(word)
# print(f"new_para_list: {new_para_list}") 

# new_para = ""

# for i in range(len(new_para_list)):
#     if i == 0:
#         new_para += new_para_list[i]
#     else:
#         new_para += " " + new_para_list[i]

# print(f"new_para: {new_para}")
# print()

# print("Babasaheb" in para)

# listu = ["Baba","Nilam","Prasad"]

# print("Baba" in listu)

# print(listu.index("Nilam"))

# s = "abccba"

# length = len(s)

# if length % 2 == 0:
#     print(s[:int((length/2))])
#     print(s[(length//2):][::-1])
#     if s[:int((length/2))] == s[int(length/2):][::-1]:
#         print("True")
#     else:
#         print("False")
# else:
#     print(s[:(length//2)])
#     print(s[(length//2)+1:][::-1])
#     if s[:(length//2)] == s[(length//2)+1:][::-1]:
#         print("True")
#     else:
#         print("False")

# words = ["Data", "Engineering", "is", "awesome"]

# sentence = "||".join(words)

# print()
# print(sentence)
# print()


a = [10,40,97,110,200]
new_list= [number for number in a if number%2 ==0 ]
print(new_list)
new_list = [ "Even" if number%2==0 else "odd" for number in a ]
print(new_list)
