import re

# 1) search : 
s = "My Name 12 Is Ashitosh 111"
exp =  re.search(r'A',s)
print(f'{exp.start()}')
print(f'{exp.end()}')
print("------------------")

# 2) match
exp2 = re.match(r'M',s)
print(exp2,exp2.start())
print("------------------")

# 3) fullmatch

num = "9527230560"
exp3 = re.fullmatch(r'[6-9]{1}[0-9]{9}',num)
if exp3 != None:
    print("Correct Mobile Number")
else:
    print("InCorrect Mobile Number")

print("------------------")


# 4) findall

pattern = '\d+'
result = re.findall(pattern,s)
print(f'Findall : {result}')

print("------------------")

# 5) split

pattern2 = re.split(r'd+',s)
print(f'Split : {pattern2}')

# maxsplit = 1
pattern22 = re.split(r'\d+',s,1)
print(f'Split : {pattern22}')

print("------------------")

