# fp = open('x_text.txt','w')
# fp.write("My name is Ashitosh")
# fp.close

# open file in read mode
fp = open('x_text.txt')
fp.read()


# open file in write mode

f1 = open("x_file.txt",'w')
f1.write("This is Python File Handeling")
f1.close()

f1=open("x_file.txt",'a')
f1.write("\n My name is Ashitosh")
f1.close()

f1=open('x_file.txt')
f1.read()

import os
print(os.listdir())