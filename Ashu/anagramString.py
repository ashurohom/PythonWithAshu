# Python Program to Check If Two Strings are Anagram

str1 = input("Enter First String : ")
str2 = input("Enter Second String : ")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("No Anagram")    

'''
Enter First String : listen
Enter Second String : silent
Anagram
'''