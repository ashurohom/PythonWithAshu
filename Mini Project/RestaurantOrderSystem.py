menu = {
    "Tea" : 15,
    "Vadapav" : 20,
    "Samosa" : 25,
    "Misal" : 70,
    "PaniPuri" : 30,  
    "Pavbhaji" : 40,
    "Lassi" : 25,
    "Colddrink" : 20,
}

print("* Welcome To Krishna Restaurant Order System *\n")
print("MenuCard:")
print('----------------')
for item, price in menu.items():
    print(f"{item} : {price} Rs.")

total_price = 0

while True:
    try:
        order = input("\nEnter Your Order: ").strip().capitalize()
        
        if order in menu:
            try:
                quantity = int(input(f"Enter {order} Quantity: "))
                if quantity <= 0:
                    print("Quantity must be a positive number. Please try again.")

                elif quantity > 100:
                    print("Quantity Limit Is Over, Please Enter Quantity Upto 100 Only ")    
                    continue
                total = menu[order] * quantity
                total_price += total
                print(f'Your item "{order}" (Quantity {quantity}) has been added to the order list.')
            except ValueError:
                print("Invalid input for quantity. Please enter a valid number.")
        else:
            print(f'Sorry, item "{order}" is not available. Please order something else.')

        new_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
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




'''
Test Cases Passed : 

Test Case 1: Valid Single Order
Test Case 2: Invalid Item
Test Case 3: Invalid Quantity (Non-Numeric)
Test Case 4: Excessive Quantity
Test Case 5: Multiple Valid Orders
Test Case 6: Quantity = 0
Test Case 7: Invalid Response for "Add Another Item"
Test Case 8: Mixed Case Item Name
Test Case 9: No Orders Placed
Test Case 10: Handling Unexpected Input in Quantity
Test Case 11: All Orders in One Attempt
'''