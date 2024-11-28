from tkinter import *
window = Tk()
window.geometry("655x455")

window.title("Ashu Rohom")

def hello():
    print("WelCome Ashu")


frame = Frame(window, borderwidth=4, bg="gray")
frame.pack(side=LEFT, anchor="nw")

b1 = Button(window, fg="black", text="Submit", command=hello)
b1.pack(padx=5, side=LEFT) 

b2 = Button(window, fg="black", text="Submit")
b2.pack(padx=5, side=LEFT) 

b3 = Button(window, fg="black", text="Submit")
b3.pack(padx=5, side=LEFT) 
window.mainloop()