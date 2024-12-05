# WAP to check email ia valid or not
import re

# email = 'ashitosh.rohom@gmail.com'
email = 'sanketpanghavane@yahoo.co'

# pattern = r'[\S+][@]{1}[a-z][.]{1}[a-z]{2,3}'
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
pattern = r'[a-zA-Z0-9.]+@[a-z.]+\.[a-z]{2,3}$'

result = re.fullmatch(pattern, email)
if result != None:
    print(f'Email Valid')
else:
    print(f'Email Not Valid')    
