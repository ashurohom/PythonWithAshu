# Write a program to convert a number entered by the user into its corresponding number in words. 
# For example, if the input is 8 then the output should be 'EighT'.
# (Hint. use dictionary for keys 0-9 and their values as equivalent words.)

dict = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
}

num=int(input("Enter Number : "))
if num>0 or num<=9:
    print(dict[num])


# WAP TO CHECK GIVEN   EMAIL  IS VALID?

import re
mail = "ashitosh.rohom@gmail.com"

a = re.fullmatch(r'[a-zA-Z0-9.\]+@[a-zA-Z]+\.[a-zA-Z]{2,3}',mail)

if a is None:
    print("Invalid Mail")
else:
    print("Valid Mail")    





# if 0<= num <=9:
#     print(dict[num]) 
# else:
#     print("Invalid Input")    
