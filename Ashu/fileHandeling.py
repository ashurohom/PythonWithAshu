import os
# print(os.listdir())     #show all file
# print(os.path.isfile('newtext.txt'))

try:
    # file = open("newtext.txt",'x')
    # file.write("This Is My First File...")
    # file.close()
    file = open('newtext.txt','a')
    s=input("Enter String : ")
    file.write(s)
    file.close()
except FileExistsError:
    print("File Exists Already")

finally:
    file = open('newtext.txt','r')
    print(file.read())
    file.close