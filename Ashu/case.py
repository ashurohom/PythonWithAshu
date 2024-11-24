print("*Case List*")
print("Case 1")
print("Case 2")
print("Case 3")

num=int(input("Enter Your Choice : "))

match num:
    case 1:
        print("Case 1")
    case 2:
        print("Case 2")    
    case 3:
        print("Case 3")
    case _:
        print("Invalid option")