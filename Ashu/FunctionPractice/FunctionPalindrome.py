'''
3. Write a function to check whether a given string is a palindrome.

A string is a palindrome if it reads the same backward as forward.
Example:
Input: "madam"
Output: True
Input: "hello"
Output: False
'''

def palindrome(str1):
    str2=str1[::-1]

    if str1 == str2:
        return True
    else:
        return False
answer = palindrome('radar')    
print(answer)

