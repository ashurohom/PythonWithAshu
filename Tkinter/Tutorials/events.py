from tkinter import *

def click(event):
    print("Thank You For Clicked Me..!")

window = Tk()
window.title("Ashitosh Rohom")
window.geometry("655x455")
widget = Button(window,text="Click Me..!")
widget.pack()

widget.bind('<Button-1>', click)
widget.bind('<Double-1>', quit)


window.mainloop()