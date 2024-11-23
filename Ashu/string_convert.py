# wap given string latter convert lower to upper and upper to lower

list = "aSHITOSH"
new_string = " "
for i in list:
    if i.islower():
        new_string += i.upper()
    elif i.isupper():
        new_string += i.lower()
    else:
        new_string += i   
print(new_string)


