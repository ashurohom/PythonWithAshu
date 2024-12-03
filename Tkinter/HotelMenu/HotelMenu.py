import tkinter as tk
from tkinter import messagebox

# Menu dictionary
menu = {
    "Vadapav": 20, 
    "Samosa": 25,
    "Misal": 70,
    "PaniPuri": 30,
    "ColdDrink": 10,
}

# Initialize global variables
total_price = 0
order_list = []

# Function to add an item to the order
def add_item():
    global total_price
    item = item_var.get().strip()
    if item in menu:
        total_price += menu[item]
        order_list.append(item)
        order_text.set("\n".join(order_list))
        price_text.set(f"Total Bill: {total_price} INR")
    else:
        messagebox.showerror("Error", f'Item "{item}" is not available!')

# Function to finalize the order
def finalize_order():
    if order_list:
        messagebox.showinfo("Order Summary", f"Your Order:\n{', '.join(order_list)}\n\nTotal Bill: {total_price} INR")
    else:
        messagebox.showwarning("No Items", "No items added to the order.")
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Nasta Center")

# Header
header_label = tk.Label(root, text="Welcome to Nasta Center", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

# Menu Display
menu_label = tk.Label(root, text="Menu:", font=("Arial", 14))
menu_label.pack()

menu_text = "\n".join([f"{item}: {price} INR" for item, price in menu.items()])
menu_display = tk.Label(root, text=menu_text, font=("Arial", 12), justify=tk.LEFT)
menu_display.pack(pady=5)

# Entry for adding items
item_var = tk.StringVar()
item_label = tk.Label(root, text="Enter Your Order:", font=("Arial", 12))
item_label.pack()

item_entry = tk.Entry(root, textvariable=item_var, font=("Arial", 12))
item_entry.pack()

# Add Item Button
add_button = tk.Button(root, text="Add Item", command=add_item, font=("Arial", 12))
add_button.pack(pady=5)

# Order List Display
order_text = tk.StringVar()
order_text.set("Order List:\n")
order_list_label = tk.Label(root, textvariable=order_text, font=("Arial", 12), justify=tk.LEFT)
order_list_label.pack(pady=5)

# Total Price Display
price_text = tk.StringVar()
price_text.set("Total Bill: 0 INR")
price_label = tk.Label(root, textvariable=price_text, font=("Arial", 12, "bold"))
price_label.pack(pady=5)

# Finalize Order Button
finalize_button = tk.Button(root, text="Finalize Order", command=finalize_order, font=("Arial", 12))
finalize_button.pack(pady=10)

# Run the main loop
root.mainloop()
