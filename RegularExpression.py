# For searching specific format
# for matching specifying format

'''
Character Classes

1. [abc]===>Either a or b or c
2. [^abc] ===>Except a and b and c
3. [a-z]=>Any Lower case alphabet symbol
4. [A-Z]=>Any upper case alphabet symbol
5. [a-zA-Z]==>Any alphabet symbol
6. [0-9] Any digit from 0 to 9
7. [a-zA-Z0-9]==>Any alphanumeric character
8. [^a-zA-Z0-9]==>Except alphanumeric characters (Special Characters)


Pre defined Character classes:
\s =  Space character
\S = Any character except space character
\d = Any digit from 0 to 9
\D = Any character except digit
\w = Any word character [a-zA-Z0-9]
\W = Any character except word character (Special Characters)
. = Any character including special characters



Qunatifiers:
We can use quantifiers to specify the number of occurrences to match.
a  = Exactly one 'a'
a+ = Atleast one 'a'
a* = Any number of a's including zero number
a? = Atmost one 'a' ie either zero number or one number
a{m} Exactly m number of a's
a{m,n} Minimum m number of a's and Maximum n number of a's


'''

import re

s = "My Name Is Ashu Rohom"

match = re.search(r'Ashu',s)
print(f'Start Index : {match.start()}')
print(f'End Index : {match.end()}')

print()

result = re.findall('[a-d]', s)
print(result)

