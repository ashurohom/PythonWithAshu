from tkinter import *

window = Tk()

def changesize():
    window.geometry(f'{high.get()}x{wid.get()}')

window.title("CodeWithAshu - HeightWidth")
window.wm_iconbitmap("icon.png")
window.configure(background="green")

frame1 = Frame(window)
Label(frame1, text="Width : ").grid(row=0, column=1)
Label(frame1, text="Height : ").grid(row=1, column=1)

height = StringVar()
high = Entry(frame1, textvariable=height)
high.grid(row=0, column=2)

width = StringVar()
wid = Entry(frame1, textvariable=width)
wid.grid(row=1, column=2)

b1 = Button(window, text="Apply", command=changesize)
b1.pack(side=BOTTOM)

frame1.pack(side=TOP)
Button(window, text="Close", command=window.destroy).pack()

window.mainloop()
