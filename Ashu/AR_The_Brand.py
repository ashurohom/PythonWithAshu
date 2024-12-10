
print("Wel-Come TO AR_The_Brand\nChoice Your Order : \n")


print("Cloths")
print("DryFruits")
print("Watches")
print("Bags")
print("Exit\n")

total_bill = 0

order = input("Enter Your Choice : ").strip().capitalize()

match order:
    case 'Cloths':

        cloth = {
            "Shirt" : 899,
            "Jins" : 699,
            "Hoodie" : 1100,
            "Jogur" : 1100,
        }

        print("* Welcome To Cloth Section *\n")
        print("Items:")
        print('----------------')
        for item, price in cloth.items():
            print(f"{item} : {price} Rs.")

        total_price = 0

        while True:
            try:
                order = input("\nEnter Your Choice: ").strip().capitalize()
        
                if order in cloth:
                    try:
                        quantity = int(input(f"Enter {order} Quantity: "))
                        if quantity <= 0:
                            print("Quantity must be a positive number. Please try again.")

                        elif quantity > 10:
                            print("Quantity Limit Is Over, Please Enter Quantity Upto 10 Only ")    
                        continue
                        total = cloth[order] * quantity
                        total_price += total
                        print(f'Your item "{order}" (Quantity {quantity}) has been added to the order list.')
                    except ValueError:
                        print("Invalid input for quantity. Please enter a valid number.")
                else:
                    print(f'Sorry, item "{order}" is not available. Please order something else.')

                new_item = input("Do you want to add another cloth? (Yes/No): ").strip().lower()
                if new_item == "no":
                    break
                elif new_item != "yes":
                    print("Invalid input. Assuming you don't want to add more items.")
                    break
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")

        if total_price == 0:
            print(f'Thank You, Visit Again')
        else:    
            print(f"\nThank you for your order! Your total bill is: {total_price} Rs.")

            

    
    
    
    
    
    
    case 'Dryfruits':
        print("2")
    case 'Watches':
        print("3") 
    case 'Bags':
        print("4")    
    case _:
        print("Exit")       