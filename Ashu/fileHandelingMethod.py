import os
print(os.path.isfile('example.txt'))

try:
    #create new file
    with open('example.txt','x') as files:
        s = input("Enter String : ")
        files.write(s)

except FileExistsError:
    print("File exists Already..!")

finally:
    #append data into existing file
    with open('example.txt','a') as files:
        files.write("\n I am Experinced Python Developer..!")

    #open file for read
    with open('example.txt','r') as files:
        print(files.read())    