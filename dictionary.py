# Dictionary

dict = {
    "Name" : "Ashu",
    "Subject" : {"1":"html","2":"python","3":"react"},
    "RollNO" : 111,
    
}
# print("DataTYpe : ",type(dict),"\nLength : ",len(dict),"\nValue : ",dict)
# print("---------------------------")


# #Accessing value using key name
# print(dict["Name"])
# print(dict["RollNO"])
# print(dict["Subject"]["1"])
# print("---------------------------")

# # update

# dict["Name"] = "Ashitosh"
# dict["Age"] = 22    #used in django
# print(dict)

# #delete
# print("---------------------------")
# del dict["Age"]
# print(dict)

# print("---------------------------")

# # clear

# # dict.clear()
# # print(dict)

# print("---------------------------")

# del dict
# print(dict)

# d=dict()
# print(type(d))

# d1 = eval(input("Enter Dictionary : "))
# print(type(d1))

# print(dict.get("Name"))

# pop()

# print(dict.pop("RollNO"))

# # keys()

# print(dict.keys())

# key = dict.keys()
# print(type(key))

# for i in key:
#     print(key[i])

# for i in dict.keys():
#     print(dict[i])

new_dict = {1:11,2:22,3:33,4:44,5:55}
print(new_dict)

key_dict = dict.keys()
print(type(key_dict))

for i in key_dict:
    print(key_dict[i])

# popitems

print(dict.popitem())




#values() = return list of all values

# print(dict.values())
# print(dict.items())

