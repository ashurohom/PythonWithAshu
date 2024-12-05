import re

# 1) search : 
s = "My Name Is Ashitosh"
exp =  re.search(r'A',s)
print(f'{exp.start()}')
print(f'{exp.end()}')

