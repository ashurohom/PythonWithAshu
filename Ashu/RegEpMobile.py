# WAP to check mobile number is valid or not
import re
num = '+919527230560'

pattern = r'[\W]{1}91[6-9]{1}[0-9]{9}$'

result = re.fullmatch(pattern,num)

if result != None:
    print(f'Mobile Number {num} Is Valid')
else:
    print(f'Mobile Number {num} Is Not Valid')
