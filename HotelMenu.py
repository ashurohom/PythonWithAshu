
menu={
    "Vadapav" : 20, 
    "Samosa" : 25,
    "Misal" : 70,
    "PaniPuri" : 30,
    "ColdDrink" : 10,
}

print("WelCOme To Nasta Center\n")
print("Vadapav : 20\n Samosa : 25\n Misal : 70\n PaniPuri : 30\n ColdDrink : 10\n")

price = 0

order1 = input("Enter Your Order : ")

if order1 in menu:
    price+=menu[order1]
    print(f'Your Item {order1} Has been Added to order list..')
else:
    print(f'item {order1} not avaliable, please order else')

newitem = input("DO You Wantt to add another item ? Yes/No ")

if newitem == "Yes":
    order2 = input("Enter Your 2nd Order : ")
    if order2 in menu:
        price+=menu[order2]
        print(f'Your Item {order2} Has been Added to order list..')
    else:
        print(f'item {order2} not avaliable, please order else')        

else:
    print(f"Thank You !")

print(f'Bill : {price}')    