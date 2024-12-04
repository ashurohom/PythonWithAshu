menu = {
    "Vadapav": 20, 
    "Samosa": 25,
    "Misal": 70,
    "PaniPuri": 30,
    "ColdDrink": 10,
}

print("Welcome to Nasta Center\n")
print("Menu:")
for item, price in menu.items():
    print(f"{item} : {price} INR")

total_price = 0

while True:
    order = input("\nEnter Your Order: ").strip()
    
    if order in menu:
        total_price += menu[order]
        print(f'Your item "{order}" has been added to the order list.')
    else:
        print(f'Sorry, item "{order}" is not available. Please order something else.')

    new_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if new_item == "no":
        break
    elif new_item != "yes":
        print("Invalid input. Assuming you don't want to add more items.")
        break

print(f"\nThank you for your order! Your total bill is: {total_price} INR")
