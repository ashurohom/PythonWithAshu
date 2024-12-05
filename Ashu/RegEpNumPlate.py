# WAP to check Given Vehical Number is valid or not

import re

number = 'MH17CC9015'

pattern = r'MH[0-5]{1}[0-9][A-Z]{1,2}+[0-9]{1,4}'

result = re.fullmatch(pattern,number)

if result != None:
    print(f'Vehical Number {number} Is Valid In MAHARASHTRA')
else:
        print(f'Vehical Number {number} Is Not Valid In MAHARASHTRA')
