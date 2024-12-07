menu = {
    "Tea" : 15,
    "Vadapav" : 20,
    "Samosa" : 25,
    "Misal" : 70,
    "PaniPuri" : 30,  
    "Pavbhaji" : 40,
    "Lassi" : 25,
    "ColdDrink" : 20,
}

print("* Welcome To ABC Restaurant Order System *\n")
print("MenuCard:")
for item, price in menu.items():
    print(f"{item} : {price} Rs.")

total_price = 0

while True:
    try:
        order = input("\nEnter Your Order: ").strip()
        
        if order in menu:
            try:
                quantity = int(input(f"Enter {order} Quantity: "))
                if quantity <= 0:
                    print("Quantity must be a positive number. Please try again.")
                    continue
                total = menu[order] * quantity
                total_price += total
                print(f'Your item "{order}" has been added to the order list.')
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

print(f"\nThank you for your order! Your total bill is: {total_price} Rs.")
