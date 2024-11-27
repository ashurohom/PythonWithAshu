from tkinter import *
from PIL import Image, ImageTk
window = Tk()

window.geometry("800x600")


#PNG Image
# img = PhotoImage(file="img1.png")
# window = Label(image=img)
# window.pack()


#JPG Image
jpg = Image.open("img2.jpg")
photo = ImageTk.PhotoImage(jpg)
window = Label(image=photo)
window.pack()


window.mainloop()