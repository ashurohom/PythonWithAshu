from tkinter import *
window = Tk()
window.geometry("555x444")
window.title("AshuRohom")

f1 = Frame(window,bg="skyblue", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

lable1 = Label(f1, text="Project Tkinter VSCode")
lable1.pack(pady=150)

f2 = Frame(window,bg="skyblue", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill="x", )

lable2 = Label(f2, text="WelCome TO VSCode",fg="red")
lable2.pack(pady=1)

window.mainloop()