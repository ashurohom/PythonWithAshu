import os

old_name = r'C:\Users\R_Ashu\OneDrive\Documents\VSCode\Python\Ashu\file\newfile2.txt'
new_name = r'C:\Users\R_Ashu\OneDrive\Documents\VSCode\Python\Ashu\file\newfile.txt'

if os.path.isfile(new_name):
    print("File name already exists. Cannot rename")
else:
    # Rename the file
    os.rename(old_name, new_name)
    print("Rename Sucessfull..!")