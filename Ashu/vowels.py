# Problem: Write a Python program that counts how many vowels (a, e, i, o, u) are present in a given string.

str = "aaaaashitoosh"
vowels = 'aeiouAEIOU'
count = {}


for i in str:
    if i in vowels:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1    
print(f'Number of Vowels {count}') 
          