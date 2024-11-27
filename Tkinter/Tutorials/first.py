from tkinter import *
from PIL import Image, ImageTk
window = Tk()

window.geometry("800x600")
window.minsize(200,200)
window.maxsize(1200,1200)

lable1 = Label(text="My First Lable")
lable1.pack()

# img = PhotoImage(file="img1.png")
# window = Label(image=img)
# window.pack()

jpg = Image.open("img2.jpg")
photo = ImageTk.PhotoImage(jpg)
window = Label(image=photo)
window.pack()


window.mainloop()