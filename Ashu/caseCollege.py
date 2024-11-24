print("Sanjivani COE Data\n")
print("1. HOD")
print("2. Teacher")
print("3. Student")
print("4. Peon")
print("5. Clark\n")

num=int(input("Enter Your Position Number : "))

match num:
    case 1:
        print("HOD")

    case 2:
        print("Teacher List\n")
        print("Ashu Sir")    
        print("Sanket Sir")    
        print("Rani Mam")    
        print("Pinki Mam\n")

        teacher = int(input("Enter Teacher Position : "))

        match teacher:
            case 1:
                print("Ashu Sir Data Found")
            case 2:
                print("Sanket Sir data Found")
            case 3:
                print("Rani Mam Data Found")
            case 4:
                print("Pinki Mam Data Found")
            case 5:
                print("Invalid Entry...!")    

    case 3:
        print("Student")

    case 4:
        print("Peon")

    case 5:
        print("Clark")

    case _:
        print("Invalid Entry...!")            