from tkinter import *
root = Tk()
root.geometry("655x555")
root.title("CodeCraftedByAshuRohom - Hotel Krishna")

# Function Code

f1 = Frame(root)
f1.grid(row=0, column=0, columnspan=3, pady=20)

l1 = Label(f1, text="Hotel Krishna", font="lucida 25 bold", fg="red")
l1.grid(row=0, column=2, padx=20)

l2 = Label(f1, text="CodeCraftedByAshu", font="lucida 8 bold", fg="orchid")
l2.grid(row=1, column=2)

l3 = Label(f1, text="Menu Card And Bill Genrator", font="lucida 15 bold", fg="orchid")
l3.grid(row=2, column=2)

l4 = Label(f1, text="PaniPuri 25RS \n Water 20Rs\n Misal 50Rs \n Vadapav 20RS \n Sweet 50Rs", font="lucida 12 bold", fg="Red")
l4.grid(row=3, column=0, pady=50)





root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.mainloop()