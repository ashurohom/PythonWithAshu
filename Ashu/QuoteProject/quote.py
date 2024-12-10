import os
# print(os.listdir())
# print(os.path.isfile('myquotes'))
def addQuote(myfile):
    if not os.path.exists(myfile):
        with open(myfile,'w') as file:
            a = input("Enter Your New Quote : ")
            file.write(a + '\n')
        print("Quote Added Sucessfully..")

    else:
        b = input("Enter Your Another New Quotes : ")
        with open(myfile,'a') as file:
            file.write(b + '\n') 
        print("New Quote Added Sucessfully..")


def showQuotes(myfile):
    try:
        with open(myfile,'r') as file:
            print('Your Quotes !')
            print(file.read())
    except FileNotFoundError:
        print(f"File {myfile} Does Not Exist")



# myfile='myquotes'
myfile = input("Enter Your Quotes File Name i.e=''myquotes : ")

if os.path.exists(myfile):

    while True:

        print("\n--- Quote Management System ---")
        print("1. Add New Quote")
        print("2. View All Quotes")
        print("3. Search Quotes")
        print("4. Delete a Quote")
        print("5. Exit")


    choice = int(input("Enter Your Choice : "))

    if os.path.exists(choice):
        match choice:
            case 1:    
                addQuote(myfile)
            case 2:    
                showQuotes(myfile)        
            case _:
                print("Invalid Choice..")
    else:
        print("File Not Found")
else:
    print(f'File {myfile} Not Exists! Do You Want To Create New File With Same File Name...')
    answer = input("Enter Yes Or No : ").strip().capitalize()

    if answer == 'Yes': 
        addQuote(myfile)
    elif answer == 'No':
        print("Thank You !")    
    