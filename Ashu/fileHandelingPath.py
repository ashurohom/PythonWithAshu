import os
print(os.listdir(r'C:\Users\R_Ashu\OneDrive\Documents\VSCode\Python\Ashu\file'))
print(os.path.isfile('newfile.txt'))
print(os.path.exists(r'C:\Users\R_Ashu\OneDrive\Documents\VSCode\Python\Ashu\file\newfile.txt'))


try:
    if os.path.exists(r'C:\Users\R_Ashu\OneDrive\Documents\VSCode\Python\Ashu\file\newfile.txt'):
        with open(r'C:\Users\R_Ashu\OneDrive\Documents\VSCode\Python\Ashu\file\newfile.txt','a') as fp:
            fp.write("\n Python Developer2")

    else:
        with open(r'C:\Users\R_Ashu\OneDrive\Documents\VSCode\Python\Ashu\file\newfile.txt','x') as fp:
            fp.write("\n Ashitosh Rohom")
except:
    print('Error')

finally:
    with open(r'C:\Users\R_Ashu\OneDrive\Documents\VSCode\Python\Ashu\file\newfile.txt','r') as fp:
        print(fp.read())
