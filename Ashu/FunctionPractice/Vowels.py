'''
4. Count Vowels in a String
Write a function named count_vowels(string) that takes a string as input and returns the number of vowels in it.
Example:
print(count_vowels("hello world"))  # Output: 3
'''

def count_vowels(string):
    vowels='a','e','i','o','u','A','E','I','O','U'
    count=0
    for i in string:
        if i in vowels:
            count+=1
    print(count)
count_vowels("hello world")            